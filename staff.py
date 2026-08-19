from person import Person


class Staff(Person):
    """
    Class for hospital staff, inheriting from Person.

    Attributes:
        name (str): The name of the staff member.
        age (int): The age of the staff member.
        position (str): The position of the staff member.
    """

    def __init__(self, name, age, position):
        """
        Initializes the Staff object.

        Args:
            name (str): The name of the staff member.
            age (int): The age of the staff member.
            position (str): The position of the staff member.
        """
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        """
        Returns staff information.

        Returns:
            str: The staff member's name, age, and position.
        """
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"