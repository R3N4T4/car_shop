import cars
import credentials
import bank_accounts
import customer
import datetime
import random


#initialize cars and costs
audi = cars.cars_class('red','Audi',200)
bmw = cars.cars_class('black', 'BMW', 300)
vw = cars.cars_class('grey','VW',344)

# create mapping between possible answers and car models
cars_list = {'1':audi,'2':bmw,'3':vw}

customer_list = {'rpuchbau':customer.customer_class('Rena', 'Puchbauer', '1234'),
                 'account2':customer.customer_class('Account2','Puchbauer','2222')}

def login():
    # authorize user by asking for username and password
    username = input("Enter your username: \n")
    password = input("Enter your password: \n")
    #check if credentials are correct
    if (username in credentials.credentials_list.keys() and credentials.credentials_list[username] == password):
        take_order(username,password)
    else:
        print("Wrong credentials! Have a good day!")
        exit()

def take_order(username, password):
    # ask for desired car model
    for x in cars_list:
        print("Press {} to buy an {}".format(x,cars_list[x].brand))
    car_model = input()

    #ask again for desired model if answer is invalid
    if car_model not in cars_list.keys():
        while car_model not in cars_list.keys():
            car_model = input("Car doesn't exist. Try again or press 'n' to exit:\n")
            if car_model == 'n':
                print("Have a good day!")
                exit()
            else:
                pass
    number_of_cars = input("How many cars do you want?\n")
    #invoke total_cost function to get total cost
    total = total_cost(car_model, int(number_of_cars))

    # add order to user
    #TODO: each order should have an order number and customer should see his order nr
    #TODO: order number should be created by a RNG and must be unique!
    customer_list[username].orderlist.append(customer.order(cars_list[car_model].brand,
                                                            number_of_cars,random_nr_gen()))


    customer_list['account2'].orderlist.append(customer.order('BMV',1,'234wa'))
    customer_list['account2'].orderlist.append(customer.order("Audi",2,"renakey2"))
    customer_list['rpuchbau'].orderlist.append(customer.order("Audi,",3,"renakey3"))

    print(customer_list['rpuchbau'].orderlist[1].ordernumber)

    print(customer_list['rpuchbau'].orderlist[1].model)
    print(customer_list['rpuchbau'].orderlist[1].amount)
    print(customer_list['rpuchbau'].orderlist[1].ordernumber)


    rena = ['rena''sigi','rena']

    print(rena)

    # for x in customer_list:
    #     for y in range (len(customer_list[x].orderlist)):
    #         print(customer_list[x].orderlist[y].ordernumber)

    for username in customer_list:
        customer = customer_list[username]
        customer_orders = customer.orderlist
        for y in range (len(customer_orders)):
            print (customer_orders[y].ordernumber)
        #y steht fuer jeden index im array


    for username in customer_list:
        customer = customer_list[username]
        customer_orders = customer.orderlist
        for x in customer_orders:
            print(x.ordernumber)


    for customer in customer_list.values():
        for x in customer.orderlist:
            print (x.ordernumber)
        #x represents each instance in the array



    rean = ['sigi', 'rena','test']


    for x in range(len(rean)):
        print (rean[x])






    #invoke credit_check function to check if user has enough money
    credit_check(total, username, password)

def random_nr_gen():
    #1.use set since set doesn't allows duplicate entries
    #2.use a function to generate 20 random strings which will be the order nr
    #3. each time time function gets invoked, it will return an order nr and then removes it from the set

    key1 = datetime.datetime.now().strftime("%f")
    print("key1:{}".format(key1))
    key2 = random.choice('abcdefghijklmnopqrstuvwxyz')
    print("key2:{}".format(key2))
    key3 = random.randint(1,99)
    print("key3:{}".format(key3))

    ordernr = key1[0:5]+key2+str(key3)
    print("order number:{}".format(ordernr))
    return ordernr



def total_cost(car_model, number_of_cars):
    total = cars_list[car_model].cost * number_of_cars
    print("Total cost: {}".format(total))
    return total


def credit_check(total, username, password):
    # ask customer for credit card information and check bank account statement,
    # if there is enough money - allow purchase
    bank_account = input("Enter your bank account number:\n")
    if bank_account not in bank_accounts.accountlist:
        while bank_account not in bank_accounts.accountlist:
            bank_account = input("Invalid account. Try again or press 'n' to exit:\n")
            if bank_account == 'n':
                print("Have a good day!")
                exit()
            else:
                pass
    if (bank_accounts.accountlist[bank_account] - total) >=0:
        confirmation = input("Credit check passed. Enter y to confirm order: \n")
        if confirmation.upper() == 'Y':
            bank_accounts.accountlist[bank_account] = bank_accounts.accountlist[bank_account] - total
            new_order = input("Order processed. Press y to buy another car or any other button to exit: \n")
            if new_order == 'y':
                take_order(username,password)
            else:
                print("Have a good day!")
                exit()
        else:
            print("Purchase cancelled. Have a good day!")
            exit()

    else:
        print("Sorry, you are too poor! Have a good day!")
        exit()



login()



