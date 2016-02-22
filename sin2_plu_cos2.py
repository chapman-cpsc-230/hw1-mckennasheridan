from math import sin, cos, pi
x = pi/4
val_1 = (sin(x))**2 + (cos(x))**2 #change 1_val to val_1 #delete 'math.' #exponent moved behind x
print (val_1) #change 1_VAL to val_1

v0 = 3 #m/s
t = 1 #s
a = 2 #m/s**2
s = v0*t+0.5*a*t**2 #changed '.' to '*'
print (s)

a = 3.3
b = 5.3 #added comma to separate variables
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = (a+b)**2
eq2_pow = (a-b)**2

print ('First equation: %g = %g' % (eq1_sum, eq1_pow))
print ('Second equation: %g = %g' % (eq2_sum, eq2_pow))
