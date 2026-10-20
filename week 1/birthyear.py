def birthyear():
    # get user detail needed
    print("enter your name")
    name = input('here...')
    print("enter birth year")
    bthyear = int(input('here...'))
    age = 2026 - bthyear
    # display a greting message
    print(f"welcome {name}, you are {age} years old!!!")
birthyear()