from bs4 import BeautifulSoup
import requests




##########################################################

def getResult(link):
	source=requests.get(link).text
	#print(source)
	soup=BeautifulSoup(source,'html.parser')

	x=soup.findAll("div",{"class":"row"})
	for t in x:
		for n in t.findAll("div",{"class":"col-lg-4 col-md-6 col-widen text-center"}):
			q=n.find("div",{"class":"well result-box nomargin"})
		#print(q.h3.text)
			try:
				z=q.h3.text
				p=q.find("a",{"class":"nounderline"})
				print(z+" Type: "+p['title'].replace("All","").replace("Skins",""))
			except(TypeError, KeyError) as e:
				pass

##########################################################



source=requests.get("https://csgostash.com/").text
soup=BeautifulSoup(source,'html.parser')
i=0

weaponList=soup.find("ul",{"class":"nav navbar-nav"})
AllWeapon=weaponList.findAll("li",{"class":"dropdown"})
for x in AllWeapon:
	if i==4:
		break
	y=x.find("ul",{"class":"dropdown-menu navbar-dropdown-large"})
	for li in y.findAll("li"):
		try:
			print(li.a['href'].replace("https://csgostash.com/weapon/","Weapon : "))
			getResult(li.a['href'])
		except(TypeError,NameError) as e:
			pass
	i=i+1	