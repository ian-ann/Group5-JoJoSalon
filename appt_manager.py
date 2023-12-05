import appointment as ap
import os

# Declare variables and constants
DAY_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
OPEN_TIME = range(9,17)
TABLE_HEADER = f'{"Client Name":<20s}{"Phone":<15s}{"Day":<10s}{"Start":<5s}   {"End":<10s}{"Type":<20s}'

def save_scheduled_appointments(appt_list, day, time, appt_type = 0, client_name = "", client_phone = "", output = True):
    current_appt = find_appointment_by_time(appt_list, day, time)

    if current_appt:
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
    print(TABLE_HEADER)
    print(f'{divider}')
    
    # check if appointment is already booked
    for appt in appt_list:
        if appt.get_day_of_week() == day:
            print(appt) 

def show_appointments_by_name(appt_list):
    pass

def find_appointment_by_time (appointment_list, day, hour):
    pass

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
        menuChoice = 'Sorry that is not a valid selection'

        print (f'\nJojo\'s Hair Salon Appointment Manager')
        print (f'{dash}')
        for menuNumbers, description in optionsBanner.items():
            print (f'{menuNumbers}) {description}')
    
    print("")
    return (menuChoice)

def check_file_exists(file_name):
    found = False

    if os.path.isfile(file_name):
        found = True

    return found
   
def load_scheduled_appointments (appointment_list, filename):
    pass

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
                appointment_file.write(appt_row + "\n")
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
    available = None
    appt_type_price = {1:"$50",2:"$80",3:"$50",4:"$120"}
    menu_desc = ap.Appointment.menu_desc
    NOT_IN_CALENDAR = 'Sorry that time slot is not in the weekly calendar!\n'
    
    print('Starting the Appointment Manager System')

    # Create weekly calendar
    create_weekly_calendar(appt_list)

    # Call Load Schedule Appointments if Yes to load
    load_file = input('Would you like to load previously scheduled appointments from a file (Y/N)? ').upper()

    if load_file == 'Y':
        file_name = input('Enter appointment filename: ')    

        while check_file_exists(file_name) == False:
            file_name = input('File not found. Re-enter appointment filename: ')

        # Get records count
        records_cnt = load_scheduled_appointments(appt_list, file_name)
        
        # Print records loaded
        print (f'{records_cnt} previously scheduled appointments have been loaded\n')

    # Call Print Menu
    menuOption = print_menu()

    while menuOption != '9':
        match menuOption:         
            case '1':
                day = input('What day: ').capitalize()
                time = int(input('Enter start hour (24 hour clock) : '))

                if (day not in DAY_OF_WEEK or time not in OPEN_TIME):
                    print(NOT_IN_CALENDAR)
                else:
                    current_appt = find_appointment_by_time(appt_list, day, time)
            
                    if not current_appt:
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
                    client_name = enter_client_name()
                    show_appointments_by_name(appt_list, client_name)
            case '3':
                print('** Print calendar for a specific day **')
                day = input('Enter day of week: ').capitalize()
                show_appointments_by_day(appt_list,day)
            case '4':
                day = input('What day: ').capitalize()
                time = int(input('Enter start hour (24 hour clock) : '))

                if (day not in DAY_OF_WEEK or time not in OPEN_TIME):
                    print(NOT_IN_CALENDAR)
                else:                 
                    current_appt = find_appointment_by_time(appt_list, day, time)
                    if not current_appt:
                        print(NOT_IN_CALENDAR)
                    else:
                        current_appt.cancel()

        menuOption = print_menu()
    
    exit_management_system(appt_list)

# Call main function
if __name__ == "__main__":
    main()