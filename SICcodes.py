'''from companies_house_api_client import CompaniesHouse

CompaniesHouse.export(COMPANIES_HOUSE_APIKEY ="a14b30ce-ee9a-43c6-8cd0-ccca0777c0cc")
CompaniesHouse.export(COMPANIES_HOUSE_HOST = "https://api.company-information.service.gov.uk")

ch = CompaniesHouse()
companies = ch.get_company_profile("12312312")'''

import requests
import json
import sys
'''
url = "https://api.companieshouse.gov.uk/company/{}"
query = "tesco"
print(sys.argv[0])
params ={
    'q': "tesco"
}
api_key = "a14b30ce-ee9a-43c6-8cd0-ccca0777c0cc"

response = requests.get(url.format(query), auth=(api_key, ''))
json_search_result = response.text
search_result = json.JSONDecoder().decode(json_search_result)
print(search_result)
print(search_result.keys())
'''
import requests
import json

url = "https://api.companieshouse.gov.uk/search/companies?q={}"
query = "tesco"
api_key = "a14b30ce-ee9a-43c6-8cd0-ccca0777c0cc" #Fake key - insert your key here

response = requests.get(url.format(query),auth=(api_key,''))
json_search_result = response.text
search_result = json.JSONDecoder().decode(json_search_result)

for company in search_result['items']:
    print(company['title'])