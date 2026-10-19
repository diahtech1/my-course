from time import*

def calage():
    # get user detail needed
    print("enter your name")
    name = input('here...')
    print("enter birth year")
    bthyear = int(input('here...'))
    age = 2026 - bthyear
    # display a greting message
    print(f"welcome {name}, you are {age} years old!!!")
calage()

def validfunds():
    # user account details
    users = {
        'james':{'name':'James',
                 'age':'35',
                 'balance':5000},
        'josiah':{'name':'josiah',
                  'age':'27',
                  'balance':200000
    },  'mary':{'name':'mary',
                      'age':'27',
                      'balance':1500
    },
} 
    # available food items 
    items = [
        {'itemid':'1', 'price':2500},
        {'itemid':'2', 'price':1000},
        {'itemid':'3', 'price':2000},
        {'itemid':'4', 'price':1500},
        {'itemid':'5', 'price':3000},
    ] 
    # validate login credentials
    while True:
        print('enter username')
        username = input('...')
        if username not in users:
            print('invalid login credentials')
            
        elif username in users:
            print('login sucessfull')
            sleep(3)
            break

        # validte the food item needed
    while True:
        print("""select item to buy:
        1. rice and chicken
        2. beans and dodo
        3. chicken and chips           
        4. fruit salad
        5. yam and egg""")
        print('enter item number')
        item =  input('...')
        #ensure user pick the right item number
        if int(item) > 5 or int(item) < 1:
            print('enter valid item number')
        elif int(item) <= 5 and int(item) > 0:
            break
           

            # locate the item picked from the list
    for itemid in items:
        if itemid['itemid'] == item:
            break
            # fetch the user details from database
    userprofile = users.get(username)
        # validate user balance is sufficient to buy item picked
    if itemid['price'] < userprofile['balance']:
        print('Approved')
    elif itemid['price'] > userprofile['balance']:
        print('Insufficient funds')

            
                    

validfunds()