import pycassa
import bisect
import hashlib
import sys,re
import csv
from collections import OrderedDict
from pycassa.system_manager import *
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('large_data',['localhost:9160'])
col_fam = ColumnFamily(pool, 'data3')

a=open('/home/neel/Downloads/airport-frequencies.csv','r')
a=csv.DictReader(a);
t=0
for row in a:
	dic2=OrderedDict()
	for key in row:
		if(not key=='description'):
			dic2[key]=row[key]
	print dic2x
	col_fam.insert(str(t),dic2);
	t=t+1





