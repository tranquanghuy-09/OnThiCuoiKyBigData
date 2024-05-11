import sys

for line in sys.stdin:
    fields = line.strip().split('$')
    if len(fields) == 6:
        product_url, title, description, price, stock, rating = fields
        print('%s\t%s' % (rating, price))
