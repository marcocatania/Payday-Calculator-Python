#Tax Year
print('\n')
print('Tax Year 2017/2018')
print('\n')

#Contractual Hours
hc = 0
try:
    hc = float(input("Enter Contractual Hours: "))
except ValueError:
    hc = 0
print('Your contractual Hours are', hc)
print('\n')

#Monthly Extra Hours
eh = 0
try:
    eh = float(input('Enter monthly extra hours: '))
except ValueError:
    eh = 0
print('Your monthly extra hours are', eh)
print('\n')

#Pay Rate
r = 0
try:
    r = float(input("Enter Rate: "))
except ValueError:
    r = 0
print('Your pay rate is', r)
print('\n')

#Total Weeks
w = 0
try:
    w = int(input("Enter Weeks: "))
except ValueError:
    w = 0
print('Your monthly worked weeks are', w)
print('\n')


#Month pay (Extra Hours Pay added)
payGrossMonth = ((hc * w) + eh) * r
payGrossMonth = float('{0:.2f}'.format(payGrossMonth))
print('Monthly Gross Pay is', payGrossMonth)
print('\n')



#NI tax month
nInsuranceMonth = None

if payGrossMonth > 680.00 and payGrossMonth <= 3750.00:
    nInsuranceMonth = ((payGrossMonth - 680.00) * 12) / 100
elif payGrossMonth > 3750.00:
    nInsuranceMonth = (((3750.00 - 680.00) * 12) / 100) + (((payGrossMonth - 3750.00) * 2) / 100)
else:
    nInsuranceMonth = 0.00
    
nInsuranceMonth = float('{0:.2f}'.format(nInsuranceMonth))
print('National Insurance month is', nInsuranceMonth)
print('\n')


#Income tax month
incomeTaxMonth = None
if payGrossMonth > 959.08 and payGrossMonth <= 3750.00:
    incomeTaxMonth = ((payGrossMonth - 959.08) * 20) / 100
elif payGrossMonth > 3750.00 and payGrossMonth <= 8333.33:
    incomeTaxMonth = (((3750.00 - 959.08) * 20) / 100) + (((payGrossMonth - 3750.00) * 40) / 100)
elif payGrossMonth > 8333.33 and payGrossMonth <= 12500.00:
    incomeTaxMonth = ((((3750.00 - (959.08 - ((payGrossMonth - 8333.33) / 2))) * 20)) / 100) + (((payGrossMonth - 3750.00) * 40) / 100)
elif payGrossMonth > 12500.00:
    incomeTaxMonth = ((3750.00 * 20) / 100) + (((payGrossMonth - 3750.00) * 40) / 100) +(((payGrossMonth - 12500.00) * 45) / 100)
else:
    incomeTaxMonth = 0

incomeTaxMonth = float('{0:.2f}'.format(incomeTaxMonth))
print('Income Tax month is', incomeTaxMonth)
print('\n')


#Total taxes month
totalTaxesMonth = nInsuranceMonth + incomeTaxMonth
totalTaxesMonth = float('{0:.2f}'.format(totalTaxesMonth))
print('Total taxes month is', totalTaxesMonth)
print('\n')


#Net pay month
netPayMonth = (payGrossMonth) - (nInsuranceMonth + incomeTaxMonth)
netPayMonth = float('{0:.2f}'.format(netPayMonth))
print('Net Pay month is', netPayMonth)
print('\n')

print('Enjoy your pay day, lucky you !!!')


