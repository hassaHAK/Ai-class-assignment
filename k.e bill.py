def add(electric_charges,uniform_charges,sales_tax,advance_tax,tv_charges):
    total=electric_charges+uniform_charges+sales_tax+advance_tax+tv_charges
    return total
def electricity(unitsi):
    if (units>=1 and units<=100):
        charges=units*9.43
    elif(units>=101 and units<=200):
        charges=units*10.20
    elif(units>=201 and units<=300):
        charges=units*12.55
    elif(units>=301 and units<=400):
        charges=units*17.35
    elif(units>=401 and units<=500):
        charges=units*18.54
    elif(units>=501 and units<=600):
        charges=units*19.76
    elif(units>=601 and units<=700):
        charges=units*20.40
    else:
        charges=units*21.07
    return charges

def uniform(units):
    if (units>=1 and units<=100):
        charges=units*13.48
    elif(units>=101 and units<=200):
        charges=units*18.95
    elif(units>=201 and units<=300):
        charges=units*22.14
    elif(units>=301 and units<=400):
        charges=units*25.53
    elif(units>=401 and units<=500):
        charges=units*27.74
    elif(units>=501 and units<=600):
        charges=units*29.16
    elif(units>=601 and units<=700):
        charges=units*30.30
    else:
        charges=units*35.22
    return charges
    
def sales_tax(units):
    if (units>=1 and units<=100):
        charges=units*9.43
    elif(units>=101 and units<=200):
        charges=units*10.29
    elif(units>=201 and units<=300):
        charges=units*12.55
    elif(units>=301 and units<=400):
        charges=units*17.38
    elif(units>=401 and units<=500):
        charges=units*18.84
    elif(units>=501 and units<=600):
        charges=units*19.76
    elif(units>=601 and units<=700):
        charges=units*20.40
    else:
        charges=units*23.87
    return charges
    
def advance_tax(units):
    charges=units*29.93
    return charges
    
def tv_charges(units):
    charges=units*29.93
    return charges
        
def main_bill(units):
    electric_charges=electricity(units)
    print("Electric Charges for",units,"=",electric_charges)
    uniform_charges=uniform(units)
    print("Uniform Charges for",units,"=",uniform_charges)
    tax=sales_tax(units)
    print("Sales Tax for",units,"=",tax)
    advance=advance_tax(units)
    print("Advance tax for",units,"=",advance)
    tv=tv_charges(units)
    print("Tv Charges for",units,"=",tv)
    total=add(electric_charges,uniform_charges,tax,advance,tv)
    return total
units=int(input("Enter Units\n"))
total=(main_bill(units))
print("Total=",total)
    
