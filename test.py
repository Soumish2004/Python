try:
 
     trying_to_check_error
 
except NameError as err: # 'as' is needed in Python 3.x
 
     print (err, 'Error Caused')
print(type('default string '))
print(b"tring wit b")
# Python program to illustrate a Dictionary

# creates a empty list
Dict = []

# putting integer values
Dict = {1: "Geeks", 2: "For", 3: 'Geeks'}

print(Dict)

#Code submitted by Susobhan AKhuli
# Python3 program to get input from user

# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num3 = num1 * num2
print("Product is: ", num3)

X=int(input())
Y=int(input())
Z=int(input())
n=int(input())
lis=[[i, j, k] for i in range(X+1) for j in range(Y+1) for k in range (Z+1) if i+j+k!=n]
print (lis)