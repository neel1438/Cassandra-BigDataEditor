import csv
from collections import OrderedDict

from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily


pool = ConnectionPool('us', ['localhost:9160'])
col_fam = ColumnFamily(pool, 'data')

a = open('/Users/Neel/Downloads/us-500.csv', 'rU')
a = csv.DictReader(a)
t = 0
for row in a:
    dic2 = OrderedDict()
    for key in row:
        if not key == 'description':
            dic2[key] = row[key]
    print dic2
    col_fam.insert(str(t), dic2)
    t += 1