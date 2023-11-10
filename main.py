from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,new_value):
        self._value=new_value

    def __str__(self):
        return str(self._value)


class Name(Field):

    def __init__(self, name):
        super().__init__(name)

    @property
    def value(self):
        return self._name

    @value.setter
    def value(self,new_value):
        self._name=new_value



class Phone(Field):


    def __init__(self, number):
        self.find_phone(number)
        super().__init__(number)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.find_phone(new_value)

    def find_phone(self, phone):
        if len(phone) == 10 and phone.isdigit():
            self._value = phone
        else:
            raise ValueError("Invalid phone number format")


class Birthday:
    def __init__(self,year,month,day):
        self._value=self.valid_birthday(year, month, day)
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,new_value):
        year,month,day=map(int,new_value.split('-'))
        self.value=self.valid_birthday(year,month,day)

    def valid_birthday(self,year,month,day):
        try:
            return datetime(year,month,day)
        except ValueError:
            raise ValueError('Enter valid date')

    @property
    def year(self):
        return self._value.year

    @property
    def month(self):
        return self._value.month

    @property
    def day(self):
        return self._value.day




class Record(Field):

    def __init__(self, name,birthday=None):
        self.name = name
        self.phone = []
        self.birthday=birthday
        super().__init__(name)

    def add_phone(self,number):
        if number:
            num=Phone(number)
            self.phone.append(num)


    def remove_phone(self, phone):
        if phone in self.phone:
            self.phone.remove(phone)

    def edit_phone(self, phone_old, phone_new):
        for phone_obj in self.phone:
            if phone_obj.value == phone_old:
                phone_obj.find_phone(phone_new)
                break


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
        phones_str = ', '.join(str(phone) for phone in self.phone)
        return f"Contact name: {self.name}, phones: {phones_str}"

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


