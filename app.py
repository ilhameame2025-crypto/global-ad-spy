import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Pro", page_icon="🚀")

# نظام تبديل اللغات
if 'lang' not in st.session_state:
    st.session_state.lang = 'English'

def change_lang():
    if st.session_state.lang == 'English':
        st.session_state.lang = 'العربية'
    else:
        st.session_state.lang = 'English'

# القائمة الجانبية
with st.sidebar:
    st.title("Settings / الإعدادات")
    st.button("Change Language / تغيير اللغة", on_click=change_lang)
    st.write("---")
    st.write("Developed by Ilham (MSD Student)")

# محتوى الموقع بناءً على اللغة
if st.session_state.lang == 'English':
    st.title("🚀 AdSpy AI: Professional Intelligence")
    tab1, tab2, tab3 = st.tabs(["Analyze Ad", "Write New Ad", "Customer Reply"])
    
    with tab1:
        st.subheader("Analyze your competitor's ad")
        ad_text = st.text_area("Paste the ad text here:")
        if st.button("Start Analysis"):
            st.info(f"Analyzing: {ad_text[:30]}...")
            st.success("Analysis: This ad is good but needs a stronger Call to Action.")
            
    with tab2:
        st.subheader("Generate a winning ad")
        product = st.text_input("What are you selling?")
        if st.button("Write Ad for me"):
            st.code(f"Special Offer! Get your {product} today with 20% discount. Limited time!")

    with tab3:
        st.subheader("Reply to Customer")
        comment = st.text_input("Customer's Question:")
        if st.button("Generate Reply"):
            st.write(f"Reply: Hello! Thank you for asking about {comment}. We'd be happy to help!")

else:
    st.title("🚀 AdSpy AI: الذكاء العالمي")
    tab1, tab2, tab3 = st.tabs(["تحليل إعلان", "كتابة إعلان جديد", "رد على زبون"])
    
    with tab1:
        st.subheader("حلل إعلان منافسيك")
        ad_text = st.text_area("لصق نص الإعلان هنا:")
        if st.button("ابدأ التحليل"):
            st.info(f"جاري تحليل: {ad_text[:30]}...")
            st.success("النتيجة: الإعلان جيد، لكن ننصح بإضافة لمسة عاطفية أكثر.")
            
    with tab2:
        st.subheader("اكتب إعلان احترافي")
        product = st.text_input("شنو هو المنتج ديالك؟")
        if st.button("اكتب لي الإعلان"):
            st.code(f"عرض خاص! احصل على {product} اليوم بخصم 20%. الكمية محدودة!")

    with tab3:
        st.subheader("رد ذكي على الزبون")
        comment = st.text_input("سؤال الزبون:")
        if st.button("توليد الرد"):
            st.write(f"الرد المقترح: أهلاً بك! شكراً على استفسارك بخصوص {comment}. نحن هنا للمساعدة!")
