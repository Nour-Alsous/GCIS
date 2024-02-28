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
    
            
