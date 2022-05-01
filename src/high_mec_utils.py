import matplotlib.pyplot as plt
import numpy as np
import math as mt
import seaborn as sns
from tqdm import tqdm
import pandas as pd
from hangul_utils import split_syllables, join_jamos
from tqdm.auto import tqdm
import re
#for window
#from eunjeon import Mecab
#for mac
from konlpy.tag import Mecab
from hanspell import spell_checker
from khaiii import KhaiiiApi

con_dict = [
    
    ['ㅏㅣ','ㅐ'], ['ㅑㅣ','ㅒ'], ['ㅓㅣ','ㅔ'],
    ['ㅕㅣ','ㅖ'], ['ㅗㅣ','ㅚ'], ['ㅗㅐ','ㅙ'],
    ['ㅜㅓ','ㅝ'], ['ㅜㅔ','ㅞ'], ['ㅡㅣ','ㅢ'],
    ['ㅣㅏ','ㅑ'], ['ㅣㅓ','ㅕ'], ['ㅣㅗ','ㅛ'],
    ['ㅣㅜ','ㅠ'], ['ㅡㅓ','ㅓ'], ['ㅗㅏ','ㅘ']
    
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
    
    'ㅅㅡㅂㄴㅣㄷㅏ',
    'ㅂㄴㅣㄷㅏ', 'ㄴㅣㄷㅏ', 'ㅂㅅㅣㄷㅏ', 'ㅅㅣㄷㅏ', 'ㄹㄹㅐㅇㅛ',
    'ㅅㅔㅇㅛ', 'ㄷㅔㅇㅛ', 'ㅇㅔㅇㅛ', 'ㅇㅖㅇㅛ', 'ㄴㅏㅇㅛ', 'ㄱㅜㄴㅇㅛ','ㅇㅡㄹㄲㅏㅇㅛ', 'ㅇㅣㄹㄲㅏㅇㅛ', 'ㄹㄲㅏㅇㅛ', 'ㅇㅡㄴㄱㅏㅇㅛ', 'ㅇㅣㄴㄱㅏㅇㅛ',
    'ㄱㅗㅇㅛ', 'ㅇㅛ',
    'ㅈㅛ',
    'ㅅㅣㅂㅅㅣㅇㅗ', 'ㅅㅣㅇㅗ', 'ㅇㅗ',
    'ㅂㄴㅣㄲㅏ',  
    
]

lis_end_2low = [
    
    'ㄷㅓㄹㅏ','ㄴㅡㄴㄷㅏ','ㄴㄷㅏ', 'ㅆㄷㅏ', 'ㄹㅗㄷㅏ', 'ㄷㅏ', 'ㄱㅔ', 'ㅈㅣ', 'ㅈㅏ', 'ㄴㅑ', 
    'ㄹㅏ',
    'ㅇㅑ', 
    'ㄴㅣㄲㅏ', 
    'ㄲㅏ', 
    'ㄴㅣ', 
    'ㅇㅏ', 
    'ㄷㅔ', 
    'ㅇㅓ', 
    'ㄴㅏ', 
    
]

lis_ic = ['ㅇㅖ', 'ㄴㅔ', 'ㅇㅏㄴㅣㅇㅗ', 'ㅇㅏㄴㅣㅇㅛ']

lis_wk = [
    
    ['ㄱㅖ', 'ㅇㅣㅆㅇㅡ'], ['ㅈㅜㅁㅜ','ㅈㅏ'], ['ㅈㅏㅂㅅㅜ','ㅁㅓㄱㅇㅡ']
    
]

# lis_end_2low = [
    
#     'ㄷㅓㄹㅏ','ㄴㄷㅏ', 'ㅆㄷㅏ', 'ㄷㅏ', 
#     'ㄹㅏ',
#     'ㅇㅑ', 
    
# ]

P_LIST = ['.', '?', '!', '\'', '\"', 'ᆞ', 'ᆢ', 'ㆍ',  '”', '’',')', '(', ',', '”']

SV_LIST = ['\'', '\"', ':', ';', '?']

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

def prepro_ch01(input, lis_ef, tag_last, lis_w_last, lis_w_last_not):
    
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
        
        if 'EF/SF' in lis_tag[i] or 'EF/SV' in lis_tag[i] or 'EC/SY'  in lis_tag[i] or 'EC/SF' in lis_tag[i] or 'EC/SSO' in lis_tag[i]:

            elemen_t = lis_tag[i].split('/')
            elemen_w = lis_word[i].split(' ')
            flag = 0
            ff=0
            
#             print('iiii')
            
            for j in range(len(elemen_t)):

                flag_end = detect_h(elemen_w[j], lis_w_last_not, lis_w_last)
                

                
                if (flag_end == 0 and 'EF' in elemen_t[j]):
#                     print('eeee')
                    for jam in lis_w_last:
                        
                        if len(elemen_w[j])>=len(jam):
                            
                            if elemen_w[j][-len(jam):]==jam:
                                
                                
                                lis_ind.append(i)
                                lis_last_word.append(jam)
                                elemen_w[j] = elemen_w[j][:-len(jam)]
                                elemen_w[j] = elemen_w[j] + '__+__'
                                ff=1
                                break
                                
                elif 'VV+EF' in elemen_t[j] or 'VA+EF' in elemen_t[j] or 'XSV+EF' in elemen_t[j] or 'VCP+EF' in elemen_t[j]:
#                     print('qq')
                    if flag_end == -1:
                        lis_ind.append(i)
                        lis_last_word.append('')
                        elemen_w[j] = elemen_w[j] + '__+__'
                    
                    
            res_w = ''.join(elemen_w)
            lis_result.append(res_w)
            
        elif ('NP' in lis_tag[i] or 'NNG' in lis_tag[i]) and ('ㄴㅏ' in lis_word[i] or 'ㄴㅐ' in lis_word[i]):

            elemen_t = lis_tag[i].split('/')
            elemen_w = lis_word[i].split(' ')
            
            jam1 = Jamodealer(elemen_w)
            s = jam1.make_one()
            
            key_u = 0
            
            ss = proc_khaiii_with_Tag(s)
            tagt = ss[1].split('/')[:-1]
            wordw = ss[0].split('/')[:-1]
            
            for u in range(len(tagt)):
                if tagt[u]=='NP':
                    if wordw[u]=='내' or wordw[u]=='나':
                        key_u = 1
            
            flag = 0
            
            for ind in range(len(elemen_t)):
                
                if flag==0 and key_u==1:
                    
                    if elemen_t[ind][:2]=='NP' or elemen_t[ind][:3]=='NNG':
                        
                        if elemen_w[ind][:2] == 'ㄴㅏ':
                            
                            elemen_w[ind] = 'ㅈㅓ' + elemen_w[ind][2:]
                            flag = 1
                        
                        elif elemen_w[ind][:2] == 'ㄴㅐ':
                            
                            elemen_w[ind] = 'ㅈㅔ' + elemen_w[ind][2:]
                            flag = 1
                            
            
            resres = ''.join(elemen_w)
            
            lis_result.append(resres)
            
                                
        else:
            
            rere = lis_word[i].split(' ')
            
            resres = ''.join(rere)
            
            lis_result.append(resres)
            
            
    return lis_result, lis_tag, lis_ind, lis_last_word

def convert_not(stc, tag, ex):
    ind_point = -1
    point = ''

#     for i in P_LIST:
#         if stc.find(i) !=-1:
#             point = i
#             break
            
    for i in range(len(stc)):
        if stc[i] in P_LIST:
            point = stc[i]
            break
            
    if point in P_LIST:
        ind_point = stc.index(point)
    
    r_word = ''
    r_pun = ''
    
    if ind_point!=-1:
        r_word = stc[:ind_point]
        r_pun = stc[ind_point:]
    else:
        r_word = stc
        
    return r_word + ex + r_pun

def convert_an(stc, tag, ex):
    
    ind_point = -1
    point = ''

#     for i in P_LIST:
#         if stc.find(i) !=-1:
#             point = i
#             break
            
#     for i in range(len(stc)):
#         if stc[len(stc) - i-1] in P_LIST:
#             point = stc[len(stc) - i-1]
#             break
    
#     for i in range(len(stc)):
#         if stc[i] in P_LIST:
#             ind_point = i
#             break
        
    ind_point = stc.index('__+__')
    stc = stc.replace('__+__', '', 1)
    
    r_word = ''
    r_pun = ''
    
    if ind_point!=-1:
        r_word = stc[:ind_point]
        r_pun = stc[ind_point:]

    else:
        r_word = stc
    
    if ex=='ㄹㅏ':
        
        if len(r_word)!=0:
            if 'ㅗ'==stc[-2]:
                return r_word+'ㅏㅇㅛ'+r_pun
            elif 'ㅎㅏ'==stc[-3:-1]:
                return r_word+'ㅣㅇㅛ'+r_pun
            elif 'ㄷㅏㄹ' in stc:
                return r_word+'ㄹㅏ'+r_pun
                if 'VA' not in tag:
                    return r_word+'ㄹㅏㅇㅛ'+r_pun
                return r_word[:-3]+'ㅈㅜㅅㅔㅇㅛ'+r_pun
            elif 'ㅗㄹ' == r_word[-2:]:
                return r_word+'ㄹㅏㅇㅛ'+r_pun
            else:

                return r_word+'ㅇㅛ'+r_pun
        else:
            return r_word+ex+r_pun

        #return r_word+'ㅇㅛ'+r_pun
    elif ex=='ㄱㅜㄴㅏ':
        return r_word+'ㄱㅜㄴㅇㅛ'+r_pun
    elif ex=='ㄴㅑ':
        return r_word+'ㄴㅏㅇㅛ'+r_pun
    elif ex=='ㅈㅏㄶㄴㅣ':
        return r_word+'ㅈㅏㄶㅇㅏㅇㅛ'+r_pun
    elif ex=='ㄱㅔ':###############################
        print(r_word)
        if 2<=len(r_word) and r_word[-2:]=='ㅎㅏ':
            return r_word+'ㅣㅇㅛ'+r_pun
        elif 2<=len(r_word) and r_word[-2:]=='ㅅㅣ':
            return r_word+'ㅓㅇㅛ'+r_pun
        return r_word+'ㄱㅔㅇㅛ'+r_pun
        
    elif ex=='ㅇㅓㄹㅏ':
        return r_word+'ㅇㅓㅇㅛ'+r_pun
    elif ex=='ㅇㅏㄹㅏ':
        return r_word+'ㅇㅏㅇㅛ'+r_pun
    elif ex=='ㄴㅗㄹㅏ':
        if stc[-3:-1]=='ㅎㅏ':
            return r_word+'ㅣㅇㅛ'+r_pun
        else:
            return r_word+'ㅇㅓㅇㅛ'+r_pun
    elif ex=='ㄷㅏㄷㅓㄹㅏ':
        return r_word+'ㄷㅐㅇㅛ'+r_pun
    elif ex=='ㄷㅓㄹㅏ':
        wd = ''
        if 'ㄷㅏ' in r_word:
#             print('dd')
            return r_word[:-1]+'ㅐㅇㅛ'+r_pun
        if r_word[-1] in jongsung_list:
            wd = r_word[-2]
        else:
            wd = r_word[-1]
        if wd=='ㅗ':
            return r_word+'ㅏㅇㅛ'+r_pun
        elif wd=='ㅜ':
            return r_word+'ㅓㅇㅛ'+r_pun
        elif wd=='ㅏ':
            return r_word+'ㅇㅏㅇㅛ'+r_pun
        else:
            return r_word+'ㅇㅓㅇㅛ'+r_pun
    elif ex=='ㄴㅣ' or ex =='ㄴㅡㄴㄱㅏ' or ex =='ㅇㅡㄴㄱㅏ':####################
        
        isVcp = tag[-11:-3]
        
        if isVcp =='VCP' or isVcp =='/VCP' or isVcp =='NNG/VCP':
            print('www')
            return r_word + 'ㅇㅖㅇㅛ' + r_pun
        elif isVcp == 'VCP/NULL':
            return r_word + 'ㅇㅔㅇㅛ' + r_pun
        
        
        if ex=='ㄴㅣ' and stc[-3:-1]=='ㅌㅔ':
            return r_word+'ㄴㅣㅇㅛ'+r_pun
        
        if ex=='ㄴㅣ' and 'XSA/EF' in tag:
            return r_word+'ㄴㅏㅇㅛ'+r_pun
        
        if ex=='ㄴㅣ' and 'NNG' in tag:
            return r_word+'ㅇㅖㅇㅛ'+r_pun
        
        return r_word+'ㄴㅏㅇㅛ'+r_pun
    elif ex=='ㅇㅑ':
        return r_word+'ㅇㅔㅇㅛ'+r_pun
#     elif ex=='ㄷㅓㄹㅏ':
#         if 'ㄷㅏ' in stc:
#             return stc[:-1]+'ㅔㅇㅛ'
#         return stc+'ㄷㅔㅇㅛ'
    elif ex=='ㅈㅣ':
        return r_word+'ㅈㅛ'+r_pun
    elif ex=='ㅈㅏ':
        return r_word+'ㅈㅛ'+r_pun
    else:
#         print('dd')
        return r_word+ex+'ㅇㅛ'+r_pun
    
def convert_da(stc, tag, ex):
    #print(tag)
    if 'UNKNOWN/' in tag:
        isVcp = tag[-17:]
    else:
        isVcp = tag[-9:]

    isETM = tag[-12:]


    ind_point = -1
    point = ''

#     for i in range(len(stc)):
#         if len(stc)-i-1==0:
#             point = stc[0]
#             ind_pont = -1
#         if stc[len(stc) - i-1] not in P_LIST:
#             point = stc[len(stc) - i-1]
#             ind_point = len(stc)-i

#             break

#     for i in range(len(stc)):
#         if stc[i] in P_LIST:
#             ind_point = i
#             break

    ind_point = stc.index('__+__')
    stc = stc.replace('__+__', '', 1)
    
#     print(ind_point)
    
#     if point in P_LIST:
#         ind_point = stc.index(point)
    
    r_word = ''
    r_pun = ''

    if ind_point!=-1:
        r_word = stc[:ind_point]
        r_pun = stc[ind_point:]
    else:
        r_word = ''
        r_pun = stc[0]
    
    try:
        jongsung = r_word[-1]
    
    except:
        return ex+r_pun
        
    if jongsung in jongsung_list:
        if  isETM.find('+ETM') != -1:
            r_word = r_word[:-1]
            final = r_word +'ㅂㄴㅣㄷㅏ'+r_pun
        else:
            final = r_word +'ㅅㅡㅂㄴㅣㄷㅏ'+r_pun
    else:
        if isVcp.find('VCP') != -1:
            if len(r_word)>=2:
                if 'ㅇㅣ' in r_word:
                    return r_word +'ㅂㄴㅣㄷㅏ'+r_pun
            final = r_word +'ㅇㅣㅂㄴㅣㄷㅏ'+r_pun
        elif 'SN/NULL' in tag:
            final = r_word +'ㅇㅣㅂㄴㅣㄷㅏ'+r_pun
        else:
            final = r_word +'ㅂㄴㅣㄷㅏ'+r_pun
    #print(final)
    return final

