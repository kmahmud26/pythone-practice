# Arithmetic operators
# a=4
# b=2
# sum = a**b
# print(sum)
# a=4
# b=2
# sum = a//b
# print(sum)
# Python Assignment Operators
# a=4
# a += 2
# print(a)
# x=3
# x**=2
# print(x)
# z = 6
# z&=7
# Python Comparison Operators:
# print(z)
# x = 20
# y = 25
# print('x == y is',x==y)
# a= 20
# b = 25  
# print('a != b is',a!=b)

# a = 10
# b= 9
# if a<b:
#     print("b is big")
# else:
#     print("a is big number")
Student_Math_Number=int(input("Enter Student Math Number ="))
if Student_Math_Number>100:
    print("Invalid grade")
elif Student_Math_Number>=80:
    print("He got grade point A+")
elif Student_Math_Number>=70:
    print("He got grade point A")
elif Student_Math_Number>=60:
    print("He got grade point A-")
elif Student_Math_Number>=50:
    print("He got grade point B")
elif Student_Math_Number>=40:
    print("He got grade point C")
elif Student_Math_Number>=33:
    print("He got grade point D")
else:
    print("Failed")
