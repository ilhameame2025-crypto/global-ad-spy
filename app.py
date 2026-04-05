import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI & Shop Builder", page_icon="🚀", layout="wide")

# نداء عاجل في أعلى الموقع
st.error("⏳ عرض محدود: باقي فقط 7 حسابات متوفرة بخصم 50% لهذا اليوم!")

# ... (باقي أجزاء الكود السابقة)

with tab4:
    st.header("💳 اختر خطتك وابدأ جني الأرباح اليوم")
    
    # ميزة: ناس كيشتركوا دابا (Social Proof)
    st.toast("🔥 شخص من الدار البيضاء اشترك في الخطة السنوية قبل 2 دقيقة")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="border: 2px solid #e0e0e0; padding: 25px; border-radius: 15px; text-align: center; background-color: white;">
            <h2 style="color: #2c3e50;">الخطة الشهرية</h2>
            <h1 style="color: #27ae60;">25$ <small style="font-size: 15px;">/ شهر</small></h1>
            <hr>
            <p>✅ <b>بناء مواقع غير محدود</b></p>
            <p>✅ تحليل إعلانات ذكي</p>
            <p>✅ دعم VIP 24/7</p>
            <p style="color: grey; font-size: 12px;">* الغاء الاشتراك في أي وقت</p>
        </div>
        """, unsafe_content_allowed=True)
        st.write("")
        st.link_button("🚀 ابدأ الآن (دفع آمن)", "https://wa.me/212607573180?text=I%20want%20to%20start%20now", use_container_width=True)

    with col2:
        # الخطة السنوية هي اللي كتركز عليها العين
        st.markdown("""
        <div style="border: 4px solid #f1c40f; padding: 25px; border-radius: 15px; text-align: center; background-color: #fffdf0; position: relative;">
            <span style="background: #f1c40f; color: black; padding: 5px 15px; border-radius: 20px; position: absolute; top: -15px; right: 20px; font-weight: bold;">الأكثر طلباً 🔥</span>
            <h2 style="color: #d4ac0d;">الخطة السنوية</h2>
            <h1 style="color: #d4ac0d;">199$ <small style="font-size: 15px;">/ سنة</small></h1>
            <hr>
            <p>🌟 <b>وفر 100$ كاملة</b></p>
            <p>🌟 استشارة مجانية في الـ Dropshipping</p>
            <p>🌟 قوالب صفحات هبوط حصرية</p>
            <p style="color: #e74c3c; font-weight: bold;">باقي 3 مقاعد فقط بهذا الثمن!</p>
        </div>
        """, unsafe_content_allowed=True)
        st.write("")
        st.link_button("🏆 احصل على العرض السنوي", "https://wa.me/212607573180?text=I%20want%20the%20Annual%20Offer", type="primary", use_container_width=True)

    st.write("---")
    
    # ميزة الضمان (Trust Signal)
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("المشتركين", "1,240+", "+15 اليوم")
    with col_b:
        st.markdown("🛡️ *ضمان استرجاع الأموال* خلال 7 أيام إذا لم تكن راضياً.")
    with col_c:
        st.markdown("💳 *طرق دفع متعددة:* CIH, PayPal, Crypto.")

st.divider()
st.caption("AdSpy Pro v8.0 | Trusted by 1000+ Entrepreneurs")
