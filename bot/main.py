from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
   def __init__(self, value):
        super().__init__(value)
        if len(str(self.value)) == 10 and str(self.value).isdigit():
            self.value = value
        else:
            raise ValueError('Invalid phone number')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number: str):
        self.phones.append(Phone(phone_number))


    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone


    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError


    def remove_phone(self, phone_number):
        phone  = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        
        
    def find(self, name: Record):
        for names in self.data:
            if names == name:
                return self.data[name]
            
            
    def delete(self, name:Record):
        if self.data.get(name):
            del self.data[name]
