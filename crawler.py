#coding=utf-8
import requests
from bs4 import BeautifulSoup
import lxml
import time

s_page=0
for p in range(s_page,1000):
	res = requests.get("http://hospital.kingnet.com.tw/free/consulting.html?start="+str(p*10)+"&department=14&outpatient=generally")
	res.encoding = 'Big5' #website_encode
	soup = BeautifulSoup(res.text, 'lxml') #extractor
	span=soup.find_all('font', 'medicine03')
	num=0
	for r in span:
        	num+=1
	#write string
	string=""
	i=0
	print str(p)
	for r in span:
		i+=1
		if(i==1):
			continue
		if(i>=num-2):
			break
		target="症狀："
		target1="補充說明："
		if(r.get_text()==target.decode('utf8')):
			if(i!=2):
				string+="\n"
			string+=r.parent.find('span').get_text()
		if(r.get_text()==target1.decode('utf8')):
			string+=r.parent.find('span').get_text()
	#create & write file
        try:
                f = open("articles/"+"page"+str(p)+".txt", "w")
        except:
                print "File Open Error"
                continue
        else:
                f.write(string.encode('utf8'))
		f.close()
		

