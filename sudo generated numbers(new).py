a = 75
c = 80
m = 2**16 + 1
#This is a built in library to get the computer system time
import time
current_time = time.time() #  This function returns the number of seconds passed since epoch.
#this is the function used to gernerate psudorandom numbers / True random numbers from the users seed or System time or file-read
def sudo_generated_number():
    
#This is another function used to print a message with the instructions for the user     
    def User_message():
        print("The Software will give you three options to run program through either system time or User input seed or file open ")
    User_message()
#This is a loop that first asks the user to choose which method he would like to use
#Also inside the loop it checks which method is used and it takes the seed and it goes through the loop 50 times    #The number of loops can be easily changed 
    user_answer = str(input("please enter m/M for manuall seed or s/S for system time seed or f/F for file_read generated seed :"))   
    if  user_answer == 's' or user_answer == 'S' :
            while True: #while the conditions are true
                seed = int(current_time)
                for i in range(50):
                    seed = (a * seed + c) % m
                    print(seed)
#After the loop cycles through for 50 times it stops using the break line
                else:
                    break
                
#Here we have another loop but this time for the user to enter the seed manually

    elif  user_answer == 'm' or user_answer == 'M' :
            while True:
                seed = int(input("please enter a seed:"))
                for i in range(50):
                    seed = (a * seed + c) % m
                    print(seed)
                else:
                    break
#Here we have another loop but this time for the user to Read from file seed
    elif  user_answer == 'f' or user_answer == 'F' :
             while True:
                file_name = input("please enter the file path & name :")
                file = open(file_name, "r")#This line opens the file #please specify the file name & path
                seed = int(file.read()) * int(current_time)# This line reads the seed from the file then multiples it by the time to be more random
                for i in range(50):
                    seed = (a * seed + c) % m
                    print(seed)
                else:
                         break
    else:
#\n is used to make a new line 
        print("\n\n\nWrong value please try again !!!")
#returning the value of the function
sudo_generated_number()


           