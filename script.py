import requests
import time

# 构建请求头
headers = {
    "X-Token": "", # 填写
}

# 构建请求数据
data = {
    "ciphertext": "", # 填写
    "checkCode": ""   # 填写
}

# 发送 POST 请求
url = "https://1.tongji.edu.cn/api/electionservice/student/elect"
response = requests.post(url, json=data, headers=headers)
print(response.text)
if(response.text == '{"message":"sessionid is not exist."}'):
    exit()
while True:
    response = requests.post(url, json=data, headers=headers)
    if(response.text == '{"message":"sessionid is not exist."}'):
        print("X-Token is wrong")
        exit()