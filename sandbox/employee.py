class Employee:
    def __init__(self, name=None, department=None):
        self.name = name
        self.department = department

    def get_promotion(self, manager):
        return manager.decide()

