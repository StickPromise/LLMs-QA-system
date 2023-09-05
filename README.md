项目简介
本项目旨在基于Langchain框架和大语言模型，对封闭的语料实现精准的问答和对应文本的高亮功能。

技术路线
框架：Langchain
模型：大语言模型（例如，GPT-3.5，cutegpt）
文件结构
LLMs-QA-system
│
├── College/
│   ├── Algorithm/
│   │   ├── QACollege.py  (主要算法代码)
│   │   ├── Collegeapp.py  (接口文件)
│   │   └── Collegetest.py (测试文件)
|   |   └── stopwords.txt  (停用词文件)
│   └── Data/              (数据文件)
│
├── Company/
│   ├── Algorithm/
│   │   ├── LangchaninQA16_0.py
│   │   ├── app.py
│   │   └── test.py
|   |   └── stopwords.txt
│   └── Data/
│
├── ...
│
├── OLdcollege/
│   ├── Algorithm/
│   │   ├── QAOldcollege.py
│   │   ├── QAOldcollegeapp.py
|   |   └── stopwords.txt
│   │   
│   └── Data/
│
├── requirements.txt      (依赖文件)
└── README.md             (项目说明)

对于每一版本中的数据集地址麻烦再检查一下是否正确，请自行调整一下
并且每一版本的app文件中也请更改一下localhost的地址和端口号
部署方法:
1.新建项目空间
2.克隆github仓库地址：git clone https://github.com/StickPromise/LLMs-QA-system.git
3.进入项目目录，安装依赖pip3 install -r requirements.txt
  在每一版本的代码文件中的load_user_data函数中和get_answer函数中检查文件地址路径是否正确
  同时在每一版本的app文件中检查get_file/<scenename>/<filename>服务中修改获取文件的地址
  修改ip地址和端口号（在每一个app服务文件的最后一行）
4.测试运行 python3 test.py(四个版本都有一个测试文件）
5.设置进程管理
  创建一个systemd服务文件来保持应用持续运行（我没试过）
6.启动并激活服务
7.修改防火墙设置

