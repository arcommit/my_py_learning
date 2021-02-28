from FPSBA_logo import logo


print(logo)
print("Welcome First-price sealed-bid auction(FPSBA)")

new_bidders = True
bidders = {}
winning_bid = 0
winner = ""

while new_bidders:
    name = input("Enter your full name:  ")
    bid_value = input("What's your bid?  $")
    next_bidder = input("are there any other bidders? Yes/No   ").lower()
    if next_bidder != "yes":
        new_bidders = False
    bidders[name] = bid_value
    print(bidders)


for name, value in bidders.items():
    if int(winning_bid) < int(value):
        winner = name
        winning_bid = value

print(f"Winner of the bid is '{winner}'")
print(f"Winning bid is '{winning_bid}'")
