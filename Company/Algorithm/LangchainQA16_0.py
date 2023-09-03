from langchain.document_loaders import DirectoryLoader
import jieba
import jieba.posseg as pseg
from langchain.text_splitter import CharacterTextSplitter
import numpy as np
import requests
import os
import torch
import json
from rank_bm25 import BM25Okapi
import dateparser
from dateparser import search
from fuzzywuzzy import fuzz
import torch
from langchain.document_loaders import PyPDFLoader
from sentence_transformers import SentenceTransformer
import numpy as np
import re
from nltk.tokenize import sent_tokenize

# 确保下载了Punkt句子分词器
import nltk
nltk.download('punkt')

device = torch.device("cpu")
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# 添加一个字典来保存每个用户的数据和索引库
scene_data = {}
scene_index = {}
history = []
# 在顶部定义一个全局变量
scenename = None
# 为文本片段增加元信息
class Document:
    def __init__(self, page_content, source, page_number, part):
        self.page_content = page_content
        self.source = source
        self.part = part
        self.page_number = page_number

# 读取停用词文件
with open("E:/工作/LangchainQA/stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = [line.strip() for line in f]

# 读取文件
def load_all_docs_and_pdfs(directory):
    data = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if filename.endswith(".docx"):
            loader = DirectoryLoader(directory, glob="**/*.docx", show_progress=True)
            document_data = loader.load()
            data.append(document_data)
        elif filename.endswith(".pdf"):
            # 使用 PyPDFLoader 读取 PDF 文件
            loader = PyPDFLoader(path)
            pages = loader.load_and_split()
            # 将每一页作为一个单独的文档添加到数据中
            for page in pages:
                data.append([page])  # 每一页作为一个文档列表的元素
    return data

# 对文本进行分割，分割后进行存储和添加信息
def process_documents(data):
    documents = []
    document_texts = set()
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0, separator='\n', length_function=len)

    for sublist in data:
        for index, doc in enumerate(sublist):
            split_text = text_splitter.split_text(doc.page_content)
            for i, text in enumerate(split_text):
                if text not in document_texts:
                    words = pseg.cut(text)
                    filtered_text = ''.join(word for word, flag in words if word not in stopwords)
                    source = f'文件名称: {doc.metadata["source"]}'
                    part = f'第 {i + 1} 部分'
                    page_number = f'文本页码：{doc.metadata["page"]}'
                    document = Document(filtered_text, source, page_number, part)
                    documents.append(document)
                    document_texts.add(filtered_text)

    tokenized_documents = [list(jieba.cut(doc.page_content)) for doc in documents]
    bm25 = BM25Okapi(tokenized_documents)
    scene_data[scenename] = (documents, bm25)

    return documents, bm25


# 当用户选择场景时，加载他们的数据并创建索引库
def load_user_data(scene):
    global scenename
    scenename = scene

    # 设置一个默认值（您可以根据实际情况进行调整）
    directory = None

    if scenename == '新员工适应向导':
        directory = "E:/工作/BkmGPT语料/BkmGPT语料/新员工适应向导"
    elif scenename == '岗位知识支持助手':
        directory = "E:/工作/BkmGPT语料/BkmGPT语料/岗位知识支持助手"
    elif scenename == 'IT系统使用向导':
        directory = "E:/工作/BkmGPT语料/BkmGPT语料/IT系统使用向导"
    elif scenename == '生产设备&工艺知识库':
        directory = "E:/工作/BkmGPT语料/BkmGPT语料/生产设备&工艺知识库"
    elif scenename == '行业&领域知识仓库':
        directory = "E:/工作/BkmGPT语料/BkmGPT语料/行业&领域知识仓库"
    # 检查directory是否已经赋值
    if directory is None:
        print(f"Scene name '{scenename}' not recognized.")
        return False

    data = load_all_docs_and_pdfs(directory)
    documents, bm25 = process_documents(data)
    scene_data[scenename] = documents
    scene_index[scenename] = bm25

    return documents, bm25
# 预处理所有文件 改为自适应功能
def load_all_data():
    global scene_data
    scenes = ['新员工适应向导', '岗位知识支持助手', 'IT系统使用向导', '生产设备&工艺知识库', '行业&领域知识仓库']
    for scene in scenes:
        documents, bm25 = load_user_data(scene)
        scene_data[scene] = (documents, bm25)
        print(f"Loaded data for scene: {scene}\n")


# 历史记录清空功能
def clean_dialogue_cache():
    # 清空历史对话，开启新的对话
    requests.post("http://10.176.40.138:23489/ddemos/cutegpt_normal/run/delete", json={
        "data": [
        ]
    }).json()


# 更新历史记录
def append_history(query, answer):
    global history
    history.append((query, answer))  # 将新的对话添加到历史中



# 调用大模型回答问题，同时考虑历史记录问题
def get_ans(query):
    global history
    # 将历史对话和当前查询传递给GPT模型
    response = requests.post("http://10.176.40.138:23489/ddemos/cutegpt_normal/run/submit", json={
        "data": [
            query,
            [item[0] for item in history],  # 历史问题
            [item[1] for item in history],  # 历史回答
        ]
    }).json()
    return response["data"][0][0][1]

def print_histories(histories):
    rnd = 0
    for query, ans in histories:
        print(f'[Round {rnd}]')
        print('Human:', query)
        print('CuteGPT:', ans)
        rnd += 1

model = SentenceTransformer('bert-base-nli-mean-tokens')


def find_most_similar_sentences(answer, documents, top_n=3):
    answer_embedding = model.encode([answer])
    similarity_scores = []
    for doc in documents:
        # 使用sent_tokenize进行句子分割
        sentences = sent_tokenize(doc)
        sentence_embeddings = model.encode(sentences)
        similarities = np.dot(sentence_embeddings, answer_embedding.T).flatten()
        top_sentences = [sentences[i] for i in similarities.argsort()[-top_n:][::-1]]
        similarity_scores.extend(top_sentences)

    return similarity_scores[:top_n]

# 全局历史记录字典，键为场景名称，值为查询和响应对的列表
history_dict = {}
def get_answer(query, scenename, reset=False):
    global history_dict
    # Step 1: 处理重置选项
    if reset:
        history_dict[scenename] = []
    history = history_dict.get(scenename, [])

    # Step 2：获取对应用户的文档和索引
    print(f"Getting answer for scene: {scenename}")
    documents, bm25 = scene_data[scenename]
    if documents is None or bm25 is None:
        return {'content': "无法找到您的数据，请检查您的用户名是否正确或联系管理员。"}

    words = pseg.cut(query)
    query_cut = [word for word, flag in words if word not in stopwords]
    scores = bm25.get_scores(query_cut)
    k = 3
    most_similar_indices = np.argsort(scores)[-30:]
    unique_documents = {(doc.page_content, doc.source, doc.page_number, doc.part): scores[i] for i, doc in enumerate(documents) if
                        i in most_similar_indices}
    sorted_unique_documents = sorted(unique_documents.items(), key=lambda x: x[1], reverse=True)
    top_k_documents = sorted_unique_documents[:k]
    if top_k_documents[0][1] < 5.0:  # 如果最高得分低于10，返回特定的消息
        return {'content': "我的信息不足以回答你的问题，请更换别的助手", 'documents': [], 'highlight': ""}
    # Step 3：构造prompts
    context = ' '.join(f"{doc[0][1]}:\n{doc[0][0]}" for doc in top_k_documents)
    prompt = f"参考这几篇文章里与问题相关的以下{k}段文本:\n{context}，然后回答后面的问题：\n基于这些内容，请回答问题：{query}\n：你应当尽量用原文回答，并在回答之后将该段原文总结，不要太短。"
    # Step 4：构造带有历史记录的提示
    history_prompt = "\n".join([f"Q: {q}\nA: {a}" for q, a in history])
    prompt_with_history = f"{history_prompt}\n{prompt}"
    # Step 5：查询GPT模型
    response = get_ans(prompt_with_history)
    # Step 6：将新的对话添加到历史记录中
    history.append((query, response))
    history_dict[scenename] = history
    # Step 7：高亮
    highlight = find_most_similar_sentences(response, [doc[0][0] for doc in top_k_documents])
    # Step 8：将数据保存到数据库
    qa_data = {
        'question': query,
        'answer': response,
        'context': json.dumps(context, ensure_ascii=False),
        'highlight': highlight,
        'top_scores': [doc[1] for doc in top_k_documents]  # Add this line to return the top BM25 scores
    }

    with open(r'E:\工作\LangchainQA\QA_record2.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(qa_data, ensure_ascii=False) + '\n')
    return {'content': response, 'documents': [(doc[0][0], doc[0][1], doc[0][2], doc[1]) for doc in top_k_documents],
            'highlight': highlight}


# load_all_data()
# scenename = 'IT系统使用向导'
# query = "公司的工单系统中如何新增用户？"
# result = get_answer(query, scenename)
# print(result)

