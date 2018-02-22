import requests
from bs4 import BeautifulSoup


baseURL = 'https://www.yelp.com/search?find_desc=restaurants&find_loc='
location = 'San Francisco,CA'
page = 0
URL = baseURL + location + "&start=" + str(page)

yelp_request = requests.get(URL)
yelp_soup = BeautifulSoup(yelp_request.text, 'html.parser')

businesses = yelp_soup.findAll('div', {'class' : 'biz-listing-large'})

print(yelp_soup.findAll('li', {'class' : 'regular-search-result'}))

print(yelp_soup.findAll('div', {'class' : 'biz-name'}))

for biz in businesses:
	title = biz.findAll('a', {'class' : 'biz-name'})[0].text
	print(title)
	address = biz.findAll('address')[0]
	print(address)
	number = biz.findAll('span', {'class' : 'biz-phone'})[0].text
	print(number)


# for name in yelp_soup.findAll('a', {'class' : 'biz-name'}):
# 	print(name.text)



# print(yelp_soup.prettify())
# print(yelp_soup.findAll('a')) 

# for link in