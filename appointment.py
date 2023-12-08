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

    #Desciption of each appointment type and their numeric identifier
    menu_desc = {0:"Available", 1:"Mens Cut", 2:"Ladies Cut", 3:"Mens Colouring",
                   4:"Ladies Colouring"}
    
    def __init__(self, day, time, name = "", phone = "", appt_type = 0):
        self.__client_name = name
        self.__client_phone = phone
        self.__appt_type = appt_type
        self.__day_of_week = day
        self.__start_time_hour = time

    def get_client_name (self):
        '''Returns the name of the client from the Appointment object'''
        return self.__client_name
    
    def get_client_phone (self):
        '''Returns the phone number of the client from the Appointment object'''
        return self.__client_phone
    
    def get_appt_type (self):
        '''Returns the appointment type of the client from the Appointment object, as a numeric value'''
        return self.__appt_type
    
    def get_day_of_week(self):
        '''Returns the day of the appointment from the Appointment object'''
        return self.__day_of_week
    
    def get_start_time_hour (self):
        '''Returns the starting hour of the appointment from the Appointment object'''
        return self.__start_time_hour
    
    def get_appt_type_desc (self):
        '''Returns the appointment type of the client from the Appointment object, as a description'''
        return Appointment.menu_desc [self.__appt_type]
    
    def get_end_time_hour (self):
        '''Returns the hour that the appointment ends, from the Appointment object'''
        return self.__start_time_hour + 1
    
    def set_client_name (self, name):
        self.__client_name = name
    
    def set_client_phone (self, phone):
        self.__client_phone = phone

    def set_appt_type (self, appt_type):
        self.__appt_type = appt_type
    
    def schedule(self, client_name, client_phone, appt_type):
        ''' Will call the setter methods and schedule the client visit on to the Appointment object'''
        self.set_client_name (client_name)
        self.set_client_phone (client_phone)
        self.set_appt_type (appt_type)

    def cancel (self): 
        ''' Will call the setter methods and cancel the client appointment by resetting the name, phone number,
        and appointment type to their default values'''
        self.set_client_name ("")
        self.set_client_phone ("")
        self.set_appt_type (0)

    def format_record (self):
        ''' Returns a string containing the client's name, phone number, appointment type (as a number), day of the appointment,
        and the starting hour of the appointment, all of which are separated by commas'''
        record = f'{self.__client_name},{self.__client_phone},{str(self.__appt_type)},{self.__day_of_week},{self.__start_time_hour:02d}'
        return record

    def __str__(self):
        '''Returns the string representation of the Appointment object'''
        schedule = f'{self.__client_name:<20s}{self.__client_phone:<15s}{self.__day_of_week:<10s}{self.__start_time_hour:>02d}{":00  -  "}{self.get_end_time_hour():<02d}{":00":<8}{self.get_appt_type_desc()}'
        return schedule
