import pickle
import os
class Member:
    def __init__(self, name, age,gender, mobile,email,bmi,membership):
        self.name=name
        self.age=age
        self.gender=gender
        self.mobile=mobile
        self.email=email
        self.bmi=bmi
        self.membership=membership
        if(bmi<18.5):
            self.regimen=regimens["18.5"]
        elif(bmi<25):
            self.regimen=regimens["25"]
        elif(bmi<30):
            self.regimen=regimens["30"]
        else:
            self.regimen=regimens["30+"]

    def view_profile(self):
        print("******************************************************")
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Gender : ",self.gender)
        print("Contact No. : ",self.mobile)
        print("Email : ",self.email)
        print("BMI : ",self.bmi)
        print("Membership Duration : ",self.membership)
        print("******************************************************")
    def view_regimen(self):
        print("******************************************************")
        for i in self.regimen:
            print(i+" : "+self.regimen[i])
        print("******************************************************")
    def set_regimen(self,key):
        self.regimen=regimens[key]

if(not os.path.isdir("regimens")):
    regimens={"18.5":{"Mon": "Chest","Tue": "Biceps","Wed": "Rest","Thu": "Back","Fri": "Triceps","Sat": "Rest","Sun": "Rest"},"25":{"Mon": "Chest","Tue": "Biceps","Wed": "Cardio/Abs","Thu": "Back","Fri": "Triceps","Sat": "Legs","Sun": "Rest"},"30":{"Mon": "Chest","Tue": "Biceps","Wed": "Abs/Cardio","Thu": "Back","Fri": "Triceps","Sat": "Legs","Sun": "Cardio"},"30+":{"Mon": "Chest","Tue": "Biceps","Wed": "Cardio","Thu": "Back","Fri": "Triceps","Sat": "Cardio","Sun": "Cardio"}}
    with open("regimens","wb") as regimens_file:
        pickle.dump(regimens,regimens_file)
else:
    with open("regimens","rb") as regimens_file:
        regimens=pickle.load(regimens_file)

flag=True

while(flag):
    print("1. Member Login")
    print("2. SuperUser Login")
    print("3. Exit")
    ch=int(input("Enter your choice : "))
    if(ch==1):
        ph=input("Enter your Phone number : ")
        if(os.path.isfile("members/"+ph)):
            with open("members/"+ph,"rb") as member_file:
                member=pickle.load(member_file)
                flag1=True
                while(flag1):
                    print("1. View Profile ")
                    print("2. View Regimen ")
                    print("3. Logout")
                    ch1=int(input("Enter your choice : "))
                    if(ch1==1):
                        member.view_profile()
                    elif(ch1==2):
                        member.view_regimen()
                    else:
                        flag1=False
        else:
            print("Phone number not found")
    elif(ch==2):
        password=input("Enter SuperUser Password : ")
        if(password=="admin"):
            flag2=True
            while(flag2):
                print("1. Create Member")
                print("2. View Member")
                print("3. Delete Member")
                print("4. Update Member")
                print("5. Create Regimen")
                print("6. View Regimen")
                print("7. Delete Regimen")
                print("8. Update Regimen")
                print("9. Logout")
                ch2=int(input("Enter your choice : "))
                if(ch2==1):
                    print("Enter The details of the member : ")
                    name=input("Name : ")
                    age=input("Age : ")
                    gender=input("Gender(M/F/O) : ")
                    mobile=input("Contact No. : ")
                    email=input("Email : ")
                    bmi=float(input("BMI : "))
                    membership=input("Membership Duration(1/3/6/12): ")
                    m=Member(name,age,gender,mobile,email,bmi,membership)
                    if(not os.path.isfile("members/"+mobile)):
                        member_file=open("members/"+mobile,"wb")
                        pickle.dump(m,member_file)
                        member_file.close()
                        print("Member created successfully")
                    else:
                        print("phone number already exists, member not created")
                elif(ch2==2):
                    mobile=input("Enter Phone number of the member : ")
                    if(not os.path.isfile("members/"+mobile)):
                        print("Phone number not found")
                    else:
                        with open("members/"+mobile,"rb") as member_file:
                            m=pickle.load(member_file)
                            m.view_profile()
                            m.view_regimen()
                elif(ch2==3):
                    mobile=input("Enter Phone number of the member : ")
                    if(not os.path.isfile("members/"+mobile)):
                        print("Phone number not found")
                    else:
                         os.remove("members/"+mobile,"rb")
                         print("Member Deleted Successfully")
                elif(ch2==4):
                    mobile=input("Enter Phone number of the member : ")
                    if(not os.path.isfile("members/"+mobile)):
                        print("Phone number not found")
                    else:
                        os.remove("members/"+mobile,"rb")
                        print("Enter The New details of the member : ")
                        name=input("Name : ")
                        age=input("Age : ")
                        gender=input("Gender(M/F/O) : ")
                        mobile=input("Contact No. : ")
                        email=input("Email : ")
                        bmi=float(input("BMI : "))
                        membership=input("Membership Duration(1/3/6/12): ")
                        m=Member(name,age,gender,mobile,email,bmi,membership)
                        member_file=open("members/"+mobile,"wb")
                        pickle.dump(m,member_file)
                        member_file.close()
                        print("Member Details updated successfully")
                elif(ch2==5):
                    reg=input("Enter the BMI range for regimen : ")
                    print("Enter regimen details as follows : ")
                    days=list(regimens["18.5"].keys())
                    for i in days:
                        regimen[reg][i]=input(i+" : ")
                    with open("regimens","wb") as regimens_file:
                        pickle.dump(regimens,regimens_file)
                    print("regimen Created successfully")
                elif(ch2==6):
                    print("The regimens are as follows : ")
                    for i in regimens:
                        print(i+" "+regimens[i])
                elif(ch2==7):
                    reg=input("Enter the BMI range for regimen you want to delete : ")
                    if(reg in regimens.keys()):
                        del regimens[reg]
                        with open("regimens","wb") as regimens_file:
                            pickle.dump(regimens,regimens_file)
                    else:
                        print("No regimen found for the given BMI range")
                elif(ch2==8):
                    reg=input("Enter the BMI range for regimen you want to update : ")
                    if(reg in regimens.keys()):
                        print("Enter regimen details as follows : ")
                        days=list(regimens["18.5"].keys())
                        for i in days:
                            regimen[reg][i]=input(i+" : ")
                        with open("regimens","wb") as regimens_file:
                            pickle.dump(regimens,regimens_file)
                    else:
                        print("No regimen found for the given BMI range")
                else:
                    flag2=False
        else:
            print("Incorrect Password")
    elif(ch==3):
        flag=False
    else:
        print("incorrect Choice")