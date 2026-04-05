import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Global", page_icon="🚀", layout="wide")

# 2. القاموس الكامل والمحدث (عربية، فرنسية، إنجليزية)
translations = {
    "English": {
        "title": "AdSpy AI Global 💎",
        "scarcity": "🔥 URGENT: 50% OFF - Only 7 Slots Left Today!",
        "sidebar_head": "🔐 Choose Your Plan",
        "monthly": "Basic: $25/Month",
        "quarterly": "Growth: $60/3 Months",
        "yearly": "Pro: $180/Year",
        "wa_msg": "I_want_to_subscribe_to_plan_",
        "tabs": ["🔍 Ad Analysis", "✍️ AI Copy", "🏗️ AI Shop Builder", "🎬 Video Scripts"],
        "builder_head": "🏗️ AI Shop Builder (Temu Style)",
        "builder_desc": "Enter product details to generate a professional store layout."
    },
    "Français": {
        "title": "AdSpy AI Global 💎",
        "scarcity": "🔥 OFFRE: -50% Aujourd'hui!",
        "sidebar_head": "🔐 Choisissez votre Plan",
        "monthly": "Basique: 25$/Mois",
        "quarterly": "Croissance: 60$/3 Mois",
        "yearly": "Pro: 180$/An",
        "wa_msg": "Je_veux_m_abonner_au_plan_",
        "tabs": ["🔍 Analyse Pub", "✍️ Rédaction IA", "🏗️ Créateur Boutique", "🎬 Scripts Vidéo"],
        "builder_head": "🏗️ Créateur de boutique IA",
        "builder_desc": "Générez un design pro pour vos produits en un clic."
    },
    "العربية": {
        "title": "AdSpy AI Global 💎",
        "scarcity": "🔥 عرض خاص: خصم 50% متبقي 7 حسابات فقط!",
        "sidebar_head": "🔐 اختر باقة الاشتراك",
        "monthly": "الباقة الشهرية: 25 دولار/شهر",
        "quarterly": "باقة 3 أشهر: 60 دولار",
        "yearly": "الباقة السنوية: 180 دولار",
        "wa_msg": "اريد_الاشتراك_في_باقة_",
        "tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "🏗️ صانع المتاجر (تيمو)", "🎬 سيناريو فيديو"],
        "builder_head": "🏗️ صانع المتاجر الذكي (ستايل Temu)",
        "builder_desc": "ادخل معلومات منتجك وصمم متجرك الاحترافي في ثوانٍ."
    }
}

# اختيار اللغة
lang_choice = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
t = translations[lang_choice]

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 3. القائمة الجانبية (الاشتراكات + معلومات البنك)
with st.sidebar:
    st.header(t["sidebar_head"])
    plan = st.radio("Plans:", [t["monthly"], t["quarterly"], t["yearly"]])
    st.divider()
    st.info("*💳 Bank Transfer (SWIFT):*")
    st.code("RIB: 007450000972130040048374\nSWIFT: BCWAMA BX", language="text")
    st.write("*Name:* ILHAM AMEZZARGOU")
    
    plan_name = plan.split(":")[0]
    wa_url = f"https://wa.me/212607573180?text={t['wa_msg']}{plan_name}"
    st.link_button("Confirm on WhatsApp ✅", wa_url)
    
    st.divider()
    key = st.text_input("License Key:", type="password")
    if st.button("Unlock PRO Access"):
        if key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.balloons()

# 4. الواجهة الرئيسية
st.title(t["title"])
st.error(t["scarcity"])

tabs = st.tabs(t["tabs"])

# ميزات فابور (تحليل الإعلانات + كاتب المحتوى)
for i in [0, 1]:
    with tabs[i]:
        st.subheader(t["tabs"][i])
        st.text_area("Input:", key=f"f_in_{i}")
        st.button("Run Process", key=f"f_bt_{i}")

# ميزة صانع المتاجر PRO (Temu Style)
with tabs[2]:
    st.header(t["builder_head"])
    if st.session_state.is_pro:
        st.write(t["builder_desc"])
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            p_name = st.text_input("Product Name / اسم المنتج")
            p_price = st.text_input("Price / الثمن")
        with col_in2:
            p_img = st.text_input("Image URL / رابط صورة المنتج")
        
        p_desc = st.text_area("Description / الوصف")
        
        if st.button("Generate Layout"):
            st.divider()
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image(p_img if p_img else "https://via.placeholder.com/300", use_container_width=True)
            with c2:
                st.title(f"🔥 {p_name}")
                st.subheader(f"Price: {p_price} USD")
                st.markdown("⭐ 4.9/5 | 📦 Free Global Shipping")
                st.write(p_desc)
                st.button("Buy Now", type="primary")
    else:
        st.warning("🔒 This tool is for PRO members only.")
        st.image("https://via.placeholder.com/800x300?text=Premium+Store+Builder+Preview")
        st.link_button("Upgrade Now", wa_url)

# ميزة سيناريو الفيديو PRO
with tabs[3]:
    st.header(t["tabs"][3])
    if st.session_state.is_pro:
        st.text_area("Script Details:")
        st.button("Generate AI Script")
    else:
        st.warning("🔒 Upgrade to unlock Video Scripts.")

st.divider()
st.caption("AdSpy Global v34.0 | Professional Edition | Dev: Ilham")
