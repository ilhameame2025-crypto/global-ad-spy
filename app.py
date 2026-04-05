import streamlit as st

# 1. Page Config
st.set_page_config(page_title="AdSpy AI Global", page_icon="🌎", layout="wide")

# 2. قاموس اللغات (عربية، إنجليزية، فرنسية) - كولشي مترجم بالكامل
translations = {
    "English": {
        "title": "AdSpy AI: Global E-com Mastery",
        "scarcity": "🔥 URGENT: 50% OFF - Only 7 Slots Left!",
        "sidebar_head": "🔐 Activate Premium",
        "price": "Now $25/Month (was $50)",
        "bank_info": "💳 Bank Transfer (Global SWIFT):",
        "wa_btn": "Get Activation Code ✅",
        "tabs": ["🔍 Ad Analysis", "✍️ AI Copy", "💡 Trends", "🏗️ Web Builder", "🎬 Video Scripts"],
        "ad_label": "✨ Supported by Ads"
    },
    "Français": {
        "title": "AdSpy AI: Maîtrise E-com Globale",
        "scarcity": "🔥 OFFRE LIMITÉE: -50% Aujourd'hui!",
        "sidebar_head": "🔐 Activer l'accès PRO",
        "price": "Seulement 25$/Mois (au lieu de 50$)",
        "bank_info": "💳 Virement Bancaire (SWIFT):",
        "wa_btn": "Obtenir le code ✅",
        "tabs": ["🔍 Analyse Pub", "✍️ Copie IA", "💡 Tendances", "🏗️ Créateur Web", "🎬 Scripts Vidéo"],
        "ad_label": "✨ Supporté par la publicité"
    },
    "العربية": {
        "title": "AdSpy AI: احتراف التجارة العالمية",
        "scarcity": "🔥 عرض خاص: خصم 50% متبقي 7 حسابات فقط!",
        "sidebar_head": "🔐 تفعيل النسخة الاحترافية",
        "price": "25 دولار فقط/شهر (بدل 50 دولار)",
        "bank_info": "💳 التحويل البنكي الدولي (SWIFT):",
        "wa_btn": "احصل على كود التفعيل ✅",
        "tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "💡 أفكار منتجات", "🏗️ صانع المواقع", "🎬 سيناريو فيديو"],
        "ad_label": "✨ مساحة إعلانية للربح"
    }
}

# 3. Sidebar Configuration
with st.sidebar:
    st.title("⚙️ Config")
    lang_choice = st.selectbox("🌐 Language", ["English", "Français", "العربية"])
    st.divider()

t = translations[lang_choice]

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 4. معلومات Bankalik الصحيحة
with st.sidebar:
    st.header(t["sidebar_head"])
    st.success(t["price"])
    st.info(f"*{t['bank_info']}*")
    # تصحيح السويفت للتجاري وفا بنك
    st.code("RIB: 007450000972130040048374\nSWIFT: BCWAMA BX", language="text")
    st.write("*Account Holder:* ILHAM AMEZZARGOU")
    
    wa_url = f"https://wa.me/212607573180?text=I_want_to_activate_Pro_v28"
    st.link_button(t["wa_btn"], wa_url)
    
    st.divider()
    key = st.text_input("License Key:", type="password")
    if st.button("Unlock"):
        if key == "GLOBAL_PRO_2026": # كود الساروت ديالك
            st.session_state.is_pro = True
            st.balloons()

# 5. Main Content + Ads Space
st.title(t["title"])
st.error(t["scarcity"])

# --- مساحة الربح من إعلانات جوجل ---
st.markdown(f"""
    <div style="background-color: #f9f9f9; padding: 15px; border-radius: 8px; text-align: center; border: 1px solid #ddd; margin-bottom: 20px;">
        <p style="color: #888; font-size: 11px; margin-bottom: 5px;">{t['ad_label']}</p>
        <div style="color: #444; font-weight: bold;">[ Google AdSense Ad Space ]</div>
    </div>
""", unsafe_allow_html=True)

# 6. Tabs Content
tabs = st.tabs(t["tabs"])

for i in range(len(t["tabs"])):
    with tabs[i]:
        if i > 2 and not st.session_state.is_pro:
            st.warning("🔒 This is a PRO Feature")
            st.write("Upgrade to unlock this tool and scale your business.")
            st.image("https://via.placeholder.com/800x200?text=Premium+Feature+Locked")
        else:
            st.subheader(t["tabs"][i])
            st.text_area("Input:", key=f"inp_{i}")
            st.button("Analyze", key=f"btn_{i}")

st.divider()
st.caption(f"AdSpy Global v28.0 | Powered by Ilham | {lang_choice} Edition")
