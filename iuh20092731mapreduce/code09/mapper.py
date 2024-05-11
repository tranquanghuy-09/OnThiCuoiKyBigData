import sys

total_price = 0
total_books = 0

header = sys.stdin.readline()

for line in sys.stdin:
    fields = line.strip().split('$')
    price = float(fields[3])
    total_price += price
    total_books += 1

average_price = total_price / total_books

sys.stdin.seek(0)
header = sys.stdin.readline()
for line in sys.stdin:
    fields = line.strip().split('$')
    price = float(fields[3])
    if price > average_price:
        print ('%s\t%s' % ("book_above_avg", line.strip()))
