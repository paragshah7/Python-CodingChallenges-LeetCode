def computepay(h,r):
    if h > 40:
        eh = h - 40
        gross_pay = (40 * r) + (1.5 * eh * r)
    else:
        gross_pay = h * r
    return gross_pay

hrs = input("Enter Hours:")
rate = input("Enter Rate: ")
fhrs = float(hrs)
frate = float(rate)
p = computepay(fhrs,frate)
print(p)