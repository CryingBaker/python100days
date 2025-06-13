import json

class NotFoundError(Exception): ...

def get_mostfrequent_email():
    try:
        password_file = open("passwords.json")
        passwords = json.load(password_file)
    except FileNotFoundError:
        return ""
    else:
        most_frequent_mail = ""
        emails = {}
        most_frequent_mail_count = 0
        for (_,value) in passwords.items():
            try:
                emails[value["username"]] += 1
            except KeyError:
                emails[value["username"]] = 1
        for (key,value) in emails.items():
            if value > most_frequent_mail_count:
                most_frequent_mail_count = value
                most_frequent_mail = key
                return most_frequent_mail

def search(website):
    try:
        password_file = open("passwords.json")
        passwords = json.load(password_file)
    except FileNotFoundError:
        raise NotFoundError
    else:
        try:
            password = passwords[website]
        except KeyError:
            raise NotFoundError
    return password
    
            