#### low -> high Dictionary####
## 사전의 순서가 중요하다. 순서를 임의로 바꾸지 말 것
## EF solo. EF 앞에 형태소가 결합형이 아닌 홀로 분석 될 경우 ex) /EP, /EF

EF_ONLY_4S = [
    # -다면서 /EF
    [['ㄷ','ㅏ','ㅁ','ㅕ','ㄴ','ㅅ','ㅓ'],['ㄷ','ㅏ','ㅁ','ㅕ','ㄴ','ㅅ','ㅓ','ㅇ','ㅛ']],
    # -고 /EF
    [['ㄹ','ㅏ','ㄱ','ㅗ'],['ㄹ','ㅏ','ㄱ','ㅗ','ㅇ','ㅛ']], ##-라고-> 라고요
    [['ㄷ','ㅓ','ㄹ','ㅏ','ㄱ','ㅗ'],['ㄷ','ㅓ','ㄹ','ㅏ','ㄱ','ㅗ','ㅇ','ㅛ']],
    [['ㄷ','ㅏ','ㄱ','ㅗ'],['ㄷ','ㅏ','ㄱ','ㅗ','ㅇ','ㅛ']],
    [['ㄴ','ㅡ','ㄴ','ㄷ','ㅏ'],['ㅅ','ㅡ','ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    [['ㄴ','ㄷ','ㅏ'],['ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    #-어서다 /EF
    [['ㅇ','ㅓ','ㅅ','ㅓ','ㄷ','ㅏ'],['ㅇ','ㅓ','ㅅ','ㅓ','ㅇ','ㅣ','ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    [['ㄷ','ㅏ'],['-special']],
    [['ㅇ','ㅓ','ㄹ','ㅏ'],['ㅇ','ㅡ','ㅅ','ㅔ','ㅇ','ㅛ']], #add jh_1115
    [['ㅇ','ㅓ'],['ㅇ','ㅓ','ㅇ','ㅛ']],
    #'-라' /EF
    [['ㄷ','ㅓ','ㄹ','ㅏ'],['ㄷ','ㅓ','ㄴ','ㄷ','ㅔ','ㅇ','ㅛ']],
    [['ㅇ','ㅏ','ㄹ','ㅏ'],['ㅇ','ㅏ','ㅇ','ㅛ']],
    [['ㄹ','ㅣ','ㄹ','ㅏ'],['ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']], ##'-리라'는 아직 해결하지 못하였다. 
    [['ㄹ','ㅏ'],['ㅅ','ㅔ','ㅇ','ㅛ']],
    
    
    # -데 /EF
    [['ㅇ','ㅡ','ㄴ','ㄷ','ㅔ'],['ㅇ','ㅡ','ㄴ','ㄷ','ㅔ','ㅇ','ㅛ']],
    [['ㄴ','ㅡ','ㄴ','ㄷ','ㅔ'],['ㄴ','ㅡ','ㄴ','ㄷ','ㅔ','ㅇ','ㅛ']],
    [['ㄷ','ㅓ','ㄴ','ㄷ','ㅔ'],['ㄷ','ㅓ','ㄴ','ㄷ','ㅔ','ㅇ','ㅛ']],
    # -걸 /EF
    [['ㄴ','ㅡ','ㄴ','ㄱ','ㅓ','ㄹ'],['ㄴ','ㅡ','ㄴ','ㄱ','ㅓ','ㄹ','ㅇ','ㅛ']],
    
    [['ㅈ','ㅏ','ㄶ','ㅇ','ㅏ'],['ㅈ','ㅏ','ㄶ','ㅇ','ㅏ','ㅇ','ㅛ']], ## -잖아 -> -잖아요
    
    #-오 /EF
    [['ㅇ','ㅗ'],['ㅅ','ㅔ','ㅇ','ㅛ']],
    #-니 /EF
    [['ㄴ','ㅣ'],['ㄴ','ㅏ','ㅇ','ㅛ']],
    #-자 /EF
    [['ㅈ','ㅏ'],['ㅅ','ㅔ','ㅇ','ㅛ']],
    #-래 /EF
    [['ㅇ''ㅡ','ㄹ','ㄹ','ㅐ'],['ㅇ''ㅡ','ㄹ','ㄹ','ㅐ','ㅇ','ㅛ']],
    [['ㄹ','ㅐ'],['ㄹ','ㅐ','ㅇ','ㅛ']],
    
    
    # -거든 /EF
    [['ㄱ','ㅓ','ㄷ','ㅡ','ㄴ'],['ㄱ','ㅓ','ㄷ','ㅡ','ㄴ','ㅇ','ㅛ']],
    
    #-마 /EF
    [['ㅁ','ㅏ'],['ㅁ','ㅏ','ㅇ','ㅛ']],
    
    #-아 /EF
    [['ㅇ','ㅏ'],['ㅇ','ㅏ','ㅇ','ㅛ']],
    #-지/EF
    [['ㅈ','ㅣ'],['ㅈ','ㅛ']],
    
    #-나 /EF
    [['ㄴ','ㅏ'],['ㄴ','ㅏ','ㅇ','ㅛ']],

    #[['ㄴ','ㅡ','ㄴ','ㄱ','ㅏ'],['-special']],
    #-는가 /EF
    [['ㄴ','ㅡ','ㄴ','ㄱ','ㅏ'],['ㄴ','ㅏ','ㅇ','ㅛ']],
    #-던가 /EF
    [['ㄷ','ㅓ','ㄴ','ㄱ','ㅏ'],['ㄷ','ㅓ','ㄴ','ㄱ','ㅏ','ㅇ','ㅛ']],
    #-을까 /EF
    [['ㅇ''ㅡ','ㄹ','ㄲ','ㅏ'],['ㅇ''ㅡ','ㄹ','ㄲ','ㅏ','ㅇ','ㅛ']],
    
    # -ㅏ /EF
    [['ㅏ'],['ㅏ','ㅅ','ㅔ','ㅇ','ㅛ']],
    # -ㅔ /EF
    [['ㅔ'],['ㅔ','ㅇ','ㅛ']],
    
    
    
    
]
## EF 결합형
## EF 앞에 형태소가 결합형인 경우 앞의 형태소도 고려해서 처리해야 한다. ex) /EP, /EF
EF_ONLY_4C = [
    
    [['ㄷ','ㅏ'],['ㅅ','ㅡ','ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    [['ㅇ','ㅓ'],['ㅅ','ㅡ','ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    [['ㅇ','ㅓ','ㄸ','ㅐ'],['ㅇ','ㅓ','ㄸ','ㅐ','ㅇ','ㅛ']],
    [['ㄴ','ㅡ','ㄴ','ㄷ','ㅔ'],['ㄴ','ㅡ','ㄴ','ㄷ','ㅔ','ㅇ','ㅛ']],
    
    # -걸 /EF
    [['ㄴ','ㅡ','ㄴ','ㄱ','ㅓ','ㄹ'],['ㄴ','ㅡ','ㄴ','ㄱ','ㅓ','ㄹ','ㅇ','ㅛ']],
    [['ㄴ','ㅣ'],['-special']],
    # -니 /EF
    [['ㄴ','ㅣ'],['ㅇ','ㅓ','ㅇ','ㅛ']],
    # -거든 /EF
    [['ㄱ','ㅓ','ㄷ','ㅡ','ㄴ'],['ㄱ','ㅓ','ㄷ','ㅡ','ㄴ','ㅇ','ㅛ']],
    [['ㅈ','ㅣ'],['ㅈ','ㅛ']],
    #[['ㄴ','ㅡ','ㄴ','ㄱ','ㅏ'],['-special']],
    [['ㄴ','ㅡ','ㄴ','ㄱ','ㅏ'],['ㄴ','ㅏ','ㅇ','ㅛ']],
    [['ㄴ','ㅏ'],['ㄴ','ㅏ','ㅇ','ㅛ']],
    
]

EP_EF_4 =[
    #[['ㄴ','ㅔ'],['ㄱ','ㅓ','ㄹ','ㄲ','ㅏ','ㅇ','ㅛ']],
    [['ㄴ','ㅔ'],['ㄴ','ㅔ','ㅇ','ㅛ']],
]

#/VCP+EF
VCP_EF_4 = [
    #[['ㄱ','ㅓ','ㄹ','ㄲ','ㅏ'],['ㄷ','ㅔ','ㅇ','ㅛ']],
    [['ㄱ','ㅓ','ㄹ','ㄲ','ㅏ'],['ㄱ','ㅓ','ㄹ','ㄲ','ㅏ','ㅇ','ㅛ']], ##bug check
    [['ㄱ','ㅓ','ㄹ'],['ㄷ','ㅔ','ㅇ','ㅛ']],
    [['ㅇ','ㅑ'],['ㅇ','ㅔ','ㅇ','ㅛ']],
    [['ㄹ','ㅐ'],['ㄹ','ㅐ','ㅇ','ㅛ']],
    [['ㄴ','ㅣ'],['ㅇ','ㅔ','ㅇ','ㅛ']], #add jh_1116
    [['ㄷ','ㅔ'],['ㄷ','ㅔ','ㅇ','ㅛ']],
    [['ㄷ','ㅏ'],['-special']]
    
]

#/VA+EF added code_JH
VA_EF_4 = [
    [['ㅇ','ㅓ','ㄸ','ㅐ'],['ㅇ','ㅓ','ㄸ','ㅐ','ㅇ','ㅛ']],
    [['ㄴ','ㅣ'],['-special']],
    [['ㅕ'],['ㅕ','ㅇ','ㅛ']],
]

## /VCP, /EF
EF_AFTER_VCP_4 = [
    [['ㅇ','ㅑ'],['ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    [['ㄷ','ㅏ'],['ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    #-오 /EF
    [['ㅇ','ㅗ'],['ㅅ','ㅔ','ㅇ','ㅛ']],
    [['ㄴ','ㅣ'],['ㅇ','ㅔ','ㅇ','ㅛ']], #add jh_1116
    [['ㄴ','ㅔ'],['ㄴ','ㅔ','ㅇ','ㅛ']],
    
]
#/XSA, /EF
EF_AFTER_XSA_4 = [
    
    [['ㄷ','ㅏ'],['-special']],
    
    
]

VV_EF_4 = [
    [['ㄱ','ㅓ','ㄹ'],['ㄱ','ㅓ','ㄹ','ㅇ','ㅛ']],
    [['ㅎ','ㅐ','ㄹ','ㅏ'],['ㅎ','ㅏ','ㅅ','ㅔ','ㅇ','ㅛ']],
    [['ㅂ','ㅘ','ㄹ','ㅏ'],['ㅂ','ㅗ','ㅅ','ㅔ','ㅇ','ㅛ']],
    [['ㅂ','ㅘ'],['ㅂ','ㅘ','ㅇ','ㅛ']],
    [['ㅎ','ㅏ','ㄹ','ㄹ','ㅐ'],['ㅎ','ㅏ','ㄹ','ㄹ','ㅐ','ㅇ','ㅛ']],
    [['ㅈ','ㅜ','ㄹ','ㄹ','ㅐ'],['ㅈ','ㅜ','ㄹ','ㄹ','ㅐ','ㅇ','ㅛ']], #add jh_1115
    [['ㄷ','ㅙ'],['ㄷ','ㅙ','ㅇ','ㅛ']],
    [['ㄴ','ㅣ'],['-special']],
    [['ㄷ','ㅡ','ㄹ','ㄹ','ㅕ'],['ㄷ','ㅡ','ㄹ','ㄹ','ㅕ','ㅇ','ㅛ']],
    [['ㄷ','ㅏ','ㅁ','ㅕ','ㄴ','ㅅ','ㅓ'],['ㄷ','ㅏ','ㅁ','ㅕ','ㄴ','ㅅ','ㅓ','ㅇ','ㅛ']],
    [['ㄹ','ㅐ'],['ㄹ','ㅐ','ㅇ','ㅛ']],
    [['ㄴ','ㄷ','ㅏ'],['ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    [['ㅇ','ㅘ'],['ㅇ','ㅘ','ㅇ','ㅛ']], 
    [['ㅊ','ㅝ'],['ㅊ','ㅝ','ㅇ','ㅛ']],
    [['ㅔ'],['ㅔ','ㅇ','ㅛ']],
    [['ㅏ'],['ㅏ','ㅇ','ㅛ']], 
    [['ㅕ'],['ㅕ','ㅇ','ㅛ']],
    
]

##added code_JH
#/XSV+EF
XSV_EF_4 = [
    [['ㄷ','ㅏ'],['special']],
    [['ㅎ','ㅐ','ㄹ','ㅏ'],['ㅎ','ㅐ','ㅇ','ㅛ']],
    [['ㅎ','ㅐ'],['ㅎ','ㅐ','ㅇ','ㅛ']],
    [['ㄹ','ㄲ','ㅏ'],['ㄹ','ㄲ','ㅏ','ㅇ','ㅛ']],
    [['ㅏ','ㄴ','ㄷ','ㅏ'],['ㅏ','ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    
]
#/XSA+EF
XSA_EF_4 = [
    [['ㄷ','ㅏ'],['special']],
    [['ㄴ','ㄷ','ㅏ'],['ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    [['ㅎ','ㅏ','ㄴ','ㄷ','ㅔ'],['ㅎ','ㅏ','ㄴ','ㄷ','ㅔ','ㅇ','ㅛ']],
    [['ㅎ','ㅐ'],['ㅎ','ㅐ','ㅇ','ㅛ']],
    
]
#/VX+EF
VX_EF_4 = [
    [['ㄷ','ㅏ'],['special']],
    [['ㅎ','ㅐ'],['ㅎ','ㅐ','ㅇ','ㅛ']],
    [['ㄹ','ㅏ'],['ㅇ','ㅛ']],
    [['ㅂ','ㅘ','ㄹ','ㅏ'],['ㅂ','ㅗ','ㅅ','ㅔ','ㅇ','ㅛ']],
    [['ㅂ','ㅘ'],['ㅂ','ㅘ','ㅇ','ㅛ']],
    [['ㅈ','ㅜ','ㄹ','ㄹ','ㅐ'],['ㅈ','ㅜ','ㄹ','ㄹ','ㅐ','ㅇ','ㅛ']], #add jh_1115
    [['ㅁ','ㅏ'],['ㅁ','ㅏ','ㅇ','ㅛ']],
    [['ㄹ','ㄱ','ㅔ'],['ㄹ','ㄱ','ㅔ','ㅇ','ㅛ']],
    [['ㅝ'],['ㅝ','ㅇ','ㅛ']],
    [['ㄴ','ㄷ','ㅏ'],['ㅂ','ㄴ','ㅣ','ㄷ','ㅏ']],
    
    
]
#/NNB+JKO
NNB_JKO_4 = [
    [['ㄱ','ㅓ','ㄹ'],['specialx']],
]
#/EC
EC_4 = [
    [['ㄷ','ㅔ'],['specialx']],
    #[['ㄷ','ㅔ'],['ㄷ','ㅔ','ㅇ','ㅛ']],
    [['ㄱ','ㅔ'],['specialx']],
    [['ㄴ','ㅔ'],['specialx']],
    #[['ㄱ','ㅔ'],['ㄱ','ㅔ','ㅇ','ㅛ']],
]

#/VV
VV_4 = [
    
    #[['ㄷ','ㅚ'],['ㄷ','ㅚ','ㅇ','ㅛ']],
]