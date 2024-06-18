# TJCS-Script_SelectCourse
同济大学选课脚本教程
# 原理
通过前端操作获取所需请求报文，用python不断向目标网站发送请求
# 操作

1. 打开到选课系统，保存已经抢好的课，同时为想抢的课留好空位（不要时间冲突）
2. 选择想抢的课，选好后打开F12开发者工具，选择“网络”，然后点击“保存课表”，在“网络”中找到“elsect”，双击，在“标头”中找到“请求标头”（火狐为“消息头”、“请求头”），讲X-Token的值复制出来存好，再在“负载”中点击“查看源”找到“ciphertext”和“checkCode”的文本（火狐为“请求”、“原始”），全选复制出来存好
3. 编写python脚本
   1. 如果理解网络请求报文是什么，那你获得上面的信息之后就可以直接写脚本了
   2. 示例代码：
```python
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
```

4. 运行。注意运行过程中用来获取信息的浏览器不要关闭再重新打开1系统，X-Token会变更
# 注意事项、Tips等

1. 如果返回“{"message":"sessionid is not exist."}”或显示“X-Token is wrong”，重新获取X-Token就行，data部分可改可不改
2. 保存的时候可以不止一门课，也就是说可以一次同时传好几个课的请求也可以分几个脚本选不同的课
3. 已经简化掉了不必要的请求头，如果出现问题看看原始的请求头
4. 如果想保存其他有名额的课的话记得先把脚本停下来
# 免责（保护）

**商用是禁止的**
仓库中所有文件，若侵，联系确认后立删；著作权只属于文件作者；拒绝未经允许的使用、分发、传播；仅用于项目所有人的存储。
