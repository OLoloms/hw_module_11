from collections import UserDict
from datetime import datetime, timedelta

class AdressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record

    def iterator(self, n):
        keys = list(self.data.keys())
        total_records = len(keys)
        current_index = 0

        while current_index < total_records:
            batch_keys = keys[current_index:current_index + n]
            batch_records = [str(self.data[key]) for key in batch_keys]
            current_index += n
            yield batch_records
            

class Record:
    def __init__(self, name, *field, birthday=None) -> None:
        self.name = name
        self.field = list(field) or []
        self.birthday = birthday.value

    def days_to_birthday(self):
        if self.birthday:
            birthday = datetime.strptime(self.birthday, '%d %B %Y')

            current_day = datetime.now().date()

            if current_day - datetime(year=datetime.now().year, month=birthday.month, day=birthday.day).date() < timedelta(days=0):
                diff = datetime(year=datetime.now().year, month=birthday.month, day=birthday.day).date() - current_day
            elif current_day - datetime(year=datetime.now().year, month=birthday.month, day=birthday.day).date() == timedelta(days=0):
                return 'Todays is your birthday'
            else:
                diff = datetime(year=datetime.now().year+1, month=birthday.month, day=birthday.day).date() - current_day
            return diff.days
        else:
            return "Birthday isn't set"
        
    def __str__(self):
        phones_list = [phone.value for phone in self.field]
        return f'Name: {self.name.name}, Phone: {phones_list}, Birthday: {self.birthday}'


class Field:
    pass

class Name:
    def __init__(self, name) -> None:
        self.name = name

class Phone:
    def __init__(self) -> None:
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if len(new_value) == 13:
            self.__value = new_value
            print('Phone number has saved')
        else:
            print('Incorrect format number')

class Birtday:
    def __init__(self) -> None:
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        data_list = new_value.split(' ')
        if 0 < int(data_list[0]) < 32 and data_list[1] in months and len(data_list[2]) == 4:
            self.__value = new_value
            print('Birthday has saved')
        else:
            print('Incorrect formar record')

name_1 = Name('Sergij')
phone_1 = Phone()
phone_1.value = '+380988623491'
birthday_1 = Birtday()
birthday_1.value = '10 January 2021'
rec_1= Record(name_1, phone_1, birthday=birthday_1)
name_2 = Name('Alina')
phone_2 = Phone()
phone_2.value = '+380988623493'
birthday_2 = Birtday()
birthday_2.value = '10 May 2021'
rec_2 = Record(name_2, phone_2, birthday=birthday_2)
name_3 = Name('Anton')
phone_3 = Phone()
phone_3.value = '+380988623411'
birthday_3 = Birtday()
birthday_3.value = '12 May 2021'
rec_3 = Record(name_3, phone_3, birthday=birthday_3)
name_4 = Name('Andrij')
phone_4 = Phone()
phone_4.value = '+380988623410'
birthday_4 = Birtday()
birthday_4.value = '18 May 2021'
rec_4 = Record(name_4, phone_4, birthday=birthday_4)
ab = AdressBook()
ab.add_record(rec_1)
ab.add_record(rec_2)
ab.add_record(rec_3)
ab.add_record(rec_4)
gen_obj = ab.iterator(3)
print(next(gen_obj))
print(next(gen_obj))





