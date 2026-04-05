import streamlit as st

# 1. إعدادات الصفحة (الأساس باش ميوقعش Error)
st.set_page_config(page_title="AdSpy AI Morocco", page_icon="🇲🇦", layout="wide")

# 2. العنوان الرئيسي
st.title("🚀 AdSpy AI: المنصة رقم #1 للمقاولين المغاربة")
st.divider()

# 3. تنظيم التبويبات (Tabs)
tab1, tab2 = st.tabs(["🔍 جرب التحليل مجاناً", "🔓 تفعيل الاشتراك (Bankalik)"])

with tab1:
    st.subheader("تحليل الإعلانات بالذكاء الاصطناعي")
    st.info("اكتب نص إعلانك لترى قوة التحليل قبل الدفع")
    ad_text = st.text_area("نص الإعلان هنا:", placeholder="مثلاً: أفضل منتج للعناية بالبشرة...")
    
    if st.button("بدء التحليل المجاني"):
        if ad_text:
            st.success("✅ تم التحليل! النص جذاب ومناسب للجمهور المغربي.")
            st.write("---")
            st.warning("⚠️ للوصول إلى التحليل العميق وبناء المواقع، المرجو تفعيل حسابك.")
        else:
            st.error("المرجو إدخال نص أولاً!")

with tab2:
    st.header("تفعيل الحساب والوصول لجميع الميزات 💎")
    
    col_info, col_form = st.columns([1, 1])
    
    with col_info:
        st.markdown("""
        ### 💳 معلومات الدفع (Bankalik)
        يمكنك الدفع عبر تطبيق *Bankalik* أو أي تطبيق بنكي مغربي آخر.
        """)
        # RIB ديالك (تأكدي منو وحطيه هنا)
        st.code("RIB: 011 450 0000000000 0000 00", language="text") 
        st.write("*الاسم الكامل:* ILHAM AMEZZARGOU")
        st.write("*الثمن:* 250 درهم فقط / شهر")
        st.success("✨ تفعيل فوري بعد إرسال صورة التحويل")

    with col_form:
        st.subheader("إرسال طلب التفعيل")
        with st.form("bank_transfer_form"):
            client_name = st.text_input("اسمك الكامل:")
            client_phone = st.text_input("رقم الواتساب الخاص بك:")
            st.write("---")
            st.write("📢 بعد إتمام التحويل، اضغط على الزر أسفله لإرسال 'الريكو' (Recu) في الواتساب.")
            
            submit_btn = st.form_submit_button("تسجيل الطلب وإرسال التوصيل 🚀")
            
            if submit_btn:
                if client_name and client_phone:
                    st.balloons()
                    st.success(f"شكراً {client_name}! طلبك قيد المعالجة.")
                    # رسالة واتساب أوتوماتيكية فيها معلومات الكليان
                    wa_url = f"https://wa.me/212607573180?text=سلام_إلهام_أنا_{client_name}_هذا_توصيل_Bankalik_لتفعيل_حسابي"
                    st.link_button("إرسال التوصيل عبر الواتساب ✅", wa_url)
                else:
                    st.error("المرجو ملء جميع الخانات!")

# 4. تذييل الصفحة
st.divider()
st.caption("AdSpy Pro v16.0 | Powered by Ilham Amezzargou | FST Marrakech")
