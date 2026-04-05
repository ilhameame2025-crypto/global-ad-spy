import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Enterprise", page_icon="🔐")

# 2. قاعدة بيانات الأكواد (كل كود تبيعية لشخص واحد فقط)
# نصيحة: ملي تبيعي كود، تقدري تمسحيه من هنا أو تكتبي حداه سميتو باش تعقلي
USER_DATABASE = {
    "ADSPY-ILHAM-001": "Ahmed_Casa",
    "ADSPY-VIP-992": "Sara_Marrakech",
    "KEY-7721-BBS": "User_Test",
    "GOLD-2026-X": "Special_Client"
}

if 'auth' not in st.session_state:
    st.session_state.auth = False

# 3. واجهة الدخول الاحترافية
if not st.session_state.auth:
    st.title("🔐 بوابة المشتركين")
    st.info("المرجو إدخال مفتاح الترخيص الخاص بك للوصول إلى المنصة.")
    
    license_key = st.text_input("مفتاح الترخيص (License Key):", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("تفعيل الحساب الآن ✅"):
            if license_key in USER_DATABASE:
                st.session_state.auth = True
                st.session_state.user = USER_DATABASE[license_key]
                st.rerun() # إعادة تحميل الصفحة للدخول
            else:
                st.error("❌ المفتاح غير صحيح أو تم استخدامه مسبقاً.")
    
    with col2:
        st.link_button("طلب مفتاح جديد (25$) 📲", "https://wa.me/212607573180")

else:
    # 4. الواجهة الاحترافية بعد الدخول
    st.sidebar.success(f"مرحباً: {st.session_state.user}")
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.auth = False
        st.rerun()

    st.title("🚀 AdSpy AI Global System")
    
    # تبويبات الخدمة
    t1, t2, t3 = st.tabs(["📊 التحليل الذكي", "🏗️ صانع المواقع", "🎁 هدايا المشتركين"])
    
    with t1:
        st.subheader("تحليل الإعلانات المتطور")
        st.write("الآن يمكنك البدء بتحليل إعلانات منافسيك.")
        # كود التحليل هنا...

    with t2:
        st.subheader("بناء صفحة هبوط في دقيقة")
        st.write("أدخل معلومات المنتج للحصول على الموقع.")
        # كود بناء المواقع هنا...
