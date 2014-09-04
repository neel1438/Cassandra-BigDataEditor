import pycassa
import bisect
import hashlib
import sys,re
import csv
from collections import OrderedDict
from pycassa.system_manager import *
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('Countries',['localhost:9160'])
col_fam = ColumnFamily(pool, 'data1')

a=open('/home/neel/Downloads/TechCrunchcontinentalUSA.csv','rU')
a=csv.DictReader(a);
t=0
for row in a:
	dic2=OrderedDict()
	for key in row:
		if(not key=='description'):
			dic2[key]=row[key]
	print dic2
	col_fam.insert(str(t),dic2);
	t=t+1