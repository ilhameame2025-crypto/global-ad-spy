import streamlit as st
import time

# إعدادات الصفحة مع الثيم الاحترافي
st.set_page_config(
    page_title="AdSpy AI Global Pro", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# نظام اختيار اللغات (عربية، فرنسية، إنجليزية)
if 'lang' not in st.session_state:
    st.session_state.lang = 'العربية'

# تنسيق الموقع بالألوان (CSS) - "زواقع" بصرية
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    .stTextArea>div>div>textarea {
        background-color: #262730;
        color: white;
    }
    </style>
    """, unsafe_content_allowed=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.title("إعدادات المنصة")
    st.session_state.lang = st.selectbox("Language / اللغة", ["العربية", "Français", "English"])
    st.write("---")
    st.markdown("### 💎 العضوية الممتازة")
    st.info("المطور: إلهام (طالبة MSD)")
    st.write("التحديث: v3.0 (2026)")

# قاعدة البيانات اللغوية
content = {
    "العربية": {
        "title": "AdSpy AI: منصة الذكاء العالمي 🚀",
        "tabs": ["تحليل إعلان", "توليد إعلان", "رد ذكي", "الاشتراك"],
        "welcome": "مرحباً إلهام! المنصة جاهزة لتحليل إعلاناتك العالمية.",
        "analyze_label": "أدخل نص الإعلان للتحليل العميق:",
        "gen_label": "اكتب اسم المنتج وسنقوم بكتابة الإعلان:",
        "reply_label": "أدخل تعليق الزبون وسنرد عليه بذكاء:",
        "pay_title": "تفعيل النسخة الاحترافية",
        "wa_text": "تواصل عبر واتساب للتفعيل ✅"
    },
    "Français": {
        "title": "AdSpy AI: Intelligence Marketing 🇫🇷",
        "tabs": ["Analyser", "Générer", "Réponse IA", "Paiement"],
        "welcome": "Bienvenue Ilham! Analysez et créez des publicités avec l'IA.",
        "analyze_label": "Collez le texte de la publicité ici :",
        "gen_label": "Quel produit voulez-vous vendre ?",
        "reply_label": "Commentaire du client :",
        "pay_title": "Activer la Version Premium",
        "wa_text": "Contactez-nous sur WhatsApp ✅"
    },
    "English": {
        "title": "AdSpy AI: Global Intelligence 🌍",
        "tabs": ["Analyze", "Generate", "AI Reply", "Payment"],
        "welcome": "Welcome Ilham! Scale your business using AI analysis.",
        "analyze_label": "Paste the ad copy here for analysis:",
        "gen_label": "What product are you selling?",
        "reply_label": "Customer comment/question:",
        "pay_title": "Unlock Full AI Access",
        "wa_text": "Contact Support via WhatsApp ✅"
    }
}

data = content[st.session_state.lang]
st.title(data["title"])
st.write(f"🔔 {data['welcome']}")

tab1, tab2, tab3, tab4 = st.tabs(data["tabs"])

with tab1:
    st.subheader(data["tabs"][0])
    ad_txt = st.text_area(data["analyze_label"], height=150)
    if st.button("Start / ابدأ", key="btn1"):
        with st.spinner('Processing...'):
            time.sleep(2)
            st.success("✅ النتيجة: الإعلان يحتاج إلى تحسين في العنونة لجذب الانتباه.")

with tab2:
    st.subheader(data["tabs"][1])
    prod_name = st.text_input(data["gen_label"])
    if st.button("Write / اكتب", key="btn2"):
        st.code(f"Ad Copy for {prod_name}:\nBest {prod_name} in the market! High quality and fast delivery. Order now!")

with tab3:
    st.subheader(data["tabs"][2])
    comm = st.text_input(data["reply_label"])
    if st.button("Generate Reply / رد", key="btn3"):
        st.info(f"🤖 الرد: شكراً على تواصلكم بخصوص {comm}. سيتم الرد عليكم في الخاص فوراً.")

with tab4:
    st.header("💰 " + data["pay_title"])
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📊 خطط الاشتراك:")
        st.write("📍 شهري: 150 درهم")
        st.write("📍 سنوي: 1000 درهم")
    
    with col2:
        # تصحيح غلط الصورة 660ff716
        whatsapp_url = "https://wa.me/212607573180?text=Hello%20Ilham%20I%20want%20to%20activate%20AdSpy%20Pro"
        st.markdown(f'<a href="{whatsapp_url}" target="_blank" style="text-decoration: none;"><div style="background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 18px;">{data["wa_text"]}</div></a>', unsafe_content_allowed=True)

st.divider()
st.caption("AdSpy AI v3.0 | Precision Engineering for MSD Students")
