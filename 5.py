import bs4
import requests

res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
print(res)

soup = bs4.BeautifulSoup(res.text ,'lxml')

data = soup.find('img', {"class":"p-qotd"})
print(data)

q = data['alt']
print(q)

i_url = data['data-img-url']
print(i_url)

p_url = "https://www.brainyquote.com" + i_url
res = requests.get(p_url)

with open("image1.png",'wb')as f:
		f.write(res.content)