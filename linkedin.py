from bs4 import BeautifulSoup
import requests

url = 'https://www.linkedin.com/jobs/search/?distance=25&f_AL=true&f_E=2&f_TPR=r86400&geoId=115729725&keywords=developer'

response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

jobs = soup.find_all('div',{'class':'base-card'})

jobslist = []

for job in jobs:
  link = job.a['href']
  title = job.span.text.strip()

  jobslist.append({'title':title,'link':link})
  
for job in jobslist:
  print(f'Title: {job['title']}')
  print(f"Link: {job['link']}\n")