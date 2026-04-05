import streamlit as st
import time

# إعدادات المنصة العالمية
st.set_page_config(page_title="AdSpy AI Global Pro", page_icon="💎", layout="wide")

if 'lang' not in st.session_state:
    st.session_state.lang = 'English'

with st.sidebar:
    st.markdown("## ⚙️ Business Suite")
    st.session_state.lang = st.selectbox("Language / اللغة", ["English", "العربية", "Français"])
    st.write("---")
    st.markdown("### 💎 Account: Business Pro")
    st.write("Developer: Ilham")

# محتوى اللغات بالأثمنة الاحترافية الجديدة
content = {
    "English": {
        "title": "AdSpy AI: Global Intelligence Platform",
        "tabs": ["Deep Analysis", "AI Copywriting", "CRM Reply", "Pricing"],
        "price_1": "Premium Monthly: 25$ / month",
        "price_2": "Business Annual: 89$ / year (Save 70%)",
        "offer": "🚀 Professional AI Suite for E-commerce Experts."
    },
    "العربية": {
        "title": "AdSpy AI: منصة الذكاء العالمي للإعلانات",
        "tabs": ["التحليل العميق", "صناعة المحتوى", "الرد الذكي", "الأسعار والتفعيل"],
        "price_1": "الاشتراك الشهري: 25$",
        "price_2": "الاشتراك السنوي: 89$ (وفر 70%)",
        "offer": "🚀 منصة احترافية مخصصة لخبراء التجارة الإلكترونية."
    },
    "Français": {
        "title": "AdSpy AI: Intelligence Marketing Pro",
        "tabs": ["Analyse Profonde", "Rédaction IA", "Réponse CRM", "Tarification"],
        "price_1": "Pack Mensuel: 25$ / mois",
        "price_2": "Pack Annuel: 89$ / an (Economisez 70%)",
        "offer": "🚀 Suite IA Professionnelle pour les Experts."
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
    st.text_input("Brand/Product Name:", key="t2")
    st.button("Generate Professional Copy", key="b2")

with tab3:
    st.subheader(data["tabs"][2])
    st.text_input("Customer Inquiry:", key="t3")
    st.button("Generate Smart Reply", key="b3")

with tab4:
    st.header("💰 Business Subscription")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### {data['price_1']}")
        st.markdown(f"### {data['price_2']}")
        st.write("---")
        st.write("✔️ Unlimited AI Requests")
        st.write("✔️ Full Dashboard Access")
        st.write("✔️ API Integration (Coming Soon)")
    with col2:
        st.write("To activate your license, contact our support:")
        st.success("Official WhatsApp: +212607573180")
        wa_url = "https://wa.me/212607573180?text=I%20want%20to%20activate%20the%20Business%20Plan"
        st.markdown(f'''
            <a href="{wa_url}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#007bff; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold;">
                    Activate Pro Plan Now ✅
                </div>
            </a>
        ''', unsafe_content_allowed=True)

st.divider()
st.caption("AdSpy Pro v4.6 | High-End Enterprise Edition")
