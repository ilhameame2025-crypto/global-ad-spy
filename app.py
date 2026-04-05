import streamlit as st

# 1. Page Config
st.set_page_config(page_title="AdSpy AI Global", page_icon="🌎", layout="wide")

# 2. القاموس الكامل للغات (بدون تداخل)
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

# 3. Sidebar Configuration
with st.sidebar:
    st.title("⚙️ Config")
    lang_choice = st.selectbox("🌐 Select Language", ["English", "Français", "العربية"])
    st.divider()

t = translations[lang_choice]

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 4. معلومات الحساب البنكي (Bankalik / Attijari)
with st.sidebar:
    st.header(t["sidebar_head"])
    st.success(t["price"])
    st.info(f"*{t['bank_info']}*")
    # الكود الصحيح للتجاري وفا بنك
    st.code("RIB: 007450000972130040048374\nSWIFT: BCWAMA BX", language="text")
    st.write("*Account Holder:* ILHAM AMEZZARGOU")
    
    wa_url = f"https://wa.me/212607573180?text=I_want_to_activate_Pro_Global_v30"
    st.link_button(t["wa_btn"], wa_url)
    
    st.divider()
    key = st.text_input("License Key:", type="password")
    if st.button("Unlock"):
        if key == "GLOBAL_PRO_2026": # هادا هو الساروت ديالك
            st.session_state.is_pro = True
            st.balloons()

# 5. Main Content Area
st.title(t["title"])
st.error(t["scarcity"])

tabs = st.tabs(t["tabs"])

# الميزات المجانية (0, 1)
for i in [0, 1]:
    with tabs[i]:
        st.subheader(t["tabs"][i])
        st.text_area("Input:", key=f"f_inp_{i}")
        st.button("Run Analysis", key=f"f_btn_{i}")

# ميزة الربح بالعمولة (Tab 2) - AliExpress Integration
with tabs[2]:
    st.header(t["trend_head"])
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://ae01.alicdn.com/kf/S8f566060934d40228066f8e709e99996p.jpg", width=250)
        st.write("*Galaxy Projector* | Margin: 70%")
        # هنا غتحطي رابطك من AliExpress Portals مستقبلاً
        st.link_button(t["source_btn"], "https://s.click.aliexpress.com/e/_DkExample")

    with col2:
        st.image("https://ae01.alicdn.com/kf/H71720888949f48f480396417740e53a2m.jpg", width=250)
        st.write("*Portable Blender* | Trend: Viral")
        st.link_button(t["source_btn"], "https://s.click.aliexpress.com/e/_DkExample2")

# ميزات الـ PRO (3, 4)
for i in [3, 4]:
    with tabs[i]:
        if st.session_state.is_pro:
            st.subheader(f"✅ {t['tabs'][i]}")
            st.write("Professional Tools Activated.")
        else:
            st.warning("🔒 PRO Feature Locked")
            st.write("Upgrade to unlock this professional skill.")
            st.image("https://via.placeholder.com/800x200?text=PRO+Dashboard+Preview")
            st.link_button(t["wa_btn"], wa_url, key=f"p_btn_{i}")

st.divider()
st.caption("AdSpy Global v30.0 | Dev: Ilham Amezzargou (FST Marrakech)")
