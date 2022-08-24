
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
#################################################################
########################## low to high ##########################
da_low= ['다', 'ㄴ다', '는다', '느냐다', '단다', '서다', '란다', 'ㄴ단다'] 

da_case1 = [
    '더다', '느냐다', '서다', '어서다', '세다', '는지다', '냐다',
    '라다', '드다', 'ㄹ지다', 'ㄴ가다', '매다', '대다', '가다',
    '어다', 'ㅂ세다', 'ㄴ지다', '거다', 'ㄹ다', '네다', '어라다',
    'ㄹ트다', '뫼다', '는가다', '을지다', '두다', '구다', '아야다',
    '조다', '아서다', '오다', '기다'
]

da_case2 = [
    'ㄴ다', '단다', '란다', 'ㄴ단다', '더란다', '넌다', '냐이다', '건다',
    '으란다', '서란다', '나다', '는단다', '인다', '렌다', '은다', '련다',
    '차다', 'ㄴ거다', '프다', '올게다'
]
da_case3 = ['는다', '잖다', '뵀다', '쫒는다', '더랬다', 'ㅂ다']
da_tag_case1 = ['SL', 'SW', 'SS', 'NNP', 'NNG']
da_tag_case2 = ['NNB', 'XSV', 'XSA', 'ETN', 'VCN', 'JKB', 'VCP', 'VV', 'VX', 'EP', 'VA', 'EC']

yoo_low = [
    '을까', 'ㄹ까', '지', '으니까', '어', '는데',
    'ㄴ가', 'ㄹ게', '래', '잖아', '네', '여', 'ㄹ래',
    '게', '나', '군', '을게', '다고', '지만', '은데',
    'ㄴ지', '는지', '라고', 'ㄴ데', '는걸', '아서',
    '거든', '더라고', '어서', '려고', '을래', '대', 
    'ㄴ대', '던데', '더군', '여서', '건가', '어야지', 'ㄹ걸',
    'ㄹ께', '아야지', '다면서', '는군', 'ㄴ다고', '은가', '다니',
    '다면', '실까', '가', '신가', '서', '까', '다니까', '데', '다던데',
    '다는데', '랄까', '거나', '라던데', '던가'
]

an_low = ['아', '야', '어', '지', '자', '을까', 'ㄹ까', '어라']

ah_low = [
    '하', '좋', '오', '같', '나오', '많', '앉', '막', '팔', '편하',
    '다녀오', '나', '만나', '보', '알', '바라', '말', '가', '귀찮',
    '들어가', '바르', '다르', '않', '아프', '내려가', '돌아오', '놀',
    '지나가', '받', '나타나', '나쁘', '남', '모르', '맞', '못하', '밝',
    '타', '들어오', '찾아오', '괜찮', '닫', '놓', '살', '춰', '다보', 
    '지내', '그리워하', '높', '잡', '가보', '힘내', '내', '찾아보', '가져오',
    '사', '달', '내보', '라', '꽂', '돌아가', '프', '나가', '여받', '밀어내',
    '빛나', '생각나', '찾아가', '깨', '걷어오', '걷어가', '맡', '자', '빠르',
    '닿', '약하', '참', '끝나', '올라가', '찾', '일어나', '깨어나', '골',
    '잦', '보내', '싸', '닦', '똑같', '따라오', '볶', '날아가', '낫',
    '갚', '떠나', '빨', '돌', '알맞', '작', '옳', '깎', '낳', '떠나가',
    '낮', '보내보', '고르', '심하', '살아가', '비싸', '고프', '담',
    '뛰어오', '녹', '멀잖', '따르', '알아보', '사오', '주말', '급하',
    '사보', '뛰어보', '모으', '가져가', '내려오', '해오', '잖', '자르',
    '좁', '삼', '마시잖', '형편없잖', '짧', '올라오', '둘러보', '시하',
    '돌아보', '도망가', '나아가', '뒤따라오', '두르러보', '달려가', '바라보',
    '돕오', '구르러가',  '흘러나오', '삶', '다가오', '살펴보', '깨닫', '빠져나오',
    '내려보', '상하'
]
########################## low to high ##########################
#################################################################