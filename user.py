class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_f_name(self):
        print(self.first_name)

    def get_l_name(self):
        print(self.last_name)

    def get_full_name(self):
        print(f"Имя: {self.first_name}, Фамилия: {self.last_name}")
