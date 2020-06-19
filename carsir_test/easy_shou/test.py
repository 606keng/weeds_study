import requests

url = "http://10.7.200.179:7002/api-olympic-admin/workorder/check/test/getCarPrice"
headers = {"token":"68774b2f709c4bb589c2a23ac6dbfae7","grp":"nba_pc"}
request_json = {"carLevel": "S", "car300": 29900}
r = requests.post(headers=headers,url=url, json=request_json)
print(r.json())