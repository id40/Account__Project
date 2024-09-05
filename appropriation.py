def Appropriation ():
    netprofit=int(input("Enter the Net Profit: "))
    check=int(input("How Do you Want to Calculate Salary,Press 1 for per Month , Press 2 for per quator , press 3 for Half Yearly or Press 4 to Give it Directly : "))
    if check == 1:
         TotalSalary=0
         sal=[]
         partner=int(input("Enter the no of partner who get Salary :"))
         for i in range(partner): 
              Salary=int(input("Enter the Amount of Salary Given to The Partner :"))
              sal.append(Salary)
              totalsalary=Salary*12
              print("Total Salary of the Partner is : ", totalsalary)
              TotalSalary=TotalSalary+totalsalary
         print("Sum Total Salary of All Partner are : ",TotalSalary) 
    elif check == 2 :
         TotalSalary=0
         sal=[]
         partner=int(input("Enter the no of partner who get Salary :"))
         for i in range(partner): 
              Salary=int(input("Enter the Amount of Salary Given to The Partner :"))
              sal.append(Salary)
              totalsalary=Salary*4
              print("Total Salary of the Partner is : ", totalsalary)
              TotalSalary=TotalSalary+totalsalary
         print("Sum Total Salary of All Partner are : ",TotalSalary)
    elif check == 3 :
         TotalSalary=0
         sal=[]
         partner=int(input("Enter the no of partner who get Salary :"))
         for i in range(partner): 
              Salary=int(input("Enter the Amount of Salary Given to The Partner :"))
              sal.append(Salary)
              totalsalary=Salary*2
              print("Total Salary of the Partner is : ", totalsalary)
              TotalSalary=TotalSalary+totalsalary
         print("Sum Total Salary of All Partner are : ",TotalSalary) 
    elif check == 4 :
         TotalSalary=0
         sal=[]
         partner=int(input("Enter the no of partner who get Salary : "))
         for i in range(partner):
              Salary=int(input("Enter the Amount of Salary Given to The Partner :"))
              sal.append(Salary)
              TotalSalary=TotalSalary+Salary
         print("Sum Total Salary of All Partner are : ",TotalSalary)
    else :      
          print("Sorry wrong input , TRY Again Later . ")

    commission=int(input("Do you want to calculate the Commission ( [Press 1] or want to give it Directly[Press 2] ): "))
    if commission == 1:
              choice=int(input("Which method do you want to do calculation press 1 for before charging such profit or Press 2 for after charging such profit : "))
              if choice == 1:
                   totalcommission=0
                   counter=0
                   noofpartner=int(input("Enter the No. of Patner Whose Commission is to be Calculated: "))
                   rate=int(input("Enter the rate at which commission is to be calculated: "))
                   while counter<noofpartner:
                        calc=(netprofit*rate)//100
                        print(calc)
                        counter+=1
                        totalcommission=totalcommission+calc
                   print(totalcommission) 
              elif choice == 2:
                totalcommission=0
                counter=0
                noofpartner=int(input("Enter the No. of Patner Whose Commission is to be Calculated: "))
                rate=int(input("Enter the rate at which commission is to be calculated: "))
                while counter<noofpartner:
                    total=100+rate
                    calc=(netprofit*rate)//total
                    print(calc)
                    counter+=1
                    totalcommission=totalcommission+calc
                print(totalcommission)
              else :
                  print("Wrong input has been made , plz try it again ." )
    elif commission == 2:
         totalcommission=0
         counter=0
         noofpartner=int(input("Enter the No. of Patner Whose Commission is to be Calculated: "))
         while counter<noofpartner :
              total=0
              comm=int(input("Enter the amount of commission to be added : "))
              calc=comm+total
              counter+=1
              totalcommission=totalcommission+calc
         print(totalcommission) 
    else :
         print("Wrong input has been made , try Again Later. ")
         

    intrestonCapital=int(input("Do you want to Calculate Interest On Capital Press 1 or Want to give it Directly for that Press 2 : "))
    if intrestonCapital == 1:
         totalinterest=0
         ratios=[]
         cap=[]
         partner=int(input ("Enter the Total no of partner in the Company : "))
         for i in range(partner):
              ratio = int(input(f"Enter the ratio for Partner {i + 1}: "))
              ratios.append(ratio)
         for j in range(partner ):
              capital = int(input(f"Enter the capital contributed by Partner {j + 1}: "))
              cap.append(capital)
         for k in range(partner):
            IOC = (cap[k] * ratios[k]) // 100
            print(f"Interest on Capital for Partner {k + 1}: {IOC}")
            totalinterest=totalinterest+IOC
         print(totalinterest) 
    
    elif intrestonCapital == 2 :
         partner=int(input("Enter the no., of Total partner in a xcompany "))
         cap=[]
         for i in range(partner):
              capital=int(input("Enter the Amountr of Interest on Capital Given to the Partner : "))
              cap.append(capital)
              totalinterest=sum(cap)
         print("Total Interest on Capital Provided to the partner is :",totalinterest)
    else :
         print("Oops! Wrong Input Has Been Given , Try Again.")
    intrestonDrawing=int(input("Do you want to Calculate Interest On Drawing Press 1 or Want to give it Directly for that Press 2 : "))
    if intrestonDrawing == 1:
         total_drawing=0
         ratios=[]
         draw=[]
         partner=int(input ("Enter the Total no of partner in the Company : "))
         for i in range(partner):
              ratio = int(input(f"Enter the ratio for Partner {i + 1}: "))
              ratios.append(ratio)
         for j in range(partner ):
              drawing = int(input(f"Enter the amount which the Partner has Drowned {j + 1}: "))
              draw.append(capital)
         for k in range(partner):
              IOD=(draw[k]*ratios[k])//100
              print(f"Interest on Drawing for Partner {k + 1}: {IOD}")
              total_drawing=total_drawing+IOD
         print(total_drawing) 
    
    elif intrestonDrawing == 2 :
         partner=int(input("Enter the no.of  partner in a Company who have used the Drawing Facilities:  "))
         draw=[]
         for i in range(partner):
              capital=int(input("Enter the Amount of Interest on Drawing Of the Partner : "))
              draw.append(capital)
         totaldrawing = sum(draw)
         print("Total Interest on Drawing Provided to the partners is:", totaldrawing)
    else :
         print("Oops! Wrong Input Has Been Given , Try Again.")
    creditside=netprofit+totaldrawing
    debitside=TotalSalary+totalcommission+totalinterest
    if creditside > debitside :
         Total=creditside-debitside
         print("There is a Profit in Appropriation :), and it is ",Total)
    elif debitside > creditside :
          Total=debitside-creditside
          print("There is a Loss in Appropriation :( , and it is ",Total)
    elif creditside == debitside :
         print ("Congurlation ! , There is no Profit no Loss Situation Everything is Alright . ")
    choose=input("Do you Want to Distribute It In Ratio [yes/no] : ")
    if choose.lower() == 'yes' and Total != 0:
         Ratio=[]
         Partner=int(input("How many Partners Are there In The Firm : "))
         for i in range(Partner):
              Ratios=int(input("Enter the Ratio Of The Partner's : "))
              Ratio.append(Ratios) 
         ToTalRatio=sum(Ratio)
         for j in range(Partner):
              Calculation=(Total*Ratio[j])//ToTalRatio
              print("Distribution of Profit or Loss To the Partner According To the Ratio are : ",Calculation)

Appropriation()     

