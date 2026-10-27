import streamlit as st
import os
from openai import OpenAI
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🐲",
    #布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",

    menu_items={}
)
#大标题
st.title("AI智能伴侣")

#logo
st.logo("./resources/logo.png")

#系统提示词
system_prompt=("你是一个AI助手,你的名字是小甜甜,请使用温柔的语气回答客户的问题")
#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages=[]
#展示聊天消息
for message in st.session_state.messages:
        if message["role"]=="user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])

#创建了与Ai大模型交换的客户端对象(DEEPSEEK_API_KEY 环境变量的名字,值就是DeepSeek的 Api_key)
client = OpenAI(
    api_key= "ollama",
    base_url="http://localhost:11434/v1")
#聊天消息的输入框

prompt=st.chat_input("请输入你要问的问题")
if prompt: #字符串会自动转换为bool值，如果字符串不为空，则为True，否则为False
    st.chat_message("user").write(prompt)
    print("------------->调用AI大模型",prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})
    #与AI大模型进行交换
    response = client.chat.completions.create(
        model="mikepfunk28/deepseekq3_coder:latest",
        messages=[
                     {"role": "system", "content":  system_prompt},
                      *st.session_state.messages
                 ] ,
        stream=True,
    )
    #保存聊天消息

    # 输出大模型返回的结果
    #非流式输出的响应方式

    # print("------------->AI大模型返回的结果", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
    #
    #流式输出的响应方式
    response_message=st.empty()
    full_response=""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content =chunk.choices[0].delta.content
            full_response+=content
            response_message.chat_message("assistant").write(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

