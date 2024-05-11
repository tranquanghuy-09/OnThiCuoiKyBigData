import sys

header = sys.stdin.readline()

for line in sys.stdin:
    fields = line.strip().split('$')
    price = float(fields[3])
    print ('%s\t%f' % ("min", price))
