class Procedure:

    def __init__(self, procedure_name, date, practitioner, charge, patient_id):
        self.__procedure_name = procedure_name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge
        self.__patient_id = patient_id

    def get_procedure_name(self):
        return self.__procedure_name

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charge(self):
        return self.__charge

    def get_patient_id(self):
        return self.__patient_id

    