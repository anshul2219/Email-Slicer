 #Taking e-mail input from user.

email=input("what is your e-mail ?").strip() #.strip function is used to cover the spaces if given in email address.

#Slicing the username by python.

user_name=email[:email.index("@")]

#Slicing the domain by python.

domain_name=email[email.index("@")+1:]

#Making it all in one and using .format method.

output="Your name is '{}' and domain name is '{}' ".format(user_name,domain_name)

#Printing the output

print(output)

#Thanks
