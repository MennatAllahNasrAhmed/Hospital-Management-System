class Department:
    """
    Class representing a department in the hospital.

    Attributes:
        name (str): The name of the department.
        patients (list): List of patients in the department.
        staff (list): List of staff members in the department.
    """

    def __init__(self, name):
        """
        Initializes the Department object.

        Args:
            name (str): The name of the department.
        """
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient):
        """
        Adds a patient to the department.

        Args:
            patient (Patient): The patient to be added.
        """
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member):
        """
        Adds a staff member to the department.

        Args:
            staff_member (Staff): The staff member to be added.
        """
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")

    def view_patients(self):
        """
        Returns information about all patients in the department.

        Returns:
            list: List of patient information.
        """
        return [patient.view_info() for patient in self.patients]

    def view_staff(self):
        """
        Returns information about all staff members in the department.

        Returns:
            list: List of staff information.
        """
        return [staff_member.view_info() for staff_member in self.staff]