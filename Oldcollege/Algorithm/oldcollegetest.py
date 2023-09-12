import requests
import json
import PyPDF2
from io import BytesIO

filename = "学校简介.pdf"

# 定义场景名称
scenename = "学校全景解读"  # 替换为您的场景名称

# 定义问题
question = "请介绍一下学校"  # 替换为您的问题

# 定义请求URL
get_answer_url = "http://101.132.161.92:5024/api/get_answer"

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
get_file_url = f"http://101.132.161.92:5024/api/get_file/{scenename}/{filename}"
print("success:", get_file_url)
get_file_response = requests.get(get_file_url)

# 打印回答
print("Answer:", json.dumps(answer_data, indent=4, ensure_ascii=False))
