import serpapi
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('SERPAPI_KEY')
client = serpapi.Client(api_key=api_key)

result = client.search(q="wastewater",engine="google",as_sitesearch="www.omanobserver.om")

print(result)