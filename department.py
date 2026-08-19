class Department:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")

    def view_patients(self):
        return [patient.view_info() for patient in self.patients]

    def view_staff(self):
        return [staff_member.view_info() for staff_member in self.staff]