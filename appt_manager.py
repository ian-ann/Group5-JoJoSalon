# *****************************************************************************************************************************
# This program was made for Jojo's Hair Salon appointment management system. This is to track their client's details including 
# name, phone number, appointment type, and corresponding schedule in terms of day and time. The program can also create a 
# one-week calendar of available appointments: Mondays - Saturdays from 9AM-4PM daily (wherein last appointment is 4PM-5PM). The 
# program also allows the users/clients to load their previously booked appointments into the calendar, and perform tasks such as 
# schedule and cancel an appointment, find appointment by name, print calendar for a specific day, and save all scheduled 
# appointments to a file.
#
#  Inputs:
#    Appointment filename
#    Day and time of appointment
#    Customer's name and phone number
#    Type of appointment (from options menu)
#
#  Output:
#    Appointment manager menu options
#    Appointment types
#    Appointment and weekly calendar
#
#  Output Messages:
#    Error messages
#    Confirmation messages  
#
#  Group Assignment
#    Victor Flores Jr
#    Marian Estrada
#    Kristel Palgan

#  Version 2023-Dec-06
# ***************************************************************************************************************************

import appointment as ap
import os

# Declare variables and constants
BINARY_CHOICE = ['Y','N']
OPERATING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
OPERATING_HOURS = range(9,17)
TABLE_HEADER = f'{"Client Name":20s}{"Phone":15s}{"Day":10s}{"Start":10s}{"End":10s}{"Type":20s}\n{"-"*80}'
APPT_TYPE_PRICE = {1:"$50",2:"$80",3:"$50",4:"$120"}
ERROR_PROMPT = 'Sorry that time slot is not in the weekly calendar!'
OPTIONS_BANNER = {'1':'Schedule an appointment', '2': 'Find appointment by name',
                     '3':'Print calendar for a specific day',
                     '4': 'Cancel an appointment', '9':'Exit the system'}


def show_appointments_by_day(appt_list, day):
    ''' This function receives the day of the appointment, searches from the appointment list and displays all matching appointments.

    Arguments: appointment list and day of appointment '''

    print(TABLE_HEADER)    
    # Check if appointment is already booked
    for appt in appt_list:
        if appt.get_day_of_week() == day:
            print(appt) 

def save_scheduled_appointments(appt_list, file_name):
    '''  This function prompts the user to input the filename for their appointment. It checks if the file already exists,
    and if so, gives the user the option to proceed (overwrite) or repeat the filename input. It then iterates over each
    appointment in the list and writes the scheduled appointments to the file in CSV format.

    Arguments: appointment list,  file name 
    
    Returns: records count / number of scheduled appointments saved '''

    records_cnt = 0
    
    if check_file_exists(file_name):
        overwrite_file = input('File already exists. Do you want to overwrite it (Y/N)?: ').upper()
        if overwrite_file == 'N':
            file_name = input('Enter appointment filename: ')

    appointment_file = open(file_name,"w")
    for appt in appt_list:
        if appt.get_appt_type() != 0:
            appt_row = appt.format_record()
            appointment_file.write(appt_row + "\n")
    appointment_file.close()

    # Check how many records in the file
    appointment_file = open(file_name,"r")
    for files in appointment_file:
        records_cnt += 1

    print (f'{records_cnt} scheduled appointments have been successfull saved\n')


def show_appointments_by_name (appointment_list, name):
    ''' This function receives the name of the client, searches from the appointment list and displays all matching appointments 
    allowing partial and non-case sensitive matches.

    Arguments: appointment list and name of customer '''
     
    name=name.strip().upper()
    nameExists = False
    print (TABLE_HEADER)
    for appt in appointment_list:
        clientName = appt.get_client_name().upper()
        if clientName.startswith(name):
            nameExists = True
            print (appt)
    if not nameExists:
        print ('No appointments found.')

def find_appointment_by_time (appointment_list, day, hour):
    ''' This function finds an appointment for a given day and start hour. If the appointment is found from the appointment
    list, it returns the appointment object otherwise, returns nothing.

    Arguments: appointment_list, appointment day, appointment start hour
    
    Returns: appointment object if found from the appointment list, otherwise returns nothing'''

    for appt in appointment_list:
        if appt.get_day_of_week() == day and \
           appt.get_start_time_hour() == hour:
            return appt

def print_menu():
    ''' This function prompts a menu and allows customer to choose from the given options.
    It ensures that the input is valid prior to returning the value. 

    No parameters/arguments taken

    Returns: menu option selected by user '''

    print (f'\n\nJojo\'s Hair Salon Appointment Manager\n{"="*37}')
    for menuNumbers, description in OPTIONS_BANNER.items():
        print (f' {menuNumbers}) {description}')

    menuChoice = input ('Enter your selection: ').strip()
    while menuChoice not in OPTIONS_BANNER:
        menuChoice = input ('Invalid Input - Enter a selection from the menu: ').strip()
    return (menuChoice)

def load_scheduled_appointments (appointment_list, filename):
    ''' This function loads a scheduled appointment from a file. It reads / iterates over each line of the appointments in the file, 
    parses the attribute values into separate variables, and calls find_appointment_by_time() to locate the corresponding appointment 
    in the list. It then invokes the schedule() method to set the properties appropriately.
    
    Arguments: appointment list and filename

    Returns: number of scheduled appointments loaded '''

    schedule_file = open (filename,'r')
    count_appts = 0
    for line in schedule_file:
        line = line.strip()
        appointment_line = line.split(',')
        name = appointment_line [0]
        phone = appointment_line [1]
        appt_type = int(appointment_line [2])
        day = appointment_line[3]
        hour = int(appointment_line [4])
        appointment_slot = find_appointment_by_time (appointment_list,day,hour)
        appointment_slot.schedule (name,phone,appt_type)
        count_appts += 1
    schedule_file.close()
    return count_appts

def create_weekly_calendar (appointment_list):
    ''' This function creates a weekly calendar by iterating through each day of the week from Mondays to Saturdays and its available 
    hours for each day from 9AM to 4PM. It then creates new appointment object and adds it to the appointment list.

    Arguments: appointment list'''

    for day in OPERATING_DAYS:
        for time in OPERATING_HOURS:
            appointment_list.append(ap.Appointment(day, time))

def check_file_exists(file_name):
    ''' This function checks and validates if the customer's given appointment file exist.
    
    Argument: appointment file name

    Returns: TRUE if appointment file is found, otherwise FALSE'''

    found = False

    if os.path.isfile(file_name):
        found = True

    return found
   
def enter_client_name():
    ''' This function is to display client's name upon input.
    
    No parameters/arguments taken

    Returns: client's name '''

    name = input('Client Name: ').capitalize()

    return name
  

def validate_day_and_time(day, time):
    ''' This function validates if client's inputted day is within Mondays to Saturdays and if inputted time is within 9AM to 5PM.

    Arguments: day (Monday-Saturday) and time (9AM - 5PM)

    Returns: TRUE if day and time is within operating days and hours, otherwise FALSE '''
    operational_times = True
    if (day not in OPERATING_DAYS or time not in OPERATING_HOURS):
        print(ERROR_PROMPT)
        operational_times = False
    return operational_times

def print_appointment_types():
    ''' This function is to print/display appointment types along with their corresponding prices '''
    menu_desc = ap.Appointment.menu_desc
    index = 0
    menu_desc_withprice = ""
    for type in APPT_TYPE_PRICE:
        if type in menu_desc:
            menu_desc_withprice += f'{type}: {menu_desc[type]} {APPT_TYPE_PRICE[type]}'
        if index != len(APPT_TYPE_PRICE) - 1:
            menu_desc_withprice += ", "
        index += 1


def main():    
    ''' Contains the main logic and functionality of the program. '''

    # Declare Variables
    appt_list = []
    
    print('\nStarting the Appointment Manager System\n')

    # Create weekly calendar
    create_weekly_calendar(appt_list)
    print('Weekly calendar created\n')

    # Call Load Schedule Appointments if Yes to load
    load_file = input('Would you like to load previously scheduled appointments from a file (Y/N)? ').upper().strip()
    while load_file not in BINARY_CHOICE:
            load_file = input('Invalid selection. Load previously scheduled appointments from a file (Y/N)? ').upper().strip()
    
    if load_file == 'Y':
        file_name = input('Enter appointment filename: ').strip()

        while check_file_exists(file_name) == False:
            file_name = input('File not found. Re-enter appointment filename: ').strip()

        # Print records loaded
        print (f'{load_scheduled_appointments (appt_list,file_name)} previously scheduled appointments have been loaded')

    # Call Print Menu
    menuOption = print_menu()

    while menuOption != '9':
        match menuOption:         
            case '1':
                print (f'\n** {OPTIONS_BANNER["1"]} **')
                day = input('What day: ').capitalize()
                time = int(input('Enter start hour (24 hour clock) : '))
                if validate_day_and_time(day, time):
                    current_appt = find_appointment_by_time(appt_list, day, time)
                      
                    if current_appt.get_appt_type() != 0::
                        print("Sorry that time slot is booked already")
                    else:
                        client_name = enter_client_name()
                        client_phone = input('Client Phone: ')
                        print_appointment_types()
                        appt_type = int(input('Type of Appointment: '))
                        if appt_type not in APPT_TYPE_PRICE:
                            print('Sorry that is not a valid appointment type!')
                        else:
                            current_appt.schedule(appt_type, client_name, client_phone)
                            print(f'OK, {client_name}\'s appointment is scheduled!')
            case '2':
                print (f'\n** {OPTIONS_BANNER["2"]} **')
                client_name = enter_client_name()
                show_appointments_by_name(appt_list, client_name)
            case '3':
                print (f'\n** {OPTIONS_BANNER["3"]} **')
                print('** Print calendar for a specific day **')
                day = input('Enter day of week: ').capitalize()
                show_appointments_by_day(appt_list,day)
            case '4':
                print (f'\n** {OPTIONS_BANNER["4"]} **')
                day = input('What day: ').capitalize()
                time = int(input('Enter start hour (24 hour clock) : '))
                if validate_day_and_time(day, time):                 
                    current_appt = find_appointment_by_time(appt_list, day, time)
                    if not current_appt:
                        print('That time slot isn\'t booked and doesn\'t need to be cancelled')
                    else:
                        current_appt.cancel()
                        print(f'Appointment: {day} {current_appt.get_start_time_hour():02d}:00 - {current_appt.get_end_time_hour()}:00 for {current_appt.get_client_name()} has been cancelled!')

        menuOption = print_menu()

    print ('\n**Exit the system**')
    save_to_file = input('Would you like to save all scheduled appointments to a file (Y/N)? ').upper().strip()
    while save_to_file not in BINARY_CHOICE:
            save_to_file = input('Invalid selection. Save all scheduled appointments to a file (Y/N)? ').upper().strip()
    if save_to_file == 'Y':
        file_name = input('Enter appointment filename: ')
        savedAppts = save_scheduled_appointments(appt_list, file_name)
        print (f'{savedAppts} scheduled appointments have been successfully saved')
    print('Good Bye!\n')

# Call main function
if __name__ == "__main__":
    main()
