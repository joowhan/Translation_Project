import matplotlib.pyplot as plt
import numpy as np
import math as mt
import seaborn as sns
from tqdm import tqdm
import pandas as pd
from hangul_utils import split_syllables, join_jamos
from tqdm.auto import tqdm
import re
#from eunjeon import Mecab
from konlpy.tag import Mecab
con_dict = [
    
        ['ㅏㅣ','ㅐ'], ['ㅑㅣ','ㅒ'], ['ㅓㅣ','ㅔ'],
        ['ㅕㅣ','ㅖ'], ['ㅗㅣ','ㅚ'], ['ㅗㅐ','ㅙ'],
        ['ㅜㅓ','ㅝ'], ['ㅜㅔ','ㅞ'], ['ㅡㅣ','ㅢ'],
        ['ㅣㅏ','ㅑ'], ['ㅣㅓ','ㅕ'], ['ㅣㅗ','ㅛ'],
        ['ㅣㅜ','ㅠ'], ['ㅡㅓ','ㅓ'], ['ㅗㅏ','ㅘ'],
    
    ]

jongsung_list = [ 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


    #lis_beta = ['EP+EF', 'VCP+EF', 'B+EF', 'B+EP+EF', 'B+VCP+EF', 'EF','EP']

lis_beta = ['EP+EF', 'EF', 'B+EF', 'B+EP+EF']

    #어말을 처리해 주기 위한 것으로, 나중에 EC등이 필요해 진다면 이 부분에 EC 등을 집어넣어준다. 참고로 말하자면 이는 마지막에 위치해야한다.
    #특이 바로 밑의 이 부분은 형태소 태그가 이 리스트 안의 것과 일치하는 경우 단순 삭제를 하는 것이고
    
lis_ef_h = ['EF', 'UNKNOWN']

    #이 부분 같은 경우는 마지막에 오는 것을 처리하는 것으로 단독으로만 들어가는게 좋겠지?
    

lis_end = [
    
        'ㅅㅡㅂㄴㅣㄷㅏ', 'ㅅㅡㅂㄴㅣㄲㅏ',
        'ㅂㄴㅣㄷㅏ', 'ㄴㅣㄷㅏ', 'ㅂㅅㅣㄷㅏ', 'ㅅㅣㄷㅏ', 'ㄹㄹㅐㅇㅛ','ㄹㅐㅇㅛ',
        'ㅇㅡㅅㅔㅇㅛ', 'ㅅㅔㅇㅛ', 'ㄷㅔㅇㅛ', 'ㅇㅔㅇㅛ', 'ㅇㅖㅇㅛ', 'ㄴㅏㅇㅛ', 'ㅇㅡㄹㄲㅏㅇㅛ', 'ㅇㅣㄹㄲㅏㅇㅛ', 'ㄹㄲㅏㅇㅛ', 'ㅇㅡㄴㄱㅏㅇㅛ', 'ㅇㅣㄴㄱㅏㅇㅛ','ㄱㅜㄴㅇㅛ','ㄴㄱㅏㅇㅛ',
        'ㄱㅗㅇㅛ','ㅇㅛ',
        'ㅈㅛ',
        'ㅅㅣㅂㅅㅣㅇㅗ', 'ㅅㅣㅇㅗ', 'ㅇㅗ',
        'ㅂㄴㅣㄲㅏ',  
    
]
lis_wk = [
    
    ['ㄱㅖ', 'ㅇㅣㅆㅇㅡ'], ['ㅈㅜㅁㅜ','ㅈㅏ'], ['ㅈㅏㅂㅅㅜ','ㅁㅓㄱㅇㅡ']
    
]
    

lis_ic = ['ㅇㅖ', 'ㄴㅔ', 'ㅇㅏㄴㅣㅇㅗ', 'ㅇㅏㄴㅣㅇㅛ']

lis_ef = ['EP+EP+EF', 'EP+EF', 'EF', 'UNKNOWN']

lis_tag_last = ['EF', 'UNKNOWN']

lis_end_2low = [
    
    'ㄷㅓㄹㅏ','ㄴㄷㅏ', 'ㅆㄷㅏ', 'ㄹㅗㄷㅏ', 'ㄷㅏ', 'ㄱㅔ', 'ㄴㅡㄴㄷㅏ',
    'ㄹㅏ',
    'ㅇㅑ', 
    'ㄴㅣㄲㅏ', 'ㄲㅏ', 'ㄹㄲㅏ', 'ㅈㅣ',
    'ㄴㅣ', 
    'ㅇㅏ', 'ㅇㅓ',
    'ㄷㅔ', 'ㄱㅏ','ㄹㅐ',
    'ㅈㅏㄶㅇㅏ', 'ㄴㅔ','ㅇㅕ', 'ㄴㅏ','ㄱㅜㄴ','ㄱㅗ',
    'ㅈㅣㅁㅏㄴ', 'ㅇㅡㄴㄷㅔ', 'ㅅㅓ', 'ㄷㅐ',
    'ㄱㅓㄹ','ㄲㅔ', 'ㄴㅑ',
]

mec = Mecab()

class Jamodealer:

    jamo = []
    pp = ''
    #각 단어들을 받아와서 자모단위로 나눈다.
    def __init__(self, lis_word):

        mec = Mecab()
    
        self.jamo = []
        for i in lis_word:
            self.jamo.append(split_syllables(i))

    def detect_h(self, input, lis_end_h, lis_end_l):
        for i in lis_end_h:
            if len(input)>=len(i):
                if input[-len(i):]==i:
                    return 1
            
        for i in lis_end_l:
            if len(input)>=len(i):
                if input[-len(i):]==i:
                    return 0
            
        return -1

    def unite(self, input, dict):
        for i in dict:
            input = re.sub(i[0],i[1],input)
        return input
    
    ##사전에서 변환된 자모단위로 분리된 문장을 합칠 때 쓰는 함수이다.     
    def make_one(self):
        #list 형태로 저장된 자모들의 집합을 하나의 string pp에 저장한다. 
        self.pp = ''
        for i in self.jamo:
             self.pp= self.pp+i
        ##종성과 종성을 합쳐야 하는 경우가 있다면 합친다.        
        self.pp = self.unite(self.pp, self.con_dict)
        
        #자모 단위의 string에서 자모 단위로 사전을 만들고 거기에 index를 부여한다.        
        chars = list(set(self.pp))
        char_to_ix = { ch:i for i,ch in enumerate(chars) }
        ix_to_char = { i:ch for i,ch in enumerate(chars) }
        
        #자모 단위로 분리되었던 문장을 다시 하나로 합친다.
        jamo_numbers = [char_to_ix[x] for x in self.pp]
        restored_jamo = ''.join([ix_to_char[x] for x in jamo_numbers])
        #합쳐진 문장을 return 한다.
        restored_text = join_jamos(restored_jamo)
        return restored_text

class isHigh(object):

    def __init__(self):
        
        mec = Mecab()

    def is_high(self, input, lis_ef, tag_last, lis_w_last, lis_w_last_not):
    
        lis_res_word = []
    
        lis_input = input.split()
        lis_word = []
        lis_tag = []
        lis_last_word = []
        lis_ind = []
        lis_ind_ele = []
    
        lis_result = []
    
        for i in range(len(lis_input)):
            ele_w = []
            ele_t = []
        
            an = mec.pos(lis_input[i])
            for j in range(len(an)):
                ele_w.append(an[j][0])
                ele_t.append(an[j][1])
            elem_w = ' '.join(ele_w)
            elem_t = '/'.join(ele_t)
        
            jam_pre = Jamodealer(elem_w)
            lis_word.append(''.join(jam_pre.jamo))
            lis_tag.append(elem_t)
    
        for i in range(len(lis_tag)):
        
            if 'EF/SF' in lis_tag[i] or 'EF/SV' in lis_tag[i] or 'EC/SY'  in lis_tag[i] or 'EC/SF' in lis_tag[i] or 'EC/SSO' in lis_tag[i] or 'IC/SF' in lis_tag[i]:
                elemen_t = lis_tag[i].split('/')
                elemen_w = lis_word[i].split(' ')
                flag = 0
                ff=0
            
#             print('iiii')
            
                for j in range(len(elemen_t)):

                    flag_end = jam_pre.detect_h(elemen_w[j], lis_w_last_not, lis_w_last)
                
                    if flag_end==1:
                    
                        return 1
                    else:
                    
                        return 0
    def isThisHigh(self, input):

        return self.is_high(input, lis_ef, lis_tag_last, lis_end_2low, lis_end)