import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Global", page_icon="💎", layout="wide")

# 2. القاموس (عربية، فرنسية، إنجليزية) - حيدت تبويب المنتجات
translations = {
    "English": {
        "title": "AdSpy AI: Global E-com Success",
        "scarcity": "🔥 LIMITED: 50% OFF - Only 7 Slots Today!",
        "sidebar_head": "🔐 Unlock PRO Version",
        "price": "Now: $25/Month",
        "bank_info": "💳 Bank Transfer (SWIFT):",
        "wa_btn": "Get My Activation Code ✅",
        "tabs": ["🔍 Ad Insights", "✍️ AI Copywriter", "🏗️ Web Builder", "🎬 Video Scripts"]
    },
    "Français": {
        "title": "AdSpy AI: Succès E-com Global",
        "scarcity": "🔥 OFFRE: -50% Aujourd'hui!",
        "sidebar_head": "🔐 Activer la Version PRO",
        "price": "Prix: 25$/Mois",
        "bank_info": "💳 Virement Bancaire (SWIFT):",
        "wa_btn": "Obtenir mon code ✅",
        "tabs": ["🔍 Analyse Pub", "✍️ Rédaction IA", "🏗️ Créateur Web", "🎬 Scripts Vidéo"]
    },
    "العربية": {
        "title": "AdSpy AI: نجاح التجارة العالمية",
        "scarcity": "🔥 عرض خاص: خصم 50% متبقي 7 حسابات فقط!",
        "sidebar_head": "🔐 تفعيل النسخة الاحترافية",
        "price": "الثمن: 25 دولار/شهر",
        "bank_info": "💳 التحويل البنكي الدولي (SWIFT):",
        "wa_btn": "احصل على كود التفعيل ✅",
        "tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "🏗️ صانع المواقع", "🎬 سيناريو فيديو"]
    }
}

with st.sidebar:
    lang_choice = st.selectbox("🌐 Language", ["English", "Français", "العربية"])
    st.divider()

t = translations[lang_choice]

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 3. معلومات Bankalik (Attijari) - المصدر الوحيد للربح دابا
with st.sidebar:
    st.header(t["sidebar_head"])
    st.success(t["price"])
    st.info(f"*{t['bank_info']}*")
    st.code("RIB: 007450000972130040048374\nSWIFT: BCWAMA BX", language="text")
    st.write("*Name:* ILHAM AMEZZARGOU")
    
    # رابط الواتساب لتلقي التحويلات
    wa_url = f"https://wa.me/212607573180?text=I_want_to_activate_PRO_v32"
    st.link_button(t["wa_btn"], wa_url)
    
    st.divider()
    key = st.text_input("Enter License Key:", type="password")
    if st.button("Activate Now"):
        if key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.balloons()

# 4. الواجهة الرئيسية
st.title(t["title"])
st.error(t["scarcity"])

tabs = st.tabs(t["tabs"])

# الميزات المجانية (التبويب الأول والثاني)
for i in [0, 1]:
    with tabs[i]:
        st.subheader(t["tabs"][i])
        st.text_area("Input Data:", key=f"f_in_{i}")
        st.button("Start Analysis", key=f"f_bt_{i}")

# ميزات الـ PRO (التبويب الثالث والرابع)
for i in [2, 3]:
    with tabs[i]:
        if st.session_state.is_pro:
            st.subheader(f"✅ {t['tabs'][i]}")
            st.info("Professional Tool Unlocked.")
        else:
            st.warning("🔒 This Feature Requires PRO Membership")
            st.image("https://via.placeholder.com/800x250?text=Premium+Access+Only")
            st.link_button(t["wa_btn"], wa_url, key=f"p_bt_{i}")

st.divider()
st.caption("AdSpy Global v32.0 | Clean Business Edition | By Ilham")
