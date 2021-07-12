def read_file():
    txt=open("user_database.txt","r")
    lines=txt.readlines() 
    txt.close()
    return lines


def write_new_user(string):
    login=open("user_database.txt","a")
    login.write("\n")
    login.write(string)
    login.close()
    
def build_dict(lines):
    dictionary={}
    login=open("user_database.txt")
    for line in login:
        line=line.split(',')
        line[0]=line[0].strip()
        line[-1]=line[-1].strip()
        k=line[0]
        v=line[-1]

        dictionary[k]=v
        dictionary[v]=k

    return dictionary
    login.close()
    
def login(dictionary):
    username=input("Enter username: ")
    password= input("Enter password: ")
    
    if username not in dictionary.keys():
        print("User does not exist. Please sign up!")
        main()
        return username
    if password in dictionary.keys():
        print("Login Successful!")
        
    else:
        print("Incorrect Password")
        print("Please Try Loging in again")
        main()
    
def main():
    options=int(input("Choose option 1. Signup 2.Enter the Username and Password to login: "))
    if options == 1:
        username=input("Enter username: ")
        
        password= input("Enter password: ")
        temp=[]
        temp.append(username)
        temp.append(password)
        s=",\t"
        temp=s.join(temp)
        write_new_user(temp)
        print("Signup Successful!")
        print("Please login to you new account!")
        main()
           
    if options == 2:
        lines =read_file()
        d=build_dict(lines)
        login(d)
main()
    
