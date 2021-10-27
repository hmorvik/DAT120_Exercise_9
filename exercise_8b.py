# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:53:45 2021

@author: havar
"""

class MultipleChoice:
    def __init__(self, start_question='', start_answer_list=[], start_correct_answer=0):
        self.question = start_question
        self.answer_list = start_answer_list
        self.correct_answer = start_correct_answer
        
    def __str__(self):
        str_text_block = 'Q:\t'+self.question+'\n'
        for n in range(len(self.answer_list)):
            if n == 0:
                str_text_block += 'A:\t'+str((n))+')\t'+self.answer_list[n]+'\n'
            else:
                str_text_block += '\t'+str((n))+')\t'+self.answer_list[n]+'\n'
        return str_text_block

    def sjekk_svar(self, chosen_answer):
        if self.correct_answer == str(chosen_answer):
            return 'Korrekt'
        else:
            return 'Galt'
        
    def korrekt_svar_tekst(self):
        return self.answer_list[int(self.correct_answer)]
    
    