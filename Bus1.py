class Bus1:
    busNum=[1,2,3,4,5]
    source= ["gaza","Nablus","istanbul","berlin","Osaka"]
    destination= ["roma","cairo","tokyo","Seoul","Paris"]
    reservedSeats1 = [2,4,5,7,9]#المقاعد المحجوزة في باص 1
    reservedSeats2 = [2,3,5,7,9]#المقاعد المحجوزة في باص 2
    reservedSeats3 = [2,1,5,7,9]#المقاعد المحجوزة في باص 3
    reservedSeats4 = [2,3,5,7,9]#المقاعد المحجوزة في باص 4
    reservedSeats5 = [2,4,5,7,9]#المقاعد المحجوزة في باص 5


    def dataBus(self,busNum):
     for i in range(len(busNum)):
      dic = {Bus1.busNum[i]:{Bus1.source[i]:Bus1.destination[i]}} 
      print(dic) 

    def add(self):
        choiceBus = int(input("Enter Your Bus:"))
        if(choiceBus == Bus1.busNum[0]):
            print("reservedSeats1 = [2,4,5,7,9]")
            i=0
            x=int(input("Enter your seat: "))   #x تمثل رقم المقعد المراد حجزه
            for i in range(len(Bus1.reservedSeats1)):
             if(x==Bus1.reservedSeats1[i]):
                print("This seat is reserved .. Choose another seat")
                while x==Bus1.reservedSeats1[i]:
                     x=int(input("Enter your seat again!: "))
                Bus1.reservedSeats1.append(x)   
                print('New seat has been reserved!', Bus1.reservedSeats1)
                break
            else: 
                Bus1.reservedSeats1.append(x)
                print('New seat has been reserved!', Bus1.reservedSeats1)

        elif(choiceBus == Bus1.busNum[1]):
            print("reservedSeats2 = [2,3,5,7,9]")
            i=0
            x=int(input("Enter your seat: "))
            for i in range(len(Bus1.reservedSeats2)):
             if(x==Bus1.reservedSeats2[i]):
                print("This seat is reserved .. Choose another seat")
                while x==Bus1.reservedSeats2[i]:
                 x=int(input("Enter your seat again!: "))
                Bus1.reservedSeats2.append(x)   
                print('New seat has been reserved!', Bus1.reservedSeats2)
                break
            else: 
                Bus1.reservedSeats2.append(x)
                print('New seat has been reserved!', Bus1.reservedSeats2)

        elif(choiceBus == Bus1.busNum[2]):
            print("reservedSeats3 = [2,1,5,7,9]")
            i=0
            x=int(input("Enter your seat: "))
            for i in range(len(Bus1.reservedSeats3)):
             if(x==Bus1.reservedSeats3[i] ):
                print("This seat is reserved .. Choose another seat")
                while x==Bus1.reservedSeats3[i]:
                 x=int(input("Enter your seat again!: "))
                Bus1.reservedSeats3.append(x)   
                print('New seat has been reserved!', Bus1.reservedSeats3)
                break
            else: 
                Bus1.reservedSeats3.append(x)
                print('New seat has been reserved!', Bus1.reservedSeats3)

        elif(choiceBus == Bus1.busNum[3]):
            print("reservedSeats4 = [2,3,5,7,9]")
            i=0
            x=int(input("Enter your seat: "))
            for i in range(len(Bus1.reservedSeats4)):
             if(x==Bus1.reservedSeats4[i]):
                print("This seat is reserved .. Choose another seat")
                while x==Bus1.reservedSeats4[i]:
                 x=int(input("Enter your seat again!: "))
                Bus1.reservedSeats4.append(x)   
                print('New seat has been reserved!', Bus1.reservedSeats4)
                break
            else: 
                Bus1.reservedSeats4.append(x)
                print('New seat has been reserved!', Bus1.reservedSeats4)

        elif(choiceBus == Bus1.busNum[4]):
            print("reservedSeats5 = [2,4,5,7,9]")
            i=0
            x=int(input("Enter your seat: "))
            for i in range(len(Bus1.reservedSeats5)):
             if(x==Bus1.reservedSeats5[i]):
                print("This seat is reserved .. Choose another seat")
                while x==Bus1.reservedSeats5[i]:
                 x=int(input("Enter your seat again!: "))
                Bus1.reservedSeats5.append(x)   
                print('New seat has been reserved!', Bus1.reservedSeats5)
                break
            else: 
                Bus1.reservedSeats5.append(x)
                print('New seat has been reserved!', Bus1.reservedSeats5)
def meun():
    print("1- Display all dataBus")
    print("2- Add new Reservation")
    print("3- Quit")
    global choice
    choice = int(input("Enter Your Choice:"))

B=Bus1()

while(True): 
    meun()
    if choice ==1:
     B.dataBus(B.busNum)  
    elif choice==2:
     B.add()
    elif choice==3:
        print("Thank you!")
        break 
    else:
        print("Invalid choice!! Try again")    