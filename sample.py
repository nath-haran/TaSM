import csv
import gzip
import simplejson
def parse(filename):
  f = gzip.open(filename, 'r')
  entry = {}
  for l in f:
    l = l.strip()
    colonPos = l.find(':')
    if colonPos == -1:
      yield entry
      entry = {}
      continue
    eName = l[:colonPos]
    rest = l[colonPos+2:]
    entry[eName] = rest
  yield entry
fieldnames=['product/productId','product/title','product/price','review/userId','review/profileName','review/helpfulness','review/score','review/time','review/summary','review/text']
with open('Electronics.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for e in parse("Electronics.txt.gz"):
		writer.writerow(e)
  
