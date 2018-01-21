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

#Week pay
#payGrossWeek = hc * r
#payGrossWeek = float('{0:.2f}'.format(payGrossWeek))
#print('Weekly Gross pay is', payGrossWeek)

#Month pay (Extra Hours Pay added)
payGrossMonth = ((hc * w) + eh) * r
payGrossMonth = float('{0:.2f}'.format(payGrossMonth))
print('Monthly Gross Pay is', payGrossMonth)
print('\n')


#NI tax week
#nInsuranceWeek = 0
#if payGrossWeek >= 157.00 :
#    nInsuranceWeek = ((payGrossWeek - 157) * 12) / 100
#if payGrossWeek >= 866.00:
#    nInsuranceWeek = (((866-157) * 12) / 100) + (((payGrossWeek - 866) * 2) / 100)
#nInsuranceWeek = float('{0:.2f}'.format(nInsuranceWeek))
#print('National Insurance week is', nInsuranceWeek)

#NI tax month
nInsuranceMonth = 0
if payGrossMonth >= 680:
    nInsuranceMonth = ((payGrossMonth - 680) * 12) / 100
if payGrossMonth >= 3750:
    nInsuranceMonth = (((3750 - 680) * 12) / 100) + (((payGrossMonth - 3750) * 2) / 100)
nInsuranceMonth = float('{0:.2f}'.format(nInsuranceMonth))
print('National Insurance month is', nInsuranceMonth)
print('\n')

#Income tax week
#incomeTaxWeek = 0
#if payGrossWeek >= 221.33:
#    incomeTaxWeek = ((payGrossWeek - 221.33) * 20) / 100
#incomeTaxWeek = float('{0:.2f}'.format(incomeTaxWeek))
#print('Income Tax week is', incomeTaxWeek)

#Income tax month
incomeTaxMonth = 0
if payGrossMonth >= 958:
    incomeTaxMonth = ((payGrossMonth - 958) * 20) / 100
incomeTaxMonth = float('{0:.2f}'.format(incomeTaxMonth))
print('Income Tax month is', incomeTaxMonth)
print('\n')

#Total taxes week
#totalTaxesWeek = nInsuranceWeek + incomeTaxWeek
#totalTaxesWeek = float('{0:.2f}'.format(totalTaxesWeek))
#print('Total taxes week is', totalTaxesWeek)

#Total taxes month
totalTaxesMonth = nInsuranceMonth + incomeTaxMonth
totalTaxesMonth = float('{0:.2f}'.format(totalTaxesMonth))
print('Total taxes month is', totalTaxesMonth)
print('\n')

#Net pay week
#netPayWeek = (payGrossWeek) - (nInsuranceWeek + incomeTaxWeek)
#netPayWeek = float('{0:.2f}'.format(netPayWeek))
#print('Net Pay week is', netPayWeek)

#Net pay month
netPayMonth = (payGrossMonth) - (nInsuranceMonth + incomeTaxMonth)
netPayMonth = float('{0:.2f}'.format(netPayMonth))
print('Net Pay month is', netPayMonth)
print('\n')

print('Enjoy your pay day, lucky you !!!')

#Compute contractual salary, then add extra hours(be careful with the tax rate)
