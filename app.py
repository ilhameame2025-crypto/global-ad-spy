import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Global", page_icon="🌐", layout="wide")

# 2. نظام اختيار اللغة في الجانب (Sidebar)
with st.sidebar:
    st.title("⚙️ Settings / الإعدادات")
    lang = st.selectbox("Choose Language / اختر اللغة", ["English", "العربية", "Français"])
    st.divider()
    
    # نظام التفعيل بالكود (للي خلصوا أوتوماتيكياً)
    st.subheader("🔐 Premium Access")
    license_key = st.text_input("Enter License Key:", type="password")
    if st.button("Unlock Pro"):
        if license_key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.success("Activated! / تم التفعيل")
        else:
            st.error("Invalid Key / كود غير صحيح")

# 3. نصوص اللغات (باش ميوقعش Error)
texts = {
    "English": {
        "title": "🚀 AdSpy AI Global System",
        "tab1": "🔍 Free Analysis",
        "tab2": "🏗️ AI Web Builder (Pro)",
        "buy_btn": "Buy License Key ($25)",
        "rib_msg": "Transfer to: 007450000972130040048374",
        "wa_msg": "Send Receipt via WhatsApp"
    },
    "العربية": {
        "title": "🚀 نظام AdSpy AI العالمي",
        "tab1": "🔍 تحليل مجاني",
        "tab2": "🏗️ صانع المواقع (نسخة PRO)",
        "buy_btn": "شراء كود التفعيل (250 درهم)",
        "rib_msg": "التحويل إلى: 007450000972130040048374",
        "wa_msg": "إرسال التوصيل عبر الواتساب"
    },
    "Français": {
        "title": "🚀 Système AdSpy AI Global",
        "tab1": "🔍 Analyse Gratuite",
        "tab2": "🏗️ Constructeur Web (Pro)",
        "buy_btn": "Acheter la Clé ($25)",
        "rib_msg": "Virement vers: 007450000972130040048374",
        "wa_msg": "Envoyer le reçu via WhatsApp"
    }
}

t = texts[lang]

# 4. واجهة الموقع الرئيسية
st.title(t["title"])

tab1, tab2 = st.tabs([t["tab1"], t["tab2"]])

with tab1:
    st.write("---")
    st.text_area("Input / النص:", placeholder="...")
    st.button("Start / ابدأ")

with tab2:
    if st.session_state.get('is_pro', False):
        st.success("✅ PRO Version Active")
        # كود بناء المواقع هنا
    else:
        st.header("💎 PRO Features")
        st.warning(f"💳 {t['rib_msg']}")
        st.write(f"*Name:* ILHAM AMEZZARGOU")
        
        col1, col2 = st.columns(2)
        with col1:
            st.link_button(t["buy_btn"], "https://gumroad.com/l/your-link") # رابط Gumroad مستقبلاً
        with col2:
            wa_url = f"https://wa.me/212607573180?text=I_paid_for_AdSpy_Pro"
            st.link_button(t["wa_msg"], wa_url)

st.divider()
st.caption(f"AdSpy Global v18.0 | Dev: Ilham (FST Marrakech)")
