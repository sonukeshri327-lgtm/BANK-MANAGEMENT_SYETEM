 
  

import json
import random
import string

from  pathlib import Path


 
class bank:
    database='data.json'
    data=[]



    try:
     if Path(database).exists():  
      with open(database) as fs:
       data=json.loads(fs.read())
     else:
      print("mp such file exists")

    except Exception as err:
     print(f"an exception occured as{err}")
     

    @staticmethod
    def update():
     with open(bank.database,'w') as fs:
       fs.write(json.dumps(bank.data))


    @classmethod
    def __accountgenerate(cls):
       alpha=random.choices(string.ascii_letters,k=3)
       num=random.choices(string.digits,k=3)
       spchar=random.choices("!@#$%^&*",k=1)
       id=alpha+num+spchar
       random.shuffle(id)
       return "".join(id)



    
    def createaccount(self):
          info={
            "name":input("tell your name-"),
            "age": int(input("your age-")),
            "email":input("your email-"),
            "pin": int(input("your pin-")),
            "account no": bank.__accountgenerate(),
            "balance": 0
          }


          if info['age']< 18 or len(str(info['pin']))!=4:
             print("Sorry you cannot create your account")
          
          else:
               print("account has created succesfully")
          for i in info:
            print(f"{i} : {info[i]}")

          print("please note down your number")

          bank.data.append(info)

          bank.update()




    def deposit(self):
      accnumber= input("please tell your ac no")
      pin=int(input("please tell your pin number"))

      userdata=[i for i in bank.data if i['account no']==accnumber and i['pin']==pin]
     
      if not userdata:
       print("no data found")
      

      else:
         amount=int(input("how much you want to deposit-")) 
         if amount>10000:
            print("soory you cannot deposit")

         else:
             userdata[0]['balance']+=amount
             bank.update()
             print("amount deposited")

      
    def withdraw(self):
      accnumber= input("please tell your ac no")
      pin=int(input("please tell your pin number"))

      userdata=[i for i in bank.data if i['account no']==accnumber and i['pin']==pin]
     
      if not userdata:
       print("no data found")
      

      else:
         amount=int(input("how much you want to withdraw-")) 

      if userdata[0]['balance']<amount:
         print("soory you dont have suffcient money")
        
      else:
          userdata[0]['balance']-=amount
          bank.update()
          print("amount withdrwan successfully")

         
    def showdetails(self):

        accnumber= input("please tell your ac no")
        pin=int(input("please tell your pin number"))
        
        
        userdata=[i for i in bank.data if i['account no']==accnumber and i['pin']==pin]
        print("\n\n") 
        for i in userdata[0]:
         print(f"{i} :{userdata[0][i]}")

    def updatedetails(self):

     accnumber = input("please tell your ac no- ")
     pin = int(input("please tell your pin number- "))
     userdata=[i for i in bank.data if i['account no']==accnumber and i['pin']==pin]

     if not userdata:
        print("no data found")
        

     print("you can't change account no, amount, age")
     print("fill the details to be changed")

     newdata = {
        "name": input("tell your new name- "),
        "email": input("tell your new email- "),
        "pin": int(input("tell your new pin- "))
      }

    # Update only the fields that can be changed
     userdata[0]["name"] = newdata["name"]
     userdata[0]["email"] = newdata["email"]
     userdata[0]["pin"] = newdata["pin"]

     bank.update()

    print("bank details updated successfully")
  
    def delete(self):
         accnumber= input("please tell your ac no")
         pin=int(input("please tell your pin number"))

         userdata=[i for i in bank.data if i['account no']==accnumber and i['pin']==pin]
     
         if not userdata:
          print("no data found")

          

         else:
             check=input("press y if you actually want to delete account or press n")
             if check=='n' or check=='N':
                print("By passed")

             else:
                 idx=bank.data.index(userdata[0])
                 bank.data.pop(idx)

                 print("deleted successfully")
                 bank.update()

          

       
   

user=bank()

print("press 1 for creating an account")

print("press 2 for deposit")

print("press 3 for withdraw")

print("press 4 for details")

print("press 5 for updating details")

print("press 6 for deleting you account")

check=int(input("tell your response-"))

if check==1:
    user.createaccount()


if check==2:
    user.deposit()

if check==3:
    user.withdraw()

if check==4:
   user.showdetails()

if check==5:
   user.updatedetails()

if check==6:
   user.delete()