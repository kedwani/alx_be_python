mi = float (input ("Enter your monthly income: "))
me = float (input("Enter your total monthly expenses: "))
ms = mi - me
a_s = (ms * 12 + (ms * 12 * 0.05))
print ("Your monthly savings are $", ms, sep="")
print ("Projected savings after one year, with interest, is: $",a_s , sep="")