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
from hanspell import spell_checker

##############################

E_list = [
    
    'EF', 'EP', 'VCP', 'VCN', 'XSA', 'XSV', 'NP', 'JX', 'JKB', #이는 어말 처리를 위한 것들이다. 어말 부분에 추가할 것이 있다면 여기에
                                                              
]

con_dict = [
    
    ['ㅏㅣ','ㅐ'], ['ㅑㅣ','ㅒ'], ['ㅓㅣ','ㅔ'],
    ['ㅕㅣ','ㅖ'], ['ㅗㅣ','ㅚ'], ['ㅗㅐ','ㅙ'],
    ['ㅜㅓ','ㅝ'], ['ㅜㅔ','ㅞ'], ['ㅡㅣ','ㅢ'],
    ['ㅣㅏ','ㅑ'], ['ㅣㅓ','ㅕ'], ['ㅣㅗ','ㅛ'],
    ['ㅣㅜ','ㅠ'], ['ㅡㅓ','ㅓ'], ['ㅗㅏ','ㅘ']
    
]

lis_beta = ['EP+EF', 'VCP+EF', 'VCP', 'B+EF', 'B+EP+EF', 'B+VCP+EF', 'EF','EP']

lis_beta_ef = ['EP+EF', 'VCP+EF', 'EF']

lis_end = [
    
    'ㅂㄴㅣㄷㅏ',
    'ㅅㅔㅇㅛ', 'ㄷㅔㅇㅛ', 'ㅇㅔㅇㅛ', 'ㅇㅖㅇㅛ', 'ㄴㅏㅇㅛ', 'ㅇㅡㄹㄲㅏㅇㅛ', 'ㅇㅣㄹㄲㅏㅇㅛ', 'ㄹㄲㅏㅇㅛ', 'ㅇㅡㄴㄱㅏㅇㅛ', 'ㅇㅣㄴㄱㅏㅇㅛ','ㅇㅛ',
    'ㅈㅛ',
    'ㅅㅣㅂㅅㅣㅇㅗ', 'ㅅㅣㅇㅗ', 'ㅇㅗ',
    'ㅂㄴㅣㄲㅏ', 'ㄴㅣㄲㅏ', 'ㄲㅏ', 
    
]



lis_plus = [
    
    'EP', 'VCP', 
    
]

##############################

mec = Mecab()

def unite(input, dict):
    for i in dict:
        input = re.sub(i[0],i[1],input)
    return input
    
## 자모 단위로 문장을 나누고 합칠 때 쓰는 class ##
class Jamodealer:
    jamo = []
    pp = ''
    #각 단어들을 받아와서 자모단위로 나눈다.
    def __init__(self,lis_word):
    
        self.jamo = []
        for i in lis_word:
            self.jamo.append(split_syllables(i))
    
    ##사전에서 변환된 자모단위로 분리된 문장을 합칠 때 쓰는 함수이다.     
    def make_one(self):
        #list 형태로 저장된 자모들의 집합을 하나의 string pp에 저장한다. 
        self.pp = ''
        for i in self.jamo:
             self.pp= self.pp+i
        ##종성과 종성을 합쳐야 하는 경우가 있다면 합친다.        
        self.pp = unite(self.pp, con_dict)
        
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

def to2lists(input):
    lis_word = []
    lis_tag = []
    #data = han.pos(input,ntags=22,flatten=True, join=False)
    data = mec.pos(input)
    for i in data:
        lis_word.append(i[0])
        lis_tag.append(i[1])
    return lis_word, lis_tag

def rememberSpace(lis, input):
    
    rlis = []
    
    for i in range(len(lis)):
        if lis[i]==input:
            rlis.append(i)
            
    for i in range(len(rlis)):
        rlis[i] = rlis[i]-i      
    return rlis

def convertSpace(lis_space,lis_lis):
    
    rlis = []
    k=0
    for i in range(len(lis_lis)):
        
        if k in lis_space:
            rlis.append(i)
            
        k = k+len(lis_lis[i])
        
    #print(rlis)  
    return rlis

def union(lis, lis_lis):
    
    k = 0
    for i in lis:
        lis_lis.insert(i+k,' ')
        k = k+1
        
def union_t(lis_lis):
    
    for i in range(len(lis_lis)-1):
        if lis_lis[i+1] != ' ' and lis_lis[i+1] !='SF' and lis_lis[i] != ' ' and lis_lis[i] !='SF':
            lis_lis[i] = lis_lis[i]+'/'
        if lis_lis[i+1]=='SF':
            lis_lis[i+1] = ' '+lis_lis[i+1]
            
def union_w(lis_w, lis_tag):
    
    for i in range(len(lis_w)-1):
        if lis_tag[i+1]==' SF':
            lis_w[i+1] = ' '+lis_w[i+1]
            
def prepro(input):
    lis_w, lis_t = to2lists(input)

    space_list = rememberSpace(input,' ')
    space_location = convertSpace(space_list, lis_w)
    union(space_location, lis_w)
    union(space_location, lis_t)
    union_t(lis_t)
    union_w(lis_w, lis_t)
    
    str_w = ''
    str_t = ''
    for i in range(len(lis_w)):
        str_w = str_w + lis_w[i]
        str_t = str_t + lis_t[i]
    
    data_w = str_w.split(' ')
    data_t = str_t.split(' ')
    
    lis_word, lis_tag = to2lists(input)
    
    lis_ind = []
    t_ind = 0
    jam1 = Jamodealer(lis_word)
    jam2 = Jamodealer(data_w)
    for i in range(len(data_w)-1):
        element = []
        leng = len(data_t[i].split('/'))
        res = jam2.jamo[i]
        ind = 0
        lenlen = 0
        #element.append(0)
        for j in range(leng):
            element.append(ind)
            ind = ind + len(jam1.jamo[t_ind])
            res = res[len(jam1.jamo[t_ind]):]
            
            lenlen = len(jam1.jamo[t_ind])+lenlen
            t_ind = t_ind+1
        
        #element = element[:-1]
        element.append(len(jam2.jamo[i]))
        lis_ind.append(element)
    
    return data_w, data_t, lis_ind

def pre_target(input, lis, target):
    result = input
    if target in input:
        res = input.split('/')
        for j in range(len(res)):
            if target in res[j] and '+' in res[j]:
                loc = res[j].index('+')
                wd = res[j][:loc]
                if wd not in lis:
                    res[j] = re.sub(wd, 'A', res[j])
        result = '/'.join(res)
    return result

def li2str(input):
    st = ""
    for i in input:
        st = st+i
    return st

def makestrdict(input):
    result = []
    for i in input:
        bullet = []
        for j in range(len(i)):
            gre = li2str(i[j])
            bullet.append(gre)
        result.append(bullet)
    return result

def isException(input):
    if 'special' in input[1]:
        return 1
    else:
        return 0
    
##############################

def delete_end(w, t, list_tag, list_end):
    
    lis_w = []
    lis_t = []
    number = len(w)
    print(len(w))
    print(len(t))
    for i in range(len(w)):
        ele = pre_target_b(t[i], lis_beta, 'EF')
        res1 = ''
        res2 = ''
        if ele not in list_tag:
            res1 = w[i]
            res2 = t[i]
        elif ele=='B+EF':
            flag = 0
            for j in list_end:
                if j in w[i]:
                    flag=1
                    ind = w[i].index(j)
                    res1 = w[i][:ind]
                    res2 = t[i]
            if flag==0:
                res1 = w[i]
                res2 = t[i]
        lis_w.append(res1)
        lis_t.append(res2)
        number = number-1
    return lis_w, lis_t

def prepro_b(input):
    lis_w, lis_t = to2lists(input)

    space_list = rememberSpace(input,' ')
    space_location = convertSpace(space_list, lis_w)
    union(space_location, lis_w)
    union(space_location, lis_t)
    union_t(lis_t)
    union_w(lis_w, lis_t)
    
    str_w = ''
    str_t = ''
    for i in range(len(lis_w)):
        str_w = str_w + lis_w[i]
        str_t = str_t + lis_t[i]
    
    data_w = str_w.split(' ')
    data_t = str_t.split(' ')
    
    lis_word, lis_tag = to2lists(input)
    
    lis_ind = []
    t_ind = 0
    jam1 = Jamodealer(lis_word)
    jam2 = Jamodealer(data_w)
    jam3 = Jamodealer(lis_tag)
    
    number, jam1.jamo, jam3.jamo = delete_end(jam1.jamo, jam3.jamo, lis_beta, lis_end)
    
    
    for i in range(len(data_w)-number-1):
        element = []
        leng = len(data_t[i].split('/'))
        res = jam2.jamo[i]
        ind = 0
        lenlen = 0
        #element.append(0)
        for j in range(leng):
            element.append(ind)
            ind = ind + len(jam1.jamo[t_ind])
            res = res[len(jam1.jamo[t_ind]):]
            
            lenlen = len(jam1.jamo[t_ind])+lenlen
            t_ind = t_ind+1
        
        #element = element[:-1]
        element.append(len(jam2.jamo[i]))
        lis_ind.append(element)
    
    return data_w, data_t, lis_ind

def pre_target_b(input, lis, target):
    result = input
    if target in input:
        res = input.split('/')
        for j in range(len(res)):
            if target in res[j] and '+' in res[j]:
                loc = res[j].index('+')
                wd = res[j][:loc]
                if wd not in lis:
                    res[j] = re.sub(wd, 'B', res[j])
        result = '/'.join(res)
    return result

def pre_target_b_test(input, lis, target):
    result = input
    if target in input:
        res = input.split('/')
        for j in range(len(res)):
            flag=0
            for k in lis:
                if k in res[j] and len(res[j].replace(target, '', 1))!=0 and flag==0:
                    loc = res[j].index(k)
                    #wd = res[j][:loc]
                    res[j] = res[j].replace(res[j][:loc], 'B+', 1)
                    flag=1
                
        result = '/'.join(res)
    return result

##############################

def delete_end_only(w, t, list_tag, list_end):
    
    lis_w = []
    lis_t = []
    
    w_last = w[-1]
    t_last = t[-1]
    
    number = len(w)
    for i in range(len(w)-1):
        if t[i+1]=='SF':
            ele = pre_target_b(t[i], lis_beta, 'EF')
            res1 = ''
            res2 = ''
            if ele not in list_tag:
                res1 = w[i]
                res2 = t[i]
            elif ele=='B+EF':
                flag = 0
                for j in list_end:
                    if j in w[i]:
                        flag=1
                        ind = w[i].index(j)
                        res1 = w[i][:ind]
                        res2 = t[i]
                if flag==0:
                    res1 = w[i]
                    res2 = t[i]
            lis_w.append(res1)
            lis_t.append(res2)
        else:
            lis_w.append(w[i])
            lis_t.append(t[i])
        number = number-1
    
    lis_w[-1] = w_last
    lis_t[-1] = t_last
    
    return lis_w, lis_t

def delete_end_only_test(w, t, list_tag, list_end):
    
    lis_w = []
    lis_t = []
    
    w_last = w[-1]
    t_last = t[-1]
    
    number = len(w)
    for i in range(len(w)-1):
        if t[i+1]=='SF':
            ele = pre_target_b(t[i], lis_beta, 'EF')
            res1 = ''
            res2 = ''
            if ele not in list_tag:
                res1 = w[i]
                res2 = t[i]
            elif 'B+' in ele:
                #print('ee')
                flag = 0
                for j in list_end:
                    if j in w[i] and flag==0:
                        flag=1
                        ind = w[i].index(j)
                        #res1 = w[i][:ind]
                        res1 = w[i].replace(j, '', 1)
                        res2 = t[i]
                        flag_plus = 0
                        for k in lis_plus:
                            if k in res2 and flag_plus==0:
                                res2 = res2.replace(k, '', 1)
                                flag_plus=1
                                
                        #res2 = t[i]
                        res2 = res2.replace('+EF', '', 1)
                if flag==0:
                    res1 = w[i]
                    res2 = t[i]
            lis_w.append(res1)
            #print(lis_w)
            #print(res1)
            lis_t.append(res2)
            #print(res2)
        else:
            lis_w.append(w[i])
            lis_t.append(t[i])
        number = number-1
    
    lis_w.append(w_last)
    lis_t.append(t_last)
    
    return lis_w, lis_t

##############################

def to2lists_beta(input, lis):
    
    lis_w, lis_t = to2lists(input)
    jam = Jamodealer(lis_w)
    lis_word, lis_tags = delete_end_only_test(jam.jamo, lis_t, lis_beta, lis)
    return lis_word, lis_tags

##############################

def prepro_after(input):
    lis_w, lis_t = to2lists(input)
    
    space_list = rememberSpace(input,' ')
    space_location = convertSpace(space_list, lis_w)
    #print(space_list)
    #print(space_location)
#     union(space_location, lis_w)
#     print(lis_w)
#     union(space_location, lis_t)
#     union_t(lis_t)
#     union_w(lis_w, lis_t)
    
    lis_w2, lis_t2 = to2lists_beta(input, lis_end)
    
    lis_w2 = lis_w2[:-1]
    lis_t2 = lis_t2[:-1]
    
    
    
    
    union(space_location, lis_w2)
    #print(lis_w)
    union(space_location, lis_t2)
    union_t(lis_t2)
    union_w(lis_w2, lis_t2)
    
    
    
    
    str_w = ''
    str_t = ''
    for i in range(len(lis_w2)):
        str_w = str_w + lis_w2[i]
        str_t = str_t + lis_t2[i]
    
    
    
    data_w = str_w.split(' ')
    data_t = str_t.split(' ')
    
    lis_word, lis_tag = to2lists_beta(input, lis_end)
    
    w_last = lis_word[-1]
    t_last = lis_tag[-1]
    
    lis_word = lis_word[:-1]
    lis_tag = lis_tag[:-1]
    
    lis_ind = []
    t_ind = 0
    jam1 = Jamodealer(lis_word)
    jam2 = Jamodealer(data_w)
    for i in range(len(data_w)):
        element = []
        leng = len(data_t[i].split('/'))
        res = jam2.jamo[i]
        ind = 0
        lenlen = 0
        #element.append(0)
        for j in range(leng):
            element.append(ind)
            ind = ind + len(jam1.jamo[t_ind])
            res = res[len(jam1.jamo[t_ind]):]
            
            lenlen = len(jam1.jamo[t_ind])+lenlen
            t_ind = t_ind+1
        
        #element = element[:-1]
        element.append(len(jam2.jamo[i]))
        lis_ind.append(element)
    
    return data_w, data_t, lis_ind, w_last, t_last

##############################

