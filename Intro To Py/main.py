import keyword
print(keyword.kwlist)
Get_Username = input("Enter A Fortnite Username To Create An Account:")
print("Hello Your Fortnite Username Is ",Get_Username)
Home = input("Which Country Do You Live In:")
print("Your Selected Country Is",Home)
age = input("Enter Your Birth Date:")
if 2024 - age < 13:
    print("You Need To Be 13 Years Old To Create A Fortnite Account")
else:
    print("Your age is",Age)
Password = input("Enter A Password")
print("Please Re-enter Your Password For Comformation")