
#Formatting name.

def format_name(f_name, l_name):

    if f_name == '' and l_name == '':
        return "Invalid inputs."
    full_name = (f_name +' '+ l_name).title()
    return f"Your full name is {full_name}."

print(format_name(input("Enter your first name: "), input("Enter your last name: ")))
