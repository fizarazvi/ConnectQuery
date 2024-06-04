import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_data(linkedin_profile_url: str, is_mock_request: bool):
    response =''
    if(is_mock_request):
       response = requests.get('https://gist.githubusercontent.com/fizarazvi/2a8ef863266db8afbced8e1f3b8aa0b6/raw/5d84495e781d12e7217b0f67028ddbcaa2f5659f/mustafa-suleyman.json')
    else:
        headers = {"Authorization": f"Bearer {os.environ.get('PROXYCURL_API_KEY')}"}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        response = requests.get(api_endpoint,
                                params={'url': linkedin_profile_url},
                                headers=headers, timeout=10)
    return response.json() 

    

if __name__ == '__main__':
    print(scrape_linkedin_data('https://www.linkedin.com/in/mustafa-suleyman/', True))
