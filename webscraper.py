import requests
import pandas as pd

from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")


job_dict = {}

df = pd.DataFrame([job_dict])

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    
    job_dict["Title"] = title_element.text.strip()
    job_dict["Company"] = company_element.text.strip()
    job_dict["Location"] = location_element.text.strip()
    df = df.append(job_dict, ignore_index=True)



df.to_csv('jobs_on_site.csv', encoding='utf-8')


print("All availible jobs have been exported to jobs_on_site.csv")

