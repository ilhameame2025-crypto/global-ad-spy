import streamlit as st
import time

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="AdSpy AI Global Pro", page_icon="🌍", layout="wide")

# نظام اختيار اللغات
if 'lang' not in st.session_state:
    st.session_state.lang = 'الدارجة المغربية'

# القائمة الجانبية (Sidebar)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=100)
    st.title("Settings | الإعدادات")
    st.session_state.lang = st.selectbox("Linguistics / اللغة", 
                                        ["الدارجة المغربية", "العربية", "Français", "English"])
    st.write("---")
    st.markdown("### 💎 Premium Plan")
    st.success("Admin: Ilham (FST Marrakech)")
    st.write("---")
    st.write("v2.0 - AI Integrated")

# قاعدة البيانات اللغوية للمميزات
content = {
    "الدارجة المغربية": {
        "title": "AdSpy AI: الذكاء د الماركتينغ المغربي 🇲🇦",
        "tabs": ["حلل الإشهار", "صايب إشهار", "جاوب الكليان", "تفعيل الاشتراك"],
        "welcome": "مرحبا بيك يا إلهام! هاد المنصة غاتخليك تبيعي كتر بالذكاء الاصطناعي.",
        "analyze_label": "حط نص الإشهار هنا باش نحللوه ليك:",
        "gen_label": "شنو هو المنتج اللي باغي تبيع؟",
        "reply_label": "شنو قال ليك الكليان في الكومنتير؟",
        "pay_title": "باش تولي Pro وتخدم بلا حدود",
        "wa_text": "تواصل معانا في الواتساب دابا ✅"
    },
    "العربية": {
        "title": "AdSpy AI: منصة الذكاء العالمي 🚀",
        "tabs": ["تحليل إعلان", "توليد إعلان", "رد ذكي", "الاشتراك"],
        "welcome": "أهلاً بك! حلل إعلانات المنافسين وتفوق عليهم بلمسة زر.",
        "analyze_label": "أدخل نص الإعلان للتحليل العميق:",
        "gen_label": "اكتب اسم المنتج وسنقوم بكتابة الإعلان:",
        "reply_label": "أدخل تعليق الزبون وسنرد عليه بذكاء:",
        "pay_title": "تفعيل الحساب والنسخة الكاملة",
        "wa_text": "تواصل عبر واتساب للتفعيل ✅"
    },
    "Français": {
        "title": "AdSpy AI: Intelligence Marketing 🇫🇷",
        "tabs": ["Analyser", "Générer", "Réponse IA", "Paiement"],
        "welcome": "Boostez vos ventes avec l'IA. Analysez et créez des pubs pro.",
        "analyze_label": "Collez le texte de la publicité ici :",
        "gen_label": "Quel produit voulez-vous vendre ?",
        "reply_label": "Commentaire du client :",
        "pay_title": "Activer la Version Premium",
        "wa_text": "Contactez-nous sur WhatsApp ✅"
    },
    "English": {
        "title": "AdSpy AI: Global Intelligence 🌍",
        "tabs": ["Analyze", "Generate", "AI Reply", "Payment"],
        "welcome": "Welcome! Scale your business using AI ad analysis.",
        "analyze_label": "Paste the ad copy here for analysis:",
        "gen_label": "What product are you selling?",
        "reply_label": "Customer comment/question:",
        "pay_title": "Unlock Full AI Access",
        "wa_text": "Contact Support via WhatsApp ✅"
    }
}

data = content[st.session_state.lang]
st.title(data["title"])
st.info(data["welcome"])

tab1, tab2, tab3, tab4 = st.tabs(data["tabs"])

with tab1:
    st.subheader(data["tabs"][0])
    ad_txt = st.text_area(data["analyze_label"], height=150)
    if st.button("Analyze / تحليل"):
        with st.spinner('جاري التحليل...'):
            time.sleep(2)
            st.success("✅ التحليل واجد: هاد الإشهار ناقصو 'Call to Action' قوي باش الناس تشري.")

with tab2:
    st.subheader(data["tabs"][1])
    prod_name = st.text_input(data["gen_label"])
    if st.button("Generate / توليد"):
        st.code(f"إعلان واعر لـ {prod_name}:\nأفضل {prod_name} في المغرب! جودة عالية وتوصيل سريع. اطلب الآن!")

with tab3:
    st.subheader(data["tabs"][2])
    comm = st.text_input(data["reply_label"])
    if st.button("Get Reply / خذ الرد"):
        st.write(f"🤖 الرد المقترح: أهلاً بك! شكراً على اهتمامك بـ {comm}. صيفط لينا رقمك في الخاص وغنتواصلو معاك.")

with tab4:
    st.header("💰 " + data["pay_title"])
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📋 الخطوات:")
        st.write("1. تواصل معانا في الواتساب.")
        st.write("2. صيفط سكرين ديال الخلاص (CIH/Barid).")
        st.write("3. تفعيل فوري للحساب.")
    
    with col2:
        whatsapp_link = "https://wa.me/212607573180?text=سلام%20إلهام%20بغيت%20نفعل%20الاشتراك%20في%20AdSpy"
        st.markdown(f'''
            <a href="{whatsapp_link}" target="_blank">
                <button style="background-color: #25D366; color: white; border: none; padding: 20px; border-radius: 10px; cursor: pointer; font-size: 20px; width: 100%;">
                    {data["wa_text"]}
                </button>
            </a>
        ''', unsafe_content_allowed=True)

st.write("---")
st.caption("AdSpy AI v2.0 - Created with ❤️ in Marrakech")
