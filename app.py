import streamlit as st
import time

# 1. إعدادات المنصة الاحترافية
st.set_page_config(page_title="AdSpy AI Global Pro", page_icon="💎", layout="wide")

if 'lang' not in st.session_state:
    st.session_state.lang = 'English'

with st.sidebar:
    st.markdown("## ⚙️ Business Suite")
    st.session_state.lang = st.selectbox("Language / اللغة", ["English", "العربية", "Français"])
    st.write("---")
    st.markdown("### 💎 Account: Business Pro")
    st.write("Developer: Ilham")

# 2. محتوى اللغات بالأثمنة الاحترافية
content = {
    "English": {
        "title": "AdSpy AI: Global Intelligence Platform",
        "tabs": ["Deep Analysis", "AI Copywriting", "CRM Reply", "Pricing"],
        "price_1": "Premium Monthly: 25$ / month",
        "price_2": "Business Annual: 89$ / year (Save 70%)",
        "offer": "🚀 Professional AI Suite for E-commerce Experts.",
        "wa_msg": "Activate Pro Plan Now ✅"
    },
    "العربية": {
        "title": "AdSpy AI: منصة الذكاء العالمي للإعلانات",
        "tabs": ["التحليل العميق", "صناعة المحتوى", "الرد الذكي", "الأسعار والتفعيل"],
        "price_1": "الاشتراك الشهري: 25$",
        "price_2": "الاشتراك السنوي: 89$ (وفر 70%)",
        "offer": "🚀 منصة احترافية مخصصة لخبراء التجارة الإلكترونية.",
        "wa_msg": "تفعيل الاشتراك الآن ✅"
    },
    "Français": {
        "title": "AdSpy AI: Intelligence Marketing Pro",
        "tabs": ["Analyse Profonde", "Rédaction IA", "Réponse CRM", "Tarification"],
        "price_1": "Pack Mensuel: 25$ / mois",
        "price_2": "Pack Annuel: 89$ / an (Economisez 70%)",
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
    st.text_area("Analyze Ad Content / حلل محتوى الإعلان:", height=150, key="t1")
    if st.button("Start Analysis", key="b1"):
        with st.spinner('Processing Deep Data...'):
            time.sleep(1.5)
            st.success("✅ Deep Analysis Finished Successfully.")

with tab2:
    st.subheader(data["tabs"][1])
    product = st.text_input("Brand/Product Name:", key="t2")
    if st.button("Generate Copy", key="b2"):
        st.code(f"Ad Copy: Experience the best {product} with premium quality.")

with tab3:
    st.subheader(data["tabs"][2])
    comment = st.text_input("Customer Inquiry:", key="t3")
    if st.button("Generate Reply", key="b3"):
        st.info(f"🤖 Suggested Reply: Thank you for asking about {comment}. Check your DM.")

with tab4:
    st.header("💰 Business Subscription")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### {data['price_1']}")
        st.markdown(f"### {data['price_2']}")
        st.write("---")
        st.write("✔️ Unlimited AI Requests | ✔️ Full Dashboard Access")
    
    with col2:
        st.write("To activate your license, contact our support:")
        # تصحيح المشكل: استعملنا st.link_button كحل رسمي وآمن
        wa_url = "https://wa.me/212607573180?text=I%20want%20to%20activate%20the%20Business%20Plan"
        st.link_button(data["wa_msg"], wa_url, type="primary", use_container_width=True)

st.divider()
st.caption("AdSpy Pro v4.7 | Enterprise Edition")
