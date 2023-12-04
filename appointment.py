class Appointment:
    __menu_desc = {0:"Available", 1:"Mens Cut", 2:"Ladies Cut", 3:"Mens Colouring",
                   4:"Ladies Colouring"}
    
    def __init__(self, day, time, name = "", phone = "", appt_type = 0):
        self.__client_name = name
        self.__client_phone = phone
        self.__appt_type = appt_type
        self.__day_of_week = day
        self.__start_time_hour = time

    def get_client_name (self):
        return self.__client_name
    
    def get_client_phone (self):
        return self.__client_phone
    
    def get_appt_type (self):
        return self.__appt_type
    
    def get_day_of_week (self):
        return self.__day_of_week
    
    def get_start_time_hour (self):
        return self.__start_time_hour
    
    def get_appt_type_desc (self):
        return Appointment.__menu_desc [self.__appt_type]
    
    def get_end_time_hour (self):
        return self.__start_time_hour + 1
    
    def set_client_name (self, name):
        self.__client_name = name
    
    def set_client_phone (self, phone):
        self.__client_phone = phone

    def set_appt_type (self, appt_type):
        self.__appt_type = appt_type
    
    def schedule (self, name, phone, appt_type):
        self.set_client_name (name)
        self.set_client_phone (phone)
        self.set_appt_type (appt_type)

    def cancel (self): 
        self.set_client_name ("")
        self.set_client_phone ("")
        self.set_appt_type (0)

    def format_record (self):
        record = f'{self.__client_name},{self.__client_phone},{str(self.__appt_type)},{self.__day_of_week},{self.__start_time_hour:02d}'
        return record

    def __str__(self):
        schedule = f'{self.__client_name:<20s}{self.__client_phone:<15s}{self.__day_of_week:<10s}{self.__start_time_hour:>02d}{":00  -  "}{self.get_end_time_hour():<02d}{":00":<8}{self.get_appt_type_desc()}\n'
        return schedule
