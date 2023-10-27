#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_format = letter_file.read()
    for name in name_list:
        new_name = name.strip()
        new_letter = letter_format.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}", mode='w') as completed_letter:
            completed_letter.write(new_letter)