import json
import requests

response = requests.get("https://api.games.mail.ru/pc/calendar/?date=2018-11-05&page=1&filter=popular&limit=30")
todos = json.loads(response.text)

print (todos)
