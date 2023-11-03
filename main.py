from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    def __init__(self, name):
        self.name = name
        super().__init__(self.name)


class Phone(Field):

    def __init__(self, number):
        if not Phone.find_phone(number):
            raise ValueError("Invalid phone number format")
        super().__init__(number)

    def find_phone(self):
        return len(self) == 10 and self.isdigit()


class Record(Field):

    def __init__(self, name):
        self.name = name
        self.phone = []
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


    def __str__(self):
        return f"Contact name: {self.name}, phones: {''.join(p for p in self.phone)}"

class AddressBook(UserDict):

    def add_record(self,name, phone):
        self.data.setdefault(name,phone)


    def find(self,name):
        if name in self.data.keys():
            return self.data[name]
        return None

    def delete(self,name):
        if name in self.data.keys():
            del self.data[name]
