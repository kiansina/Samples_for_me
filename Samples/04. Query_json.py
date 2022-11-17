import requests
import json
response_API = requests.get('https://dati.inail.it/api/OpenData/DatiConCadenzaSemestraleInfortuni')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
print("Active cases in South Andaman:", active_case)
