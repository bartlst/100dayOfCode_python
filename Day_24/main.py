#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

letter_content = ""

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

with open("./Input/Names/invited_names.txt") as file:
    name_list = file.readlines()


for name in name_list:
    name = name.replace("\n", "")
    new_letter = letter_content.replace("[name]", name)
    file_name = name + ".txt"
    file_path = "./Output/ReadyToSend/" + file_name
    with open(file_path, mode="w") as ready_letter:
        ready_letter.write(new_letter)

