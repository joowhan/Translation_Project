from hangul_utils import split_syllables, join_jamos
from tqdm.auto import tqdm
import re
#from eunjeon import Mecab
from konlpy.tag import Mecab
from hanspell import spell_checker

import dict_low_01 as dl
import dict_common_01 as dc
import dict_ex_low_01 as exl

import dict_high_01 as dh
import dict_ex_high_01 as exh


mec = Mecab()

#### End of Common Dictionary ####
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
        self.pp = unite(self.pp, dc.con_dict)
        
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
##End of Jamodealer class##

# def tojamo(korean_word):
#     r_lst = []
#     for w in list(korean_word.strip()):
#         ## 영어인 경우 구분해서 작성함. 
#         if '가'<=w<='힣':
#             ## 588개 마다 초성이 바뀜. 
#             ch1 = (ord(w) - ord('가'))//588
#             ## 중성은 총 28가지 종류
#             ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
#             ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
#             r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
#         else:
#             r_lst.append([w])
#     return r_lst

#Use in makestrdict
#Convert list to String
def li2str(input):
    st = ""
    for i in input:
        st = st+i
    return st

##Used when make dictionaries
def makestrdict(input):
    result = []
    for i in input:
        bullet = []
        for j in range(len(i)):
            gre = li2str(i[j])
            bullet.append(gre)
        result.append(bullet)
    return result

### *추가한 사전에 대한 str 사전을 생성, mapping 시키는 부분* ###

# * 기존의 방식은 다음과 같다. 어말어미는 어말어미 변환 방식 코드를 참고하면 된다.
# - 앞으로  사전을 추가하고 싶으면 여기서 코드를 추가하고 수정하면 된다.
# - dictionary를 만들고 해당 형태소에 해당하는 dictionary를 추가하면 된다.
#   예를 들어, EP(선어말어미)에 대한 사전을 만들고 싶다면 EP_dict = makestrdict(EP)를 선언하고
#   Dict_list에 'EP'를 추가하면 된다. 그 후 Mapping이 되도록 Dict_map에도 생성한 EP_dict를 추가하면 된다.

#EP_dict = makestrdict(EP)
EF_dict = makestrdict(dl.EF)
NP_dict = makestrdict(dl.NP)
JX_dict = makestrdict(dl.JX)
VX_dict = makestrdict(dl.VX)
VV_dict = makestrdict(dl.VV)
XR_dict = makestrdict(dl.XR)
NNG_dict = makestrdict(dl.NNG)
NNP_dict = makestrdict(dl.NNP)
UNKNOWN_dict = makestrdict(dl.UNKNOWN)

Dict_list=['NNP','NP','JX','VX','VV','XR','NNG', 'UNKNOWN']

Map_family=[['V_fam',['VCP, VA, VX']], ['X_fam',['XSA','XSV']]]

Dict_map = [NNP_dict,NP_dict,JX_dict,VX_dict, VV_dict, XR_dict, NNG_dict, UNKNOWN_dict]

##현재의 어말어미 변환방식은 밑에 코드를 추가, 변경하면 된다. 
#high->low of string dictionary
EF_ONLY_dict = makestrdict(dl.EF_ONLY)
EP_EF_dict = makestrdict(dl.EP_EF)
VCP_EF_dict = makestrdict(dl.VCP_EF)
A_EF_dict = makestrdict(dl.A_EF)
XSA_EF_dict = makestrdict(dl.XSA_EF)
XSV_EF_dict = makestrdict(dl.XSV_EF)


#low->high of string dictionary
EF_ONLY_4S_dict = makestrdict(dh.EF_ONLY_4S)
EF_ONLY_4C_dict = makestrdict(dh.EF_ONLY_4C)
EP_EF_4_dict = makestrdict(dh.EP_EF_4)
EF_AFTER_VCP_4_dict = makestrdict(dh.EF_AFTER_VCP_4)
VCP_EF_4_dict = makestrdict(dh.VCP_EF_4)
EF_AFTER_XSA_4_dict = makestrdict(dh.EF_AFTER_XSA_4) ## add code_JM
VA_EF_4_dict = makestrdict(dh.VA_EF_4)
VV_EF_4_dict = makestrdict(dh.VV_EF_4)
VX_EF_4_dict = makestrdict(dh.VX_EF_4)
XSV_EF_4_dict = makestrdict(dh.XSV_EF_4)
NNB_JKO_4_dict = makestrdict(dh.NNB_JKO_4)##add code_JH
EC_4_dict = makestrdict(dh.EC_4)
VV_4_dict = makestrdict(dh.VV_4)

##Use in Changer
def to2lists(input):
    lis_word = []
    lis_tag = []
    #data = han.pos(input,ntags=22,flatten=True, join=False)
    data = mec.pos(input)
    for i in data:
        lis_word.append(i[0])
        lis_tag.append(i[1])
    return lis_word, lis_tag

#add in 2021.09.26

#space의 index 찾는다.
#rememberSpace와 convertSpace는 문장의 space를 찾아 변환하고 그 위치에 다시 space를 넣기 위한 함수이다.
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
        
##특정 형태소를 찾는다. 종결어미(EF)를 찾아서 높임말 반말 변환 시 사용된다.         
def findTargetMorphology(input, word):
    
    i=0
    lis = []
    for j in range(len(input)):
        if word in input[j]:
            lis.append(j)
            
    return lis

def del_over(input):
    
    res = set(input) #집합set으로 변환
    result = list(res) #list로 변환
    return result
