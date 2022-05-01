import low_mec_utils as ut

class Changer(object):
    
    #def make_end_low(self, sentence, ending, taglist, kstn, kend, ktag):
    def convert_EF(self, sentence, taglist, ending):
        re_value =''
        temp =''
        ni = 0
        flag = 0
        
        #존칭 동사 또는 보조 동사를 파악하고 이를 변환 전에 미리 바꿔주어야 한다. 
        for key in ut.EF:
            if ending == key:
                flag = 1
                re_value = ut.EF[key]
                #나요, 으세요(으세요, 세요 모두 함수에서 커버 가능), 습니까 case
                if re_value == 'special0':
                    #시처리하기
                    after_si, ni = ut.delete_EP_si(sentence, taglist)
                    if after_si != '':
                        sentence = after_si
                        after_si =''
                    temp = ut.convertSpecialCase_AhOh(sentence)
                    re_value = ut.treatSF(sentence, temp)
                    #ㅗ,ㅜ 이면 ㅘ, ㅝ로 결합할 것
                    #print(re_value)
                #-세요,십니다, 십니까
                elif re_value == 'special1':
                    #시처리하기
                    after_si, ni = ut.delete_EP_si(sentence, taglist)
                    if after_si != '':
                        sentence = after_si
                        after_si =''
                    re_value = ut.convertSpecialCase_SaeYo(sentence, ending, taglist)
                elif re_value == 'special2':
                    re_value = ut.convertSpecialCase_Da(sentence, ending, taglist)
                elif re_value == 'special3':
                    #시처리 안함 '시' 보존
                    #re_value = convertSpecialCase_Nida(sentence, ending, taglist, kstn, kend, ktag)
                    re_value = ut.convertSpecialCase_Nida(sentence, ending, taglist)
                elif re_value == 'special4':
                    re_value = ut.convertSpecialCase_SaeYo(sentence, ending, taglist)
                    if ending == 'ㅇㅡㅂㅅㅣㄷㅏ':
                        temp = ut.convertSpecialCase_AhOh(sentence)
                        re_value = ut.treatSF(sentence, temp)
                elif re_value == 'special5':
                    re_value = ut.convertSpecialCase_Yo(sentence, ending, taglist)
                else:
                    #위험하기 때문에 데이터 확인 후 수정
#                     if taglist.find('EP') !=-1 and sentence[-4:].find('ㅅㅣ.'):
#                         sentence = delete_EP_si(sentence, taglist)
#                         re_value = convertSpecialCase_SaeYo(sentence, ending)
#                     else:
#                         re_value = treatSF(sentence,re_value)
                    re_value = ut.treatSF(sentence,re_value)
        if flag ==0:
            return ut.treatSF(sentence, ending)
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
        re_value = ut.treatSF(re_value, sentence)
        return re_value
    
    def make_end_low(self, sentence, taglist, ending):
        re_value =''
        sentence = ut.treatFormal_vv(sentence)
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
        converted_w, converted_t, target_ind ,last_ef = ut.prepro_ch02(result, ut.lis_beta_ef, ut.lis_tag_last, ut.lis_end_2low, ut.lis_end, ut.lis_ic)
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
            jam = ut.Jamodealer(res)
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
            if r_word[-1] in ut.SV_LIST:
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