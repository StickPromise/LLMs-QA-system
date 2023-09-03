import requests
import json
import PyPDF2
from io import BytesIO

filename = "学校简介.pdf"

# 定义场景名称
scenename = "新学员适应向导"  # 替换为您的场景名称

# 定义问题
question = "请你介绍一下上海电机学院"  # 替换为您的问题

# 定义请求URL
get_answer_url = "http://172.16.20.239:5002/api/get_answer"

# 定义发送的JSON数据
request_data = {
    'message': question,
    'scenename': scenename,
    'reset': True  # 可以根据需要修改
}

# 发送POST请求到/api/get_answer端点，获取回答
get_answer_response = requests.post(get_answer_url, json=request_data)

# 获取JSON响应数据
answer_data = get_answer_response.json()

# 打印回答
print("Answer:", json.dumps(answer_data, indent=4, ensure_ascii=False))

# 调用/get_file/<scenename>/<filename>端点获取文件
get_file_url = f"http://172.16.20.239:5002/get_file/{scenename}/{filename}"
get_file_response = requests.get(get_file_url)

# 打印回答
print("Answer:", json.dumps(answer_data, indent=4, ensure_ascii=False))
