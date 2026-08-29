from Hospital_Magement_System.person import Person


class Patient(Person):
    """
    Class for hospital patients, inheriting from Person.

    Attributes:
        name (str): The name of the patient.
        age (int): The age of the patient.
        medical_record (str): The medical record of the patient.
    """

    def __init__(self, name, age, medical_record):
        """
        Initializes the Patient object.

        Args:
            name (str): The name of the patient.
            age (int): The age of the patient.
            medical_record (str): The medical record of the patient.
        """
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        """
        Returns the patient's medical record.

        Returns:
            str: The patient's medical record.
        """
        return f"Patient Record: {self.medical_record}"