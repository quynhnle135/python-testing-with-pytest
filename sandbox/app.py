class User:
    def __init__(self, first_name=None, last_name=None, id=0, dob=None):
        self.first_name = first_name
        self.last_name = last_name
        self.__id = id
        self.dob = dob

    def get_user_id(self):
        return self.__id

    def __str__(self):
        return f"User's full name: {self.first_name} {self.last_name}"

    def able_to_enroll_health_insurance(self, age):
        if age < 0:
            raise Exception("Age cannot be negative")

        if age < 60:
            return False
        else:
            return True


