import appointment as ap
import os

# Declare variables and constants
BINARY_CHOICE = ['Y','N']
OPERATING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
OPERATING_HOURS = range(9,17)
TABLE_HEADER = f'{"Client Name":20s}{"Phone":15s}{"Day":10s}{"Start":10s}{"End":10s}{"Type":20s}\n{"-"*80}'
ERROR_PROMPT = 'Sorry that time slot is not in the weekly calendar!\n'
APPT_TYPE_PRICE = {1:"$50",2:"$80",3:"$50",4:"$120"}
ERROR_PROMPT = 'Sorry that time slot is not in the weekly calendar!'
OPTIONS_BANNER = {'1':'Schedule an appointment', '2': 'Find appointment by name',
                     '3':'Print calendar for a specific day',
                     '4': 'Cancel an appointment', '9':'Exit the system'}


def show_appointments_by_day(appt_list,day):
    ''' This function will print the appointment based on the input value of day'''
    divider = "-" * 90
    print(f'Appointments for {day}')
    print("")
    print(TABLE_HEADER)
    print(TABLE_HEADER)
    print(f'{divider}')
    
    # check if appointment is already booked
    for appt in appt_list:
        if appt.get_day_of_week() == day:
            print(appt) 

def save_scheduled_appointments(appt_list, file_name):
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

    # check how many records in the file
    appointment_file = open(file_name,"r")
    for files in appointment_file:
        records_cnt += 1

    print (f'{records_cnt} scheduled appointments have been successfull saved\n')

def show_appointments_by_name():
    pass

def find_appointment_by_time (appointment_list, day, hour):
    pass

def print_menu():
    print (f'\n\nJojo\'s Hair Salon Appointment Manager\n{"="*37}')
    for menuNumbers, description in OPTIONS_BANNER.items():
        print (f' {menuNumbers}) {description}')

    menuChoice = input ('Enter your selection: ').strip()
    while menuChoice not in OPTIONS_BANNER:
        menuChoice = input ('Invalid Input - Enter a selection from the menu: ').strip()
    return (menuChoice)

def load_scheduled_appointments (appointment_list, filename):
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
    for day in OPERATING_DAYS:
        for time in OPERATING_HOURS:
            appointment_list.append(ap.Appointment(day, time))

def check_file_exists(file_name):
    found = False

    if os.path.isfile(file_name):
        found = True

    return found
   
def enter_client_name():
    name = input('Client Name: ').capitalize()

    return name

def check_previous_appointments():
    appointment_exists = False

    return appointment_exists

def validate_day_and_time(day, time):
    if (day not in OPERATING_DAYS or time not in OPERATING_HOURS):
        print(ERROR_PROMPT)
        return False
    return True

def print_appointment_types():
    menu_desc = ap.Appointment.menu_desc

    index = 0
    for type in APPT_TYPE_PRICE:
        for appt_type in menu_desc:
            if type == appt_type:
                print(f'{type}: {menu_desc[appt_type]} {APPT_TYPE_PRICE[type]}',end='')
        if index != len(APPT_TYPE_PRICE) - 1:
            print(', ', end='')
        index += 1
    print('')

def save_schedule(appt_list, day, time, appt_type = 0, client_name = "", client_phone = "", output = True):
    current_appt = find_appointment_by_time(appt_list, day, time)

    if current_appt:
        # book it 
        current_appt.set_client_name(client_name)
        current_appt.set_client_phone(client_phone)
        current_appt.set_appt_type(appt_type) 
        
    if output:
        print(f'OK, {client_name}\'s appointment is scheduled!')

def main():    
    # Declare Variables
    appt_list = []
    
    print('Starting the Appointment Manager System')

    # Create weekly calendar
    create_weekly_calendar(appt_list)
    print('Weekly calendar created')

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
                day = input('What day: ').capitalize()
                time = int(input('Enter start hour (24 hour clock) : '))
                if validate_day_and_time(day, time):
                    current_appt = find_appointment_by_time(appt_list, day, time)
                      
                    if not current_appt:
                        print("Sorry that time slot is booked already")
                    else:
                        client_name = enter_client_name()
                        client_phone = input('Client Phone: ')
                        print_appointment_types()
                        print_appointment_types()
                        appt_type = int(input('Type of Appointment: '))
                        if appt_type not in APPT_TYPE_PRICE:
                            print('Sorry that is not a valid appointment type!')
                        if appt_type not in APPT_TYPE_PRICE:
                            print('Sorry that is not a valid appointment type!')
                        else:
                            save_schedule(appt_list, day, time, appt_type, client_name, client_phone)
            case '2':
                client_name = enter_client_name()
                show_appointments_by_name(appt_list, client_name)
                client_name = enter_client_name()
                show_appointments_by_name(appt_list, client_name)
            case '3':
                print('** Print calendar for a specific day **')
                day = input('Enter day of week: ').capitalize()
                show_appointments_by_day(appt_list,day)
            case '4':
                day = input('What day: ').capitalize()
                time = int(input('Enter start hour (24 hour clock) : '))
                if validate_day_and_time(day, time):                 
                    current_appt = find_appointment_by_time(appt_list, day, time)
                    if not current_appt:
                        print('That time slot isn\'t booked and doesn\'t need to be cancelled')
                    else:
                        current_appt.cancel()
                        print(f'Appointment: {day} {current_appt.get_start_time_hour} - {current_appt.get_end_time_hour} for {current_appt.get_client_name} has been cancelled!')

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