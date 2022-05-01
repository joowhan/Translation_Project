import changer_utils_01 as ut

## Main Class ## 
class Changer(object):
    
    ## High -> Low ##    
    def high_low(self, stc):
        result = stc
        
        space_list = ut.rememberSpace(stc,' ')
        
        lis_word, lis_tag = ut.to2lists(result)
        space_location = ut.convertSpace(space_list, lis_word)
        jam = ut.Jamodealer(lis_word)
        lis = []
        key = -1
        for i in ut.dc.H_LIST:
            if i in lis_word[-2]:
                key = 1
        #if key>0:
        if key>0 or key<0:     
            for i in range(len(lis_tag)):
                res = jam.jamo[i]
                dic = []
                if 'EF' in lis_tag[i]:
                    if 'EF' == lis_tag[i]:
                        dic = ut.EF_ONLY_dict
                    elif 'EP' in lis_tag[i]:
                        dic = ut.EP_EF_dict
                    elif 'VCP' in lis_tag[i]:
                        dic = ut.VCP_EF_dict
                    elif 'XSA' in lis_tag[i]:
                        dic = ut.XSA_EF_dict
                    elif 'XSV' in lis_tag[i]:
                        dic = ut.XSV_EF_dict
                    else:
                        dic = ut.A_EF_dict
                        
                #else Dict_list[k] in lis_tag[i]:
                else:
                    for k in range(len(ut.Dict_list)):
                        if ut.Dict_list[k] in lis_tag[i]:
                            dic = ut.Dict_map[ut.Dict_list.index(ut.Dict_list[k])]
                            break
                        
                flag = 0    
                for j in range(len(dic)):
                    if dic[j][0] in res:
                        flag = 1
                        if self.isExcept(dic[j])==1:
                            for q in range(len(ut.exl.EXC_deal_1)):
                                if dic[j][0]==ut.exl.EXC_deal_1[q][0]:
                                    for r in range(1,len(ut.exl.EXC_deal_1[q])):
                                        if jam.jamo[i-1][-1]==ut.exl.EXC_deal_1[q][r][0]:
                                            res = ut.re.sub(dic[j][0],ut.exl.EXC_deal_1[q][r][1],res)
                                        
                        elif self.isExcept(dic[j])==2:
                            for q in range(len(ut.exl.EXC_deal_2)):
                                if dic[j][0]==ut.exl.EXC_deal_2[q][0]:
                                    if i+1 in space_location:
                                        res = ut.re.sub(dic[j][0], ut.exl.EXC_deal_2[q][2], res)
                                    else:
                                        res = ut.re.sub(dic[j][0], ut.exl.EXC_deal_2[q][1], res)
                                    
                        elif self.isExcept(dic[j])==3:
                            for q in range(len(ut.exl.EXC_deal_3)):
                                if dic[j][0]==ut.exl.EXC_deal_3[q][0]:
                                    for o in range(len(ut.exl.EXC_deal_3[q][1])):
                                        
                                        l = len(ut.exl.EXC_deal_3[q][1][o][0])
                                        l = l*(-1)
                                        
                                        if jam.jamo[i-1][l:]==ut.exl.EXC_deal_3[q][1][o][0]:
                                            res = ut.re.sub(dic[j][0],ut.exl.EXC_deal_3[q][1][o][1],res)
                                        else:
                                            if o==len(ut.exl.EXC_deal_3[q][1])-1:
                                                res = ut.re.sub(dic[j][0],ut.exl.EXC_deal_3[q][2],res)
                                    
                        else:
                            res = ut.re.sub(dic[j][0],dic[j][1],res)
                            
                        if flag==1:
                            break
                            
                        #jam.jamo[i] = res
                lis.append(res)
            
            
            #print(jam.jamo[i])
        
        ut.union(space_location, lis)
        jam.jamo = []
        for i in range(len(lis)):
            jam.jamo.append(lis[i])
            #print(lis[i])
        
        #union(space_location, jam.jamo)
        
        return jam.make_one()
    
    def low_high(self, stc):
        result = stc
        
        space_list = ut.rememberSpace(stc, ' ')
        
        lis_word, lis_tag = ut.to2lists(result)
        space_location = ut.convertSpace(space_list, lis_word)
        jam = ut.Jamodealer(lis_word)
        #print(jam.jamo)
        lis = []
        
        ## 종결어미만을 변경
        ind_trans_ef = ut.findTargetMorphology(lis_tag, 'EF')
        ind_trans_jko = ut.findTargetMorphology(lis_tag, 'JKO')
        ind_trans_ec = ut.findTargetMorphology(lis_tag, 'EC')
        ind_trans_vv = ut.findTargetMorphology(lis_tag, 'VV')
        
        ind_union = ind_trans_ef + ind_trans_jko + ind_trans_ec + ind_trans_vv
        ind_union = ut.del_over(ind_union)
        
        for ind in ind_union:  #modified_2021.10.31
            key = -1

            for i in ut.dc.H_LIST:
                if i not in lis_word[ind]:
                    key = 1
                else:
                    key = -1
                if key==-1:
                    break
            if key >0:
                res = jam.jamo[ind]
                dic = []
                #EF
                if 'EF' in lis_tag[ind]:

                    if 'EF' == lis_tag[ind]:
                        if '+' in lis_tag[ind-1]:
                            dic = ut.EF_ONLY_4C_dict
                        elif lis_tag[ind-1]=='VCP':
                            dic = ut.EF_AFTER_VCP_4_dict
                        elif lis_tag[ind-1]=='XSA':
                            dic = ut.EF_AFTER_XSA_4_dict
                        else:
                            dic = ut.EF_ONLY_4S_dict
                            #print('ee')

                    elif 'EP' in lis_tag[ind]:
                        dic = ut.EP_EF_4_dict
                    elif 'VCP' in lis_tag[ind]:
                        dic = ut.VCP_EF_4_dict
                    elif 'VA' in lis_tag[ind]:
                        dic = ut.VA_EF_4_dict
                    elif 'VV' in lis_tag[ind]:
                        dic = ut.VV_EF_4_dict
                    elif 'VX' in lis_tag[ind]:
                        dic = ut.VX_EF_4_dict
                    elif 'XSV' in lis_tag[ind]:
                        dic = ut.XSV_EF_4_dict
                    else:
                        dic = ut.A_EF_dict
                #JKO      
                elif 'JKO' in lis_tag[ind]:
                    dic = ut.NNB_JKO_4_dict
                    

                elif 'EC' in lis_tag[ind]:
                    dic = ut.EC_4_dict
            
                ##added by JM
                flag = 0        
                for j in range(len(dic)):
                    if dic[j][0] in res:
                        flag = 1
                        
                        if self.isExcept(dic[j])==1:
                            for q in range(len(ut.exh.EXC_4_deal_1)):
                                if dic[j][0]==ut.exh.EXC_4_deal_1[q][0]:
                                    flag_1=0
                                    for r in range(1,len(ut.exh.EXC_4_deal_1[q])-1):
                                        if flag_1==1:
                                            break
                                        if ut.exh.EXC_4_deal_1[q][r][0] in jam.jamo[ind]:
                                            res = ut.re.sub(ut.exh.EXC_4_deal_1[q][r][0]+dic[j][0],ut.exh.EXC_4_deal_1[q][r][1],res)
                                            flag_1=1
                                    if flag_1==0:
                                        res = ut.re.sub(dic[j][0],ut.exh.EXC_4_deal_1[q][-1],res)

                        elif self.isExcept(dic[j])==2:
                            for q in range(len(ut.exh.EXC_4_deal_2)):
                                if dic[j][0]==ut.exh.EXC_4_deal_2[q][0]:
                                    if ind+1 in space_location:
                                        res = ut.re.sub(dic[j][0], ut.exh.EXC_4_deal_2[q][2], res)
                                    else:
                                        res = ut.re.sub(dic[j][0], ut.exh.EXC_4_deal_2[q][1], res)
                                        
                        elif self.isExcept(dic[j])==3:
                            for q in range(len(ut.exh.EXC_4_deal_3)):
                                if dic[j][0]==ut.exh.EXC_4_deal_3[q][0]:
                                    flag_1 = 0
                                    for r in range(1,len(ut.exh.EXC_4_deal_3[q])-1):
                                        if flag_1==1:
                                            break
                                        if jam.jamo[ind-1][-1]==ut.exh.EXC_4_deal_3[q][r][0]:
                                            flag_1=1
                                            li_1 = list(jam.jamo[ind-1])
                                            li_1[-1] = ut.exh.EXC_4_deal_3[q][r][1]
                                            jam.jamo[ind-1] = ''.join(li_1)
                                            res = ut.re.sub(dic[j][0],ut.exh.EXC_4_deal_3[q][r][2],res)
                                    if flag_1==0:
                                            res = ut.re.sub(dic[j][0],ut.exh.EXC_4_deal_3[q][-1],res)
                                            
                        elif self.isExcept(dic[j])==4:
                            for q in range(len(ut.exh.EXC_4_deal_4)):
                                if dic[j][0]==ut.exh.EXC_4_deal_4[q][0]:
                                    if lis_tag[ind+1] =='SF':
                                        if lis_tag[ind-1]=='VV':
                                            flag_1=0
                                            for t in range(len(ut.exh.EXC_4_deal_4[q][2])-1):
                                                if flag_1==1:
                                                    break
                                                    
                                                
                                                    
                                                if ut.exh.EXC_4_deal_4[q][2][t][0] in jam.jamo[ind-1]:
                                                    if len(ut.exh.EXC_4_deal_4[q][2][t][0])>1:
                                                        li_1 = list(jam.jamo[ind-1])
                                                        li_1=li_1[:-len(ut.exh.EXC_4_deal_4[q][2][t][0])]
                                                        li_1.append(ut.exh.EXC_4_deal_4[q][2][t][1])
                                                        jam.jamo[ind-1] = ''.join(li_1)

                                                        #jam.jamo[ind-1] = re.sub(EXC_4_deal_4[q][2][t][0],EXC_4_deal_4[q][2][1],jam.jamo[ind-1])
                                                        res = ut.re.sub(dic[j][0], ut.exh.EXC_4_deal_4[q][2][t][2],res)
                                                        flag_1=1
                                                        
                                                    else:
                                                        li_1 = list(jam.jamo[ind-1])
                                                        li_1[-1] = ut.exh.EXC_4_deal_4[q][2][t][1]
                                                        jam.jamo[ind-1] = ''.join(li_1)

                                                        #jam.jamo[ind-1] = re.sub(EXC_4_deal_4[q][2][t][0],EXC_4_deal_4[q][2][1],jam.jamo[ind-1])
                                                        res = ut.re.sub(dic[j][0], ut.exh.EXC_4_deal_4[q][2][t][2],res)
                                                        flag_1=1
                                                    
                                            if flag_1==0:
                                                res = ut.re.sub(dic[j][0],ut.exh.EXC_4_deal_4[q][2][-1],res)
                                        else:
                                            res = ut.re.sub(dic[j][0],ut.exh.EXC_4_deal_4[q][1],res)
                                    else:
                                        res = ut.re.sub(dic[j][0],ut.exh.EXC_4_deal_4[q][-1],res)
                    
                        else:
                            res = ut.re.sub(dic[j][0],dic[j][1],res)

                        
                        if flag==1:
                            break
                        
                jam.jamo[ind] = res


            
        
        
        ut.union(space_location, jam.jamo)
        
        return jam.make_one()
            
          
    def isExcept(self, input):
        if input[1]=='special':
            return 1
        elif input[1]=='special-':
            return 2
        elif input[1]=='-special':
            return 3
        elif input[1]=='specialx':
            return 4
        else:
            return 0
        
    def indicator(self, ind, lis, tag, ex_word, exc_tags):
        re = 1
        for j in range(len(ex_word)):
            if exc_tags[j] in tag[ind+1]:
                for i in range(len(ex_word)):
                    if ex_word[i][0] in lis[ind+1]:
                       
                        re = ex_word[i][1]
                        break
                        
                        print(lis[ind-1])
        return re
        
        
#     def processText(self,stc):
#         result = stc
#         res = self.high_low(result)
#         #spacing = Spacing()
#         #res = spacing(res)
#         return res
#     ##change function name
#     def processText_convertHigh(self,stc):
#         result = stc
#         res = self.low_high(result)
#         return res
    def processText(self,stc):
        result = stc
        
        flag = 0
        if result[-1]=='\n':
            result = result.replace('\n','')
        if result[-1] =='?' or result[-1] =='.' or result[-1] =='!' or result[-1] =='\"':
            result = result
        else:
            result = result+'.'
            flag = 1
        
        res = self.high_low(result)
        
        if flag ==1:
            res = res[:-1]
        
        #spacing = Spacing()
        #res = spacing(res)
        return res
    
    def processText_convertHigh(self,stc):
        result = stc
        
        flag = 0
        if result[-1]=='\n':
            result = result.replace('\n','')
        if result[-1] =='?' or result[-1] =='.' or result[-1] =='!' or result[-1] =='\"':
            result = result
        else:
            result = result+'.'
            flag = 1
        
        res = self.low_high(result)
        
        if flag ==1:
            res = res[:-1]
        return res
