import requests
from bs4 import BeautifulSoup
# get html code by using requests.get
indeed_result = requests.get("https://www.indeed.co.uk/jobs?as_and=python+developer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")
# print(monitor_result.text)

# get texts by using BeautifulSoup to find how many pages there
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
# print(indeed_soup)

# find div 
pagination = indeed_soup.find("div", {"class" : "pagination"})
# print(pagination)

# find all links
links = pagination.find_all('a')
# print(pages)

# find "span" and append in the list as an integer except the last page which is 'next page'
pages = []
for link in links[:-1]:
	pages.append(int(link.find("span").string))

max_page = pages[-1]
print(max_page)