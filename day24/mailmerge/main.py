with open("Input/Letters/starting_letter.txt") as docs:
    starting_letter = docs.read()

print(starting_letter)

with open("Input/Names/invited_names.txt") as namesdocs:
    namecontent = namesdocs.readlines()

namelist = []

for name in namecontent:
    namelist.append(name[:-1])

for name in namelist:
    newletter = starting_letter.replace("[name]",name,-1)
    with open(f"Output/ReadyToSend/{name}'s letter.txt","w") as letter:
        letter.write(newletter)