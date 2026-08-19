class Person:
    """
    Base class for all people in the hospital.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    """

    def __init__(self, name, age):
        """
        Initializes the Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def view_info(self):
        """
        Returns basic information about the person.

        Returns:
            str: The person's name and age.
        """
        return f"Name: {self.name}, Age: {self.age}" 
