from low_mec_changer import Changer as ch_low
from high_mec_ch import Changer as ch_high
changer_low = ch_low()
changer_high = ch_high()

txt = "전 늘 컴퓨터를 재밌게 공부합니다."
print("높임말 -> 반말 변환 예시")
print("before: ",txt)
print("After: ",changer_low.processText(txt))

print("반말 -> 높임말 변환 예시")
#txt = "난 늘 컴퓨터를 재밌게 공부한다."
txt = "내 생각도 그래. 여긴 내복이 필요한 만큼 추워. 난 나갈래. 나랑 함께할 사람?"
print("before: ",txt)
print("After: ",changer_high.processText(txt))
