import streamlit as st
import time

# 1. الإعدادات الأساسية (لازم تكون هي الأولى)
st.set_page_config(page_title="AdSpy AI Pro", page_icon="💰", layout="wide")

# 2. القاموس اللغوي (مرتب ومنظم)
content = {
    "العربية": {
        "title": "الذكاء العالمي للإعلانات",
        "tabs": ["التحليل الذكي", "كتابة الإعلان", "بناء المواقع", "خطط الاشتراك"],
        "promo": "⏳ عرض محدود: باقي 7 حسابات فقط بخصم 50%!",
        "wa_msg": "اريد تفعيل الخطة السنوية والاستفادة من العرض"
    },
    "English": {
        "title": "AdSpy AI Global Pro",
        "tabs": ["Smart Analysis", "AI Copy", "Web Builder", "Pricing"],
        "promo": "⏳ Hurry! Only 7 slots left with 50% discount!",
        "wa_msg": "I want to activate my Annual Plan now"
    }
}

# 3. القائمة الجانبية
with st.sidebar:
    st.header("⚙️ Settings")
    lang_choice = st.selectbox("Language / اللغة", ["العربية", "English"])
    st.write("---")
    st.info("Status: Enterprise Pro Edition")
    st.write("Dev: Ilham (FST Marrakech)")

data = content[lang_choice]

# 4. الواجهة الرئيسية
st.title(f"💎 {data['title']}")
st.error(data['promo'])

# تعريف التبويبات (هنا الحل النهائي لمشكل NameError)
tab1, tab2, tab3, tab4 = st.tabs(data["tabs"])

with tab1:
    st.subheader(data["tabs"][0])
    st.text_area("Analyze / تحليل:", height=150, key="analysis_input")
    if st.button("Start AI Scan", key="btn_scan"):
        with st.spinner('Analyzing...'):
            time.sleep(1)
            st.success("✅ Analysis Complete.")

with tab2:
    st.subheader(data["tabs"][1])
    prod_name = st.text_input("Product Name:", key="prod_name")
    if st.button("Generate Ad Copy", key="btn_copy"):
        st.code(f"أفضل {prod_name} في السوق! جودة عالية وتوصيل سريع. اطلب الآن!")

with tab3:
    st.subheader(data["tabs"][2])
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Site Title / عنوان الموقع", key="s_title")
        st.text_input("Price / الثمن", key="s_price")
    with c2:
        st.text_area("Description / الوصف", key="s_desc")
    
    if st.button("Generate Live Site 🚀", key="btn_build"):
        st.success("✅ الموقع جاهز! (Preview Mode Active)")

with tab4:
    st.header("💳 انضم لأكثر من 1000 مقاول ناجح")
    st.toast("🔥 شخص جديد اشترك في الخطة السنوية قبل قليل!")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.info("### الخطة الشهرية: 25$")
        st.write("✅ بناء مواقع غير محدود")
        st.write("✅ دعم VIP عبر الواتساب")
        st.link_button("اشترك شهرياً", f"https://wa.me/212607573180?text={data['wa_msg']}")

    with col_right:
        st.warning("### الخطة السنوية: 199$ (Best Value)")
        st.write("🌟 *وفر 100$ كاملة*")
        st.write("🌟 استشارة مجانية في الـ Dropshipping")
        st.write("🌟 أولوية في تحديثات الذكاء الاصطناعي")
        st.link_button("🏆 احصل على العرض السنوي", f"https://wa.me/212607573180?text={data['wa_msg']}", type="primary")

    st.divider()
    st.markdown("🔒 *ضمان استرجاع الأموال* | 💳 *CIH, PayPal, Crypto*")

st.divider()
st.caption("AdSpy Pro v9.0 | Built by Ilham Amezzargou")
