# to calculate tip for a bill at restaurant
# The total bill should be shared by the number of folks along with the tip
# choice of tip % can be given to the user to decide
# the calculator should provide cost to be paid by each individual including the tip

def calculate_tip(total_bill, tip_percent, headcount):
    cost_per_head = (total_bill + ((total_bill * tip_percent) / 100)) / headcount
    return round(cost_per_head,2)


def get_headcount():
    headcount = int(input("Enter the number of people sharing the bill \n"))
    if headcount >= 1:
        flag = False
        return headcount
    else:
        print("headcount is 0 / less than 0")


def get_tip_percent():
    tip_percent = int(input("choose a tip percentage: 10% or 12% or 15%"))
    if tip_percent == 10 or tip_percent == 12 or tip_percent == 15:
        return tip_percent
    else:
        print("Incorrect tip value. Please try again")


def get_total_bill_value():
    total_bill_value = float(input("Enter the bill amount \n $"))
    if total_bill_value >= 1:
        return total_bill_value
    else:
        print("Bill value is 0 / less than 0")


print("Cost to be paid per person = " + str(calculate_tip(get_total_bill_value(), get_tip_percent(), get_headcount())))
