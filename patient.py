from person import Person

class Patient(Person):
    """Class for hospital patients, inheriting from Person."""

    def init(self, name, age, medical_record):
        super().init(name, age)
        self.medical_record = medical_record

    def view_record(self):
        """View patient record."""
        return f"Patient Record: {self.medical_record}"