# auction_bids = {"maxbid":{"name":"","bid":0}}
auction_bids = {}
max_bidder = ""
max_bid = 0

while True:
    name = input("Enter your name:")
    bid = int(input("Enter your bid: ₹"))
    auction_bids[name] = bid
    doContinue = input("Are there any more bidders? Type 'yes' or 'no': ")
    if doContinue == 'no':
        break

for key in auction_bids:
    # if key != "maxbid":
        if auction_bids[key]>auction_bids["maxbid"]["bid"]:
            # auction_bids["maxbid"]["name"] = key
            max_bidder = key
            # auction_bids["maxbid"]["bid"] = auction_bids[key]
            max_bid = auction_bids[key]

# print(f"{auction_bids["maxbid"]["name"]} bid the highest at ₹{auction_bids["maxbid"]["bid"]}") 
print(f"{max_bidder} bid the highest at ₹{max_bid}")