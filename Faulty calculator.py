print("choose your operator + - * / \n")
var3 = input()
print("choose your 1st number\n")
var1 = int(input())
print("choose your 2nd number\n")
var2 = int(input())


if var3 == '*' and var1 == 45 and var2 == 3:
    print(555)

elif var3 == '+' and var1 == 56 and var2 == 9:
    print(77)

elif var3 == '/' and var1 == 56 and var2 == 4:
    print(4)

elif  var3 == '+':
    print(var1 + var2)

elif var3 == '-':
    print(var1 - var2)

elif var3 == '*':
    print(var1 * var2)

elif var3 == '/':
    print(var1 / var2)

else:
    print("try later")