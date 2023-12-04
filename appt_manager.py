import appointment as ap
import os

# Declare variables and constants
DAY_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
OPEN_TIME = range(9,17)

def save_scheduled_appointments(appt_list, day, time, appt_type = 0, client_name = "", client_phone = "", output = True):
    print(type(appt_list))
    current_appt = find_appointment_by_time(appt_list, day, time)

    if len(current_appt) > 0:
        # book it 
        current_appt.set_client_name(client_name)
        current_appt.set_client_phone(client_phone)
        current_appt.set_appt_type(appt_type) 
        
    if output:
        print(f'OK, {client_name}\'s appointment is scheduled!')

def show_appointments_by_day(appt_list,day):
    ''' This function will print the appointment based on the input value of day'''
    divider = "-" * 90
    print(f'Appointments for {day}')
    print("")
    print(f'{"Client Name":<20s}{"Phone":<15s}{"Day":<10s}{"Start":<5s}   {"End":<10s}{"Type":<20s}')
    print(f'{divider}')
    
    # check if appointment is already booked
    for appt in appt_list:
        if appt.get_day_of_week() == day:
            print(appt) 

def show_appointments_by_name(appt_list):
    pass

def find_appointment_by_time(appt_list, day, hour):

    return appt_list # test only

def print_menu():
    optionsBanner = {'1':'Schedule an appointment', '2': 'Find appointment by name',
                     '3':'Print calendar for specific day',
                     '4': 'Cancel an appointment', '9':'Exit the system'}
    dash = "=" * 45

    print (f'\nJojo\'s Hair Salon Appointment Manager')
    print (f'{dash}')
    for menuNumbers, description in optionsBanner.items():
        print (f'{menuNumbers}) {description}')

    menuChoice = input ('Enter your selection: ').strip()
    while menuChoice not in optionsBanner:
        menuChoice = input ('Sorry that is not a valid selection').strip()
    
    print("")
    return (menuChoice)

def check_file_exists(file_name):
    found = False

    if os.path.isfile(file_name):
        found = True

    return found
   
def load_schedule_appointments(appt_list, file_name):      
        appt_file = open(file_name, 'r')
        records_cnt = 0

        # loop through appointment file and save to list
        for appt_record in appt_file:
            appt_row = appt_record.split(",")
            client_name = appt_row[0]
            client_phone = appt_row[1]
            appt_type = int(appt_row[2])
            day = appt_row[3]
            time = int(appt_row[4].strip('\n'))
            save_scheduled_appointments(appt_list,day, time, appt_type, client_name, client_phone,False)
            
            records_cnt += 1

        print (f'{records_cnt} previously scheduled appointments have been loaded\n')

def create_weekly_calendar (appointment_list):
    for day in DAY_OF_WEEK:
        for time in OPEN_TIME:
            appointment_list.append(ap.Appointment(day, time))
    
    print('Weekly calendar created')

def enter_client_name():
    name = input('Client Name: ').capitalize()

    return name

def check_previous_appointments():
    appointment_exists = False

    return appointment_exists

def exit_management_system(appt_list):
    print ('\n** Exit the system **\n')
    records_cnt = 0
    save_to_file = input('Would you like to save all scheduled appointments to a file (Y/N)? ').upper()
    if save_to_file == 'Y':
        file_name = input('Enter appointment filename: ')
        if check_file_exists(file_name):
            overwrite_file = input('File already exists. Do you want to overwrite it (Y/N)?: ').upper()
            if overwrite_file == 'N':
                file_name = input('Enter appointment filename: ')

        appointment_file = open(file_name,"w")
        for appt in appt_list:
            if appt.get_appt_type() != 0:
                appt_row = appt.format_record()
                appointment_file.write(appt_row)
        appointment_file.close()

        # check how many records in the file
        appointment_file = open(file_name,"r")
        records_cnt = 0
        for files in appointment_file:
            records_cnt += 1

        print (f'{records_cnt} scheduled appointments have been successfull saved\n')
    
    print('Good Bye!')

def main():    
    # Declare Variables
    appt_list = []
    appt_type_price = {1:"$50",2:"$80",3:"$50",4:"$120"}
    menu_desc = {0:"Available", 1:"Mens Cut", 2:"Ladies Cut", 3:"Mens Colouring",
                   4:"Ladies Colouring"}
    NOT_IN_CALENDAR = 'Sorry that time slot is not in the weekly calendar!\n'
    
    print('Starting the Appointment Manager System')

    # Create weekly calendar
    create_weekly_calendar(appt_list)

    # Call Loadd Scheduale Appointments
    load_file = input('Would you like to load previously scheduled appointments from a file (Y/N)? ').upper()

    if load_file == 'Y':
        file_name = input('Enter appointment filename: ')    

        while check_file_exists(file_name) == False:
            file_name = input('File not found. Re-enter appointment filename: ')

        # Load schedule to appoint list from file name
        load_schedule_appointments(appt_list, file_name)

    # Call Print Menu
    menuOption = print_menu()

    while menuOption != '9':
        if menuOption == '1' or menuOption == '4':
            valid = True

            day = input('What day: ').capitalize()
            time = int(input('Enter start hour (24 hour clock) : '))

            if (day not in DAY_OF_WEEK or time not in OPEN_TIME):
                print(NOT_IN_CALENDAR)
                valid = False
            else:
                available, _ = find_appointment_by_time(appt_list, day, time)

        match menuOption:         
            case '1':
                if not available:
                    print("Sorry that time slot is booked already")
                else:
                    client_name = enter_client_name()
                    client_phone = input('Client Phone: ')
                    index = 0
                    for type in appt_type_price:
                        for appt_type in menu_desc:
                            if type == appt_type:
                                print(f'{type}: {menu_desc[appt_type]} {appt_type_price[type]}',end='')
                        if index != len(appt_type_price) - 1:
                            print(', ', end='')
                        index += 1

                    print('')
                    appt_type = int(input('Type of Appointment: '))
                    if appt_type not in appt_type_price:
                        print('Sorry that is not a valid appointment type!')
                    else:
                        save_scheduled_appointments(appt_list, day, time, appt_type, client_name, client_phone)
            case '2':
                show_appointments_by_name()
            case '3':
                print('** Print calendar for a specific day **')
                day = input('Enter day of week: ').capitalize()
                show_appointments_by_day(appt_list,day)
            case '4':
                current_appt = find_appointment_by_time(appt_list, day, time)
                if len(current_appt) > 0:
                    current_appt.cancel()
                else:
                    print(NOT_IN_CALENDAR)

        menuOption = print_menu()
    
    exit_management_system()

# Call main function
if __name__ == "__main__":
    main()