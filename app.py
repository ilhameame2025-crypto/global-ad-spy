import streamlit as st

# 1. Config
st.set_page_config(page_title="AdSpy AI Global", page_icon="🚀", layout="wide")

# 2. القاموس (حيدت تيمو وعوضتها بصانع الصفحات الذكي)
translations = {
    "English": {
        "title": "AdSpy AI: Pro Marketing Suite",
        "sidebar_head": "🔐 Premium Subscription",
        "plans": ["Basic: $25/Mo", "Growth: $60/3 Mo", "Elite: $180/Year"],
        "tabs": ["🔍 Analysis", "✍️ Copywriter", "🏗️ AI Store Builder", "🎬 Video Tools"],
        "builder_head": "🏗️ AI Landing Page Generator",
        "builder_desc": "Convert product data into a professional high-converting layout."
    },
    "Français": {
        "title": "AdSpy AI: Suite Marketing Pro",
        "sidebar_head": "🔐 Abonnement Premium",
        "plans": ["Basique: 25$/Mois", "Croissance: 60$/3 Mois", "Elite: 180$/An"],
        "tabs": ["🔍 Analyse", "✍️ Rédaction IA", "🏗️ Créateur de Page", "🎬 Vidéo Tools"],
        "builder_head": "🏗️ Générateur de Page de Vente",
        "builder_desc": "Transformez vos données produits en un design professionnel."
    },
    "العربية": {
        "title": "AdSpy AI: منصة المقاولين المحترفين",
        "sidebar_head": "🔐 باقات الاشتراك",
        "plans": ["باقة شهر: 25 دولار", "باقة 3 أشهر: 60 دولار", "باقة سنة: 180 دولار"],
        "tabs": ["🔍 تحليل", "✍️ كاتب المحتوى", "🏗️ صانع الصفحات الذكي", "🎬 أدوات الفيديو"],
        "builder_head": "🏗️ مولد صفحات الهبوط الاحترافية",
        "builder_desc": "حول معلومات منتجك إلى تصميم احترافي عالي التحويل في ثوانٍ."
    }
}

lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
t = translations[lang]

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 3. Sidebar
with st.sidebar:
    st.header(t["sidebar_head"])
    plan = st.radio("Choose Plan:", t["plans"])
    st.divider()
    st.info("*💳 Transfer (SWIFT):*")
    st.code("RIB: 007450000972130040048374\nSWIFT: BCWAMA BX")
    st.write("*Name:* ILHAM AMEZZARGOU")
    
    wa_url = f"https://wa.me/212607573180?text=I_want_to_join_the_{plan.split(':')[0]}"
    st.link_button("Confirm on WhatsApp ✅", wa_url)
    
    st.divider()
    key = st.text_input("License Key:", type="password")
    if st.button("Unlock"):
        if key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.balloons()

# 4. Main
st.title(t["title"])
tabs = st.tabs(t["tabs"])

# ميزات فابور
for i in [0, 1]:
    with tabs[i]:
        st.subheader(t["tabs"][i])
        st.text_area("Input:", key=f"inp_{i}")
        st.button("Run AI", key=f"btn_{i}")

# صانع الصفحات الاحترافي (PRO)
with tabs[2]:
    st.header(t["builder_head"])
    if st.session_state.is_pro:
        st.write(t["builder_desc"])
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Product Name")
            price = st.text_input("Price")
        with c2:
            img = st.text_input("Image URL")
        
        desc = st.text_area("Product Benefits")
        
        if st.button("Build Landing Page"):
            st.divider()
            st.subheader(f"🚀 Preview: {name}")
            col_p1, col_p2 = st.columns([1, 2])
            with col_p1:
                st.image(img if img else "https://via.placeholder.com/300")
            with col_p2:
                st.title(f"{name}")
                st.header(f"Price: ${price}")
                st.write(desc)
                st.button("Check Out", type="primary")
    else:
        st.warning("🔒 PRO Feature: Get a professional landing page generator.")
        st.image("https://via.placeholder.com/800x300?text=Landing+Page+Generator+Preview")
        st.link_button("Upgrade to PRO", wa_url)

# ميزات الـ PRO الأخرى
with tabs[3]:
    st.header(t["tabs"][3])
    if not st.session_state.is_pro:
        st.warning("🔒 Subscribtion Required")
