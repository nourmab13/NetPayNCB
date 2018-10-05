#Gain insight into how much job for N would contribute to family finances
#Taxable items (input these): extra_pay; dividends;capital gains; IRAMandatedWithdrawals; SocialSecurityIncome
##Decrement income by: FedIncomeTax; StateIncomeTax;FICA; MedicareTax
#Fed rate is for tax bracket for famiy with new pay included (likely 22 or 24%)
#NC has flat rate of 5.5%; FICA rate is 6.2%; MedicareTax 1.45%
class TaxableItems:
    def __init__(self, extra_income=0, interest=0, dividends=0, cap_gains=0, IRA_llb=0, soc_sec_llb=0):
        self.set_extra_income (extra_income)
        self.set_interest (interest)
        self.set_dividends (dividends)
        self.set_cap_gains (cap_gains)
        self.set_IRA_llb (IRA_llb)
        self.set_soc_sec_llb (soc_sec_llb)
        self.set_sum_taxable_income()

#define setters
    def set_extra_income(self, extra_income):
        if extra_income == 0:
            self.extra_income=float(input("Enter extra income: "))
        else:
            self.extra_income = extra_income

    def set_interest(self, interest):
        if interest == 0:
            self.interest=float(input("Enter interest income: "))
        else:
            self.interest = interest

    def set_dividends(self, dividends):
        if dividends == 0:
            self.dividends=float(input("Enter dividends income: "))
        else:
            self.dividends = dividends

    def set_cap_gains(self, cap_gains):
        if cap_gains == 0:
            self.cap_gains=float(input("Enter capital gains income: "))
        else:
            self.cap_gains = cap_gains

    def set_IRA_llb(self, IRA_llb):
        if IRA_llb == 0:
            self.IRA_llb=float(input("Enter income from Larry's mandated IRA withdrawals: "))
        else:
            self.IRA_llb = IRA_llb

    def set_soc_sec_llb(self, soc_sec_llb):
        if soc_sec_llb == 0:
            self.soc_sec_llb=float(input("Enter Larry's social security income: "))
        else:
            self.soc_sec_llb = soc_sec_llb

#define sum function
    def set_sum_taxable_income (self):
        self.sum_taxable_income = self.get_extra_income() + self.get_interest() + self.get_dividends() + self.get_cap_gains() + self.get_IRA_llb() + self.get_soc_sec_llb()

#define getters
    def get_extra_income(self):
        return self.extra_income

    def get_interest(self):
        return self.interest

    def get_dividends(self):
        return self.dividends

    def get_cap_gains(self):
        return self.cap_gains

    def get_IRA_llb(self):
        return self.IRA_llb

    def get_soc_sec_llb(self):
        return self.soc_sec_llb

    def get_sum_taxable_income (self):
        return self.sum_taxable_income

class TaxesDecrement:
    def __init__(self, fed_income_tax=0.24, state_income_tax=0.055, FICA=0.062, medicare_tax=0.0145):
        self.fed_income_tax = fed_income_tax
        self.state_income_tax = state_income_tax
        self.FICA = FICA
        self.medicare_tax = medicare_tax
        self.set_percent_tax_liability()

#first pass of program, no need for setters
    def set_percent_tax_liability(self):
        self.percent_tax_liability = self.get_fed_income_tax() + self.get_state_income_tax() + self.get_FICA() + self.get_medicare_tax()

# getters
    def get_fed_income_tax(self):
        return self.fed_income_tax

    def get_state_income_tax(self):
        return self.state_income_tax

    def get_FICA(self):
        return self.FICA

    def get_medicare_tax(self):
        return self.medicare_tax

    def get_percent_tax_liability (self):
        return self.percent_tax_liability

def calculate_net_pay():
#gather the taxable TaxableItems
    taxable_income=TaxableItems()
    tax_liability=TaxesDecrement()
    print("Total taxable income is: ", taxable_income.get_sum_taxable_income())
    print("Based on total taxable income of ${}, and {}% tax liability, net income after taxes is ${}".format(taxable_income.get_sum_taxable_income(), tax_liability.get_percent_tax_liability()*100, taxable_income.get_sum_taxable_income()*(1- tax_liability.get_percent_tax_liability())))
calculate_net_pay()
