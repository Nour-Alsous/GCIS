def main():
    while True: #we intiated the infinte loop until we reach a break statement
        #this is the structure of the main menu
        
        print("    \"Main Menu\"  ")
        print('-----------------')
        print("Welcome to Currency Convertor\n 1. Convert from AED to other currencies \n 2.Convert from other currnecies to AED \n 3. Exit")
        
        #user is asked to input which option they want
        
        service = input("Please select your option 1,2,3:")
        
        #if user enter 1 this code is executed
        
        if service == "1":
            #the user is asked to enter the amount of  money they want
            user_aed = int(input("Please type the amount of money you want to convert: "))
            
            #user is asked to choose the conversion they want
            x = int(input(" 1 to convert to USD \n 2 to convert to GBP \n 3 to convert to Euro"))
            
            #functions are called accordingly
            aed_to_eur(user_aed,x)
            aed_to_dollar(user_aed,x)
            aed_to_britishPound(user_aed,x)
        
        elif service=='2': #starts in case the user enters 2
            
            #user enters the amount of money
            amount = int(input("Please type the amount of money you want to convert: "))
            
            #user chooses the currency
            curr_type = int(input("what currency would you like to convert from? \n 1 from USD \n 2 from GBP \n 3 from Euro"))
            
            #functions are called
            eur_to_aed(curr_type,amount)
            britishPound_to_aed(curr_type , amount)
            dollar_to_aed(curr_type , amount)
        
        elif service=='3': #if user writes 3 they will exit the code
            break
        else:
            print("incorrect input") #if user enters a wrong input then it will say incorrect input
            
        while True: #this whiel loop is used to make the code repeat again until the user enter n that stand for no and then the code
            #stops working
            
            repeats=input("Do you want to repeat? y/n")
            
            if repeats=='y': # this makes the code repeat
                 break
            elif repeats=='n': #this makes the code stop
                print("Existing program")
                return
            else:
                print("Please choose either y or n") #this tells the user to put in either y or n
            
                
if __name__=="__main__":
    main()
