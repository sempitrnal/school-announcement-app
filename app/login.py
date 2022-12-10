from users import *
from school import *
class Login():
    def login(self,school: School(), choice):
     
        match(choice):
            case 1:
                uid = int(input('Enter ID: '))
                for stud in school.getRegistrar().get_students_list():
                    # print(stud.getId())
                    if(stud.getId() == uid):
                        logged = stud
                if(logged == None):
                    print('User does not exist!')
                else:
                    pword = input('Enter account password: ')
                    if hashlib.md5((pword+'brow').encode()).hexdigest() ==logged.get_pword():
                        print(f"\n\nWelcome back, {logged.getName()}!")
                        print(f"Class Level: {logged.get_type()}")
                        print(f"ACTIONS:")
                    else:
                        print("Wrong Password!")
                        logged = None
                return logged
            case 2:
                uid = int(input('Enter ID: '))
                if(school.getRegAdmin().getId() == uid):
                    logged = school.getRegAdmin()
                        
                if(logged == None):
                    print('User does not exist!')
                else:
                    pword = input('Enter account password: ')
                    if hashlib.md5((pword+'brow').encode()).hexdigest() ==logged.get_pword():
                        print(f"\n\nWelcome, {logged.getName()}!")
                        print(f"ACTIONS")
                    else:
                        print("Wrong Password!")
                        logged = None
                return logged
            case 3:
                uid = int(input('Enter ID: '))
                if(school.getUniPres().getId() == uid):
                    logged = school.getUniPres()
                        
                if(logged == None):
                    print('User does not exist!')
                else:
                    pword = input('Enter account password: ')
                    if hashlib.md5((pword+'brow').encode()).hexdigest() ==logged.get_pword():
                        print(f"\n\nWelcome, President {logged.getName()}!")
                        print(f"ACTIONS")
                    else:
                        print("Wrong Password!")
                        logged = None
                return logged
            case _:
                print("Wrong choice input!")