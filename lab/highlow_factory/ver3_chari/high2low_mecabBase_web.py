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
#from hanspell import spell_checker
from khaiii import KhaiiiApi

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
lis_beta_ef = ['EP+EP+EF', 'EP+EF', 'EF', 'UNKNOWN']
lis_beta_ef_h = ['EF', 'UNKNOWN']

#이 부분 같은 경우는 마지막에 오는 것을 처리하는 것으로 단독으로만 들어가는게 좋겠지?
lis_tag_last = ['EF', 'UNKNOWN']

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

lis_ic = ['ㅇㅖ', 'ㄴㅔ', 'ㅇㅏㄴㅣㅇㅗ', 'ㅇㅏㄴㅣㅇㅛ']

# yo = [
#     '을까', 'ㄹ까', '지', '으니까', '어', '아',
#     '는데', 'ㄴ가', 'ㄹ게', '래', '잖아', '네',
#     '여', 'ㄹ래', '게', '나', '군', '을게', '다고',
#     '지만', '은데', 'ㄴ지', '는지', '라고', 'ㄴ데',
#     '는걸', '아서', '거든', '더라고', '어서', '려고',
#     '을래', '대', 'ㄴ대', '던데', '더군', '여서', '건가',
#     '어야지', 'ㄹ걸', 'ㄹ께', '아야지', '다면서', '는군',
#     'ㄴ다고', '은가', '다니', '다면', '실까', '가', '신가',
#     '서', '까'
# ]

P_LIST = ['.', '?', '!', '\'', '\"', 'ᆞ', 'ᆢ', 'ㆍ',  '”', '’',')', '(', ',', '”']

SV_LIST = ['\'', '\"', ':', ';']

lis_plus = [
    
    'EP', 'VCP', 
    
]

mec = Mecab()
khai = KhaiiiApi()

def detect_h(input, lis_end_h, lis_end_l):
    for i in lis_end_h:
        if len(input)>=len(i):
            if input[-len(i):]==i:
                return 1
            
    for i in lis_end_l:
        if len(input)>=len(i):
            if input[-len(i):]==i:
                return 0
            
    return -1

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

def to2lists_khaiii(input):
    lis_word = []
    lis_tag = []
    analyzed = khai.analyze(input)  
    for data in analyzed:
        for morph in data.morphs:
            lis_word.append(morph.lex)
            lis_tag.append(morph.tag)
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

def union_t_03(lis_tag):
    
    for i in range(1, len(lis_tag)):
        if lis_tag[i-1] ==' ' or lis_tag[i]==' ':
            lis_tag[i] = lis_tag[i]
        else:
            lis_tag[i] = '/'+lis_tag[i]
            
def union_w_03(lis_w, lis_tag):
    
    for i in range(1, len(lis_w)):
        if lis_tag[i]==' SF':
            lis_w[i] = ' '+lis_w[i+1]
def proc_khaiii_with_Tag(input):
    
    r_sen = input
    
    res1 = ''
    res2 =''
    slis = []
    for i in range(len(input)):
        if r_sen[i]==' ':
            slis.append(1)
        elif r_sen[i]=='  ':
            slis.append(2)
            
    wlis = r_sen.split(' ')
    
    uu = khai.analyze(wlis[0])
    
    elem = ''
    tag =''
    
    for data in uu[0].morphs:
        elem = elem + data.lex+'/'
        tag = tag+data.tag+'/'
    
    res1 = res1+elem
    res2 = res2+tag
    
    for i in range(len(slis)):
        elem = ''
        tag = ''
        elem = elem+slis[i]*' '
        if i != len(wlis)-1:
            uu = khai.analyze(wlis[i+1])
            for data in uu[0].morphs:
                elem = elem+data.lex+'/'
                tag = tag+data.tag+'/'
        res1 = res1+elem
        res2 = res2+tag
    return res1,res2


def prepro_khaiii(input):
    lis_w, lis_t = to2lists_khaiii(input)

    space_list = rememberSpace(input,' ')
    space_location = convertSpace(space_list, lis_w)
    union(space_location, lis_w)
    union(space_location, lis_t)
    union_t_03(lis_t)
    union_w_03(lis_w, lis_t)
    
    str_w = ''
    str_t = ''
    for i in range(len(lis_w)):
        str_w = str_w + lis_w[i]
        str_t = str_t + lis_t[i]
    
    data_w = str_w.split(' ')
    data_t = str_t.split(' ')
    
    lis_word, lis_tag = to2lists_khaiii(input)
    
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

        element.append(len(jam2.jamo[i]))
        lis_ind.append(element)
        
    return data_w, data_t, lis_ind

def prepro_beta_khaiii(input, lis_ef, tag_last, lis_w_last, lis_w_last_not):
    data_w, data_t, lis_ind = prepro_khaiii(input)
    
    last_words = []

    data_w_jamo = []

    data_t_after = []
    
    lis_target_ind = []
    
    for i in data_w:
        jam_ele = Jamodealer(i)
        ele = ''
        for j in jam_ele.jamo:
            ele = ele+j
        data_w_jamo.append(ele)
    
    for i in range(len(data_t)):
        #if i<len(data_t)-1:
        if i<len(data_t):
            lis_res = []
            for ind in range(len(lis_ind[i])-1):
                lis_res.append(data_w_jamo[i][lis_ind[i][ind]:lis_ind[i][ind+1]])

        
        if 'EF/SF' in data_t[i] or 'EF/SV' in data_t[i] or 'UNKNOWN/SF' in data_t[i] or 'UNKNOWN/SV' in data_t[i]:# and 'EC/SF' not in data_t[i]:
            if 'EF/SF' in data_t[i] or 'UNKNOWN' in data_t[i]:
                elements = data_t[i].split('/')
                flag = 0

                for j in range(len(elements)):
                
                    flag_end = detect_h(lis_res[j], lis_w_last,  lis_w_last_not)

                    if elements[j] in lis_ef and flag_end==1: #and j == len(elements)-1:

                        elements[j] = 'NULL'
                    
                        last_words.append(data_w_jamo[i][lis_ind[i][j]:lis_ind[i][j+1]])
                        lis_res[j]=''
                    
                        lis_target_ind.append(i)
                    
#                         elements_post = '/'.join(elements)
#                         data_t_after.append(elements_post)
                        
                    elif 'EF' in elements[j] and flag_end==1:# + EF를 처리하는 부분이므로 + EF 만을 마지막에서 처리한다.
                        for jam in lis_w_last:
                            if len(lis_res[j])>=len(jam):

                                res_out_punc = lis_res[:lis_ind[i][-2]][j]

                                if res_out_punc[-len(jam):]==jam:

                                    #print(jam)
                                    lis_target_ind.append(i)
                                
                                    last_words.append(jam)
                                    lis_res[j] = lis_res[j].replace(jam, '', 1)

                                    for k in tag_last:

                                        if k in elements[j]:
                                        
                                            if '+' in elements[j]:
                                            
                                                ind = elements[j].index('+'+k)
                                                elements[j] = elements[j][:ind]
                                    break
                                
                                elif lis_w_last.index(jam)==len(lis_w_last)-1:#new
                                    for k in tag_last:

                                        if k in elements[j]:
                                        
                                            if '+' in elements[j]:
                                            
                                                ind = elements[j].index('+'+k)
                                                elements[j] = elements[j][:ind]
                                            
                                    lis_target_ind.append(i)
                                    last_words.append('')
                                    break

                
                elements_post = '/'.join(elements)
                data_t_after.append(elements_post)
                
                data_w_jamo[i] = ''.join(lis_res)

                #elements_post = '/'.join(elements)
                #data_t_after.append(elements_post)
                    
            #######################################
            
            #data_t_after.append(data_t[i])
            
        elif 'EC/SF' in data_t[i] or 'JX/SF' in data_t[i]:
            #print('ee')
            elements = data_t[i].split('/')
            
            flag = 0
            for j in range(len(elements)):
                
                flag_end = -1
                if 'EC' in elements[j] or 'JX' in elements[j]:
                    flag_end = detect_h(lis_res[j], lis_w_last, lis_w_last_not)

                #print(flag_end)
                if flag_end==1 and i not in lis_target_ind:
                    for jam in lis_w_last:

                        if len(jam)<=len(lis_res[j]):
                            #print(lis_res[j])
                            if lis_res[j][-len(jam):]==jam:

                                last_words.append(jam)
                                lis_res[j] = lis_res[j].replace(jam, '', 1)
                                #print(lis_res[j])
                    lis_target_ind.append(i)
                    #last_words.append('')
            data_t_after.append(data_t[i])
            data_w_jamo[i] = ''.join(lis_res)
        ####### #######
            
        else:
            data_t_after.append(data_t[i])
            
    
    
        lis_normal = []
    
        for i in data_w_jamo:
            jam_n = Jamodealer(i)
            lis_normal.append(jam_n.make_one())
    
        
        
    for i in range(len(lis_target_ind)):
        if 'ㅅㅔㅇㅛ' == last_words[i] or 'ㄹㄹㅐㅇㅛ' == last_words[i]:
            
            for wk in lis_wk:
                #print(data_w_jamo[lis_target_ind[i]][-len(wk[0])-1:-1])
                if data_w_jamo[lis_target_ind[i]][-len(wk[0])-1:-1] ==wk[0]:
                    #print('rrrr')
                    ele = data_w_jamo[lis_target_ind[i]][:-len(wk[0])-1]
                    ele = ele + wk[1]
                    ele = ele + data_w_jamo[lis_target_ind[i]][-1]
                    data_w_jamo[lis_target_ind[i]] = ele
                    
                    break
        
    return data_w, data_t, lis_ind, data_w_jamo, data_t_after, last_words, lis_target_ind

def prepro_ch03(input, lis_ef, tag_last, lis_w_last, lis_w_last_not, lis_ic):
    
    lis_res_word = []
    
    lis_input = input.split()
    lis_word = []
    lis_tag = []
    lis_last_word = []
    lis_ind = []
    
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
        
        if 'EF/SF' in lis_tag[i] or 'EF/SV' in lis_tag[i] or 'EF/SC' in lis_tag[i] or 'JX/SF' in lis_tag[i] or 'JX/SC' in lis_tag[i] or 'IC' in lis_tag[i] or 'IC' in lis_tag[i] or (('NP' in lis_tag[i] or 'NNG' in lis_tag[i]) and ('ㅈㅓ' in lis_word[i] or 'ㅈㅔ' in lis_word[i] or 'ㄷㅏㅇㅅㅣㄴ' in lis_word[i])):
            elemen_t = lis_tag[i].split('/')
            elemen_w = lis_word[i].split(' ')
            flag = 0
            
            
            for j in range(len(elemen_t)):

                flag_end = detect_h(elemen_w[j], lis_w_last_not, lis_w_last)

                
                if (flag_end == 1 and 'EF' in elemen_t[j]) or (flag_end == 1 and 'JX' in elemen_t[j]):
                    
                    for jam in lis_w_last_not:
                        
                        if len(elemen_w[j])>=len(jam):
                            
                            if elemen_w[j][-len(jam):]==jam:
                                
                                
                                lis_ind.append(i)
                                lis_last_word.append(jam)
                                elemen_w[j] = elemen_w[j][:-len(jam)]
                                elemen_w[j] = elemen_w[j] + '__+__'
                                
                                break
                                
#                 elif 'IC' in elemen_t[j] or 'IC' in elemen_t[j]:
                    
#                     for ii in lis_ic:
                        
#                         if len(elemen_w[j])>=len(ii):
                            
#                             if elemen_w[j][-len(ii):]==ii:
                                
                                
#                                 lis_ind.append(i)
#                                 lis_last_word.append(ii)
#                                 elemen_w[j] = elemen_w[j][:-len(ii)]
#                                 elemen_w[j] = elemen_w[j] + '__+__'
                                
#                                 break
                                
                elif (('NP' in lis_tag[i] or 'NNG' in lis_tag[i]) and ('ㅈㅓ' in lis_word[i] or 'ㅈㅔ' in lis_word[i] or 'ㄷㅏㅇㅅㅣㄴ' in lis_word[i])) or ('IC' in lis_tag[i] and('ㄴㅔ' in lis_word[i] or 'ㅇㅏㄴㅣㅇㅛ' in lis_word[i])):
                    
                    jam1 = Jamodealer(elemen_w)
                    s = jam1.make_one()

                    key_u = 0

                    ss = proc_khaiii_with_Tag(s)
                    tagt = ss[1].split('/')[:-1]
                    wordw = ss[0].split('/')[:-1]

                    for u in range(len(tagt)):
                        if tagt[u]=='NP':
                            if wordw[u]=='저' or wordw[u]=='제':
                                key_u = 1
                            elif wordw[u]=='당신':
                                key_u = 2
                        elif tagt[u]=='IC':
                            if wordw[u]=='네':
                                key_u = 3
                        elif tagt[u]=='VCN' or tagt[u]=='IC':
                            if wordw[u][:2]=='아니':
                                key_u = 4
            
                    flag = 0
                    for ind in range(len(elemen_t)):
                        #print(elemen_w[ind])
                        if flag==0 and key_u>0:

                            if key_u == 1:

                                if elemen_t[ind][:2]=='NP' or elemen_t[ind][:3]=='NNG':
                                    
                                    if elemen_w[ind][:2] == 'ㅈㅓ':
                                        
                                        elemen_w[ind] = 'ㄴㅏ' + elemen_w[ind][2:]
                                        flag = 1

                                    elif elemen_w[ind][:2] == 'ㅈㅔ':

                                        elemen_w[ind] = 'ㄴㅐ' + elemen_w[ind][2:]
                                        flag = 1
                            
                            elif key_u==2:
                                if len(elemen_w[ind])>=6:
                                    if elemen_w[ind][:6] == 'ㄷㅏㅇㅅㅣㄴ':

                                        elemen_w[ind] = 'ㄴㅓ' + elemen_w[ind][6:]
                                        flag = 1
                                        if len(elemen_t)-1 >ind:
                                            if elemen_t[ind+1] == 'JX' or elemen_t[ind+1] == 'JKS' or elemen_t[ind+1] == 'JKO' or elemen_t[ind+1] == 'JKB':
                                                if elemen_w[ind+1] == 'ㅇㅡㄹ':
                                                    elemen_w[ind+1] = 'ㄹㅡㄹ'
                                                elif elemen_w[ind+1] == 'ㅇㅡㄴ':
                                                    elemen_w[ind+1] = 'ㄴㅡㄴ'
                                                elif elemen_w[ind+1] == 'ㅇㅣ':
                                                    elemen_w[ind+1] = 'ㄱㅏ'
                                                    
                            elif key_u==3:
                                if len(elemen_t)>1:
                                    
                                    if elemen_t[1]=='SC' or elemen_t[1]=='SF':
                                        if elemen_w[ind][:2] == 'ㄴㅔ':
                                        
                                            elemen_w[ind] = 'ㅇㅡㅇ' + elemen_w[ind][2:]
                                            flag = 1
                            else:
                                if elemen_t[ind][:2] == 'IC':

                                    if elemen_w[ind][4:6] == 'ㅇㅛ':

                                        elemen_w[ind] = elemen_w[ind][:4] + elemen_w[ind][6:]

                                        flag = 1

                    
                                
            res_w = ''.join(elemen_w)
            lis_result.append(res_w)
                                
        else:
            
            rere = lis_word[i].split(' ')
            
            resres = ''.join(rere)
            
            lis_result.append(resres)
            
            
    return lis_result, lis_tag, lis_ind, lis_last_word

######높임말 -> 반말
#현재 만들어진 것은 EF만 잘라낼 것이다. 
#원래 ef사전에 mapping 되는 것을 찾아낸다.
#python dictionary로 접근
#종결어미 처리
EF = {
    ###하십시오체###
    #평서문
    #'ㅂㄴㅣㄷㅏ': 'ㄷㅏ',
    'ㅂㄴㅣㄷㅏ': 'special3',
    'ㅅㅡㅂㄴㅣㄷㅏ':'special2',
    'ㅇㅗㄹㅅㅣㄷㅏ':'ㄷㅏ', #**
    'ㅂㅈㅣㅇㅛ':'지', #**
    'ㅅㅣㅂㄴㅣㄷㅏ':'special1',
    'ㅇㅡㅅㅣㅂㄴㅣㄷㅏ':'ㅇㅡㅅㅣㄴㄷㅏ',
    'ㅇㅡㅅㅣㅂㄴㅣㄲㅏ':'ㅇㅡㅅㅣㄴㅣ',

    #의문문
    'ㅅㅡㅂㄴㅣㄲㅏ':'ㄴㅣ',
    'ㅂㄴㅣㄲㅏ': 'ㄴㅣ',
    'ㅅㅣㅂㄴㅣㄲㅏ':'special1', #EP+EF
    #명령법
    'ㅇㅡㅅㅔㅇㅛ': 'special0',
    'ㅅㅔㅇㅛ':'special1',
    'ㅅㅣㅇㅓㅇㅛ': 'special1',
    'ㅅㅣㅂㅅㅣㅇㅗ':'ㅅㅣㅇㅗ',
    #청유법
    'ㅂㅅㅣㄷㅏ':'special4',
    'ㅇㅡㅂㅅㅣㄷㅏ':'special4',
    ###하오체###
    
    ###해요체###
    #평서문
    'ㅇㅓㅇㅛ':'ㅇㅓ',
    'ㅇㅏㅇㅛ':'ㅇㅏ',
    'ㅈㅛ':'ㅈㅣ',
    'ㅇㅔㅇㅛ':'ㅇㅑ',
    'ㅇㅖㅇㅛ':'ㅇㅑ',
    'ㅇㅛ':'special5',
    'ㄷㅐㅇㅛ':'ㄷㅐ',
    'ㄷㅔㅇㅛ':'ㄷㅔ',
    'ㄴㅔㅇㅛ':'ㄴㅔ',
    'ㄴㅡㄴㄷㅔㅇㅛ':'ㄴㅡㄴㄷㅔ',
    'ㄱㅓㄷㅡㄴㅇㅛ':'ㄱㅓㄷㅡㄴ',
    'ㄱㅜㄴㅇㅛ': 'ㄱㅜㄴㅏ',
    'ㅇㅡㄴㄷㅔㅇㅛ':'ㅇㅡㄴㄷㅔ',
    'ㅈㅏㄱㅜㅇㅛ':'ㅈㅏㄱㅜ',
    'ㄴㅣㄲㅏㅇㅛ': 'ㄴㅣㄲㅏ',
    'ㅈㅣㅇㅛ':'ㅈㅣ',
    
    #의문문
    'ㄴㅏㅇㅛ':'special6',
    'ㄹㄲㅏㅇㅛ':'ㄹㄲㅏ',
    'ㅇㅡㄹㄲㅏㅇㅛ':'ㅇㅡㄹㄲㅏ',
    'ㄴㄱㅏㅇㅛ':'ㄴㄱㅏ',
    'ㄹㄹㅐㅇㅛ':'ㄹㄹㅐ',
    'ㄹㅐㅇㅛ':'ㄹㅐ',
    'ㄱㅗㅇㅛ':'ㄱㅗ',
    'ㅇㅡㄴㄱㅏㅇㅛ':'ㅇㅡㄴㄱㅏ',
    'ㅇㅣㄴㄱㅏㅇㅛ':'ㅇㅣㄴㄱㅏ',
}
need_origin_EF = {
    'ㅂㅅㅣㄷㅏ':'ㅈㅏ',
}
#'ㄹ'규칙 활용 -> ㄹ 규칙 활용이 일어나는 동사들을 최대한 모아두고, 만약 하나의 단어에 여러 의미가 담긴다면?
EF_R_rule= {
    'ㄱㅜ':'ㄹ',
    'ㄴㅗ':'ㄹ',
    'ㄴㅏ':'ㄹ',
    'ㄷㅗ':'ㄹ',
    'ㄷㅡ':'ㄹ',
    'ㄷㅏ':'ㄹ',
    'ㄷㅜ':'ㄹ',
    'ㅂㅜ':'ㄹ',
    'ㄲㅗ':'ㄹ',
    'ㅁㅣ':'ㄹ',
    'ㅁㅜ':'ㄹ',
    #'ㅂㅗㅍㅜ':'ㄹ', #error predicate 수정
    'ㅂㅜ':'ㄹ',
    'ㅅㅡ':'ㄹ',
    'ㄸㅓ':'ㄹ',   
}

def treatSF(stc, ex):
    ind_point = -1
    point = ''
    
    # for i in range(len(stc)):
    #     if stc[i] in P_LIST:
    #         point = stc[i]
    #         break
            
    # if point in P_LIST:
    #     ind_point = stc.index(point)
    # print('uhyo',stc)
    if '__+__' in stc:
        ind_point = stc.index('__+__')
        stc = stc.replace('__+__', '', 1)
    
    r_word = ''
    r_pun = ''
    
    if ind_point!=-1:
        r_word = stc[:ind_point]
        r_pun = stc[ind_point:]
    else:
        r_word = stc
    return r_word+ex+r_pun

def delete_EP_si(stn, taglist):
    si = stn[-3:-1]
    eusi = stn[-5:-1]
    check_si = taglist[-11:-2]
    #@
    
    result =''
    flag = 0
    if taglist.find('SF') !=-1:
        if (eusi =='ㅇㅡㅅㅣ') and (check_si.find('EP+EP')!=-1 or check_si.find('EP/NULL')!=-1):
            result = stn[:-5]+stn[-1]
            flag = 1
        elif (si =='ㅅㅣ') and (check_si.find('/EP/')!=-1):
            #@
            #print('alalalalal')
            result = stn[:-3]+stn[-1]
            #print('s')

    return result, flag

def check_VV_VA(sentence, tag):
    #t= tag[-9:-3]
    #print(t, tag)
    tt = tag.split('/SF')
    t= tt[0][-6:]
    if 'VV' in t or 'VX' in t or 'XSV' in t or ('VV/EP' in tag and 'ㅅㅣ' in sentence[-5:-1]) :
        return 1
    elif 'VA' in t:
        return 0
    else:
        return -1
def detach_endmark(sentence):
    endmark = sentence[-6:-1]
    #print(sentence, endmark)
    if endmark == '__+__':
        sentence = sentence[:-6]+sentence[-1]
    else:
        endmark = -1
    return sentence, endmark
def attach_endmark(sentence):
    endmark = '__+__'
    sentence = sentence[:-1]+endmark+sentence[-1]
    return sentence

## 'ㅏ', 'ㅗ' 처리
def convertSpecialCase_AhOh(stc):
    #print(sentence[-1][-2:])
    #print(sentence[-1][-4:])
    ## 수정할 필요 있음!
    #danger
    sentence, endmark = detach_endmark(stc)
    if sentence[-3:-1] == 'ㅍㅡ' or sentence[-3:-1] == 'ㅃㅡ':
        if sentence[-5:-3].find('ㅏ') !=-1 or sentence[-5:-3].find('ㅗ')!=-1:
            return 'ㅏ'
        else:
            return 'ㅓ'
    elif sentence[-3:].find('ㅏ') !=-1 or sentence[-3:].find('ㅗ') !=-1:
        return 'ㅇㅏ'
    else:
        return 'ㅇㅓ'
def treatFormal_vv(sentence):
    formal_vv ={
        'ㄱㅖ':'ㅇㅣㅆㅇㅡ',
        'ㅈㅜㅁㅜ':'ㅈㅏ',
        'ㅈㅏㅂㅅㅜ':'ㅁㅓㄱㅇㅡ'
    }
    for key in formal_vv:
        if sentence.find(key) !=-1:
            sentence = sentence.replace(key,formal_vv[key])
    return sentence
def check_NoRule(stem,predicate):
    #this is temp function. Need to modify this function
    if predicate.find('ㅓ') !=-1:
        #print(stem+predicate)
        if (stem+predicate) =='ㄱㅡㄹㅓ':
            return 'ㅐ'
    else:
        return ''
#'ㅇㅗㄹㅡ'
def convertSpecialCase_SaeYo(stc, ending, tag):
    result = ''
    end_EF=''
    final=''
    sentence, endmark = detach_endmark(stc)
    #print(endmark)
    pun = sentence[-1:]
    predicate = sentence[-3:-1]
    stem = sentence[:-3]
    isVcp = tag[-12:]
    #print(sentence, ending, tag, predicate)
    #만약 VCP가 있다면 '야'를 붙이고 return 한다.
    if isVcp.find('VCP/EP+EF') != -1 or isVcp.find('VCP+EP+EF') !=-1:
        final = 'ㅇㅑ'
        if endmark !=-1: # 문장에 __+__가 있었으면
            sentence = attach_endmark(sentence)
        converted = treatSF(sentence, final)
        return converted
    # 'ㄹ'규칙 활용
    elif predicate in EF_R_rule:
        result= EF_R_rule[predicate]
        #sentence[-1] += result
        ##'아' 또는 '어' 로 처리
        end_EF = convertSpecialCase_AhOh(sentence)
        #sentence.append(end_EF)
        final = result +end_EF
        #print(final)
    #'르' 불규칙 활용
    elif predicate =='ㄹㅡ':
        # 용언 종성에 ㄹ이 있다면
        #sentence[-1] = sentence[-1].replace('ㄹㅡ','')
        predicate = predicate.replace('ㄹㅡ','')
        sentence = stem+predicate + pun
        end_EF = convertSpecialCase_AhOh(sentence)
        end_EF = end_EF[-1]
        #print(end_EF, sentence, 'sss')
        if sentence[-1].find('ㄹ') != -1:
            final = 'ㄹ'+end_EF
        else:
            final  = 'ㄹㄹ'+end_EF
        
    #'우' 불규칙 활용
    # '푸'를 제외한 다른 'ㅜ'는 'ㅓ'와 결합
    elif predicate.find('ㅍㅜ') !=-1:
        #sentence[-1] = sentence[-1].replace('ㅜ','ㅓ')
        predicate = predicate.replace('ㅜ','')
        sentence = stem+predicate + pun
        final = 'ㅓ'
        #final = sentence[-1][-1:]
    #'오' 불규칙 활용(고려하지 않을 수 있음)
    #'하' 불규칙 활용
    elif predicate.find('ㅎㅏ') !=-1:
        #sentence[-1] = sentence[-1].replace('ㅏ','ㅐ')
        predicate = predicate.replace('ㅏ','')
        sentence = stem + predicate + pun
        final = 'ㅐ'
    #활용이 안되었던 용언 처리
    else:
        if predicate.find('ㅡ') !=-1:
            end_EF = convertSpecialCase_AhOh(sentence)
            #sentence[-1] = sentence[-1].replace('ㅡ',end_EF)
            predicate = predicate.replace('ㅡ','')
            sentence = stem + predicate + pun
            #print(sentence, '처리후')
            final = end_EF[-1]
        ## 수정할 필요 있음!!
        elif predicate.find('ㅗ') !=-1:
            #sentence[-1] = sentence[-1].replace('ㅗ','ㅘ')
            predicate = predicate.replace('ㅗ','')
            sentence = stem+predicate+ pun
            final = 'ㅘ'
        elif predicate.find('ㅜ') !=-1:
            #sentence[-1] = sentence[-1].replace('ㅜ','ㅝ')
            predicate = predicate.replace('ㅜ','') 
            sentence = stem + predicate+ pun
            final = 'ㅝ'
        elif predicate.find('ㅣ') !=-1:
            #sentence[-1] = sentence[-1].replace('ㅣ','ㅕ')
#             if predicate == 'ㅇㅣ':
#                 sentence = sentence.replace('ㅇㅣ','')
            predicate = predicate.replace('ㅣ','')
            sentence = stem+predicate+ pun
            final = 'ㅕ'
        else:
            final = convertSpecialCase_AhOh(sentence)
            #sentence = sentence.append(final)
            if  predicate.find('ㅏ') !=-1:
                final = ''
            elif  predicate.find('ㅓ') !=-1:
                final = check_NoRule(stem,predicate)
                #print(sentence)
                if final != '':
                    ind = sentence.rfind('ㅓ')
                    sentence = sentence[:ind]+sentence[ind+1:]
                    #print(sentence,'a')
            elif  predicate.find('ㅐ') !=-1:
                final = ''
#                 return final, sentence
#             return final, sentence
#     return final, sentence
    if endmark !=-1: # 문장에 __+__가 있었으면
        sentence = attach_endmark(sentence)
    converted = treatSF(sentence, final)
    #print(converted)
    return converted
    
def convertSpecialCase_Da(stc, ending, taglist):
    #print(sentence, ending, taglist)
    sentence, endmark = detach_endmark(stc)
    final =''
    isEp = sentence[-2:-1]
    if (isEp == 'ㅆ' or sentence.find('ㅇㅏㄶ') !=-1)and (taglist.find('VV/EF') !=-1 or taglist.find('VX/EF') !=-1):
        final = 'ㄷㅏ'
    elif taglist.find('EP/EF') !=-1 or taglist.find('VA/EF') !=-1 or taglist.find('VX/EF') !=-1:
        #print('다로 변경할 것')
        final = 'ㄷㅏ'
    elif taglist.find('VV/EF') !=-1:
        final = 'ㄴㅡㄴㄷㅏ'
    elif taglist.find('VV') !=-1:
        #print('현재형 동사가 왔으므로, 는다로 변경할 것')
        final = 'ㄴㅡㄴㄷㅏ'
    if endmark !=-1: # 문장에 __+__가 있었으면
        sentence = attach_endmark(sentence)
    converted = treatSF(sentence, final)
    return converted

#def convertSpecialCase_Nida(sentence, ending, taglist, kh_stn, kh_end, kh_tag):
def convertSpecialCase_Nida(sentence, ending, taglist):
    #print(sentence, ending, taglist)
    #시가 있으면 ㄴ다를 붙인다. 
    #형용사, 서술격 조사일 경우 convertSpecialCase_SaeYo를 통해 변경한 다음, 아/어를 제거 후 다를 붙이고
    #동사일 경우 ㄴ다를 붙여서 해결한다. 
    predicate = check_VV_VA(sentence, taglist)
    #VV
    if predicate == 1:
        final = 'ㄴㄷㅏ'
        converted = treatSF(sentence, final)
    #VA
    #형용사의 경우, 세요를 거친 후 마지막을 붙인다면 이상해질 수 있다. 그냥 khaiii를 쓰는 것이 안전하다고 판단된다. 
    elif predicate == 0:
        final = 'ㄷㅏ'
        #print(treatSF(sentence,ending))
        temp=treatSF(sentence,ending)
        jam1 = Jamodealer(temp)
        s = jam1.make_one()
        #print(temp, taglist)
        converted_kh = proc_khaiii(s)
        converted_kh = converted_kh.replace('ㅂ니다', '__+__')
        #print(converted_kh)
        converted = treatSF(converted_kh, final)
    else:
        final = 'ㄷㅏ'
        converted = treatSF(sentence, final)
    return converted
def convertSpecialCase_Yo(stc, ending, tag):
    sentence, endmark = detach_endmark(stc)
    pun = sentence[-1:]
    predicate = sentence[-3:-1]
    stem = sentence[:-3]
    isVcp = tag[-11:]
    #@
    # print(sentence, ending, pun, predicate, stem, isVcp)
    temp =''
    ni = 0
    after_si, ni = delete_EP_si(sentence, tag)
    # print(after_si, ni)
    if after_si != '':
        sentence = after_si
        after_si =''
    
    if isVcp.find('VCP') != -1:
        final = 'ㅇㅑ'
    #temporary condition(일시적으로 넣어둔 오류 문장 처리 기능 -> 에요)
    # elif sentence[-3:-1]=='ㅇㅔ':
    #     sentence = sentence[:-3]+pun
    #     final = 'ㅇㅑ'
    else:
        final = ''
    
    if endmark !=-1: # 문장에 __+__가 있었으면
        sentence = attach_endmark(sentence)
    
    converted = treatSF(sentence, final)
    return converted
def convertSpecialCase_NaYo(sentence, ending, taglist):
    #print(sentence, ending, taglist)
    final ='ㄴㅣ'
    if taglist.find('/VCP+EF/') !=-1:
        final='ㄴㅏㄴㅣ'
    converted = treatSF(sentence, final)
    return converted

##if Verb & adjective
## '-시' 등 선어말 처리
## 습니다는 동사면 '는다', 그외에는 '다'로 간다
def rememberSpace_k(lis, input):
    
    rlis = []
    
    for i in range(len(lis)):
        if lis[i]==input:
            rlis.append(i)
            
    for i in range(len(rlis)):
        rlis[i] = rlis[i]-i      
    return rlis

def convertSpace_k(lis_space,lis_lis):
    
    rlis = []
    k=0
    for i in range(len(lis_lis)):
        
        if k in lis_space:
            rlis.append(i)
            
        k = k+len(lis_lis[i])
        
    #print(rlis)  
    return rlis

def proc_khaiii(input):
    
    r_sen = input
    
    res = ''
    slis = []
    for i in range(len(input)):
        if r_sen[i]==' ':
            slis.append(1)
        elif r_sen[i]=='  ':
            slis.append(2)
            
    wlis = r_sen.split(' ')
    
    uu = khai.analyze(wlis[0])
    
    elem = ''
    
    for data in uu[0].morphs:
        elem = elem + data.lex
    
    res = res+elem
    
    for i in range(len(slis)):
        elem = ''
        elem = elem+slis[i]*' '
        if i != len(wlis)-1:
            uu = khai.analyze(wlis[i+1])
            for data in uu[0].morphs:
                elem = elem+data.lex
        res = res+elem
    return res

def proc_khaiii_with_Tag(input):
    
    r_sen = input
    
    res1 = ''
    res2 =''
    slis = []
    for i in range(len(input)):
        if r_sen[i]==' ':
            slis.append(1)
        elif r_sen[i]=='  ':
            slis.append(2)
            
    wlis = r_sen.split(' ')
    
    uu = khai.analyze(wlis[0])
    
    elem = ''
    tag =''
    
    for data in uu[0].morphs:
        elem = elem + data.lex+'/'
        tag = tag+data.tag+'/'
    
    res1 = res1+elem
    res2 = res2+tag
    
    for i in range(len(slis)):
        elem = ''
        tag = ''
        elem = elem+slis[i]*' '
        if i != len(wlis)-1:
            uu = khai.analyze(wlis[i+1])
            for data in uu[0].morphs:
                elem = elem+data.lex+'/'
                tag = tag+data.tag+'/'
        res1 = res1+elem
        res2 = res2+tag
    return res1,res2

class Changer(object):
    
    #def make_end_low(self, sentence, ending, taglist, kstn, kend, ktag):
    def convert_EF(self, sentence, taglist, ending):
        re_value =''
        temp =''
        ni = 0
        flag = 0
        
        #존칭 동사 또는 보조 동사를 파악하고 이를 변환 전에 미리 바꿔주어야 한다. 
        for key in EF:
            if ending == key:
                flag = 1
                re_value = EF[key]
                #나요, 으세요(으세요, 세요 모두 함수에서 커버 가능), 습니까 case
                if re_value == 'special0':
                    #시처리하기
                    after_si, ni = delete_EP_si(sentence, taglist)
                    if after_si != '':
                        sentence = after_si
                        after_si =''
                    temp = convertSpecialCase_AhOh(sentence)
                    re_value = treatSF(sentence, temp)
                    #ㅗ,ㅜ 이면 ㅘ, ㅝ로 결합할 것
                    #print(re_value)
                #-세요,십니다, 십니까
                elif re_value == 'special1':
                    #시처리하기
                    after_si, ni = delete_EP_si(sentence, taglist)
                    if after_si != '':
                        sentence = after_si
                        after_si =''
                    re_value = convertSpecialCase_SaeYo(sentence, ending, taglist)
                elif re_value == 'special2':
                    re_value = convertSpecialCase_Da(sentence, ending, taglist)
                elif re_value == 'special3':
                    #시처리 안함 '시' 보존
                    #re_value = convertSpecialCase_Nida(sentence, ending, taglist, kstn, kend, ktag)
                    re_value = convertSpecialCase_Nida(sentence, ending, taglist)
                elif re_value == 'special4':
                    re_value = convertSpecialCase_SaeYo(sentence, ending, taglist)
                    #print(re_value)
                    if ending == 'ㅇㅡㅂㅅㅣㄷㅏ':
                        temp = convertSpecialCase_AhOh(sentence)
                        re_value = treatSF(sentence, temp)
                elif re_value == 'special5':
                    re_value = convertSpecialCase_Yo(sentence, ending, taglist)
                elif re_value == 'special6':
                    re_value = convertSpecialCase_NaYo(sentence, ending, taglist)
                else:
                    #위험하기 때문에 데이터 확인 후 수정
#                     if taglist.find('EP') !=-1 and sentence[-4:].find('ㅅㅣ.'):
#                         sentence = delete_EP_si(sentence, taglist)
#                         re_value = convertSpecialCase_SaeYo(sentence, ending)
#                     else:
#                         re_value = treatSF(sentence,re_value)
                    re_value = treatSF(sentence,re_value)
        if flag ==0:
            return treatSF(sentence, ending)
        # print(sentence)
        return re_value
    
    def convert_IC(self, sentence, taglist, ending):
        IC = {'ㅇㅖ':'ㅇㅡㅇ', 'ㄴㅔ':'ㅇㅡㅇ', 'ㅇㅏㄴㅣㅇㅗ':'ㅇㅏㄴㅣ', 'ㅇㅏㄴㅣㅇㅛ':'ㅇㅏㄴㅣ'}
        re_value = ''
        flag = 0
        for key in IC:
            if ending == key:
                re_value = IC[key]
                flag = 1
        if flag != 1:
            re_value = ending
        re_value = treatSF(re_value, sentence)
        return re_value
    
    def make_end_low(self, sentence, taglist, ending):
        re_value =''
        sentence = treatFormal_vv(sentence)
        if taglist.find('IC') !=-1 and len(taglist)<6:
             re_value = self.convert_IC(sentence, taglist, ending)
        else:
            re_value = self.convert_EF(sentence, taglist, ending)
        return re_value
    
    def to_low(self, input):

        if '  ' in input:
            return input
        result = input

        #space_list = rememberSpace(input,' ')
        
#         test_w, test_t = to2lists(result)
#         pre_w, pre_t, pre_ind = prepro(result)

        converted_w, converted_t, target_ind ,last_ef = prepro_ch03(result, lis_beta_ef, lis_tag_last, lis_end_2low, lis_end, lis_ic)

        #ori_w, ori_t, ind, converted_w, converted_t, last_ef,target_ind  = prepro_beta_09(result,lis_beta_ef_h, lis_tag_last, lis_end, lis_end_2low)
         #@
        #print(converted_w, converted_t, target_ind ,last_ef)
        #space_location = convertSpace(space_list, ori_w)
#         lis_target_final = []

        if len(target_ind)!=0:

            #jam = Jamodealer(converted_w)
            for i in range(len(target_ind)):
                #new_end = self.make_end_low(converted_w[target_ind[i]], last_ef[i], converted_t[target_ind[i]], kconverted_w[ktarget_ind[i]], klast_ef[i], kconverted_t[ktarget_ind[i]])
                new_end = self.make_end_low(converted_w[target_ind[i]], converted_t[target_ind[i]], last_ef[i])
                
                converted_w[target_ind[i]] = new_end
            
            res = ' '.join(converted_w)
            jam = Jamodealer(res)
#             jam.jamo.append(w_last)
            #union(space_location, jam.jamo)
            return jam.make_one()

        return input

    def processText(self,stc):
        result = stc
        flag = 0
        if result[-1]=='\n':
            result = result.replace('\n','')   
        num = 0
        while 1:
            if result[-1-num]!=' ':
                break
            else:
                num = num+1
                
        if num==0:
            rere = result
        else:
            rere = result[:-num]
            
        
        r_pun = ''
        r_word = rere
        while True:
            if r_word[-1] in SV_LIST:
                r_pun = r_pun+r_word[-1]
                r_word = r_word[:-1]
            else:
                break
        
        num_space = 0
        for i in r_word:
            if i==' ':
                num_space = num_space+1
            else:
                break
            
        if num_space!=0:
            r_word = r_word[num_space:]

        plus = ''
        for s in range(num_space):
            plus = plus+' '
    
        if r_word[-1] =='?' or r_word[-1] =='.' or r_word[-1] =='!' or r_word[-1] =='\"':
            r_word = r_word
        else:
            r_word = r_word+'.'
            flag = 1

        res = self.to_low(r_word)
#         try:
#             res = self.to_low(r_word)
#         except:
#             print('exception sentece number: ', count)
#             res = r_word
        
        r_word = plus+r_word
        res = plus+res
        
        if flag ==1:
            res = res[:-1]

        return res+r_pun[::-1]

##########################TESTING PART##########################

txt = input("Enter Korean Sentence: ")
ch = Changer()
print("Converted Result:", ch.processText(txt))