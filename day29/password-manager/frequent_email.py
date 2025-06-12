def get_mostfrequent_email():
    emails = []

    with open("passwords.txt") as password_file:
        entries = password_file.readlines()
        for entry in entries:
            email_start = entry.index("|") + 1
            email_end = entry.index("|",email_start)
            emails.append(entry[email_start:email_end].strip())

    frequent_emails = {}
    most_frequent_email = ""
    most_frequent_email_count = 0

    for email in emails:
        if email in frequent_emails.keys():
            frequent_emails[email] += 1
        else:
            frequent_emails[email] = 1

    for (key,value) in frequent_emails.items():
        if value > most_frequent_email_count:
            most_frequent_email_count = value
            most_frequent_email = key

    return most_frequent_email