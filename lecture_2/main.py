from functions import generate_profile, display_users_profile # import our function generate_profile and display_users_profile

user_name = input("Welcome! Please, enter your name: ") # asking user about his name, and storing it to user_name
birth_year_str = input("Please, enter your birth age: ") # asking user about his birth age, and storing it to birth_year_str

birth_year = int(birth_year_str) # converting birth_year_str to an integer birth_year

current_age = 2025 - birth_year # calculating the users current age, and storing it to current_age

hobbies = [] # create an empty list for users hobbies

while True: # creating loop that continue indefinitely
    user_answer = input("Please, enter your hobby or type 'stop' to finish: ") # taking users hobby or command to stop
    if user_answer.lower() == "stop": # if user type 'stop' in any case
        break # breaking loop
    else: # if user types something else
        hobbies.append(user_answer) # append this to hobbies list

life_stage = generate_profile(current_age) # creating life_stage variable, which contains the generate_profile return

user_profile = {
    "name":user_name,
    "age":current_age,
    "stage":life_stage,
    "hobbies":hobbies
}

display_users_profile(user_profile)