import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="stream入门",
    page_icon="🧊",
    #布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",

    menu_items={

    }
)

#大标题
st.title("Stream 入门展示")
st.header("Stream  一级标题")
st.subheader("Stream  二级标题")

#段落
st.write("\n\n帅哥在这里想跟你聊聊一种非常惹人怜爱的猫咪——布偶猫！它们就像童话里走出来的精灵，拥有着一双圆溜溜、如同碧玉般的大眼睛，眼神纯净又充满好奇。最标志性的就是那身柔软浓密、像棉花糖一样蓬松的长毛被毛，尤其是颈部那一圈更显眼的“围巾”，简直是萌翻全场！它们体型中等偏小，身体比例匀称，给人一种圆润舒适的感觉。\n\n布偶猫原产于美国，以其乖巧温顺的性格而闻名。它们性情稳定、安静内敛，不像一些品种那样好动吵闹，特别适合喜欢宁静氛围的家庭饲养。虽然外表看起来有点憨态可掬，但它们其实非常聪明，并且对人有着极强的亲和力，会用撒娇和依赖来表达爱意，是出了名的“粘人精”。不过，布偶猫有个特点就是睡得特别多，一天中有一半时间都在呼呼大睡呢！\n\n总的来说，布偶猫是一种外表甜美、性格温顺且适应性强的家庭伴侣动物。它们那独特的外貌和安静优雅的气质，让无数爱猫人士为之倾倒。如果你正在寻找一个毛茸茸的小天使来陪伴你，布偶猫绝对是一个值得考虑的选择哦！")

#图片
st.image("./resources/huiyuan.png",width=500)
# st.image("resources/huiyuan.png",width=500)


#音频
st.audio("./resources/封茗囧菌 - 东京不太热 (Single Version).flac",)

#视频

st.video("./resources/yjwj.mp4")

#Logo
st.logo("./resources/logo.png")

#表格
studentdata={
    "姓名": ["小明","小红","小李","小白"],
    "学号":["20009","20008","2007","2006"],
    "数学":[98,68,76,78],
    "语文":[96,78,86,88],
    "英语":[78,76,78,79]

}
st.table(studentdata)


#输入框

name=st.text_input("请输入姓名")
st.write(f"你输入的姓名是:{name}")


password=st.text_input("请输入密码",type="password")
st.write(f"你输入的密码是:{password}")


#单选按钮
gender=st.radio(
    "请输入你的性别",
    ["男","女","未知"],index=1
)
st.write(f"你的性别是{gender}")