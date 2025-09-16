age=int(input("Enter your age:"))
height=int(input("Enter your height:"))
credits=int(input("Enter your credits:"))

if age==18:
    print("Welcome VIP! Your ticket is free")
elif age<7:
     print("You are too young. Please go to the kids Zone")
elif 7<=age<=12:
      print("Welcome! You can go to the Space Playground")
elif 13<=age<=15:
     print("Graet! You can go to the training mission")
else:
     if 16<=age<=17 & height>160:
        print("You are tell enough. You can fly the small ships")
     else:
          print("Sorry, you are too short to fly the ships")
          
          if age>=19 & credits>=100:
               print("Welcome Explorer! You can join the Galaxy Mission")
          else:
            print("Sorry, you don`t have enough credits")   
