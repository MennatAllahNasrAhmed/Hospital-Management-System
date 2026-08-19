from person import Person

class Staff(Person):
    """Class for hospital staff, inheriting from Person."""
    def init(self, name, age, position):
        super().init(name, age)
        self.position = position
    def view_info(self):
        """View staff information."""
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"