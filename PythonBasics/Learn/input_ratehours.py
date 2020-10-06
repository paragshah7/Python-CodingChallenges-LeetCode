hrs = input("Enter Hours:")
rate = input("Enter Rate: ")
fhrs = float(hrs)
frate = float(rate)
if fhrs > 40:
    ehrs=fhrs-40
    gross_pay = (40*frate) + (1.5*ehrs*frate)
else:
    gross_pay = fhrs * frate
pay = print(gross_pay)