import question_bank

def count_true_false_questions():
    true_count = 0
    false_count = 0
    for question in question_bank.questions:
        # Assuming each question has an 'answers' attribute/list
        answers = question.get('answers', [])
        if set(answers) == {True, False} or set(answers) == {False, True}:
            # Assuming the correct answer is stored in 'correct_answer'
            correct = question.get('correct_answer')
            if correct is True:
                true_count += 1
            elif correct is False:
                false_count += 1
    return true_count, false_count



if __name__ == "__main__":
    true_count, false_count = count_true_false_questions()
    print(f"Number of True/False questions with correct answer True: {true_count}")
    print(f"Number of True/False questions with correct answer False: {false_count}")

    