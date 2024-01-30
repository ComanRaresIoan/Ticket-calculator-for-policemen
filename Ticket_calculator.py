from datetime import datetime

name = input("What's your name?\n")
current_datetime = datetime.now()
print(current_datetime)

def speed_limit():
    speed_recorded = float(input("Enter speed:"))
    max_limit = 50
    speed_ticket = 25
    ticket1 = 0

    if speed_recorded >= max_limit:
        if speed_recorded <= max_limit + 10:
            n = 1
            print("The ticket you get is", n * speed_ticket, "$")
            ticket1 = n * speed_ticket
        elif speed_recorded <= max_limit + 20:
            n = 2
            print("The ticket you get is", n * speed_ticket, "$")
            ticket1 = n * speed_ticket
        elif speed_recorded <= max_limit + 30:
            n = 3
            print("The ticket you get is", n * speed_ticket, "$")
            ticket1 = n * speed_ticket
        else:
            n = 5
            print("The ticket you get is", n * speed_ticket, "$")
            ticket1 = n * speed_ticket
    else:
        print("You are within limits, no ticket for you")

    return ticket1

def alcohol_test():
    recorded_speed = speed_limit()
    print("You must take an alcohol test!")
    alcohol_in_blood = round(float(input("Enter alcohol level:")), 2)
    alcohol_ticket = 30
    ticket2 = 0

    if recorded_speed > 50:
        if alcohol_in_blood == 0:
            n = 0
            print('The ticket you get is', n * alcohol_ticket, "$")
            ticket2 = n * alcohol_ticket
        elif 0.01 <= alcohol_in_blood <= 0.39:
            n = 2
            print("The ticket you get is", n * alcohol_ticket, "$")
            ticket2 = n * alcohol_ticket
        elif 0.40 <= alcohol_in_blood <= 0.79:
            n = 3
            print("The ticket you get is", n * alcohol_ticket, "$")
            ticket2 = n * alcohol_ticket
        elif alcohol_in_blood >= 0.80:
            n = 4
            print("The license is suspended, and the ticket you get is", n * alcohol_ticket, "$")
            ticket2 = n * alcohol_ticket
        else:
            n = 5
            print("Your license is suspended, and you get a ticket of", n * alcohol_ticket, "$")
            ticket2 = n * alcohol_ticket
    else:
        n = 0
        print("You are within limits, no ticket for you.")

    return ticket2

# Call each function only once and store the results in variables
speed_ticket = speed_limit()
alcohol_ticket = alcohol_test()

total_ticket = speed_ticket + alcohol_ticket

print("Total ticket is:", total_ticket, "$")
with open(f'ticket_for_{name}.txt', 'a') as f:
    f.write(f"Driver: {name}\nGot a total ticket of {total_ticket}$, which consists of {alcohol_ticket}$ for alcohol and {speed_ticket}$ for speeding.\n"
            f"The time of the ticket providing: {current_datetime}\n\n")
