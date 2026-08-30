from department import Department


class Hospital:
    """
    Class for managing hospital operations.

    Attributes:
        name (str): The name of the hospital.
        location (str): The location of the hospital.
        departments (list): List of departments in the hospital.
    """

    def __init__(self, name, location):
        """
        Initializes the Hospital object.

        Args:
            name (str): The name of the hospital.
            location (str): The location of the hospital.
        """
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        """
        Adds a department to the hospital.

        Args:
            department (Department): The department to be added.
        """
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")

    def find_department(self, name):
        """
        Finds a department by its name.

        Args:
            name (str): The name of the department.

        Returns:
            Department or None: The matching department if found,
            otherwise None.
        """
        for department in self.departments:
            if department.name.lower() == name.lower():
                return department
        return None

    def view_departments(self):
        """
        Returns the names of all departments in the hospital.

        Returns:
            list: List of department names.
        """
        return [department.name for department in self.departments]