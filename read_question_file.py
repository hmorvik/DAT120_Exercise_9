# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:07:02 2021

@author: havar
"""

def read_question_file(question_file):
    from exercise_8b import MultipleChoice
    questions = []
    q_file = open(question_file, 'r', encoding='UTF8')
    for line in q_file:
        question = line.split(':')[0].strip()
        correct_answer = str(line.split(':')[1].strip())
        answer_list = line.split(':')[2].strip()
        answer_list = answer_list[1:-1].split(', ')
        questions.append(MultipleChoice(question, answer_list, correct_answer))
    return questions






if __name__ == '__main__':
    questions = read_question_file('sporsmaalsfil.txt')
    points1 = 0
    points2 = 0
    for n in range(len(questions)):
        print(questions[n])
        a1 = int(input('Velg et svaralternativ for spiller 1: '))
        a2 = int(input('Velg et svaralternativ for spiller 2: '))
        print('\n')
        print('Korrekt svar: '+questions[n].korrekt_svar_tekst())
        print('\n')
        print('Spiller 1:\t'+questions[n].sjekk_svar(a1))
        if questions[n].sjekk_svar(a1) == 'Korrekt':
            points1 += 1
        print('\t\t\tTotal poengsum: '+str(points1))
        print('Spiller 2:\t'+questions[n].sjekk_svar(a2))
        if questions[n].sjekk_svar(a2) == 'Korrekt':
            points2 += 1
        print('\t\t\tTotal poengsum: '+str(points2))
        print('\n\n')
    
    print('\nQuizen er ferdig. Poengsummen ble:\n')
    print('Spiller 1:\t'+str(points1))
    print('Spiller 2:\t'+str(points2))