from question import Question

question_prompts = [
    "What color are apple?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

# create question object
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


# define test function
def run_test(questions_list):
    score = 0
    for question in questions_list:
        answer = input(question.prompt + "Your answer: ")
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/ " + str(len(questions_list)) + " correct answer")


run_test(questions)
