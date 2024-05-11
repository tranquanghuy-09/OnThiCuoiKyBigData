import sys

current_rating = None
max_price = float('-inf')

for line in sys.stdin:
    rating, price = line.strip().split('\t')
    if current_rating != rating:
        if current_rating is not None:
            print('%s\t%s' % (current_rating, max_price))
        current_rating = rating
        max_price = float(price)
    else:
        max_price = max(max_price, float(price))

if current_rating is not None:
    print('%s\t%s' % (current_rating, max_price))
