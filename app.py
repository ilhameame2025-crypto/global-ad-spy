import streamlit as st

# 1. Config
st.set_page_config(page_title="AdSpy AI Global", page_icon="🚀", layout="wide")

# 2. القاموس المطور بالميزات الجديدة
translations = {
    "English": {
        "sidebar_head": "🔐 Choose Your Plan",
        "monthly": "Basic: $25/Month",
        "quarterly": "Growth: $60/3 Months",
        "yearly": "Pro: $180/Year",
        "wa_msg": "I_want_to_subscribe_to_plan_",
        "tabs": ["🔍 Ad Analysis", "✍️ AI Copy", "🏗️ Temu-Style Builder", "🛠️ Tool Box"],
        "builder_head": "🏗️ AI Shop Builder (Temu Style)",
        "builder_desc": "Enter your product details to generate a professional store layout."
    },
    "Français": {
        "sidebar_head": "🔐 Choisissez votre Plan",
        "monthly": "Basique: 25$/Mois",
        "quarterly": "Croissance: 60$/3 Mois",
        "yearly": "Pro: 180$/An",
        "wa_msg": "Je_veux_m_abonner_au_plan_",
        "tabs": ["🔍 Analyse Pub", "✍️ Rédaction IA", "🏗️ Créateur Temu-Style", "🛠️ Boîte à outils"],
        "builder_head": "🏗️ Créateur de boutique IA",
        "builder_desc": "Générez un design pro pour vos produits en un clic."
    },
    "العربية": {
        "sidebar_head": "🔐 اختر باقة الاشتراك",
        "monthly": "الباقة الشهرية: 25 دولار/شهر",
        "quarterly": "باقة 3 أشهر: 60 دولار",
        "yearly": "الباقة السنوية: 180 دولار",
        "wa_msg": "اريد_الاشتراك_في_باقة_",
        "tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "🏗️ صانع متاجر (Temu)", "🛠️ صندوق الأدوات"],
        "builder_head": "🏗️ صانع المتاجر الذكي (ستايل Temu)",
        "builder_desc": "ادخل معلومات منتجك وصمم متجرك الاحترافي في ثوانٍ."
    }
}

lang_choice = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
t = translations[lang_choice]

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 3. Sidebar (Payment & Activation)
with st.sidebar:
    st.header(t["sidebar_head"])
    plan = st.radio("Plans:", [t["monthly"], t["quarterly"], t["yearly"]])
    st.divider()
    st.code("RIB: 007450000972130040048374\nSWIFT: BCWAMA BX", language="text")
    st.write("*Name:* ILHAM AMEZZARGOU")
    
    plan_name = plan.split(":")[0]
    wa_url = f"https://wa.me/212607573180?text={t['wa_msg']}{plan_name}"
    st.link_button("Confirm on WhatsApp ✅", wa_url)
    
    st.divider()
    key = st.text_input("License Key:", type="password")
    if st.button("Unlock PRO"):
        if key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.balloons()

# 4. Main Interface
st.title("AdSpy AI Global 💎")
tabs = st.tabs(t["tabs"])

# الميزات المجانية
for i in [0, 1]:
    with tabs[i]:
        st.subheader(t["tabs"][i])
        st.text_area("Input:", key=f"f_{i}")
        st.button("Run", key=f"fb_{i}")

# ميزة صانع المتاجر (PRO)
with tabs[2]:
    st.header(t["builder_head"])
    if st.session_state.is_pro:
        st.write(t["builder_desc"])
        p_name = st.text_input("Product Name / اسم المنتج")
        p_price = st.text_input("Price / الثمن")
        p_desc = st.text_area("Description / الوصف")
        
        if st.button("Generate Temu Layout"):
            st.divider()
            # محاكاة لشكل Temu
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image("https://via.placeholder.com/300", caption="Product Image")
            with col2:
                st.title(f"🔥 {p_name}")
                st.subheader(f"Price: {p_price} USD")
                st.write(f"✅ Free Shipping | ⭐⭐⭐⭐⭐ (4.9/5)")
                st.write(p_desc)
                st.button("Add to Cart (Demo Only)", type="primary")
                st.success("تم توليد التصميم! يمكنك نسخه لمتجرك.")
    else:
        st.warning("🔒 This feature is for PRO members only.")
        st.image("https://via.placeholder.com/800x300?text=Temu+Store+Builder+Preview")
        st.link_button("Upgrade to Unlock", wa_url)

# ميزة صندوق الأدوات (PRO)
with tabs[3]:
    st.header(t["tabs"][3])
    if st.session_state.is_pro:
        st.button("📦 Inventory Tracker")
        st.button("📈 Profit Calculator")
        st.button("📧 Email Marketing Scripts")
    else:
        st.warning("🔒 Upgrade to PRO to access all tools.")
   
