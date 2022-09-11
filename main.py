with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as name_files:
    names = name_files.readlines()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/Letter To {stripped_name}", mode="w") as Completed_letter:
            final_letter = Completed_letter.write(new_letter)
