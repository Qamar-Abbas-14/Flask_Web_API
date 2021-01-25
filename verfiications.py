from datetime import datetime


class Card_Verifications():
    def __init__(self):
        self.CCN=None
        self.CH=None
        self.SC=None
        self.ED=None
        self.AMT=None

    def verify(self, data):
        print("Verifying data...")
        try:
             self.CCN=data['CCN']
             self.CH=data['CH']
             self.SC=data['SC']
             self.ED=data['ED']
             self.AMT=data['AMT']

             is_ccn_valid=self.__check_CCN_Validity(self.CCN)
             is_ch_valid=self.__check_CH_Validity(self.CH)
             is_sc_valid=self.__check_SC_Validity(self.SC)
             is_ed_valid=self.__check_ED_Validity(self.ED)
             is_amt_valid=self.__check_AMT_Validity(self.AMT)
             print("Credit Card Validity: ",  is_ccn_valid)
             print("Card Holder Validity: ",  is_ch_valid)
             print("Security Validity: ",  is_sc_valid)
             print("Expiry Date Validity: ",  is_ed_valid)
             print("Amount Validity: ",  is_amt_valid)

             if is_ccn_valid and is_ch_valid and is_sc_valid and is_ed_valid and is_amt_valid:
                 return True
             else:
                 return False
        except:
            return False

    def __check_CCN_Validity(self, CCN):
        CCN_rev=CCN[::-1]
        ccn_lst=[int(i) for i in CCN_rev]
        check_digit=ccn_lst[0]
        ccn_calc=ccn_lst[1:]
        for i in range(0,len(ccn_calc),2):
            ccn_calc[i]=ccn_calc[i]*2

        for idx,elem in enumerate(ccn_calc):
            elem_str=str(elem)
            elem_int=0
            for i in elem_str:
                elem_int=elem_int+int(i)
            ccn_calc[idx]=elem_int

        sum_ccn=sum(ccn_calc)+check_digit
        validity=(sum_ccn%10 == 0 and len(ccn_lst)==16)
        return validity
    
    def __check_CH_Validity(self, CH):
        return type(CH).__name__ == 'str'

    def __check_SC_Validity(self, SC):
        try:
            sc_lst=[int(i) for i in SC]
            return len(sc_lst)==3
        except:
            return False
    def __check_ED_Validity(self, ED):
        Date_Validity=False
        try:
            EDY, EDM =ED.split('/')[1], ED.split('/')[0]
            Date_Now=datetime.today()
            Date_Now=datetime(Date_Now.year, Date_Now.month, 1)

            Date_Exp=datetime(1900, 1, 1)
            EDY=int(int(EDY)>2000 and int(EDY)<=2099)*int(EDY)
            EDM=int(int(EDM)>0 and int(EDM)<=12)*int(EDM)
            if EDM!=0:
                Date_Exp=datetime(EDY, EDM, 1)

            Date_Validity=Date_Exp>Date_Now
        except:
            print("Date Format not Correct it Should be MM/YYYY and should not be Current Month of present year ")
        return Date_Validity

    def __check_AMT_Validity(self, AMT):
        return (type(AMT).__name__ == 'float' and AMT>0)

            


