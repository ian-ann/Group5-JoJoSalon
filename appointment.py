class Appointment:

    def __init__(self, day_of_week, start_time_hour):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour

    def get_client_name(self):
        return self.client_name
    
    def get_client_phone(self):
        return self.client_phone
    
    def get_appt_type(self):
        return self.appt_type
    
    def get_day_of_week(self):
        return self.day_of_week
    
    def get_start_time_hour(self):
        return self.start_time_hour
    
    def get_appt_type_desc(self):
        if self.appt_type == 0:
            return 'Available'
        elif self.appt_type == 1:
            return 'Mens Cut'
        elif self.appt_type == 2:
            return 'Ladies Cut'
        elif self.appt_type == 3:
            return 'Mens Colouring'
        elif self.appt_type == 4:
            return 'Ladies Colouring'
        else:
            return 'Unknown'
        
    #def get_appt_type_desc(self):
    #description = ['Available', 'Mens Cut', 'Ladies Cut', 'Mens Colouring', 'Ladies Colouring']
    #return descriptions[self.appt_type] 
    #if 0 <= self.appt_type < len(descriptions) else 'Unknown'

    def get_end_time_hour(self): 
        return self.start_time_hour + 1
    
    def set_client_name(self, client_name):
        self.client_name = client_name

    def set_client_phone(self, client_phone):
        self.client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.appt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)

    def cancel(self):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0

    def format_record(self):
        format_str = '{},{},{},{:02d}'.format(self.client_name, self.client_phone, self.day_of_week, self.start_time_hour)
        return format_str
    
    def __str__(self):
        format_str = f'{self.client_name}'
        format_str += f'{self.client_phone:>15s}'
        format_str += f'{self.day_of_week:10s}'
        format_str += f'{self.start_time_hour:02d}:00 - {self.get_end_time_hour():02d}:00\n'
        format_str += f'{self.get_appt_type_desc():>20s}'
        return format_str
        