import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {phonetic["letter"]:phonetic["code"] for (index,phonetic) in nato_alphabet.iterrows()}

user_string = input("Enter your string:").upper()

string_to_nato = [nato_alphabet_dict[character] for character in user_string if character in nato_alphabet_dict.keys()]

print(string_to_nato)