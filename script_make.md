# 前言
同济大学1系统选课脚本制作方法，本方法有门槛、但技术性较低，不需要分析加密和获取密钥，比较麻烦，局限性交大，可以作为Web初学者练手和理解，同时限制大范围使用和黄牛
# 原理
通过前端操作获取所需请求报文，用python不断向目标网站发送请求
# 操作

1. 准备两个浏览器，选择不常用的或者F12工具较熟悉的那个
2. 打开到选课系统，保存已经抢好的课，同时为想抢的课留好空位（不要时间冲突）
3. 选择想抢的课，选好后打开F12开发者工具，选择“网络”，然后点击“保存课表”，在“网络”中找到“elsect”，双击，在“标头”中找到“请求标头”（火狐为“消息头”、“请求头”），讲X-Token的值复制出来存好，再在“负载”中点击“查看源”找到“ciphertext”和“checkCode”的文本（火狐为“请求”、“原始”），全选复制出来存好
4. 编写python脚本
   1. 如果理解网络请求报文是什么，那你获得上面的信息之后就可以直接写脚本了
   2. 代码实例
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
# 注意事项、Tips等

1. 该脚本或许有风险（比如误操导致掉了已经选好的课），另外不会用我也不会回答你（应该也问不到我），所以对选课系统逻辑比较了解/有些研究/对Web有些基础再来用吧
2. 请只操作自己的账户，当然应该也只能操作自己的账户
3. 不要宣传，自己学学就行了（虽然这写得很烂应该也没人看）
4. 保存的时候可以不止一门课，也就是说可以一次同时传好几个课的请求也可以分几个脚本选不同的课
5. 已经简化掉了不必要的请求头，如果出现问题试着全加上去看看
