#1. From python website or anaconda distribution

#2. Yes

#3. pv = (1, 2) | We can't change it's values as tuples are immutable

#4.
import math
d = 9.7
print(math.pi * (d/2)**2)

#5.
new = 2

#6. On the internet

#7.
help(int)

#8.
help(print)

#9. The functions that come with python standard library

#10. Yes | it's the same as a**b, makes exponent

#11.
dir(__builtins__)
len(dir(__builtins__))

#12.
math.sqrt(3)

#13.
pv=124
c=50
r=c/pv

#14. The formula is 1 + r_annual = (1 + r_quarterly)**(1/4)
rq = (1+r)**(1/4) - 1

#15.
g = 0.025
r = 0.085
pv = c / (r-g)

#16. The formula is o_ndays**2 = n*o_daily**2
od = 0.2
nod = od*math.sqrt(10)

#17. The formula is pv = fv /(1+r)**t
fv = 25000
t = 5
r = 0.045
pv = fv /(1+r)**t

#18. It's from re module which 11 functions

#19.
o_annual = o_daily * math.sqrt(252) = o_monthly * math.sqrt(12)

#20. r - portfolio mean return, rf - mean risk free rate, o - risk of the portfolio
sharpe = (r - rf) / o




