
#Korean vowel combination
con_dict = [
    
    ['ㅏㅣ','ㅐ'], ['ㅑㅣ','ㅒ'], ['ㅓㅣ','ㅔ'],
    ['ㅕㅣ','ㅖ'], ['ㅗㅣ','ㅚ'], ['ㅗㅐ','ㅙ'],
    ['ㅜㅓ','ㅝ'], ['ㅜㅔ','ㅞ'], ['ㅡㅣ','ㅢ'],
    ['ㅣㅏ','ㅑ'], ['ㅣㅓ','ㅕ'], ['ㅣㅗ','ㅛ'],
    ['ㅣㅜ','ㅠ'], ['ㅡㅓ','ㅓ'], ['ㅗㅏ','ㅘ'],
    
]

#jongsung_list = [ 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


# lis_beta = ['EP+EF', 'VCP+EF', 'B+EF', 'B+EP+EF', 'B+VCP+EF', 'EF','EP']

# lis_beta = ['EP+EF', 'EF', 'B+EF', 'B+EP+EF']

#어말을 처리해 주기 위한 것으로, 나중에 EC등이 필요해 진다면 이 부분에 EC 등을 집어넣어준다. 참고로 이는 문장의 마지막에 위치해야한다.
#특이 바로 밑의 이 부분은 형태소 태그가 이 리스트 안의 것과 일치하는 경우 단순 삭제를 하는 것
lis_beta_ef = ['EP+EP+EF', 'EP+EF', 'EF', 'UNKNOWN']
lis_beta_ef_h = ['EF', 'UNKNOWN']

lis_tag_last = ['EF', 'UNKNOWN']

# 존칭 명사 동사를 낮추기 위한 list
lis_wk = [
    
    ['ㄱㅖ', 'ㅇㅣㅆㅇㅡ'], ['ㅈㅜㅁㅜ','ㅈㅏ'], ['ㅈㅏㅂㅅㅜ','ㅁㅓㄱㅇㅡ']
    
]
# 존칭 종결어미
lis_end = [
    
    'ㅅㅡㅂㄴㅣㄷㅏ', 'ㅅㅡㅂㄴㅣㄲㅏ',
    'ㅂㄴㅣㄷㅏ', 'ㄴㅣㄷㅏ', 'ㅂㅅㅣㄷㅏ', 'ㅅㅣㄷㅏ', 'ㄹㄹㅐㅇㅛ','ㄹㅐㅇㅛ',
    'ㅇㅡㅅㅔㅇㅛ', 'ㅅㅔㅇㅛ', 'ㄷㅔㅇㅛ', 'ㅇㅔㅇㅛ', 'ㅇㅖㅇㅛ', 'ㄴㅏㅇㅛ', 'ㅇㅡㄹㄲㅏㅇㅛ', 'ㅇㅣㄹㄲㅏㅇㅛ', 'ㄹㄲㅏㅇㅛ', 'ㅇㅡㄴㄱㅏㅇㅛ', 'ㅇㅣㄴㄱㅏㅇㅛ','ㄱㅜㄴㅇㅛ','ㄴㄱㅏㅇㅛ',
    'ㄱㅗㅇㅛ','ㅇㅛ',
    'ㅈㅛ',
    'ㅅㅣㅂㅅㅣㅇㅗ', 'ㅅㅣㅇㅗ', 'ㅇㅗ',
    'ㅂㄴㅣㄲㅏ',  
    
]

# 반말 종결어미
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

P_LIST = ['.', '?', '!', '\'', '\"', 'ᆞ', 'ᆢ', 'ㆍ',  '”', '’',')', '(', ',', '”']

SV_LIST = ['\'', '\"', ':', ';']

lis_plus = [
    
    'EP', 'VCP', 
    
]
############################## EF Dictionary ##############################
###########################################################################

############ 높임말 -> 반말 ############
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
#'ㄹ'규칙 활용 -> ㄹ 규칙 활용이 일어나는 동사들을 최대한 모아둔 Dictionary
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

IC = {'ㅇㅖ':'ㅇㅡㅇ', 'ㄴㅔ':'ㅇㅡㅇ', 'ㅇㅏㄴㅣㅇㅗ':'ㅇㅏㄴㅣ', 'ㅇㅏㄴㅣㅇㅛ':'ㅇㅏㄴㅣ'}

formal_vv ={
    'ㄱㅖ':'ㅇㅣㅆㅇㅡ',
    'ㅈㅜㅁㅜ':'ㅈㅏ',
    'ㅈㅏㅂㅅㅜ':'ㅁㅓㄱㅇㅡ'
}