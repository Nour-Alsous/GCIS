'''NAMES---
Nour Alsoos worked on the main
Mohin Ayaz worked on functions
Nabil worked on functions
This program is created to take input from the user and convert the number into another currency. The user can convert the amount they want 
from AED to pound, dollar, or euro or the other way around. The user enters what currency they want converted from and to with the amount. Then the code converts
it and prints it out.
Nour's repoistory:https://github.com/Nour-Alsous/GCIS
Mohsin's repository: https://github.com/ayazmohsin/rep-1.git 
Nabil's repository:
'''

#the constants to convert from AED to other currencies
usd1 = 0.27
euro1 = 0.25
gbp1 = 0.22

#the constants to convert from other currencies to AED
usd2=3.67
euro2=3.98
gbp2=4.65

#AED to Euro function

def aed_to_eur(user_aed,x): 
    if x == 1:
        print (user_aed * euro1)

#AED to pound function
        
def aed_to_britishPound(user_aed,x):
    if x == 2:
        print (user_aed * gbp1)
        
#AED to dollars function

def aed_to_dollar(user_aed,x): 
    if x == 3:
        print (user_aed * usd1)

#Dollar to AED
        
def dollar_to_aed(curr_type , amount):
    if curr_type == 1:
        print (amount * usd2)

#Pound to AED
        
def britishPound_to_aed(curr_type , amount): 
    if curr_type == 2:
        print (amount * gbp2)
        
#Euro to AED

def eur_to_aed(curr_type , amount):
    if curr_type == 3:
        print (amount * euro2)
    


def main():
    while True: #we initiated the infinite loop until we reached a break statement
        #this is the structure of the main menu
        
        print("    \"Main Menu\"  ")
        print('-----------------')
        print("Welcome to Currency Convertor\n 1. Convert from AED to other currencies \n 2.Convert from other currencies to AED \n 3. Exit")
        
        #user is asked to input which option they want
        
        service = input("Please select your option 1,2,3:")
        
        #if the user enters 1 this code is executed
        
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
        
        elif service=='3': #if the user writes 3 they will exit the code
            break
        else:
            print("incorrect input") #if a user enters a wrong input then it will say incorrect input
            
        while True: #this while loop is used to make the code repeat until the user enters n that stands for no and then the code
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
