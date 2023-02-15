class Salon:
    def __init__(self, salon_name, country):
        self.salon_name = salon_name
        self.country = country

    def introduce(self):
        print(f"{self.salon_name} is in {self.country}")

    def which_salon(self):
        print(f"There is a company named {self.salon_name}")

    def location(self):
        print(f"Salon placed in {self.country}")


class Car(Salon):
    def __init__(self, salon_name, country, name, model):
        super().__init__(salon_name, country)
        self.name = name
        self.model = model

    def introduce(self):
        print(
            f"This car name is {self.name}, {self.model}. Located in {self.salon_name} in {self.country}"
        )

    def which_name(self):
        print(f"There is a car {self.name}")

    def what_model_again(self):
        print(f"The model of the {self.name} is {self.model}")


class Self(Car):
    def __init__(self, salon_name, country, name, model, ID, age):
        super().__init__(salon_name, country, name, model)
        self.ID = ID
        self.age = age

    def introduce(self):
        print(
            f"This is  {self.name} - {self.model}. This car located in {self.salon_name} and year of release {self.age}"
        )

    def __show_id(self):
        print(f"{self.name} ID is {self.ID}")

    def which_age(self):
        print(f"{self.name} released in {self.age}")


a = Salon("Avtoroom", "Moscow")
b = Car("GerAvto", "Germany", "BMW", "M5")
c = Self("ItalAvto", "Italia", "Ferrari", "812 Superfast", 7, 2019)
a.which_salon()
a.location()

b.which_name()
b.what_model_again()

c.which_age()

a.introduce()
b.introduce()
c.introduce()
