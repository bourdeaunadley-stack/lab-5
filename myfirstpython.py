#Nadley

print("Hello world!")

name = input ("What is your name?")
print (name)

a = 10
b = 7


print(a+b)
print (b-a)
print (a*b)
print (a/b)
print (a//b)
print (b%a)
print (a**b)

if a<b:
    print(a , " is less than " , b)
elif a>b:
    print(b , " is less than " , a)
else:
    print("The values are equal")

userinput = ""
while userinput != "n":
    userinput = input("type 'n' to exit!")
