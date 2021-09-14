from konlpy.tag import Kkma, Komoran, Okt, Mecab

mec = Mecab()
okt = Okt()
kkm = Kkma()
kom = Komoran()
	
txt = '안녕하세요 오늘의 날씨는 참 습하고 덥네요.'
mec.pos(txt, flatten=False, join=True) #mecab
kom.pos(txt,flatten=False, join=True) #komoran
kkm.pos(txt,flatten=False, join=True) #kkma
okt.pos(txt,norm=True, stem=True, join=True) #okt
