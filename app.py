import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Global", page_icon="🌎", layout="wide")

# 2. القاموس الكامل (الإنجليزية، الفرنسية، العربية)
translations = {
    "English": {
        "title": "AdSpy AI: Global E-com Mastery",
        "scarcity": "🔥 URGENT: 50% OFF - Only 7 Slots Left Today!",
        "sidebar_head": "🔐 Activate Premium",
        "price": "Special: $25/Month",
        "bank_info": "💳 Bank Transfer (SWIFT):",
        "wa_btn": "Get Activation Code ✅",
        "tabs": ["🔍 Ad Analysis", "✍️ AI Copy", "💡 Product Trends", "🏗️ Web Builder", "🎬 Video Scripts"],
        "trend_head": "💡 Winning Products (Ready to Source)",
        "source_btn": "🚀 Source on AliExpress"
    },
    "Français": {
        "title": "AdSpy AI: Maîtrise E-com Globale",
        "scarcity": "🔥 OFFRE LIMITÉE: -50% Aujourd'hui!",
        "sidebar_head": "🔐 Activer l'accès PRO",
        "price": "Spécial: 25$/Mois",
        "bank_info": "💳 Virement Bancaire (SWIFT):",
        "wa_btn": "Obtenir le code ✅",
        "tabs": ["🔍 Analyse Pub", "✍️ Copie IA", "💡 Tendances", "🏗️ Créateur Web", "🎬 Scripts Vidéo"],
        "trend_head": "💡 Produits Gagnants (Prêts à Sourcer)",
        "source_btn": "🚀 Sourcer sur AliExpress"
    },
    "العربية": {
        "title": "AdSpy AI: احتراف التجارة العالمية",
        "scarcity": "🔥 عرض خاص: خصم 50% متبقي 7 حسابات فقط!",
        "sidebar_head": "🔐 تفعيل النسخة الاحترافية",
        "price": "عرض: 25 دولار فقط/شهر",
        "bank_info": "💳 التحويل البنكي الدولي (SWIFT):",
        "wa_btn": "احصل على كود التفعيل ✅",
        "tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "💡 أفكار منتجات", "🏗️ صانع المواقع", "🎬 سيناريو فيديو"],
        "trend_head": "💡 منتجات رابحة (جاهزة للطلب)",
        "source_btn": "🚀 اطلب من علي إكسبريس"
    }
}

with st.sidebar:
    lang_choice = st.selectbox("🌐 Select Language", ["English", "Français", "العربية"])
    st.divider()

t = translations[lang_choice]

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 3. معلومات Bankalik (Attijari)
with st.sidebar:
    st.header(t["sidebar_head"])
    st.success(t["price"])
    st.info(f"*{t['bank_info']}*")
    st.code("RIB: 007450000972130040048374\nSWIFT: BCWAMA BX", language="text")
    st.write("*Account Holder:* ILHAM AMEZZARGOU")
    
    wa_url = f"https://wa.me/212607573180?text=I_want_to_activate_Pro_Global_v30"
    st.link_button(t["wa_btn"], wa_url)
    
    st.divider()
    key = st.text_input("License Key:", type="password")
    if st.button("Unlock"):
        if key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.balloons()

# 4. الواجهة الرئيسية
st.title(t["title"])
st.error(t["scarcity"])

tabs = st.tabs(t["tabs"])

# ميزات فابور
for i in [0, 1]:
    with tabs[i]:
        st.subheader(t["tabs"][i])
        st.text_area("Input:", key=f"f_inp_{i}")
        st.button("Run Analysis", key=f"f_btn_{i}")

# --- 🚀 ميزة الربح بالعمولة مع الصور الحقيقية ---
with tabs[2]:
    st.header(t["trend_head"])
    col1, col2 = st.columns(2)
    
    with col1:
        # صورة جهاز العرض (Galaxy Projector)
        st.image("https://ae01.alicdn.com/kf/S8f566060934d40228066f8e709e99996p.jpg", use_container_width=True)
        st.subheader("Galaxy Star Projector")
        st.write("🔥 *Demand:* High | *Profit:* $15/unit")
        # رابط حقيقي (مؤقت حتى تبدليه برابطك الخاص)
        st.link_button(t["source_btn"], "https://www.aliexpress.com/item/1005005866144414.html")

    with col2:
        # صورة الخلاط المحمول (Portable Blender)
        st.image("https://ae01.alicdn.com/kf/H71720888949f48f480396417740e53a2m.jpg", use_container_width=True)
        st.subheader("Portable Blender Pro")
        st.write("🔥 *Trend:* Viral | *Profit:* $10/unit")
        # رابط حقيقي (مؤقت حتى تبدليه برابطك الخاص)
        st.link_button(t["source_btn"], "https://www.aliexpress.com/item/1005005463428329.html")

# ميزات الـ PRO
for i in [3, 4]:
    with tabs[i]:
        if st.session_state.is_pro:
            st.subheader(f"✅ {t['tabs'][i]}")
            st.write("Tool Active.")
        else:
            st.warning("🔒 PRO Feature Locked")
            st.image("https://via.placeholder.com/800x200?text=PRO+Dashboard+Preview")
            st.link_button(t["wa_btn"], wa_url, key=f"p_btn_{i}")

st.divider()
st.caption("AdSpy Global v30.0 | Dev: Ilham Amezzargou (FST Marrakech)")
