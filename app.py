import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Global", page_icon="💎", layout="wide")

# 2. القاموس المطور بالرسائل التسويقية (الإغراءات)
translations = {
    "English": {
        "title": "AdSpy AI: Pro Marketing Suite 🚀",
        "social_proof": "⭐ Joined by 1,200+ Successful Entrepreneurs",
        "scarcity": "🔥 FLASH SALE: -50% OFF Ends Soon!",
        "sidebar_head": "🔐 Choose Your Empire Plan",
        "plans": ["Basic: $25/Mo", "Growth: $60/3 Mo (Most Popular)", "Elite: $180/Year"],
        "tabs": ["🔍 Ad Spy", "✍️ AI Copy", "🏗️ AI Store Builder", "🎬 Video Tools"],
        "wa_msg": "I_want_to_join_the_elite_group_"
    },
    "Français": {
        "title": "AdSpy AI: Suite Marketing Pro 🚀",
        "social_proof": "⭐ Rejoint par plus de 1 200 entrepreneurs",
        "scarcity": "🔥 OFFRE ÉCLAIR: -50% finit bientôt !",
        "sidebar_head": "🔐 Choisissez votre Plan",
        "plans": ["Basique: 25$/Mois", "Croissance: 60$/3 Mois", "Elite: 180$/An"],
        "tabs": ["🔍 Analyse", "✍️ Rédaction IA", "🏗️ Créateur de Page", "🎬 Vidéo Tools"],
        "wa_msg": "Je_veux_rejoindre_le_groupe_"
    },
    "العربية": {
        "title": "AdSpy AI: منصة المقاولين المحترفين 🚀",
        "social_proof": "⭐ انضم إلينا الآن أكثر من 1,200 مقاول ناجح",
        "scarcity": "🔥 عرض حصري: خصم 50% ينتهي قريباً جداً!",
        "sidebar_head": "🔐 اختر باقتك وابدأ النجاح",
        "plans": ["باقة الانطلاق: 25 دولار/شهر", "باقة النمو: 60 دولار (الأكثر طلباً)", "باقة النخبة: 180 دولار/سنة"],
        "tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "🏗️ صانع الصفحات الذكي", "🎬 أدوات الفيديو"],
        "wa_msg": "اريد_الانضمام_لمجتمع_المقاولين_"
    }
}

lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
t = translations[lang]

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 3. Sidebar (الإغراءات ومعلومات البنك)
with st.sidebar:
    st.markdown(f"### {t['sidebar_head']}")
    st.success(t['social_proof']) # إغراء "أكثر من 1000 مقاول"
    
    plan = st.radio("Select Plan:", t["plans"])
    st.divider()
    
    st.error(t['scarcity']) # إغراء الوقت (Scarcity)
    
    st.info("*💳 Bank Transfer (SWIFT):*")
    st.code("RIB: 007450000972130040048374\nSWIFT: BCWAMA BX")
    st.write("*Account:* ILHAM AMEZZARGOU")
    
    wa_url = f"https://wa.me/212607573180?text={t['wa_msg']}{plan.split(':')[0]}"
    st.link_button("Confirm Payment on WhatsApp ✅", wa_url)
    
    st.divider()
    key = st.text_input("Enter License Key:", type="password")
    if st.button("Activate My Account"):
        if key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.balloons()

# 4. Main Page
st.title(t["title"])
st.warning(t['social_proof']) # تذكير بالإغراء في الصفحة الرئيسية

tabs = st.tabs(t["tabs"])

# الميزات المجانية
for i in [0, 1]:
    with tabs[i]:
        st.subheader(t["tabs"][i])
        st.text_area("Input Data:", key=f"inp_{i}")
        st.button("Analyze Now", key=f"btn_{i}")

# صانع الصفحات (PRO)
with tabs[2]:
    st.header(t["tabs"][2])
    if st.session_state.is_pro:
        st.write("Convert your product info into a high-converting landing page.")
        # ... (كود صانع الصفحات اللي درنا قبل)
    else:
        st.warning("🔒 This feature is for PRO members. Join 1,200+ professionals today!")
        st.image("https://via.placeholder.com/1000x300?text=Premium+Landing+Page+Preview")
        st.link_button("Get Started Now", wa_url)

st.divider()
st.caption("AdSpy Global v37.0 | Empowering Entrepreneurs | Dev: Ilham")
