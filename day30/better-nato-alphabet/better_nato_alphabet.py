import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {phonetic["letter"]:phonetic["code"] for (index,phonetic) in nato_alphabet.iterrows()}

while True:
    try:
        user_string = input("Enter your string:").upper()
        string_to_nato = [nato_alphabet_dict[character] for character in user_string]
    except KeyError:
        print("Only letters in the alphabet please")
    else:
        print(string_to_nato)
        break