master_pwd = input("enter the master password ? ")

def view():
    with open('passwords.txt','r')as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:", user ,"| Password:",passw)
def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt','a')as f:
        f.write(name + "|" + pwd +"\n ")







while True:
    mode = input("would you like to add a new password or view or quit (add/view/q) ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("enter a valid option")
        continue
        
    
