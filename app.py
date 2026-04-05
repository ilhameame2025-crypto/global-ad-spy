import streamlit as st
import time

# إعدادات الصفحة والستايل (الزواقع)
st.set_page_config(page_title="AdSpy AI Global", page_icon="🚀", layout="wide")

# كود لتغيير الألوان والشكل (Dark Mode & Professional Colors)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #0f0c29, #302b63, #24243e);
        color: white;
    }
    .stButton>button {
        background-color: #00d2ff;
        color: white;
        border-radius: 20px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #3a7bd5;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_content_allowed=True)

# نظام اللغات
if 'lang' not in st.session_state:
    st.session_state.lang = 'العربية'

with st.sidebar:
    st.header("🌐 Configuration")
    st.session_state.lang = st.selectbox("Language / اللغة", ["العربية", "Français", "English"])
    st.divider()
    st.markdown("### 👑 Premium Status")
    st.info("Dev: Ilham Amezzargou")
    st.caption("FST Marrakech - MSD Department")

# محتوى اللغات
content = {
    "العربية": {
        "title": "الذكاء العالمي للإعلانات",
        "tabs": ["تحليل معمق", "توليد نصوص", "ردود ذكية", "تفعيل الاشتراك"],
        "btn": "تحليل الآن",
        "pay": "تواصل معنا لتفعيل حسابك"
    },
    "Français": {
        "title": "AdSpy Intelligence Global",
        "tabs": ["Analyse", "Générateur", "Réponses", "Paiement"],
        "btn": "Lancer l'analyse",
        "pay": "Contactez-nous pour activer"
    },
    "English": {
        "title": "AdSpy AI Global Pro",
        "tabs": ["Deep Analysis", "AI Copywriting", "Smart Reply", "Activation"],
        "btn": "Run Analysis",
        "pay": "Contact support for activation"
    }
}

data = content[st.session_state.lang]
st.title(f"🚀 {data['title']}")

tab1, tab2, tab3, tab4 = st.tabs(data["tabs"])

with tab1:
    st.subheader(data["tabs"][0])
    ad_input = st.text_area("Paste here / حط النص هنا:", height=150)
    if st.button(data["btn"], key="btn1"):
        with st.spinner('AI is thinking...'):
            time.sleep(1.5)
            st.success("✅ النتيجة: الإعلان ممتاز تقنياً، لكن يحتاج لتركيز أكبر على فوائد المنتج.")

with tab2:
    st.subheader(data["tabs"][1])
    p_name = st.text_input("Product Name / اسم المنتج:")
    if st.button("Generate / توليد", key="btn2"):
        st.code(f"AI Written Ad: Get the best {p_name} today! Limited offer.")

with tab3:
    st.subheader(data["tabs"][2])
    q = st.text_input("Customer Question / سؤال الزبون:")
    if st.button("Get Reply / رد", key="btn3"):
        st.info("🤖 Reply: Hello! We have sent you a private message with all details.")

with tab4:
    st.header(data["tabs"][3])
    st.write(data["pay"])
    # رابط واتساب برقمك 0607573180
    wa_link = "https://wa.me/212607573180?text=Hello%20Ilham%20I%20want%20to%20subscribe"
    st.markdown(f'''
        <a href="{wa_link}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold;">
                WhatsApp : تفعيل الاشتراك ✅
            </div>
        </a>
    ''', unsafe_content_allowed=True)

st.divider()
st.caption("AdSpy AI v4.0 | Powered by Streamlit & Ilham's Logic")
