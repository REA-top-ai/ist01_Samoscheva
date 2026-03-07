answers = ['A', 'C', 'A', 'A', 'D',
           'B', 'C', 'A', 'C', 'B',
           'A', 'D', 'C', 'A', 'D',
           'C', 'B', 'B', 'D', 'A']
mistakes = []
correct = 0
incorrect = 0
stud_answers = []
for meow in range(20):
    stud_answer = input(f'введите ответ на вопрос {meow+1}: ')
    stud_answers.append(stud_answer)
for cats in range(20):
    if stud_answers[cats] == answers[cats]:
        correct += 1
    else:
        incorrect += 1
        mistakes.append(cats + 1)
if incorrect <= 5:
    print('экзамен сдан\n'
          'количество правильных ответов:',  correct, '\n'
          'количество неправильных ответов:', incorrect, '\n'
          'задания с ошибкой:', mistakes)
else:
    print('экзамен не сдан\n'
          'количество правильных ответов:',  correct, '\n'
          'количество неправильных ответов:', incorrect, '\n'
          'задания с ошибкой:', mistakes)

