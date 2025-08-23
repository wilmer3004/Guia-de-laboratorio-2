class Student:
    # Create the constructor method
    def __init__(self, cod_student, name, last_name, email, code_type, blood_type, phone_number, address, city, country):
        self.cod_student = cod_student
        self.name = name
        self.last_name = last_name
        self.email = email
        self.code_type = code_type
        self, phone_number = phone_number
        self.blood_type = blood_type
        self.address = address
        self.city = city
        self.country = country

    # Getters
    def get_cod_student(self):
        return self.cod_student

    def get_name(self):
        return self.name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_code_type(self):
        return self.code_type
    
    def get_blood_type(self):
        return self.blood_type    
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_address(self):
        return self.address
    
    def get_city(self):
        return self.city
    
    def get_country(self):
        return self.country
    
    # Setters
    def set_cod_student(self, cod_student):
        self.cod_student = cod_student

    def set_name(self, name):
        self.name = name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email
    
    def set_code_type(self, code_type):
        self.code_type = code_type
    
    def set_blood_type(self, blood_type):
        self.blood_type = blood_type
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city
    
    def set_country(self, country):
        self.country = country
    