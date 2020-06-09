from Question import Question

question_prompts = [
    "Jakiego koloru są banany?\n(a) rzółte\n(b) żółte\n(c) żułte\n\n",
    "Gdzie są rzeki bez wody?\n(a) w Rosji\n(b) w rosji\n(c) na mapach\n\n",
    "Jaki koń widzi równie dobrze z przodu i z tyłu?\n(a) każdy\n(b) ślepy\n(c) żaden\n\n",
    "Który miesiąc ma 28 dni?\n(a) luty\n(b) czerwiec\n(c) każdy\n\n",
    "Jaka jest różnica między czarodziejką a czarownicą?\n(a) umiejętności\n(b) jakieś 50lat\n(c) nie wiem\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Masz " + str(score) + "/" + str(len(questions)) + " poprawnych odpowiedzi.")

run_test(questions)