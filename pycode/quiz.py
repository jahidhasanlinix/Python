from question import question


que =[
    "Where do you live?\n(a) Gazipur\n(b) Astana\n(c) Oslo\n\n",
    "Where does Messi born?\n(a) Spain\n(b) Argentina\n(c) Brazil\n\n",
    "Do you movies?\n(a) Yes\n(b) No\n(c) Neutral\n\n",
    "Do yo like comedy?\n(a) Yes\n(b) No\n(c) Neutral\n\n",
]

#create datatype
questions = [
    question(que[0],'a'),
    question(que[1],'b'),
    question(que[2],'a'),
    question(que[3],'a'),
]

def run_test(questions):
    score = 0
    for que in questions:
        answer = input(que.prompt)
        if answer == que.answer:
            score += 1
    print('You got '+ str(score) + '/' + str(len(questions)) + ' correct')

run_test(questions)