def revaluation():
    selection = []
    decision = []
    negative = 0
    positive = 0
    sum_total1 = 0
    sum_total2 = 0

    print("""Description
	   In asset:-
	   press 1 for stock
	   press 2 for plant/machinery
	   press 3 for land/building
	   press 4 for furniture
	   press 5 for investment
	   press 6 for patent
	   press 7 for cash/bank
	   
	   In liability:-
	   press 8 for provision for doutfull debt
	   press 9 creditor
	   press 10 for workman compensioation reserve """)

    choose_1 = int(input(
        "How many input do you want to give in debit side of revaluation account: "))
    while sum_total1 < choose_1:
        select = int(input(
            "See the above description and enter the no.of asset and liability which will go to the debit side of revaluaition account: "))
        selection.append(select)
        sum_total1 += 1
        if sum_total1 == choose_1:
            check_1 = input("Do you want to add any more data[yes/no]: ")
            if check_1.lower() == 'yes':
                sum_total1 = 0
                more = int(
                    input("How many more data do you want to add more: "))
                choose_1 = more
    for i in selection:
        if i == 1:
            accept = int(input("Enter the decreased amount of stock: "))
            negative = negative+accept
        elif i == 2:
            accept = int(
                input("Enter the depreciated amount of plant/machinery: "))
            negative += accept
        elif i == 3:
            accept = int(input("Enter the amount of land and building: "))
            negative += accept
        elif i == 4:
            accept = int(input("Enter the amount of depreciated furniture: "))
            negative += accept
        elif i == 5:
            accept = int(input("Enter the deducted amount of investment:  "))
            negative += accept
        elif i == 6:
            accept = int(input("Enter the amount of patent: "))
            negative += accept
        elif i == 7:
            accept = int(input("Enter the amount cash/bank :"))
            negative += accept
        elif i == 8:
            accept = int(
                input("Enter the amount of provision for doubtful debt: "))
            negative += accept
        elif i == 9:
            accept = int(input("Enter the amount for creditor : "))
            negative += accept
        elif i == 10:
            accept = int(
                input("Enter the amount of workmen compensation reserve : "))
            negative += accept
        else:
            print("Sorry!, wrong input has been made try again later. ")

    choose_2 = int(input(
        "How many input do you want to give in credit side of revaluation account: "))
    while sum_total2 < choose_2:
        decide = int(input(
            "See the above description and enter the no.of asset and liability which will go to credit side of revaluaition account: "))
        decision.append(decide)
        sum_total2 += 1
        if sum_total2 == choose_2:
            check = input("Do you want to add more data[yes/no]: ")
            if check.lower() == 'yes':
                sum_total2 = 0
                more_2 = int(
                    input("How many more data do you want to enter: "))
                choose_2 = more_2
    for j in decision:
        if j == 1:
            amount = int(
                input("Enter the amount in which stock has been appreciated: "))
            positive += amount
        elif j == 2:
            amount = int(
                input("Enter the appreciated amount of plant/machinery: "))
            positive += amount
        elif j == 3:
            amount = int(input("Enter the amount of land and building"))
            positive += amount
        elif j == 4:
            amount = int(input("Enter the appreciated amount of furniture: "))
            positive += amount
        elif j == 5:
            amount = int(
                input("Enter the amount by which investment has been increased:  "))
            positive += amount
        elif j == 6:
            amount = int(input("Enter the increased amount of patent: "))
            positive += amount
        elif j == 7:
            amount = int(input("Enter the amount cash/bank :"))
            positive += amount
        elif j == 8:
            amount = int(
                input("Enter the amount of provision for doubtful debt: "))
            positive += amount
        elif j == 9:
            amount = int(input("Enter the amount for creditor : "))
            positive += amount
        elif j == 10:
            amount = int(
                input("Enter the amount of workmen compensation reserve : "))
            positive += amount
        else:
            print("Sorry!, wrong input has been made try again later. ")

    if negative > positive:
        total = negative-positive
        print("There is a loss on revaluation :(, and it is:", total)

    elif positive > negative:
        total = positive-negative
        print("There is a profit on revaluation :), and it is: ", total)

    else:
        print("There is a no profit, no loss situation on revaluation.")

    choice = input(
        "Do you want to distribute revaluation in partners ratio[yes/no]: ")
    if choice.lower() == 'yes':
        total_ratio = 0
        ratios = []
        partner = int(input(f"Enter the no. of partners' in a firm: "))
        for i in range(partner):
            ratio = int(input(f"Enter the ratios of the partners {i+1}: "))
            ratios.append(ratio)
        total_ratio = sum(ratios)
        for j in range(partner):
            total_rev = (total*ratios[j])//total_ratio
            print(
                f"partner {j+1} distribution of profit/loss on revalution are: {total_rev} ")


revaluation()
