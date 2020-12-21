import requests

# 定义请求参数，将字符串作为文件report.jpg来发送
from requests_toolbelt import MultipartEncoder

file = {"files": ("1.jpg", open("image.png", "rb"), 'image/jpeg')}
file["businessName"] = "轻松购"
file["productName"] = "中国银行"
file["businessType"] = "1"
file["productType"] = "1"
file["materialDescribe"] = "123"
file["fileTab"] = "fileTab_0"
file["materialName"] = "report.doc"
# 定义headers
headers = {}
#将请求参数转换为数据流
data = MultipartEncoder(file)
#获取数据流的Content-Type
headers["Content-Type"] = data.content_type
# 人人网Cookie
headers[
    "Authorization"] = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiUk9MRV9BRE1JTiIsInRva2VuX2lkIjoiYWI2MjBkN2YtODExYi00MTkwLThmY2MtMGYyYjJjMDJmM2ZmIiwic3ViIjoiMTg3OTEwNzY2MTQiLCJpYXQiOjE2MDg0NzM2MjQsImV4cCI6MTYwOTA3ODQyNCwiaXNzIjoiQUNDRVNTIn0.6eVy78dSk61Pnq9euLLTrZGY3WI6B61AF-74oOT52oMN48fGSb314wUEy9qWgq9EZLqx5kGf3mgtgCDxykAQ4g"  # 人人网上传头像接口
headers["grp"] = "carsir_olympic"
headers["username"] = "18791076614"
r = requests.post(
    "https://test.carsir.xin/admin/MaterialController/uploadMaterialFiles",
    headers=headers, data=data)
print(r.json())
