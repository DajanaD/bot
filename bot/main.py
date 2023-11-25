from collections import UserDict
import datetime


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value
 
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass

class Birthday(Field):
    @Field.value.setter
    def value(self, value: str):
        self.__value = datetime.strptime(value, '%Y.%m.%D').date()

class Phone(Field):
   def __init__(self, value):
        super().__init__(value)
        @Field.value.setter
        def value(self, value: str):
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

    def days_to_birthday(self, birthday):
        if birthday:
            now = datetime.datetime.now()
            then = datetime.datetime.strptime(birthday, '%Y.%m.%D')
            delta1 = datetime.datetime(now.year, then.month, then.day)
            delta2 = datetime.datetime(now.year+1, then.month, then.day)

            result = ((delta1 if delta1 > now else delta2) - now).days
            print(f'{result} days left until birthday')

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

    def iterator(self, item_number):
        counter = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {record}'
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = '' 
