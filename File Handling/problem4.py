#problem:4
'''
login Authentication system
a company wants to store user credentials
write a program:
1.Register users into users.txt
2.login using username and password
3.validate the credentials from file
4.handle invalid login attempts

'''
class LoginSystem:
    def register(self):
        username =input("enter the username:")
        password =input("enter the password:")
        with open("users.txt","a") as file:
            file.write(
                username + " "+password+"\n"
            )
        print("Registration successful")
    def  login(self):
        try:
            username =input("enter the username:")
            password =input("enter the password:")
            found = False
            with open("users.txt","r")as file:
            
             for line in file:
                u,p =line.strip().split()
                if (username == u and password == p):
                    found = True
                    break
            if found:
                print("login successful")
            else:
                print("Invalid credentials")
        except FileNotFoundError as e:
             print(e)

obj = LoginSystem()
obj .register()
obj.login()