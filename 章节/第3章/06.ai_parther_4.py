

import streamlit as st
import os

from openai import OpenAI
import datetime
import json




#保存会话数据
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "personality": st.session_state.personality,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        # 如果sessions不存在,则创建一个文件夹
        if not os.path.exists("sessions"):
            os.makedirs("sessions")
        # 保存会话数据到文件
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)


#生成会话标志函数
def generate_session_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


#加载所有会话列表信息
def load_sessions():
    session_list=[]
    #加载sessions目录的文件
    if os.path.exists("sessions"):
        file_list=os.listdir("sessions")
        for file in file_list:
            if file.endswith(".json"):
                session_list.append(file[:-5])
    return  session_list

#加载指定的历史会话
def  load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            # 读取会话数据
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["messages"]
                st.session_state.personality = session_data["personality"]
                st.session_state.current_session = session_name
    except Exception as e:
        st.error("加载会话失败")

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
st.logo("🐷")

#系统提示词
system_prompt = """
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

#会话的标志
if "current_session" not in st.session_state:
   st.session_state.current_session=generate_session_name()

st.text(f"会话昵称:{st.session_state.current_session}")
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
    st.subheader("AI控制面板 ")
    if st.button("新建会话",width="stretch",icon="✏"):
        #1.保持当前会话信息
        save_session()

        # 2.创建新的会话数据
        if  st.session_state.messages:#(如果聊天信息为空则是ture,否则是false)
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()

            st.rerun()  # 重新运行当前页面
    st.text("历史会话")
    session_list = load_sessions()
    for session in session_list:
        column1, column2 = st.columns([4, 1])
        with column1:
            pass
        with column2:
            if st.button("", width="stretch", icon="❌️", key=f"delete{session}"):
                pass






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
#保持当前会话
    save_session()
