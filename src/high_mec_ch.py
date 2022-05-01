import high_mec_utils as ut

class Changer(object):
    
    def make_end_h(self, stc, tag, ex):

#         print(ex)
        if 'ㄷㅏ'== ex[-2:]:

            return ut.convert_da(stc, tag, ex)
            #return convert_not(stc, tag, ex)
        else:
            #return convert_not(stc, tag, ex)
            return ut.convert_an(stc, tag, ex)

    
    def to_high(self, input):
        
        if '  ' in input:
            return input
        
        result = input
        
        

        
        lis_w, lis_t, lis_target_ind, off_word = ut.prepro_ch01(result, ut.lis_beta_ef, ut.lis_tag_last, ut.lis_end_2low, ut.lis_end)

        
        if len(lis_target_ind)!=0:

            for i in range(len(lis_target_ind)):

                new_end = self.make_end_h(lis_w[lis_target_ind[i]], lis_t[lis_target_ind[i]], off_word[i])
                lis_w[lis_target_ind[i]] = new_end
            
            
#             jam.jamo.append(w_last)
            
            res = ' '.join(lis_w)
            jam = ut.Jamodealer(res)
            
            
            return jam.make_one()

        return input

#################################################################################
        
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

#         cc = ch.processText(line)
    
        plus = ''
        for s in range(num_space):
            plus = plus+' '
    
        if r_word[-1] =='?' or r_word[-1] =='.' or r_word[-1] =='!' or r_word[-1] =='\"':
            r_word = r_word
        else:
            r_word = r_word+'.'
            flag = 1
        try:
            res = self.to_high(r_word)
        except:
            res = r_word
            
        r_word = plus+r_word
        res = plus+res
        
        
        
#         if r_word[-1] =='?' or r_word[-1] =='.' or r_word[-1] =='!' or r_word[-1] =='\"':
#             r_word = r_word
#         else:
#             r_word = r_word+'.'
#             flag = 1
        
#         res = self.to_high(r_word)
        
        if flag ==1:
            res = res[:-1]
        
        #spacing = Spacing()
        #res = spacing(res)
        return res+r_pun[::-1]