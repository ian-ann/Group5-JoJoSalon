def save_scheduled_appoints():
    pass

def show_appointments_by_day():
    pass 

def show_appointments_by_name():
    pass

def final_appointment_by_time():
    pass

def print_menu():
    pass

def load_schedule_apportments():
    pass

def create_weekly_calendar (appointment_list):
    dayOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for day in dayOfTheWeek:
        for time in range (9,17):
            appointment_list.append(ap.Appointment(day, time))

def main():
    pass

# Call main function
if __name__ == "__main__":
    main()