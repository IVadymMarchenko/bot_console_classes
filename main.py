from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)


class Name(Field):

    def __init__(self, name):
        self.name = name
        super().__init__(self.value)

    @property
    def value(self):
        return self._name

    @value.setter
    def value(self,new_value):
        self._name=new_value



class Phone(Field):


    def __init__(self, number):
        if not Phone.find_phone(number):
            raise ValueError("Invalid phone number format")
        super().__init__(number)

    def find_phone(number):
        return len(number) == 10 and number.isdigit()


class Birthday:
    def __init__(self,year,manth,day):
        self.year=year
        self. month=manth
        self.day=day


class Record(Field):

    def __init__(self, name,birthday=None):
        self.name = name
        self.phone = []
        self.birthday=birthday
        super().__init__(name)

    def add_phone(self, number):
        if Phone.find_phone(number):
            self.phone.append(number)
        else:
            raise ValueError("Invalid phone number format")

    def remove_phone(self, phone):
        if phone in self.phone:
            self.phone.remove(phone)


    def edit_phone(self, phone_old, phone_new):
        if phone_old in self.phone and len(phone_new) == 10:
            index_phone = self.phone.index(phone_old)
            self.phone[index_phone] = phone_new
        else:
            raise ValueError


    def find_phone(self, number):
        if number in self.phone:
            return Phone(number)

    def days_to_birthday(self):
        if self.birthday:
            now_data = datetime.now()
            old_data = datetime(year=self.birthday.year, month=self.birthday.month, day=self.birthday.day)
            if now_data.month <= old_data.month:
                days_before_birthday = old_data.replace(year=now_data.year)
                result = days_before_birthday - now_data
            else:
                days_before_birthday = old_data.replace(year=now_data.year + 1)
                result = days_before_birthday - now_data

            return f'{result.days} days before birthday {self.name}'
        return f'birthday is unknown'

    def __str__(self):
        return f"Contact name: {self.name}, phones: {''.join(p for p in self.phone)}"

class AddressBook(UserDict):
    index_iterator=0

    def add_record(self, record):
        name = record._value
        self.data[name] = record


    def find(self,name):
        if name in self.data.keys():
            return self.data[name]
        else:
            return None


    def delete(self,name):
        if name in self.data.keys():
            del self.data[name]
        else:
            return None

    def iterator(self, note):
        if note > len(self.data):
            note = len(self.data)
        index_iteration = 0
        list_data = list(self.data.items())
        while index_iteration < len(list_data):
            contacts = [f'{record}' for name, record in list_data[index_iteration:index_iteration + note]]
            yield  '\n'.join(contacts)
            index_iteration += note



