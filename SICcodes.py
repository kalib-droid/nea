from companies_house_api_client import CompaniesHouse

export COMPANIES_HOUSE_APIKEY=your-api-key
export COMPANIES_HOUSE_HOST=https://api.company-information.service.gov.uk


companies = ch.get_company_profile("12312312")