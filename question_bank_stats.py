import queston_bank as qb


def count_true_false_questions():
    true_count = 0
    false_count = 0
    question_counter = 0
    for question in qb.QuestionBank.questions:
        # Check if the question is a true_false question
        if question.answer_type == "true_false":
            question_counter += 1
            if question.answer == "1":  # Assuming "1" represents True
                true_count += 1
            elif question.answer == "2":  # Assuming "2" represents False
                false_count += 1
    return true_count, false_count, question_counter


def most_popular_single_choice_answer():
    answer_frequency = {}
    for question in qb.QuestionBank.questions:
        if question.answer_type == "single":
            if question.answer in answer_frequency:
                answer_frequency[question.answer] += 1
            else:
                answer_frequency[question.answer] = 1
    if not answer_frequency:
        return None, 0
    most_popular_answer = max(answer_frequency, key=answer_frequency.get)
    return most_popular_answer, answer_frequency[most_popular_answer]


def count_single_choice_questions():
    single_choice_count = 0
    for question in qb.QuestionBank.questions:
        if question.answer_type == "single":
            single_choice_count += 1
    return single_choice_count


def num_questions_with_n_correct_answers(n: int):
    count = 0
    for question in qb.QuestionBank.questions:
        if question.answer_type != "multiple":
            continue    
        correct_answers = len(question.answer)
        if correct_answers == n:
            print(f"Question ID {question.id} has exactly {n} correct answers.")
            count += 1
    return count


def main():
    true_count, false_count, question_counter = count_true_false_questions()
    print(f"Number of True/False questions with correct answer True: {true_count}")
    print(f"Number of True/False questions with correct answer False: {false_count}")
    print(f"Total number of True/False questions: {question_counter}")

    # number of questions with exactly 2 correct answers
    two_correct_count = num_questions_with_n_correct_answers(2)
    print(f"Number of questions with exactly 3 correct answers: {two_correct_count}")



    # number of questions with exactly 3 correct answers
    three_correct_count = num_questions_with_n_correct_answers(3)
    print(f"Number of questions with exactly 3 correct answers: {three_correct_count}")


    # number of questions with exactly 4 correct answers
    four_correct_count = num_questions_with_n_correct_answers(4)
    print(f"Number of questions with exactly 4 correct answers: {four_correct_count}")

    most_popular_answer, frequency = most_popular_single_choice_answer()
    single_choice_count = count_single_choice_questions()
    if most_popular_answer is not None:
        print(
            f"Most popular single-choice answer: {most_popular_answer} (chosen {frequency} times)"
        )
        print(f"Total number of single-choice questions: {single_choice_count}")


if __name__ == "__main__":
    main()
