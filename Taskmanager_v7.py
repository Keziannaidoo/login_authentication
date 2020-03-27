#------------------------------------------------Defining My functions -----------------------------------------------#
#Defining the menu option for admin user
index = 0
from datetime import datetime
def print_adminmenu():
    print('\nPlease select one of the following option:')
    print('r  - register user')
    print('ds - Stats')
    print('gr - generate report')
    print('a  - add task')
    print('va - view all task')
    print('vm - view my tasks')
    print('e  - exit')
    
#Defining the menu option for normal user
def print_usermenu():
    print('\nPlease select one of the following option:')
    print('a  - add task')
    print('va - view all task')
    print('vm - view my tasks')
    print('e  - exit')

    
#Part 1 : Login verify Fuction
#this function will verify the login details user enters with details stored in txt file.
#this function only gets called once user enters details 
def Verifylogin():
    confirm = True #set a boolean value to tru so the input will repeat untill correct
    while confirm:
        username_input = input("Please enter a vaild Username: ")
        password_input = input("Please enter a vaild Password: ")
        #The bottom will open user txt and see if the user input match the details stored 

        with open('User.txt', 'r') as Userfile:#opens txt file in read only
            f = Userfile.read()
                        
            if username_input and password_input in f: #if details are correct then function will return the user name 
               print("\nWelcome " + username_input + " you have succssfully logged in : \n")
               confirm = False                       
               return username_input

            else: #if login is not valid user will be prompted to enter again
                print("\nThe credentials entered in not vaild please try again! ")
            

        Userfile.close() #close txt file


#Part 2.1 : Register new user Function 
#function only gets called if user selects r option, they will be required to register new user
#user will first have to input username and password and password 
def RegisterUser():
    user_add_verify = True
    
    while user_add_verify: # the while loop will keep prompting user to enter until user registers
        #user input 
        print("\nPlease enter the following information below to add a user: \n")
        username_reg = input("Please input a usernme: ")
        password_reg = input("Please input your desired password: ")
        password_reg_confirm = input("Please input your password again: ")

        with open('User.txt', 'r') as UserfileAdd :#opens txt file in read only
            p = UserfileAdd.read() #reads the lines in the txt file 

            #if passwords entered does not match the second one user will be prompted to enter again until theres a match
            if username_reg in p:
                print('Username taken please try again!')

            #If the password entered dont match the second password user will have to try again
            elif password_reg != password_reg_confirm :
                print("\nThe password credentials entered does not match please enter again: ")

            #if the two passwords match and the username isnt in user.txt than the username and password will than be stored to user.txt
            elif password_reg == password_reg_confirm and username_reg not in p :
                user_add_verify = False
                print("\nWelcome " + username_reg + " you have succssfully registered: \n")
                #The following will write the username and password to txt file 
                with open('User.txt', 'a+') as UserfileAd :#opens txt file in read only
                    UserfileAd.write("\n")
                    UserfileAd.write(str(username_reg))#write the inputed username to user.txt file
                    UserfileAd.write(", ")
                    UserfileAd.write(str(password_reg)) #write the inputed password to user.txt file
                    UserfileAd.close()
                    
        UserfileAdd.close() #close file 


#Part 2.2 : add task function
#this function will only b if user selects a
#if user selects option a they will be answering questions to add a task to system, which will be stored in txt file 
def addtask():
    t = open('tasks.txt', 'a+') # Open the file again! and write
    #the following is user input that will assist in adding the task
    user_task_assigned = input("Enter the username of the person the task is assigned to: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the description of the task: ")
       
    #Below the 3 lines is used to get the current date 'todays date' and store it as the assigned date
    from datetime import date #imports function to be able to output current date 
    task_assigned_date = date.today().strftime('%d/%m/%Y') #saves current date in format dd/mm/yyyy and saves to variable
    print("The task assigned date is: " + task_assigned_date)
            
    task_due_date = input("Enter the due date dd/mm/yyyy of the task: ")
    task_status = "No"

    print("\nYour task has been added, to view please select option 'va' or 'vm' ")
    
    #write inputs that were entered by user to task.txt file
    t.write(user_task_assigned + ", ")
    t.write(task_title + ", ")
    t.write(task_description + ", ")
    t.write(str(task_assigned_date) + ", ")
    t.write(str(task_due_date) + ", ")
    t.write(task_status)
    t.write("\n")
    t.close() #close file once done

#Part 2.3 : View all tasks Function
#if user selects va than they want to see all tasks that are assigned to users, this will show them all tasks
#recalls information from txt file 
def VAtask():
    task_dict = {}
    i = 1
    with open("tasks.txt", 'r') as e:
        print("Please see all tasks below: \n")
        for line in e:
            listDetails = line.strip().split(', ')
            task_dict[i] = {"user_task_assigned": listDetails[0]}
            task_dict[i].update({"task_title": listDetails[1]})
            task_dict[i].update({"task_description": listDetails[2]})
            task_dict[i].update({"task_assigned_date": listDetails[3]})
            task_dict[i].update({"task_due_date": listDetails[4]})
            task_dict[i].update({"task_status": listDetails[5]})
            i+=1
    for T_id, T_info in task_dict.items():
        print("\nPerson ID:", T_id)
                
        for key in T_info:
            print(key + ':', T_info[key])

    e.close() #close txt file 


#Part 2.4 : View all tasks assigned to the current user signed in Fuction 
#if user selects vm in second menu, they will see all task that are assigned to them only
#[1] splits all lines in to the following groups so you can use data to only display current users tasks
def VMtask():
    task_dict = {} #empty Dictionary
    i = 1 #count to giev each task a number so you can edit task
    with open("tasks.txt", 'r+') as m:
        print("\nPlease see all tasks that have been assigned to " + current_user + " only! \n")
        for line in m:
            listDetails = line.strip().split(', ')
            if current_user == listDetails[0]: # display only tasks assigned t user signed in
                task_dict[i] = {"user_task_assigned": listDetails[0]}
                task_dict[i].update({"task_title": listDetails[1]})
                task_dict[i].update({"task_description": listDetails[2]})
                task_dict[i].update({"task_assigned_date": listDetails[3]})
                task_dict[i].update({"task_due_date": listDetails[4]})
                task_dict[i].update({"task_status": listDetails[5]})
                i+=1      
                
    for T_id, T_info in task_dict.items():
        print("\nTask ID:", T_id)

        for key in T_info:
            print(key + ':', T_info[key])
            
    edit_task(task_dict) #
  

    m.close() #close txt file
    

#Part 2.4.1 : Edit users task 
def edit_task(task_dict):
        Task_id_input = int(input("Enter Task ID :(Edit Task or Change Task Status) or ('-1')for main menu  : "))
        if Task_id_input in task_dict.keys(): #and task_dict[Task_id_input]["task_status"] == 'No':
            task_edit_choice = input("Enter 'e' - [Edit Task] or Enter 's' - [Change Task Status] : ")

            #Change the staus of the task you has specified 
            if task_edit_choice == 's':
                staus_edit = input("The Task is currently not complete, Would you like to Mark as complete ('Yes' or 'No') : ")

                if staus_edit == 'Yes': #if user enters yes tatus will change to yes
                    task_dict[Task_id_input]["task_status"] = staus_edit
                    print('Task Staus has been changed to Complete')
                    rewrite_tasks(task_dict)
                    
                else:
                    print("Task Staus not Changed")
                                                
            #If user select e than will be allowed to edit task shown below. 
            elif task_edit_choice == 'e':
                edit_task = input('Enter option to edit : \n"D" (Due Date) \n"UA" (User Assigned Task) : ')
                #If user decides to change the due date of the task.
                if edit_task == 'D':
                    task_due_date_edit = input("Enter the new due date dd/mm/yyyy for the task: ")
                    task_dict[Task_id_input]["task_due_date"] = task_due_date_edit
                    print('Task due date has been changed to Complete')
                    rewrite_tasks(task_dict)

                #If user decides to change the name of the user assigned to the task  
                elif edit_task == 'UA':
                    user_task_assigned_edit = input("Enter the Username Of the person you want to be assigned to task.") 
                    task_dict[Task_id_input]["user_task_assigned"] = user_task_assigned_edit
                    print('User assigned to task has been changed')
                    rewrite_tasks(task_dict)

        else: #if user enters -1 will be taken back to main menu
            print('Returning back to main menu') 
        
# Run through the task dictionary and write each value to the text file
def rewrite_tasks(task_dict):
    task_file = open('tasks.txt', 'w')
    for task in task_dict.values():
        for key, value in task.items():
            
            task_file.write(value + ", ")
        task_file.write("\n")
    task_file.close()

    
                
#Part 2.5 : Display Stats 
def DisplayStats():
    s = open('tasks.txt', 'r') #opens txt file in read only 
    print("\nNumber of Tasks Created:")
    number_of_tasks = len(s.readlines(  )) #counts the number of lines in the txt file,
    print(str(number_of_tasks) + " Tasks created")
    

    u = open('User.txt', 'r') #opens txt file in read only 
    print("\nNumber Of Users Registered : ")
    number_of_users = len(u.readlines(  )) #counts the number of lines in the txt file,
    print(str(number_of_users) + " users registered.")
    
    s.close()
    u.close()

#Part 2.6 : Generate report
#This function will aid in exporting stat about tasks and user to two txt file for admindef Generate_report():
    #Part2.6.1
def Generate_report():
    with open("tasks.txt", 'r') as e:
        count_overdue = 0 #Counts number of task over due
        count_no = 0  #counts number of tasks not complete
        count_yes = 0 #counts number of tasks complete
        task_dict = {} #empty dictionary to store info in text file 
        i = 1  #count for each task 
        for line in e: #this will loop over every line in txt and sort info in these groups, creating a dictionary for each line 
            listDetails = line.strip().split(', ')
            task_dict[i] = {"user_task_assigned": listDetails[0]}
            task_dict[i].update({"task_title": listDetails[1]})
            task_dict[i].update({"task_description": listDetails[2]})
            task_dict[i].update({"task_assigned_date": listDetails[3]})
            task_dict[i].update({"task_due_date": listDetails[4]})
            task_dict[i].update({"task_status": listDetails[5]})
            i+=1

            #Number of taskes created all together. 
            Number_of_tasks = len(task_dict)
            

            #Number of Tasks Completed 
            completed_tasks = listDetails[5] == "Yes" 
            if completed_tasks == True: #if true means task meets conditions above 
                count_yes += 1 #counting number of completed task
           
            #Number of Tasks Not Completed 
            not_completed_tasks = listDetails[5] == "No"
            if not_completed_tasks == True: #if true means task meets conditions above  
                count_no += 1 #counting number of not completed task 

                
            #The total number of tasks that haven’t been completed and that are overdue.  
            #the bottom converts all date to the corrent format so that we can compare dates 
            due_date_convert = datetime.strptime(listDetails[4], '%d/%m/%Y') #converts due dates 
            current_date = datetime.today().strftime('%d/%m/%Y') #This calcs the current date 
            curr_date = datetime.strptime(current_date, '%d/%m/%Y')#converts current date 

            overdue_tasks = listDetails[5] == "No" and due_date_convert < curr_date 
            if overdue_tasks == True: #if overdue is = to true means task meets both conditions above 
                count_overdue += 1
                
            
            #The percentage of tasks that are incomplete. 
            percent_incompleted = ((count_no / Number_of_tasks) * 100 )

            #The percentage of tasks that are overdue
            percent_overdue = ((count_overdue / Number_of_tasks) * 100 )


        #Below is print of all info calculated above
        print("Please Task Overview report on all tasks below: \n")
        print("Number of tasks Created                       : " + str(Number_of_tasks))
        print("Number of tasks not completed                 : " + str(count_no))
        print("Number of tasks completed                     : " + str(count_yes))        
        print("Number of tasks overdue                       : " + str(count_overdue))
        print("Percentage of tasks that are incomplete (%)   : " + str(int(percent_incompleted)))
        print("Percentage of tasks overdue/not completed (%) : " + str(int(percent_overdue)))

        with open("task_overview.txt", 'w') as gr:
            gr.write("Please report on all tasks below: ")
            gr.write("\nNumber of tasks Created                       : " + str(Number_of_tasks))
            gr.write("\nNumber of tasks not completed                 : " + str(count_no))
            gr.write("\nNumber of tasks completed                     : " + str(count_yes))
            gr.write("\nNumber of tasks overdue                       : " + str(count_overdue))
            gr.write("\nPercentage of tasks that are incomplete (%)   : " + str(int(percent_incompleted)))
            gr.write("\nPercentage of tasks overdue/not completed (%) : " + str(int(percent_overdue)))

        gr.close() #close file that writes info to

    (user(task_dict)) #calling next function 
    
    e.close() #close txt file


def user(task_dict):
    #Part 2.6.2: user overview, print stats on user and the task assigned to them 
    print('\n')
    print("User Overview report on all tasks below: \n")
    with open('User.txt', 'r') as Userfile:#opens txt file in read only
        user_dict = {} #empty dictionary to store info in text file 
        u = 1  #count for each task
        user_data_report = ""
        
        #Part 2.6.2.1 : 
        for line in Userfile: #this will loop over every line in txt and sort info in these groups, creating a dictionary for each line
            userlistDetails = line.strip().split(', ')
            user_dict[u] = {"username": userlistDetails[0]}
            user_dict[u].update({"password": userlistDetails[1]})
            u+= 1
            
            #list of variable which will store data and clear each loop 
            total_tasks = len(task_dict)
            total_users = len(user_dict)
            user_task_count = 0
            complete_count = 0
            overdue_count = 0
            not_complete_count = 0
            not_complete_overdue = 0
                            
            #Part 2.6.2.2 : loop that runs through task_dict values and stores them in 'task'
            for task in task_dict.values():
                #importing the current data and the task due dates and converting to 1 format
                task_due_date = task["task_due_date"] #open up the due dates and stores them in task
                today = datetime.today().strftime('%d/%m/%Y') #populates the current date
                curr_date = datetime.strptime(today, '%d/%m/%Y')#converts todays date
                due_date_convert = datetime.strptime(task["task_due_date"], '%d/%m/%Y') #converts due datesto format so the cyrrent date and due date can be compared 

                #Keeps count of number of task is assigned to each user.
                #for every loop the count adds by 1 is the user matches the task assigned name 
                if task["user_task_assigned"] == userlistDetails[0]:
                    user_task_count += 1
                    if user_task_count != 0: #if user task count is greater than 0 the following will apply to calculate the required
                        #percentage of the tasks assigned to that user have been complete
                        if task["task_status"].lower() == "yes":
                            complete_count += 1
                        #Percentage of the tasks assigned to that user must still be completed
                        if task["task_status"].lower() == "no":
                            not_complete_count += 1        
                        #Calculating the percentage of task that are incomplete and overdue for each user 
                        if task["task_status"].lower() == "no" and curr_date > due_date_convert: #if both confition are met that 1 will be added to count 
                            not_complete_overdue += 1 #count       
                    else: #if user task count is 0 due to user not having a task then the value in formula will be 0 
                        percent_not_complete = 0
                        percent_overdue_notcomplete = 0
                        percent_complete_count = 0


            #formulas to calculate user and task stats                   
            total_percent = int((user_task_count/total_tasks) * 100)               
            percent_complete_count = int((complete_count / user_task_count) *100)
            percent_not_complete = int((not_complete_count / user_task_count) * 100)
            percent_overdue_notcomplete = int((not_complete_overdue / user_task_count) * 100)
                
            #print out all data for user on screen 
            print("\n" + (userlistDetails[0].upper())) #print list of users
            print(" Number of tasks assigned  " + str(user_task_count)) #Number of task assigned to each user
            print(" Percentage of total tasks assigned to each user " + str(total_percent) + "%")
            print(" Percentage of tast that is completed " + str( percent_complete_count)+ "%")
            print(" Percentage of tast that must still be completed " + str(percent_not_complete) + "%")
            print(" Percentage of tasks not complete and overdue " + str(percent_overdue_notcomplete) + "%")

            user_data_report += ("\n" + (userlistDetails[0].upper())
                     +("\nNumber of tasks assigned  " + str(user_task_count))
                     +("\nPercentage of total tasks assigned to each user " + str(total_percent) + "%")
                     +("\nPercentage of tast that is completed " + str( percent_complete_count)+ "%")
                     +("\nPercentage of tast that must still be completed " + str(percent_not_complete) + "%")
                     +("\nPercentage of tasks not complete and overdue " + str(percent_overdue_notcomplete) + "%")
                     +("\n")
                      )

        print("\nTotal number Of task created  : " + str(total_tasks))
        print("Total number Of users created : " + str(total_users))

        #Storing all data constructed to txt file report
        #as each loop passes the data will be stored in the variable listed below  
        with open("user_overview.txt", 'w') as uo: #opens txt file, to write data to file
            uo.write(user_data_report)
            uo.write(("\nTotal number Of task created  : " + str(total_tasks)))
            uo.write("\nTotal number Of users created : " + str(total_users))
                                
        uo.close()#Close txt file 
        
    Userfile.close() #close txt file


#------------------------------------------------------Program logic -------------------------------------------------------------#
#Part B :
#Part 1 : user must enter login details
current_user = Verifylogin()

#Part 2.1 :if (Verifylogin(username_input, password_input)) "Username_input" == admin than the user will see admin menu only
#(Verifylogin(username_input, password_input)) recalls the return value which is the username_input
if current_user  == 'admin':
    while True: #this will loop the menu so that once user is done with task they can go into another option 
        print_adminmenu()#runs function which printes out menu 
        adminmenu = input("Enter option : ")
        #user options below which are than referred back to there relevant def function above 
        if adminmenu == "r":
            RegisterUser()

        elif adminmenu == "ds": #view Stats
            Generate_report()

        elif adminmenu == "gr": #view Stats
            Generate_report()
            
        elif adminmenu == "a": #add tasks 
            addtask()        
            
        elif adminmenu == "va": #View all Tasks
            VAtask()
            
        elif adminmenu == "vm":#View Task of signed in user 
            VMtask()            

        elif adminmenu == "e": #this option will exit program 
            exit()
                    
#Part 2.2 : if username_input is not == admin than user will see normal menu 
elif current_user != 'admin':
    while True : #this will loop the menu so that once user is done with task they can go into another option 
        print_usermenu() #runs function which printes out menu 
        usermenu = input("Enter option : ") #user input
        #user options below which are than referred back to there relevant def function above
        if usermenu == "a": #add tasks 
            addtask()
            
        elif usermenu == "va": #View all Tasks 
            VAtask()
            
        elif usermenu == "vm":#View Task of signed in user 
            VMtask()
            
        elif usermenu == "e": #this option will exit program 
            exit()


    



    
    
    


   
