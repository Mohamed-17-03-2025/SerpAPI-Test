import serpapi
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('SERPAPI_KEY')
client = serpapi.Client(api_key=api_key)

articles = []

for iterand in range (0,20):
    result = client.search(q="wastewater",engine="google",as_sitesearch="www.omanobserver.om",start=iterand*10)
    articles.append(result)

print(result)
print("=============================================================================================================================================")
print(articles)

with open("oman_observer_articles.txt", "w") as output:
    output.write(str(articles))