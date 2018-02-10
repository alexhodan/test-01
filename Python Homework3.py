
name = input('Enter your name: ')
age = int(input("Your age: "))

while (age<120):
    if age <0:
        print("Enter positive age ")
        break
    if age>=0:
        print("Your name is: ", age)
        age=age+1
        print("Your name is: ",name)


