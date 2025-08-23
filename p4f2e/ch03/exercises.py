#1.
206 / (1+0.025)**10

#2. The future value of perpetuity is infinite

#3. For the normal project there are initial outflows followed by inflows (meaning one sign change),
#   the more the discount rate the less the future inflows value today,
#   meaning the less NPV 

#4.
5000 * (1+r)**25

#5.
55/2 / (0.0541 / 2) * (1 - 1 / (1+0.0541/2)**(2*20))

#6
2400 * 0.0312 / ( (1+0.0312)**5 - 1 )

#7. Because here the cash inflow and outflow have the same sign

#8.
(4 / 2) ** (1 / 9) - 1

#9. As pv_f is not working as excel function meaning not the same sign convention

#10.
-3000 + 5000 / (1+0.1) + 8000 . (1+0.12)**2

#11.
40 / (1+0.05) + 40 / (1+0.05)**2 + 40 / (1+0.06)**3 + 1040 / 1+(0.06)**4
# 1040

#12.
4000 / (1+0.05)**4

#13.
5000 * (1+0.06)**10 * (1+0.09)**15

#14. It's good for safety and usability but it makes hidden assumptions

#15. pv - pv / (1+r-g) = c / (1+r-g) => pv(1+r-g) - pv = c => pv*r - pv*g = c => pv(r-g) = c => pv = c/(r-g)


#16.
2500000 * (0.0341/12) / (1 - 1 / (1 + 0.0341 / 12) ** ((65-32)*12))

#17. In the first case we can access all the function only by using fin101.* while in another case directly by name

#18. For example logical bounds

#19.
investment = 256
total = 0
pb_period = 0
cashflows = [34, 44, 55, 67, 92, 70, 50]

for c in cashflows:
    if investment - (total + c):
        total += c
        pb_period += 1
    else:
        pb_period += (investment - total) / c
        break

#20
investment = 256
total = 0
pb_period = 0
cashflows = [34, 44, 55, 67, 92, 70, 50]
r = 0.077
n = 0

for c in cashflows:
    if investment - (total + c):
        total += c / (1+r)**n
        pb_period += 1
    else:
        pb_period += (investment - total) / (c / (1+r)**n )
        break
  






