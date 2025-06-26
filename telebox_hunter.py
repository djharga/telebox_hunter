import streamlit as st
from googlesearch import search
import pyttsx3

# إعدادات واجهة
st.set_page_config(page_title="Telebox Web Hunter", layout="centered", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
      body {background-color:#121212; color:#e0e0e0;}
      .stButton>button { background:linear-gradient(to right,#00c6ff,#0072ff); color:white; }
      .stTextInput>div>input {background:#223; color:white;}
      a {color:#4da6ff;}
    </style>
""", unsafe_allow_html=True)
st.title("🕵️‍♂️ Telebox Web Hunter")

# مربع البحث
default_keywords = ["روابط telebox", "Telebox links", "iPlayer روابط", "Telebox أفلام"]
choice = st.selectbox("اختر أو اكتب كلمات البحث:", default_keywords + ["<اكتب بنفسك>"])
if choice == "<اكتب بنفسك>":
    query = st.text_input("📌 اكتب كلمة البحث هنا:", "")
else:
    query = choice

# زر البحث
if st.button("🔍 ابحث الآن"):
    if not query.strip():
        st.warning("من فضلك اكتب أو اختر كلمة بحث.")
    else:
        st.info(f"جاري البحث عن روابط لكلمة: **{query}**")
        links = []
        for url in search(query, num_results=20):
            lower = url.lower()
            if "telebox" in lower or "iplayer" in lower:
                links.append(url)

        if links:
            st.success(f"تم العثور على {len(links)} روابط:")
            for link in links:
                st.markdown(f"- [🔗 {link}]({link})")
        else:
            st.error("لم تُعثر على روابط تحتوي على telebox أو iPlayer.")

# زر القراءة الصوتية
if st.button("🔊 اقرأ النتائج"):
    engine = pyttsx3.init()
    engine.say("تم البحث عن روابط Telebox و iPlayer، اضغط على النتائج لتدخل عليها مباشرة.")
    engine.runAndWait()
              
