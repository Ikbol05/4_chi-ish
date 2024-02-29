
# 1 chi masalala

import string

class Full_name:
    def __init__(self):
        self.__full_name = ""

    def __get__(self, instance, owner):
        return self.__full_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Name str bo'lishi kerak")

        if not value.isalpha():
            raise ValueError("Name faqat harflardan iborat bo'lishi kerak")

        self.__full_name = value

    def __delete__(self, instance):
        del self.__full_name






class Person:
    full_name = Full_name()

    def __init__(self, full_name, email, phon_number, address):
        self.full_name = full_name
        self.email = email
        self.phone_number = phon_number
        self.address = address


user = Person("Ikbol", "muxtorovikboljon1@gmai.com", "+998333055323", "Fargona")
print(user.full_name)








































