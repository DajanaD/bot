import re

def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please or missing space'
        except IndexError:
            return 'Enter user name'
    return inner

USERS = {}


def hello():
    return "How can I help you?" 


def exit_handler():
    return "Good bye!"


@error_handler
def add(*args, **kwargs):
    
    name, phone = args
    USERS[name] = phone
    return "Add"

@error_handler
def change(*args, **kwargs):
    name, phone = args
    USERS[name] = phone
    return "Change"


def phone(*args, **kwargs):
    name = args
    USERS[name]



def show_all():
    for key, value in  USERS.items:
        f'{key} - {value}'


def main():
    while True:
        s = input("...")
        s = s.lower()       
        if s == "hello":
            print(hello())
        elif re.search(r'add', s):
            new_text = s.replace("add ", "").split(" ")
            print (add(new_text))
        elif re.search(r'change', s):
            new_text = s.replace("change ", "").split(" ")
            print(change(new_text))
        elif re.search(r'phone', s):
            new_text = s.replace("phone ", "").split(" ")
            print(phone(new_text[1]))
        elif re.search(r'show all ', s):  
            print(show_all())
        elif s == "good bye" or "close" or "exit":
            exit_handler()
            break
        elif s:
            print('No command...')
        
if __name__ == "__main__":

    main()
