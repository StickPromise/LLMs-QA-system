pkill -f "flask run"

# 启动第一个服务
export FLASK_APP="/chatgpt/LLMs-QA-system/College/Algorithm/Collegeapp.py"
nohup flask run --host=0.0.0.0 --port=5020 &

# 启动第二个服务
export FLASK_APP="/chatgpt/LLMs-QA-system/Company/Algorithm/app.py"
nohup flask run --host=0.0.0.0 --port=5021 &

# 启动第三个服务
export FLASK_APP="/chatgpt/LLMs-QA-system/Dangwu/Algorithm/QAdangwuapp.py"
nohup flask run --host=0.0.0.0 --port=5022 &

# 启动第四个服务
export FLASK_APP="/chatgpt/LLMs-QA-system/Oldcollege/Algorithm/QAOldcollegeapp.py"
nohup flask run --host=0.0.0.0 --port=5024 &

# 启动第五个服务
export FLASK_APP="/chatgpt/LLMs-QA-system/streettown/Algorithm/QAstreetapp.py"
nohup flask run --host=0.0.0.0 --port=5023 &
