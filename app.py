import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Global", page_icon="🚀", layout="wide")

# 2. اللغات فوق كلشي
lang = st.selectbox("🌐 Choose Language / اختر اللغة", ["English", "العربية", "Français"])

# 3. نظام الاشتراك
if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 4. ترجمة النصوص مع "الإغراءات"
translations = {
    "English": {
        "title": "AdSpy AI: The #1 Tool for Entrepreneurs",
        "offer": "🔥 LIMITED OFFER: 50% OFF for the next 7 accounts!",
        "free_tabs": ["🔍 Ad Analysis", "✍️ AI Copywriter", "💡 Product Ideas", "📊 Sales Tracker"],
        "pro_tab": "🏗️ AI Web Builder (PRO)",
        "sidebar_title": "Unlock Premium Access",
        "price": "Only $25/Month (was $50)",
        "rib_msg": "Transfer to RIB: 007450000972130040048374",
        "wa_btn": "Send Receipt to Activate ✅",
        "key_placeholder": "Enter your License Key"
    },
    "العربية": {
        "title": "AdSpy AI: الأداة رقم #1 للمقاولين",
        "offer": "🔥 عرض محدود: خصم 50% متبقي 7 حسابات فقط لهذا اليوم!",
        "free_tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "💡 أفكار منتجات", "📊 تتبع المبيعات"],
        "pro_tab": "🏗️ صانع المواقع (PRO)",
        "sidebar_title": "تفعيل الاشتراك الممتاز",
        "price": "250 درهم فقط/شهر (بدل 500 درهم)",
        "rib_msg": "التحويل إلى RIB: 007450000972130040048374",
        "wa_btn": "إرسال التوصيل لتفعيل الحساب ✅",
        "key_placeholder": "أدخل كود التفعيل هنا"
    },
    "Français": {
        "title": "AdSpy AI: L'outil #1 pour les entrepreneurs",
        "offer": "🔥 OFFRE LIMITÉE: -50% pour les 7 prochains comptes !",
        "free_tabs": ["🔍 Analyse Pub", "✍️ Copywriter AI", "💡 Idées Produits", "📊 Tracker Ventes"],
        "pro_tab": "🏗️ Constructeur Web (PRO)",
        "sidebar_title": "Débloquer l'accès Premium",
        "price": "Seulement 25$/Mois (au lieu de 50$)",
        "rib_msg": "Virement vers RIB: 007450000972130040048374",
        "wa_btn": "Envoyer le reçu pour activer ✅",
        "key_placeholder": "Entrez votre clé de licence"
    }
}

t = translations[lang]

# 5. القائمة الجانبية (Sidebar) بتصميم جذاب
with st.sidebar:
    st.header(t["sidebar_title"])
    st.success(f"💎 {t['price']}")
    st.info(t["rib_msg"])
    st.write("*Name:* ILHAM AMEZZARGOU")
    
    # زر الواتساب لإرسال التوصيل
    wa_url = f"https://wa.me/212607573180?text=Hello_Ilham_I_paid_for_AdSpy_Pro"
    st.link_button(t["wa_btn"], wa_url)
    
    st.divider()
    # خانة إدخال الكود
    license_key = st.text_input(t["key_label"] if "key_label" in t else t["key_placeholder"], type="password")
    if st.button("Unlock PRO Access"):
        if license_key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.balloons()
            st.success("Welcome to PRO! ✅")

# 6. الواجهة الرئيسية
st.title(t["title"])
st.error(t["offer"]) # شريط الإغراء (تخفيض 50%)

# التبويبات (4 فابور + 1 برو)
tabs = st.tabs(t["free_tabs"] + [t["pro_tab"]])

for i in range(4):
    with tabs[i]:
        st.subheader(t["free_tabs"][i])
        st.info("Feature available in free version / هذه الميزة متاحة مجاناً")
        st.text_area(f"Input for {t['free_tabs'][i]}:", height=150)
        st.button(f"Start {t['free_tabs'][i]}")

with tabs[4]: # صانع المواقع PRO
    if st.session_state.is_pro:
        st.header("🏗️ AI Landing Page Builder")
        st.write("Welcome, Ilham! Start building your viral pages.")
        # هنا غتحطي الكود اللي كيبني المواقع بصح
    else:
        st.warning("🔒 This feature is reserved for PRO members.")
        st.markdown(f"### {t['price']}")
        st.write("Join 1000+ successful entrepreneurs.")
        st.image("https://via.placeholder.com/1000x400?text=Premium+Dashboard+Preview")

st.divider()
st.caption(f"AdSpy Global v20.0 | Dev: Ilham (FST Marrakech)")
