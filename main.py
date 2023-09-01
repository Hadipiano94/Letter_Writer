PLACE_HOLDER = "[name]"

with open("Starting_Letter/letter.txt") as letter:
    sample_letter = letter.read()

with open("Names_Folder/names.txt") as names:
    names_list = names.readlines()
    for i in names_list:
        i = i.strip()

for raw_name in names_list:
    name = raw_name.strip()
    new_letter = sample_letter.replace(PLACE_HOLDER, name)
    with open(f"Ready_to_send/{name}'s_letter.txt", mode="w") as individual_letter:
        individual_letter.write(new_letter)
