import requests
from bs4 import BeautifulSoup
import lxml
import time
res = requests.get("http://www.babyhome.com.tw/mboard/list.php?style=baby&page=1")
soup = BeautifulSoup(res.text, 'lxml')
#print soup

n=5
a_id=0;
for i in range(1,n):
	res = requests.get("http://www.babyhome.com.tw/mboard/list.php?style=baby&page="+str(i))
	soup = BeautifulSoup(res.text, 'lxml')
	print res.text
	for tr in soup.find_all("tr"):
		if (tr['class'] ==  ['span_thread', ''] and tr.find('a')!=None):
			article_name = str(tr.find('a').get('title').encode('utf8'))
			print article_name
			href =  tr.find('a').get('href')
			sub_res = requests.get("http://www.babyhome.com.tw/mboard/"+href)
			sub_soup = BeautifulSoup(sub_res.text, 'lxml')
			result = sub_soup.find("div", class_="comment_content")
	 		s = ""
			for t in result.find_all('p'):
				t.replaceWith('') 
				s+= t.get_text()

			#create file
			try:
				f = open("articles/"+str(a_id)+"_"+article_name+".txt", "w")
			except:
				print "File Open Error"
				continue
			else:
				 f.write(s.encode('utf8'))
			a_id+=1
		



