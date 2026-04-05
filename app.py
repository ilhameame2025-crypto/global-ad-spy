import streamlit as st
import time

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="AdSpy AI & Website Builder", page_icon="🚀", layout="wide")

# 2. اللغات والمحتوى (مضبوط بالكامل)
content = {
    "العربية": {
        "title": "AdSpy AI: منصة النجاح المتكاملة",
        "tabs": ["التحليل الذكي", "كتابة الإعلان", "بناء موقعك المباشر", "خطط الاشتراك"],
        "hero_msg": "⏳ عرض محدود: باقي فقط 7 حسابات متوفرة بخصم 50% لهذا اليوم!",
        "wa_text": "اريد تفعيل الاشتراك والحصول على الاستشارة المجانية"
    },
    "English": {
        "title": "AdSpy AI: Success Platform",
        "tabs": ["Smart Analysis", "AI Copy", "Live Builder", "Pricing"],
        "hero_msg": "⏳ Limited Offer: Only 7 slots left for 50% discount today!",
        "wa_text": "I want to activate my plan and get free consultation"
    }
}

# اختيار اللغة من الجنب
with st.sidebar:
    st.header("⚙️ Settings")
    lang = st.selectbox("Language / اللغة", ["العربية", "English"])
    st.write("---")
    st.info("Status: Enterprise Edition")
    st.write("Dev: Ilham (FST Marrakech)")

data = content[lang]

# 3. واجهة الموقع
st.title(f"🚀 {data['title']}")
st.error(data['hero_msg']) # نداء عاجل

# تعريف التبويبات (هنا فين كان المشكل، دابا مضبوطين)
tab1, tab2, tab3, tab4 = st.tabs(data["tabs"])

with tab1:
    st.subheader(data["tabs"][0])
    st.text_area("Analyze / تحليل:", height=150)
    st.button("Start AI Analysis")

with tab2:
    st.subheader(data["tabs"][1])
    prod = st.text_input("Product Name:")
    if st.button("Generate Copy"):
        st.code(f"أفضل {prod} في السوق! جودة خيالية وتوصيل فابور. اطلب دابا!")

with tab3:
    st.subheader(data["tabs"][2])
    col_a, col_b = st.columns(2)
    with col_a:
        t = st.text_input("Title / العنوان")
        p = st.text_input("Price / الثمن")
    with col_b:
        d = st.text_area("Desc / الوصف")
    
    if st.button("Build Website 🚀"):
        with st.spinner('Building...'):
            time.sleep(1)
            st.success("✅ موقعك جاهز للمعاينة!")
            # معاينة بسيطة
            st.markdown(f"""
            <div style="border: 2px solid #ddd; padding: 20px; border-radius: 10px; text-align: center;">
                <h1>{t}</h1>
                <p>{d}</p>
                <h2 style="color: red;">{p} DH</h2>
                <button style="background: green; color: white; padding: 10px 20px; border: none; border-radius: 5px;">Buy Now / اطلب الآن</button>
            </div>
            """, unsafe_content_allowed=True)

with tab4:
    st.header("💎 ابدأ جني الأرباح اليوم")
    st.toast("🔥 شخص من مراكش اشترك في الخطة السنوية قبل قليل")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div style="border: 1px solid #ddd; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>الخطة الشهرية</h3>
            <h1 style="color: green;">25$</h1>
            <p>✅ بناء مواقع غير محدود</p>
            <p>✅ دعم فني 24/7</p>
        </div>
        """, unsafe_content_allowed=True)
        st.link_button("اشترك شهرياً", f"https://wa.me/212607573180?text={data['wa_text']}", use_container_width=True)

    with c2:
        st.markdown("""
        <div style="border: 3px solid #f1c40f; padding: 20px; border-radius: 10px; text-align: center; background-color: #fffdf0;">
            <h3 style="color: #d4ac0d;">الخطة السنوية 🔥</h3>
            <h1 style="color: #d4ac0d;">199$</h1>
            <p>🌟 <b>وفر 100$ كاملة</b></p>
            <p>🌟 استشارة مجانية للتجارة الإلكترونية</p>
            <p style="color: red;">باقي 3 مقاعد فقط!</p>
        </div>
        """, unsafe_content_allowed=True)
        st.link_button("🏆 احصل على العرض السنوي", f"https://wa.me/212607573180?text={data['wa_text']}", type="primary", use_container_width=True)

    st.write("---")
    st.markdown("🛡️ *ضمان استرجاع الأموال 7 أيام* | 💳 *CIH, PayPal, Crypto*")

st.divider()
st.caption("AdSpy Pro v8.5 | Official Build")
