def generate_profile(age):
    if (age >= 0) and (age <= 12):
        return "Child"
    elif (age >= 13) and (age <= 19):
        return "Teenager"
    elif age >= 20:
        return "Adult"
    

print(generate_profile(12))
print(generate_profile(11))
print(generate_profile(0))

print(generate_profile(13))
print(generate_profile(14))
print(generate_profile(19))

print(generate_profile(20))
print(generate_profile(30))