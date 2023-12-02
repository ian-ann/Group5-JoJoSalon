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
import time
class Appointment :
    def __init__(self,day_of_week, start_time_hour,appt_type = 0, client_name = "", client_phone="") :
        self.__appt_day = day_of_week
        self.__start_time_hour = start_time_hour
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type

    def get_client_name(self):
        return self.__client_name
     
    def get_client_phone(self):
        return self.__client_phone
    
    def get_appt_type(self):
        return self.__appt_type
    
    def get_day_of_week(self):
        return self.__appt_day
    
    def get_start_time_hour(self):
        return self.__start_time_hour
    
    def get_app_type_desc(self):
        appt_type = self.__appt_type
        appt_desc_dictionary = {0:'Available',
                                1:'Mens Cut', 
                                2:'Ladies Cut',
                                3:'Mens Colouring', 
                                4:'Ladies Colouring'}
        
        for type in appt_desc_dictionary:
            if appt_type == type:
                desc = appt_desc_dictionary[appt_type]
        
        return desc

    def get_end_time_hour(self):
        start_time = self.__start_time_hour
        end_time_hr = start_time + 1

        return end_time_hr

    def set_client_name(self, client_name):
        self.__client_name = client_name
        
    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        Appointment.set_client_name(self, client_name)
        Appointment.set_client_phone(self, client_phone)
        Appointment.set_appt_type(self, appt_type)

    def cancel(self):
        Appointment.set_client_name(self,"")
        Appointment.set_client_phone(self,"")
        Appointment.set_appt_type(self,0)

    def format_record(self):
       record = f'{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__appt_day},{self.__start_time_hour}'       
       return record

    def format_time(time):
        if time < 10: 
            time =  '0' + str(time) + ':00'
        else:
            time =  str(time) + ':00'

        return time

    def __str__(self):
        end_time_hr = Appointment.get_end_time_hour(self)
        end_time_hr = Appointment.format_time(end_time_hr)
        start_time_hr = Appointment.format_time(self.__start_time_hour)
        appt_desc = Appointment.get_app_type_desc(self)
        record = f'{self.__client_name:<20}{self.__client_phone:<15}{self.__appt_day:<10}{start_time_hr:>10} - {end_time_hr:<5}{appt_desc:>20}'
        return record