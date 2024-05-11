import sys

min_price = sys.float_info.max

for line in sys.stdin:
    key, value = line.strip().split('\t')
    price = float(value)
    if price < min_price:
        min_price = price

print ("%s\t%s" % ("min", min_price))
