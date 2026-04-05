import streamlit as st

st.set_page_config(page_title="AdSpy AI Global", layout="wide")

# زر اختيار اللغة في الجنب
lang = st.sidebar.selectbox("Select Language / اختر اللغة", ["English", "العربية"])

if lang == "English":
    title = "🚀 AdSpy AI: Global Intelligence"
    desc = "Analyze competitor ads using AI to scale your business."
    label = "Enter Ad Copy or URL:"
    btn = "Start Analysis"
    success_msg = "✅ Analyzing data for global markets..."
    sidebar_title = "Settings"
elif lang == "العربية":
    title = "🚀 AdSpy AI: المنصة العالمية"
    desc = "حلل إعلانات المنافسين بالذكاء الاصطناعي لتطوير تجارتك."
    label = "أدخل نص الإعلان أو الرابط:"
    btn = "ابدأ التحليل"
    success_msg = "✅ جاري تحليل البيانات للسوق العربي..."
    sidebar_title = "الإعدادات"

# واجهة الموقع المتغيرة
st.title(title)
st.write(desc)

ad_content = st.text_area(label)

if st.button(btn):
    if ad_content:
        st.success(success_msg)
    else:
        st.warning("Please enter text / المرجو إدخال نص")

st.sidebar.title(sidebar_title)
st.sidebar.write("💰 Premium: $29/mo")
