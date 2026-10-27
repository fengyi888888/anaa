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
system_prompt = """"
你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用 ❤ 🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容，要充分体现伴侣的性格特征
            伴侣性格：
                    %s
            你必须严格遵守上述规则来回复用户。
"""
#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages=[]
 #昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name="小甜甜"
#性格
if "personality" not in st.session_state:
    st.session_state.personality="活泼开朗的东北姑娘"


#展示聊天消息
for message in st.session_state.messages:
        if message["role"]=="user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])

#创建了与Ai大模型交换的客户端对象(DEEPSEEK_API_KEY 环境变量的名字,值就是DeepSeek的 Api_key)
client = OpenAI(
    api_key= os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#侧边栏
# st.sidebar.subheader("伴侣信息")
# nick_name=st.sidebar.text_input("请输入伴侣的名字")

#侧边栏 --- with streamlit 中上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")

    nick_name=st.text_input("请输入伴侣的名字",value=st.session_state.nick_name)
    if nick_name is not None:
        st.session_state.nick_name=nick_name


    st.subheader("伴侣性格")
    personality=st.text_area("请输入伴侣的性格特征",value=st.session_state.personality)
    if personality is not None:
        st.session_state.personality=personality



#聊天消息的输入框
prompt=st.chat_input("请输入你要问的问题")
if prompt: #字符串会自动转换为bool值，如果字符串不为空，则为True，否则为False
    st.chat_message("user").write(prompt)
    print("------------->调用AI大模型",prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})
    #与AI大模型进行交换
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
                     {"role": "system", "content":  system_prompt %(st.session_state.nick_name,st.session_state.personality)   },
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

