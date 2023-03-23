print("ax^2+bx+c=0 denkleminin köklerini bulma  programı.")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
delta = b**2-4*a*c
print("Delta:" , delta)
x1 = (-b+(delta**(0.5)))/2*a
x2 = (-b-(delta**(0.5)))/2*a
print("Birinci kök: " , x1)
print("İkinci kök: " , x2)