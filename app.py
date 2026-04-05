import streamlit as st

# 1. Config
st.set_page_config(page_title="AdSpy AI Global", page_icon="💎", layout="wide")

# 2. القاموس باللغات (مع إضافة باقات الاشتراك)
translations = {
    "English": {
        "sidebar_head": "🔐 Choose Your Plan",
        "monthly": "Basic: $25/Month",
        "quarterly": "Growth: $60/3 Months (Save 20%)",
        "yearly": "Pro: $180/Year (Save 40%)",
        "wa_msg": "I_want_to_subscribe_to_plan_",
        "tabs": ["🔍 Ad Analysis", "✍️ AI Copy", "🏗️ Web Builder", "🎬 Video Scripts"]
    },
    "Français": {
        "sidebar_head": "🔐 Choisissez votre Plan",
        "monthly": "Basique: 25$/Mois",
        "quarterly": "Croissance: 60$/3 Mois (-20%)",
        "yearly": "Pro: 180$/An (-40%)",
        "wa_msg": "Je_veux_m_abonner_au_plan_",
        "tabs": ["🔍 Analyse Pub", "✍️ Rédaction IA", "🏗️ Créateur Web", "🎬 Scripts Vidéo"]
    },
    "العربية": {
        "sidebar_head": "🔐 اختر باقة الاشتراك",
        "monthly": "الباقة الشهرية: 25 دولار/شهر",
        "quarterly": "باقة 3 أشهر: 60 دولار (وفر 20%)",
        "yearly": "الباقة السنوية: 180 دولار (وفر 40%)",
        "wa_msg": "اريد_الاشتراك_في_باقة_",
        "tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "🏗️ صانع المواقع", "🎬 سيناريو فيديو"]
    }
}

lang_choice = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
t = translations[lang_choice]

# 3. عرض الاشتراكات في القائمة الجانبية
with st.sidebar:
    st.header(t["sidebar_head"])
    
    plan = st.radio("Select Plan / اختر باقة:", [t["monthly"], t["quarterly"], t["yearly"]])
    
    st.divider()
    st.info("*💳 Bank Transfer (SWIFT):*")
    st.code("RIB: 007450000972130040048374\nSWIFT: BCWAMA BX", language="text")
    st.write("*Name:* ILHAM AMEZZARGOU")
    
    # تحديد رسالة الواتساب على حسب الباقة
    plan_name = plan.split(":")[0]
    wa_url = f"https://wa.me/212607573180?text={t['wa_msg']}{plan_name}"
    st.link_button("Confirm Payment on WhatsApp ✅", wa_url)

# 4. الواجهة الرئيسية (نفس ميزات النسخة السابقة)
st.title("AdSpy AI Global 🚀")
tabs = st.tabs(t["tabs"])

# ميزات فابور (تجريبية)
for i in [0, 1]:
    with tabs[i]:
        st.subheader(t["tabs"][i])
        st.text_area("Input:", key=f"f_{i}")
        st.button("Analyze", key=f"fb_{i}")

# ميزات الـ PRO
for i in [2, 3]:
    with tabs[i]:
        if 'is_pro' in st.session_state and st.session_state.is_pro:
            st.success("Unlocked ✅")
        else:
            st.warning("🔒 PRO Feature")
            st.link_button("Upgrade Now", wa_url)

# تفعيل الكود (Manual Activation)
st.sidebar.divider()
key = st.sidebar.text_input("License Key:", type="password")
if st.sidebar.button("Activate"):
    if key == "GLOBAL_PRO_2026":
        st.session_state.is_pro = True
        st.balloons()
