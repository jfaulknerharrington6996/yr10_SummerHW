#times table prgram by josiah harrington
#this program will ask the user for a number and display the times table of that number up to however much that the user wants

###imports###
import time #time.sleep is added for pauses so the user can understand what is going on at a better pace

###variables###
z = 1 #this variable has been made as a counter that can be used so that the times table will be displayed appropriatly
User_Amount = 0 #this is for asking how many times the user wants to find out how many times tables and their awnsers

###funtions###
def User_Number():#this is a funtion to have the user enter a number that will go to the loop_print funtion
    global User_Amount
    global number #global funtions allow it to be used in another funtion when it has been assigned inside a different funtion
    number = int(input("Please enter a number to find its times table\n")) #this uses a int( peramiter so the only thing that can be entered is a interger and not an letters
    time.sleep(0.5)
    User_Amount = int(input("How many times tables of this number would you like to know?\n")) #this variable has been made to ask the user how many times they would like to find out the times table of the certain number
    time.sleep(0.5)
    Loop_Print() #this leads to the next step of the loop which will print out the outcomes
    return User_Amount #returns te value of User_Amount to be used in another place

def Loop_Print():
    global User_Amount
    global z
    for x in range(0,User_Amount,1): #this is a 'for' loop which will be used to make sure that the loop is only being used to display x number of times tables depending on the users choice
        newnumber = number * z #this is the calclation for the times tables to take place
        z = z + 1 #the counter is being increased by one each time to have a different times table number to be displayed
        time.sleep(0.5)
        print ("{0} x {1} = {2}".format(z - 1,number,newnumber))#this displays the end result of the calculation in a appropriate form
        time.sleep(0.025)
    Second_number() #this calls the next funtion for the task
    
def Second_number(): # this funtion will ask the user if they want to find the times tables of another number
    global z
    global number
    z = 1
    time.sleep(0.5)
    choice = input("\nWould you like to select another number?\n" # this is the choice stage where the user input decides if they will either select another times table or to quit the program
                       "Yes = Y\n"
                       "No = N\n")
    time.sleep(0.5)
    if choice == "Y": #this if statement makes it so if the user wants to carry on and do another times table then it goes back to the User_Number funtion
        User_Number()
    if choice == "N": #this if statement will make the program close if the user doesnt want to carry on with the program
        time.sleep(0.5)
        print("This program will now close") #displaint that the program is closing
        time.sleep(0.5)
        quit #this is terminating everthing that is running and stop the code

def Main_Menu(): #this funtion is the first to be called and will display a menu to the user to guid them of what to do next
    time.sleep(1)
    print("Welcome to the times table program\n") #welcoming the user to the program
    time.sleep(1)
    print("This program is used to find out the times table of a number up to how ever much you want\n") #explaing what the program does
    time.sleep(1)
    User_Number() #calls the funtion to start off the code and find the Users first numner to find the selected amount of times table to display

###Main Probgram###
Main_Menu() #this is the first funtion in the main program that will display the main menu to the user to show them what they have to do next

