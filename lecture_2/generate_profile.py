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