import appointment as ap
import os.path

TABLE_HEADER = f'{"Client Name":20s}{"Phone":15s}{"Day":10s}{"Start":10s}{"End":10s}{"Type":20s}\n{"-"*80}'
BINARY_CHOICE = ['Y','N']
MENS_CUT_PRICE =  50
LADIES_CUT_PRICE = 80
MENS_COLOR_PRICE = 50
LADIES_COLOR_PRICE = 120
OPTIONS_BANNER = {'1':'Schedule an appointment', '2': 'Find appointment by name',
                     '3':'Print calendar for a specific day',
                     '4': 'Cancel an appointment', '9':'Exit the system'}
OPERATING_HOURS = range (9,17)
OPERATING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
ERROR_PROMPT = 'Sorry that time slot is not in the weekly calendar!'

def save_scheduled_appointments():
    pass

def show_appointments_by_day():
    pass 

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

def main():
    appt_list = []
    create_weekly_calendar (appt_list)
    print('\nStarting the Appointment Manager System\nWeekly calendar created\n')
    load_file = input('Would you like to load previously scheduled appointments from a file (Y/N)? ').upper().strip()
    while load_file not in BINARY_CHOICE:
            load_file = input('Invalid selection. Load previously scheduled appointments from a file (Y/N)? ').upper().strip()
    
    if load_file == 'Y':
        file_name = input('Enter appointment filename: ').strip()

        while not os.path.isfile(file_name):
            file_name = input('File not found. Re-enter appointment filename: ').strip()

        print (f'{load_scheduled_appointments (appt_list,file_name)} previously scheduled appointments have been loaded')

    menuOption = print_menu()

    while menuOption != '9':
        match menuOption:         
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
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