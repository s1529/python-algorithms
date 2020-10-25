#WAP to swap to number.

a=int(input('enter first no.'))
b=int(input('enter second no.'))

print("First way")
c=a
a=b
b=c
print("Now First No . is ",a)
print("Second No. is " , b)

print()
print("Second way")
a=a+b
b=a-b
a=a-b
print("Now First No . is ",a)
print("Second No. is " , b)



print("\nThird way")
a,b=b,a
print("Now First No . is ",a)
print("Second No. is " , b)
