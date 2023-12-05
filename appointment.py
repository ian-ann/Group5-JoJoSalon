# ***************************************************************************************************************************
# This class will create an individual appointment for Jojo's Hair Salon clients. 
#
#  Input 
#     day_of_week
#     start_time_hour
#     appt_type
#     client_name
#     client_phone
#
#  Output:
#     Appointment Schedule
#     Appointment List
#     
# ***************************************************************************************************************************
class Appointment :
    menu_desc = {0:"Available", 1:"Mens Cut", 2:"Ladies Cut", 3:"Mens Colouring",
                   4:"Ladies Colouring"}

    def __init__(self, day_of_week, start_time_hour, appt_type = 0, client_name = "", client_phone = "") :
        ''' Initialize the Appointment class that requires the the properties day_of_week, start_time_hour, and optional properties of 
        appt_type, client_name and client_phone '''
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type

    def get_client_name(self):
        ''' Getter method for client name'''
        return self.__client_name
     
    def get_client_phone(self):
        ''' Getter method for client phone'''
        return self.__client_phone
    
    def get_appt_type(self):
        ''' Getter method for appoint type'''
        return self.__appt_type
    
    def get_day_of_week(self):
        ''' Getter method for day of week'''
        return self.__day_of_week
    
    def get_start_time_hour(self):
        ''' Getter method for start time in hours'''
        return self.__start_time_hour
    
    def get_appt_type_desc(self):
        ''' Getter method for the appointment description based on appointment type'''       
        return self.__menu_desc [self.__appt_type]

    def get_end_time_hour(self):
        ''' Getter method for end time based on start time hour'''
        start_time = self.__start_time_hour
        end_time_hr = start_time + 1

        return end_time_hr

    def set_client_name(self, client_name):
        ''' Setter method for client name'''
        self.__client_name = client_name
        
    def set_client_phone(self, client_phone):
        ''' Setter method for client phone'''
        self.__client_phone = client_phone
       
    def set_appt_type(self, appt_type):
        ''' Setter method for appointment type'''
        self.__appt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        ''' Will call the setter methods and schedule a client visit'''
        self.set_client_name (client_name)
        self.set_client_phone (client_phone)
        self.set_appt_type (appt_type)

    def cancel (self): 
        ''' Will call the setter methods and cancel a client visit'''
        self.set_client_name ("")
        self.set_client_phone ("")
        self.set_appt_type (0)

    def format_record (self):
        record = f'{self.__client_name},{self.__client_phone},{str(self.__appt_type)},{self.__day_of_week},{self.__start_time_hour:02d}'
        return record

    def __str__(self):
        schedule = f'{self.__client_name:<20s}{self.__client_phone:<15s}{self.__day_of_week:<10s}{self.__start_time_hour:>02d}{":00  -  "}{self.get_end_time_hour():<02d}{":00":<8}{self.get_appt_type_desc()}'
        return schedule
