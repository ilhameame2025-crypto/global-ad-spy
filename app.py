import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Pro", page_icon="💎", layout="wide")

# نظام الترجمة الذكي
if 'lang' not in st.session_state:
    st.session_state.lang = 'العربية'

with st.sidebar:
    st.header("⚙️ الإعدادات / Settings")
    st.session_state.lang = st.selectbox("اختر اللغة", ["العربية", "English", "Français"])
    st.write("---")
    st.info("إصدار الشركات Pro")
    st.write("المطور: إلهام أمزرغو")

# محتوى اللغات
translations = {
    "العربية": {
        "tabs": ["التحليل العميق", "صناعة المحتوى", "بناء المواقع", "الأسعار"],
        "analysis_label": "حلل محتوى الإعلان:",
        "analysis_btn": "بدء التحليل",
        "pricing_title": "انضم لأكثر من 1000 مقاول ناجح",
        "monthly": "الخطة الشهرية",
        "annual": "الخطة السنوية (الأكثر توفيراً)",
        "wa_text": "أريد تفعيل اشتراكي الآن"
    },
    "English": {
        "tabs": ["Deep Analysis", "AI Copywriting", "Web Builder", "Pricing"],
        "analysis_label": "Analyze Ad Content:",
        "analysis_btn": "Start Analysis",
        "pricing_title": "Join 1000+ Successful Entrepreneurs",
        "monthly": "Monthly Plan",
        "annual": "Annual Plan (Best Value)",
        "wa_text": "I want to activate my plan"
    },
    "Français": {
        "tabs": ["Analyse Profonde", "Rédaction IA", "Créateur Web", "Tarification"],
        "analysis_label": "Analyser le contenu :",
        "analysis_btn": "Lancer l'analyse",
        "pricing_title": "Rejoignez 1000+ Entrepreneurs",
        "monthly": "Pack Mensuel",
        "annual": "Pack Annuel (Meilleure Valeur)",
        "wa_text": "Je veux activer mon pack"
    }
}

t = translations[st.session_state.lang]

st.title(f"💎 AdSpy AI - {st.session_state.lang}")
st.error("⏳ عرض خاص: خصم 50% ينتهي بنهاية اليوم!")

tab1, tab2, tab3, tab4 = st.tabs(t["tabs"])

with tab1:
    st.subheader(t["tabs"][0])
    st.text_area(t["analysis_label"], height=150)
    if st.button(t["analysis_btn"]):
        with st.spinner('جاري المعالجة...'):
            time.sleep(1)
            st.success("✅ تمت العملية بنجاح")

with tab4:
    st.header(t["pricing_title"])
    st.toast("🔥 اشتراك جديد من طنجة قبل 5 دقائق!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="border: 2px solid #e0e0e0; padding: 20px; border-radius: 15px; text-align: center; background-color: white;">
            <h3 style="color: #333;">{t['monthly']}</h3>
            <h1 style="color: #27ae60;">25$</h1>
            <p>✅ بناء مواقع غير محدود</p>
            <p>✅ دعم VIP 24/7</p>
        </div>
        """, unsafe_content_allowed=True)
        st.write("")
        st.link_button(f"🚀 {t['monthly']}", f"https://wa.me/212607573180?text={t['wa_text']}", use_container_width=True)

    with col2:
        st.markdown(f"""
        <div style="border: 3px solid #f1c40f; padding: 20px; border-radius: 15px; text-align: center; background-color: #fffdf0;">
            <h3 style="color: #d4ac0d;">{t['annual']} 🔥</h3>
            <h1 style="color: #d4ac0d;">199$</h1>
            <p>🌟 <b>وفر 100$ كاملة</b></p>
            <p>🌟 استشارة مجانية في التجارة الإلكترونية</p>
            <p style="color: #e74c3c; font-weight: bold;">باقي 3 مقاعد فقط!</p>
        </div>
        """, unsafe_content_allowed=True)
        st.write("")
        st.link_button(f"🏆 {t['annual']}", f"https://wa.me/212607573180?text={t['wa_text']}", type="primary", use_container_width=True)

st.divider()
st.caption(f"AdSpy Pro v9.5 | Designed by Ilham Amezzargou | Marrakech")
