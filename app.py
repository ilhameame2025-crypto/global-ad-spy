import streamlit as st
import time

# إعدادات المنصة
st.set_page_config(page_title="AdSpy AI Global Pro", page_icon="💎", layout="wide")

if 'lang' not in st.session_state:
    st.session_state.lang = 'English'

with st.sidebar:
    st.markdown("## ⚙️ Business Suite")
    st.session_state.lang = st.selectbox("Language / اللغة", ["English", "العربية", "Français"])
    st.write("---")
    st.markdown("### 💎 Account: Business Pro")
    st.write("Developer: Ilham")

# الترجمة الكاملة (كل لغة معزولة)
content = {
    "English": {
        "title": "AdSpy AI: Global Intelligence",
        "tabs": ["Deep Analysis", "AI Copywriting", "CRM Reply", "Pricing"],
        "input_label": "Analyze Ad Content:",
        "input_place": "Paste your ad text here...",
        "btn_start": "Start Analysis",
        "offer": "🚀 Professional AI Suite for E-commerce Experts.",
        "wa_msg": "Activate Pro Plan Now ✅"
    },
    "العربية": {
        "title": "AdSpy AI: منصة الذكاء العالمي",
        "tabs": ["التحليل العميق", "صناعة المحتوى", "الرد الذكي", "الأسعار والتفعيل"],
        "input_label": "حلل محتوى الإعلان:",
        "input_place": "ضع نص الإعلان هنا...",
        "btn_start": "بدء التحليل",
        "offer": "🚀 منصة احترافية مخصصة لخبراء التجارة الإلكترونية.",
        "wa_msg": "تفعيل الاشتراك الآن ✅"
    },
    "Français": {
        "title": "AdSpy AI: Intelligence Globale",
        "tabs": ["Analyse Profonde", "Rédaction IA", "Réponse CRM", "Tarification"],
        "input_label": "Analyser le contenu publicitaire :",
        "input_place": "Collez le texte de votre pub ici...",
        "btn_start": "Lancer l'analyse",
        "offer": "🚀 Suite IA Professionnelle pour les Experts.",
        "wa_msg": "Activer le Plan Pro ✅"
    }
}

data = content[st.session_state.lang]

st.title(f"💎 {data['title']}")
st.info(data["offer"])

tab1, tab2, tab3, tab4 = st.tabs(data["tabs"])

with tab1:
    st.subheader(data["tabs"][0])
    # هنا صلحنا المشكل: الـ label و الـ placeholder كيتبدلو على حساب اللغة
    st.text_area(data["input_label"], placeholder=data["input_place"], height=150, key="t1")
    if st.button(data["btn_start"], key="b1"):
        with st.spinner('AI Processing...'):
            time.sleep(1.5)
            st.success("✅ Process Finished.")

with tab2:
    st.subheader(data["tabs"][1])
    st.text_input("Brand/Product:" if st.session_state.lang != "العربية" else "اسم المنتج:", key="t2")
    st.button("Generate" if st.session_state.lang != "العربية" else "توليد", key="b2")

with tab3:
    st.subheader(data["tabs"][2])
    st.text_input("Customer Inquiry:" if st.session_state.lang != "العربية" else "استفسار العميل:", key="t3")
    st.button("Reply" if st.session_state.lang != "العربية" else "رد", key="b3")

with tab4:
    st.header("💰 Business Subscription")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Premium: 25$ / month")
        st.markdown("### Business: 89$ / year")
    with col2:
        wa_url = "https://wa.me/212607573180?text=I%20want%20to%20activate%20AdSpy%20Pro"
        st.link_button(data["wa_msg"], wa_url, type="primary", use_container_width=True)

st.divider()
st.caption("AdSpy Pro v4.8 | Enterprise Edition")
