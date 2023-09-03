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
│   │   └── Collegetest.py       (测试文件)
│   └── Data/              (数据文件)
│
├── Company/
│   ├── Algorithm/
│   │   ├── LangchaninQA16_0.py
│   │   ├── app.py
│   │   └── test.py
│   └── Data/
│
├── ...
│
├── OLdcollege/
│   ├── Algorithm/
│   │   ├── QAOldcollege.py
│   │   ├── QAOldcollegeapp.py
│   │   
│   └── Data/
│
├── requirements.txt      (依赖文件)
└── README.md             (项目说明)

