


def get_data():
    with open('file.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    return data

def add_contact(contact):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        file.write('\n')

def find(contact):
    return