class Customer:
    def __init__(self, fName, lName, phone, email, vetDisabled):
        self.fName = fName
        self.lName = lName
        self.phone = phone
        self.email = email
        self.vetDisabled = vetDisabled
        
    def set_fName(self, fName):
        self.__fName = fName
    def get_fName(self):
        return self.__fName
    
    def set_lName(self, lName):
        self.__lName = lName
    def get_lName(self):
        return self.__lName
    
    def set_phone(self, phone):
        self.__phone = phone
    def get_phone(self):
        return self.__phone
    
    def set_email(self, email):
            self.__email = email
    def get_email(self):
        return self.__email
    
    def set_vetDisabled(self, vetDisabled):
            self.__vetDisabled = vetDisabled
    def get_vetDisabled(self):
        return self.__vetDisabled