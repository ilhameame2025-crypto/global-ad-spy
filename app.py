import streamlit as st

# 1. إعدادات بسيطة وآمنة
st.set_page_config(page_title="AdSpy AI Global", page_icon="🚀")

# 2. اللغات
if 'lang' not in st.session_state:
    st.session_state.lang = 'العربية'

# 3. القائمة الجانبية
with st.sidebar:
    st.title("الإعدادات")
    st.session_state.lang = st.selectbox("Language", ["العربية", "Français", "English"])
    st.write("---")
    st.info("Dev: Ilham (FST Marrakech)")

# 4. الترجمة
langs = {
    "العربية": {"t": "الذكاء العالمي للإعلانات", "b": "تحليل", "tabs": ["تحليل", "كتابة", "رد", "تفعيل"]},
    "Français": {"t": "AdSpy Intelligence", "b": "Analyser", "tabs": ["Analyse", "Ecrire", "Réponse", "Paiement"]},
    "English": {"t": "AdSpy AI Pro", "b": "Analyze", "tabs": ["Analyze", "Write", "Reply", "Payment"]}
}
d = langs[st.session_state.lang]

# 5. الواجهة (الألوان درتهم بطريقة آمنة)
st.title(d["t"])

tab1, tab2, tab3, tab4 = st.tabs(d["tabs"])

with tab1:
    st.subheader(d["tabs"][0])
    st.text_area("Text / النص:", key="t1")
    st.button(d["b"], key="btn1")

with tab2:
    st.subheader(d["tabs"][1])
    st.text_input("Product / المنتج:", key="t2")
    st.button("Generate", key="btn2")

with tab3:
    st.subheader(d["tabs"][2])
    st.text_input("Comment / تعليق:", key="t3")
    st.button("Reply", key="btn3")

with tab4:
    st.header(d["tabs"][3])
    st.write("تواصل معنا عبر الواتساب لتفعيل الحساب:")
    # هاد السطر هو اللي كان كيدير المشكل، دابا صلحناه
    st.success("WhatsApp: +212607573180")
    wa_url = "https://wa.me/212607573180"
    st.markdown(f"[اضغط هنا للتواصل في الواتساب]({wa_url})")

st.divider()
st.caption("AdSpy Pro v4.1 | Fix Edition")
