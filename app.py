import streamlit as st
import streamlit.components.v1 as components
import time

# إعدادات المنصة الاحترافية
st.set_page_config(page_title="AdSpy AI & Shop Builder", page_icon="🛍️", layout="wide")

if 'lang' not in st.session_state:
    st.session_state.lang = 'العربية'

with st.sidebar:
    st.header("⚙️ Admin Panel")
    st.session_state.lang = st.selectbox("Language", ["العربية", "English", "Français"])
    st.write("---")
    st.info("Status: Website Builder Suite")

# محتوى اللغات (إضافة ميزة بناء المواقع المباشر)
content = {
    "العربية": {
        "title": "AdSpy AI: منصة إدارة المبيعات المتكاملة",
        "tabs": ["التحليل الذكي", "كتابة الإعلان", "بناء موقع مبيعات واجد", "الاشتراك الممتاز"],
        "builder_label": "أدخل تفاصيل المنتج لبناء موقعك المباشر:",
        "btn_build": "إنشاء الموقع ومعاينته الآن 🚀"
    },
    "English": {
        "title": "AdSpy AI: All-in-One Website Platform",
        "tabs": ["Smart Analysis", "AI Copywriting", "Build Live Sales Page", "Premium Plans"],
        "builder_label": "Enter product details for your live page:",
        "btn_build": "Build & Preview My Page 🚀"
    },
    "Français": {
        "title": "AdSpy AI: Créateur de Site de Vente Tout-en-Un",
        "tabs": ["Analyse Smart", "Rédaction IA", "Créer un Site Live", "Abonnements"],
        "builder_label": "Entrez les détails du produit :",
        "btn_build": "Créer & Prévisualiser la Page 🚀"
    }
}

data = content[st.session_state.lang]
st.title(f"🛍️ {data['title']}")

tab1, tab2, tab3, tab4 = st.tabs(data["tabs"])

with tab1:
    st.subheader(data["tabs"][0])
    st.text_area("Analyze / تحليل:", key="t1")
    st.button("Start / ابدأ", key="b1")

with tab2:
    st.subheader(data["tabs"][1])
    p_name = st.text_input("Product Name / اسم المنتج:", key="t2")
    if st.button("Generate Copy / توليد", key="b2"):
        st.code(f"إعلان احترافي لـ {p_name}: أفضل جودة، توصيل سريع. اطلب الآن!")

# --- التبويب المطور: بناء موقع مبيعات واجد ومباشر ---
with tab3:
    st.subheader(data["tabs"][2])
    st.write(data["builder_label"])
    
    col_a, col_b = st.columns(2)
    with col_a:
        prod_title = st.text_input("Product Title / عنوان المنتج", key="prod_title")
        prod_price = st.text_input("Price / الثمن (DH)", key="prod_price")
    with col_b:
        prod_desc = st.text_area("Description / وصف قصير", key="prod_desc")
    
    if st.button(data["btn_build"], key="b3"):
        with st.spinner('Generating Professional Live Website...'):
            time.sleep(1.5)
            # ديزاين احترافي لصفحة المبيعات (أوتوماتيكي)
            landing_html = f"""
            <html>
                <body style='font-family: Arial, sans-serif; text-align: center; padding: 40px; background-color: #f4f7f6;'>
                    <div style='background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 600px; margin: auto;'>
                        <h1 style='color: #2c3e50; font-size: 32px;'>{prod_title}</h1>
                        <p style='font-size: 18px; color: #7f8c8d;'>{prod_desc}</p>
                        <h2 style='color: #e74c3c; font-size: 28px; margin-top: 20px;'>السعر: {prod_price} درهم</h2>
                        <button style='background-color: #27ae60; color: white; padding: 15px 30px; border: none; border-radius: 5px; font-size: 22px; cursor: pointer; margin-top: 25px;'>
                            اشترِ الآن
                        </button>
                    </div>
                </body>
            </html>
            """
            st.success("✅ تم إنشاء الموقع بنجاح! يمكن لزبنائك الآن معاينة موقع المبيعات الخاص بهم.")
            st.write("---")
            st.markdown("### معاينة الموقع (Preview):")
            # عرض الموقع مباشرة داخل Streamlit
            components.html(landing_html, height=500)
            st.markdown("### كود الموقع (HTML Code):")
            st.code(landing_html, language="html")

with tab4:
    st.header("💳 الخطط الشهرية")
    st.markdown("### اشتراك صانع المواقع: 25$ / الشهر")
    st.write("- تحليل إعلانات غير محدود")
    st.write("- بناء عدد غير محدود من صفحات الهبوط المباشرة")
    wa_url = "https://wa.me/212607573180?text=I%20want%20to%20activate%20AdSpy%20Builder"
    st.link_button("Activate My Account ✅", wa_url, type="primary")

st.divider()
st.caption("AdSpy Pro v6.0 | Website Builder Enterprise")
