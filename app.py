import streamlit as st
import time

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="AdSpy AI Global", page_icon="🚀", layout="wide")

# 2. نظام اختيار اللغات
if 'lang' not in st.session_state:
    st.session_state.lang = 'العربية'

# 3. تصميم الواجهة (الألوان والزواقع) - CSS
st.markdown("""
    <style>
    /* خلفية الموقع */
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 100%);
        color: #ffffff;
    }
    /* تنسيق الأزرار */
    .stButton>button {
        background-color: #4e73df;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #224abe;
        border: 1px solid white;
    }
    /* تنسيق التبويبات */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #3a3a52;
        border-radius: 10px 10px 0px 0px;
        color: white;
        padding: 10px;
    }
    </style>
    """, unsafe_content_allowed=True)

# 4. القائمة الجانبية
with st.sidebar:
    st.markdown("### 🌐 Language / اللغة")
    st.session_state.lang = st.selectbox("Select Language", ["العربية", "Français", "English"])
    st.divider()
    st.markdown("### 💎 Account Status")
    st.success("User: Ilham (MSD)")
    st.info("Version: 4.0 Pro")

# 5. محتوى اللغات
translations = {
    "العربية": {
        "title": "الذكاء العالمي للإعلانات 🚀",
        "tabs": ["تحليل الإعلان", "كتابة إعلان", "رد ذكي", "الاشتراك"],
        "welcome": "مرحباً إلهام! المنصة جاهزة للعمل بأحدث تقنيات الذكاء الاصطناعي.",
        "btn": "بدء التحليل"
    },
    "Français": {
        "title": "AdSpy Intelligence 🇫🇷",
        "tabs": ["Analyse", "Rédaction", "Réponse IA", "Abonnement"],
        "welcome": "Bienvenue Ilham! La plateforme est prête avec l'IA.",
        "btn": "Lancer l'analyse"
    },
    "English": {
        "title": "AdSpy Global AI 🌍",
        "tabs": ["Ad Analysis", "AI Writing", "Smart Reply", "Subscription"],
        "welcome": "Welcome Ilham! Your AI-powered dashboard is ready.",
        "btn": "Run Analysis"
    }
}

t = translations[st.session_state.lang]

# 6. واجهة المستخدم الرئيسية
st.title(t["title"])
st.write(f"✨ {t['welcome']}")

tab1, tab2, tab3, tab4 = st.tabs(t["tabs"])

with tab1:
    st.subheader(t["tabs"][0])
    txt = st.text_area("Input / النص :", height=150, key="area1")
    if st.button(t["btn"], key="b1"):
        with st.spinner('AI Thinking...'):
            time.sleep(1.5)
            st.success("✅ تم التحليل بنجاح!")

with tab2:
    st.subheader(t["tabs"][1])
    prod = st.text_input("Product Name / اسم المنتج:", key="in1")
    if st.button("Generate / توليد", key="b2"):
        st.code(f"Ad: High quality {prod} for you!")

with tab3:
    st.subheader(t["tabs"][2])
    quest = st.text_input("Customer Comment / تعليق:", key="in2")
    if st.button("Get Reply / رد", key="b3"):
        st.info("🤖 AI Reply: Thank you! We will contact you soon.")

with tab4:
    st.header(t["tabs"][3])
    st.write("للحصول على المميزات الكاملة، يرجى تفعيل حسابك:")
    # زر واتساب آمن بدون مشاكل برمجية
    wa_url = "https://wa.me/212607573180?text=Hello%20Ilham%20Activate%20Pro"
    st.markdown(f'''
        <a href="{wa_url}" target="_blank" style="text-decoration:none;">
            <div style="background-color:#25D366; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold; font-size:20px;">
                WhatsApp : تفعيل الاشتراك ✅
            </div>
        </a>
    ''', unsafe_content_allowed=True)

st.divider()
st.caption("AdSpy Pro v4.0 | Created by Ilham (FST Marrakech)")
