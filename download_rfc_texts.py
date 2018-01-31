import urllib2
import time

print("start")

for i in range(8000):
	url = 'https://www.ietf.org/rfc/rfc{}.txt'.format(i)
	print(url)
	try:
		response = urllib2.urlopen(url)
		data = response.read()
		filename = "./data_source/rfc/rfc{}.txt".format(i)
		file_ = open(filename, 'w')
		file_.write(data)
		file_.close()
		print("success {}".format(i))
	except:
		print("fail {}".format(i))
	time.sleep(0.7)
