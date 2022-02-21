class Patient:
    
    def __init__(self, id, name, address, phone, vet_status):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__vet_status = vet_status

    def get_patient_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_veteran_status(self):
        return self.__vet_status

