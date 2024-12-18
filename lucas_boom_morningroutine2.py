import time                                                                     #imports time posibility
import datetime                                                                 #imports day possiblity

print ("Alarm!")                                                                #dispalay message "alarm!"                                                  #


while True:                                                                     #forever loop
    try:                                                                        #attempt the following
       hours = int(input("What hour is it: "))                                  #stores user response in variable hours
        minutes = int(input("What minute is it: "))                             #stores user response in variable minutes
        seconds = int(input("What second is it: "))                             #stores user response in variable seconds
        if hours <= 23 and hours >= 0 and minutes <= 59 and minutes >= 0 and seconds <= 59 and seconds >=0: #all time possilbies for seconds, hours, and years
            break                                                               #end loop
        else:                                                                   #else statement
            print("Please enter a possible time number")                        #tells user to print a possible time integer
    except ValueError:                                                          #do this except if there's a value error
        print("Enter integers only please")                                     #tells user to please enter a number

current_time = datetime.datetime(2024, 10, 23, hours, minutes, seconds)         #sets current time as hours, minutes, seconds
print(current_time.strftime("%H:%M:%S"), end='\r')                              #displanys current time

while True:                                                                     #Forever loop
    wake = str.lower(input("wake up? yes/no:"))                                 #stores user response in variable wake
    if wake == "yes":                                                           #if user inputs yes
        print ("get out of bed")                                                #display message
        current_time += datetime.timedelta(minutes=5)                           #adds 5 minutes to current time
        print(current_time.strftime("%H:%M:%S"), end='\r')                      #displays current time
        break                                                                   #leaves forever loop
    elif wake == "no":                                                          #if user inputs no
        print ("Sleep for 5 more minutes")                                      #display message
        time.sleep(2)                                                           #waits 2 seconds
        current_time += datetime.timedelta(minutes=5)                           #displays current time
        print(current_time.strftime("%H:%M:%S"), end='\r')                      #displays current time
    else:
        print ("invalid reponse")                                               #display message

while True:                                                                     #Forever loop
    shower = str.lower(input("shower? yes/no: "))                               #stores user response in variable shower                       
    if shower == "yes":                                                         #if user inputs yes
        print ("take a shower and get dry")                                     #display message
        current_time += datetime.timedelta(minutes=5)                           #displays current time
        print(current_time.strftime("%H:%M:%S"), end='\r')                      #displays current time
        break                                                                   #leaves forever loop
    elif shower == "no":                                                        #if user inputs no
        while True:                                                             #Forever loop
            brushteeth = str.lower(input("brushteeth? yes/no: "))               #stores user response in variable brushteeth
            if brushteeth == "yes":                                             #if user inputs yes
                print ("Brushing teeth")                                        #display message
                current_time += datetime.timedelta(minutes=5)                   #displays current time
                print(current_time.strftime("%H:%M:%S"), end='\r')              #displays current time
                break                                                           #leaves forever loop
            elif brushteeth == "no":                                            #if user inputs no
                print ("get dressed")                                           #display message
                current_time += datetime.timedelta(minutes=5)                   #displays current time
                print(current_time.strftime("%H:%M:%S"), end='\r')              #displays current time
                break                                                           #leaves forever loop
            else:
                print ("Invalid Response")                                      #display message
        break

while True:                                                                     #Forever loop                                     
    get_dressed = str.lower(input("getdressed? yes/no: "))                      #stores user response in variable get dressed 
    if get_dressed == "yes":                                                    #if user inputs yes
        print ("Getting dressed!")                                              #display message
        current_time += datetime.timedelta(minutes=5)                           #displays current time
        print(current_time.strftime("%H:%M:%S"), end='\r')                      #displays current time
        break                                                                   #leaves forever loop
    elif get_dressed == "no":                                                   #if user inputs no
        print ("Checking phone")                                                #display message
        current_time += datetime.timedelta(minutes=5)                           #displays current time
        print(current_time.strftime("%H:%M:%S"), end='\r')                      #displays current time
        break                                                                   #leaves forever loop
    else:
        print("invalid response")                                               #display message

while True:                                                                     #Forever loop
    brushhair = str.lower(input("brushhair? yes/no: "))                         #stores user response in variable brushhair
    if brushhair == "yes":                                                      #if user inputs yes
        print ("brush my hair")                                                 #display message
        current_time += datetime.timedelta(minutes=5)                           #displays current time
        print(current_time.strftime("%H:%M:%S"), end='\r')                      #displays current time
        break                                                                   #leaves forever loop
    elif brushhair == "no":                                                     #if user inputs no
        print ("go downstairs")                                                 #display message
        print ("put in contacts")                                               #display message                           
        print ("drive to school")                                               #display message
        current_time += datetime.timedelta(minutes=5)                           #adds 5 minutes to current time
        print(current_time.strftime("%H:%M:%S"), end='\r')                      #displays current time
        break                                                                   #leaves forever loop
    else:
        print("invalid response")                                               #display message

while True:                                                                     #Forever loop
    contacts = str.lower(input("contacts? yes/no: "))                           #stores user response in variable contacts
    if contacts == "yes":                                                       #if user inputs yes
        print ("put in contacts")                                               #display message
        print ("go downstairs")                                                 #display message
        print ("Drive to school")                                               #display message
        break                                                                   #leaves forever loop                                                               
    elif contacts == "no":                                                      #if user inputs no
        print ("brush my hair")                                                 #display message
        print ("go downstairs")                                                 #display message
        print ("drive to school")                                               #display message
        break                                                                   #leaves forever loop
    else:
        print("invalid response")                                               #display message

