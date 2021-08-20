
#In[1]: 
from tqdm.auto import tqdm
from kiwipiepy import Kiwi
import re

lis = [
    [['ㅈ','ㅓ','_','ㄴ','ㅡ','ㄴ'],['ㄴ','ㅏ','_','ㄴ','ㅡ','ㄴ']],
    [[' ','ㅈ','ㅓ','ㄴ',' '],['ㄴ','ㅏ','_','ㄴ','ㅡ','ㄴ']],
    [['ㅇ','ㅓ','_','ㅇ','ㅛ','_'],['ㄷ','ㅏ','_']]

]

lili = [
    ["ㅂ니다","ㄴ다"],
    ["전 ","나는 "],
    ["줘요","줘"],
    [" 합니다"," 한다"],
    ["하세요","해라"],
    ["저는","나는"],
    ["제가","내가"],
    ["습니다","다"] 
]

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = ['_', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def tojamo(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        ## 영어인 경우 구분해서 작성함. 
        if '가'<=w<='힣':
            ## 588개 마다 초성이 바뀜. 
            ch1 = (ord(w) - ord('가'))//588
            ## 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
        else:
            r_lst.append([w])
    return r_lst

def toword(arr):
    print('wow')
    
# 1차원 배열로 바꾸는 것이다. 
def to1dim(input):
    result=[]
    for i in input:
        for j in i:
            result.append(j)
    return result
# 2차원 배열로 바꾸는 것이다. 
def to2dim(input):
    result = []
    li = []
    for i in input:
        if i == ' ':
            result.append([' '])
        else:
            li.append(i)
        if len(li)==3:
            result.append(li)
            li = []
    return result

# 자모로 분리된 단어를 다시 하나로 합쳐준다. 
def makeone(input):
    result = ''
    li = ''
    for i in input:
        if i[0]==' ':
            result = result+' '
        else:
            ind = ord('가')
            ind +=CHOSUNG_LIST.index(i[0])*588
            ind +=JUNGSUNG_LIST.index(i[1])*28
            ind +=JONGSUNG_LIST.index(i[2])
            result = result+chr(ind)
    return result

# convert list to string     
def li2str(input):
    st = ""
    for i in input:
        st = st+i
    return st

# convert string to list
def str2li(input):
    li = []
    for i in range(len(input)):
        li.append(input[i])
    return li

def makejamodict(input):
    result = []
    for i in input:
        bullet = []
        one = []
        two = []
        gre1 = tojamo(i[0])
        for j in gre1:
            for k in j:
                one.append(k)
        bullet.append(one)
        gre2 = tojamo(i[1])
        for j in gre2:
            for k in j:
                two.append(k)
        bullet.append(two)
        result.append(bullet)
    return result

def makestrdict(input):
    result = []
    for i in input:
        bullet = []
        gre1 = li2str(i[0])
        gre2 = li2str(i[1])
        bullet.append(gre1)
        bullet.append(gre2)
        result.append(bullet)
    return result

#strlis = makestrdict(lis)

strlis = makejamodict(lili)
strlis = makestrdict(strlis)

class Changer(object):
    def __init__(self):
        print('the changer starts!')
        
    def high_low(self, stc):
        result = stc
        result = tojamo(result)
        result = to1dim(result)
        result = li2str(result)#string으로 변경해 준다
        for i in range(len(strlis)):
            result = re.sub(strlis[i][0],strlis[i][1],result)
        result = str2li(result)
        result = to2dim(result)
        result = makeone(result)
        return result
    
    def processText(self, stc):
        
        result = stc
        res = self.high_low(result)
        return res
    
#In[2]:
la = makejamodict(lili)
print(la)

#In[3]:
la

#In[4]:
ro = makestrdict(la)
ro

#In[5]:
txt = '정말 잘 합니다'
ch = Changer()
tt = ch.processText(txt)
print(tt)