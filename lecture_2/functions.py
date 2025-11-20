def generate_profile(age):
    '''
    This function determines, which one age group we need to assign the subject
    '''
    if (age >= 0) and (age <= 12):
        return "Child"
    elif (age >= 13) and (age <= 19):
        return "Teenager"
    elif age >= 20:
        return "Adult"
    
def display_users_profile(user_profile):
    '''
    This function display users profile data
    '''
    print("---")
    print("PROFILE SUMMARY")
    print(f"Name: {user_profile["name"]}")
    print(f"Age: {user_profile["age"]}")
    print(f"Life stage: {user_profile["stage"]}")
    if len(user_profile["hobbies"]) > 0:
        print(f"Favorite hobbies ({len(user_profile["hobbies"])}): ")
        for hobby in user_profile["hobbies"]:
            print(f"- {hobby}")
    else:
        print("You didn't mention any hobbies.")
    print("---")