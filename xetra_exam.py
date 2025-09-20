"""
A Streamlit app to conduct a quiz using questions from QuestionBank.
To run the app, use the command:
    - navigate to the directory containing this file and execute:
    - streamlit run xetra_exam.py
"""

import streamlit as st
from queston_bank import QuestionBank


def run_quiz():
    st.title("📘 Xetra Quiz")

    max_questions = len(QuestionBank.questions)
    # --- Question range inputs ---
    col1, col2 = st.columns(2)
    lower = col1.number_input("Lower Question ID", min_value=1, value=1, step=1)
    upper = col2.number_input("Upper Question ID", min_value=1, value=max_questions, step=1)

    # --- Initialize session state ---
    if "current_question" not in st.session_state:
        st.session_state.current_question = QuestionBank.get_random_in_range(
            lower, upper
        )
        st.session_state.answered = False
        st.session_state.correct = None
        st.session_state.go_next = False
        st.session_state.lower = lower
        st.session_state.upper = upper

        # Initialize score
        st.session_state.correct_count = 0
        st.session_state.incorrect_count = 0
        st.session_state.total_count = 0

    # --- Reset if user changes the range ---
    if lower != st.session_state.lower or upper != st.session_state.upper:
        st.session_state.current_question = QuestionBank.get_random_in_range(
            lower, upper
        )
        st.session_state.answered = False
        st.session_state.correct = None
        st.session_state.go_next = False
        st.session_state.lower = lower
        st.session_state.upper = upper

        # Reset score
        st.session_state.correct_count = 0
        st.session_state.incorrect_count = 0
        st.session_state.total_count = 0

    # --- Handle Next Question ---
    if st.session_state.get("go_next", False):
        st.session_state.current_question = QuestionBank.get_random_in_range(
            lower, upper
        )
        st.session_state.answered = False
        st.session_state.correct = None
        st.session_state.go_next = False
        st.rerun()  # refresh immediately

    q = st.session_state.current_question
    st.subheader(f"Question {q.id}")
    st.write(q.question)

    # --- Display image if available ---
    if q.link_pic:
        st.image(q.link_pic, use_container_width=True)

    # --- Display options ---
    options = [line.strip() for line in q.choices.strip().split("\n") if line.strip()]
    user_answers = []

    if q.answer_type == "multiple":
        for i, option in enumerate(options):
            if st.checkbox(option, key=f"chk_{q.id}_{i}"):
                user_answers.append(option.split(".")[0].strip())
    else:
        ans = st.radio("Choose your answer:", options, key=f"rad_{q.id}", index=None)
        if ans:
            user_answers.append(ans.split(".")[0].strip())

    # --- Submit answer ---
    if st.button("Submit Answer"):
        if not user_answers:
            st.warning("Please select at least one answer.")
        else:
            st.session_state.answered = True

            # Normalize correct answer
            if isinstance(q.answer, list):
                correct_set = set(str(a).strip() for a in q.answer)
            else:
                correct_set = set(a.strip() for a in q.answer.split(","))

            is_correct = set(user_answers) == correct_set
            st.session_state.correct = is_correct

            # Update score
            st.session_state.total_count += 1
            if is_correct:
                st.session_state.correct_count += 1
            else:
                st.session_state.incorrect_count += 1

    # --- Feedback and Next Question ---
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct!")
        else:
            if isinstance(q.answer, list):
                correct_display = ", ".join(str(a) for a in q.answer)
            else:
                correct_display = q.answer
            st.error(f"❌ Incorrect. Correct answer: {correct_display}")

        if st.button("Next Question"):
            st.session_state.go_next = True
            st.rerun()

    # --- Display score ---
    st.markdown("---")
    total = st.session_state.total_count
    correct = st.session_state.correct_count
    incorrect = st.session_state.incorrect_count
    percentage = (correct / total * 100) if total > 0 else 0

    st.subheader("📊 Score")
    st.write(f"✅ Correct answers: {correct}")
    st.write(f"❌ Incorrect answers: {incorrect}")
    st.write(f"📝 Total answered: {total}")
    st.write(f"📈 Percentage correct: {percentage:.1f}%")


def main():
    run_quiz()


if __name__ == "__main__":
    main()
