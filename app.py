import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Global PRO", page_icon="💎", layout="wide")

# 2. اللغات والميزات (عربية، فرنسية، إنجليزية)
translations = {
    "English": {
        "title": "AdSpy AI Global: Pro E-com Suite 🚀",
        "scarcity": "🔥 HURRY! 50% Discount Ends In:",
        "plans_head": "🔐 Premium Subscriptions",
        "monthly": "Starter: $25/Month",
        "quarterly": "Growth: $60/3 Months (Best Seller)",
        "yearly": "Empire: $180/Year (VIP)",
        "tabs": ["🔍 Ad Spy", "✍️ AI Copy", "🏗️ Temu Builder", "🎬 Video Ads"],
        "builder_btn": "Generate Temu Page",
        "wa_msg": "I_want_to_join_the_plan_"
    },
    "Français": {
        "title": "AdSpy AI Global: Suite Pro E-com 🚀",
        "scarcity": "🔥 VITE! Remise -50% finit dans:",
        "plans_head": "🔐 Abonnements Premium",
        "monthly": "Starter: 25$/Mois",
        "quarterly": "Croissance: 60$/3 Mois (Populaire)",
        "yearly": "Empire: 180$/An (VIP)",
        "tabs": ["🔍 Ad Spy", "✍️ Rédaction IA", "🏗️ Créateur Temu", "🎬 Pub Vidéo"],
        "builder_btn": "Générer Page Temu",
        "wa_msg": "Je_veux_m_abonner_au_plan_"
    },
    "العربية": {
        "title": "AdSpy AI Global: منصة المقاولين المحترفين 🚀",
        "scarcity": "🔥 عاجل! ينتهي الخصم (50%-) بعد:",
        "plans_head": "🔐 باقات الاشتراك الاحترافية",
        "monthly": "باقة البداية: 25 دولار/شهر",
        "quarterly": "باقة النمو: 60 دولار/3 أشهر (الأكثر طلباً)",
        "yearly": "باقة الإمبراطور: 180 دولار/سنة (VIP)",
        "tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "🏗️ صانع صفحات (تيمو)", "🎬 فيديو إعلاني"],
        "builder_btn": "صمم صفحة Temu الآن",
        "wa_msg": "اريد_الاشتراك_في_باقة_"
    }
}

# اختيار اللغة
lang = st.sidebar.selectbox("🌐 Select Language", ["English", "Français", "العربية"])
t = translations[lang]

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 3. القائمة الجانبية (الباقات + العداد + البنك)
with st.sidebar:
    st.title("💎 Premium Access")
    # إضافة عداد تنازلي وهمي للضغط النفسي (Scarcity)
    st.error(f"{t['scarcity']} 02:45:12")
    
    st.header(t["plans_head"])
    plan = st.radio("Choose Your Level:", [t["monthly"], t["quarterly"], t["yearly"]])
    
    st.divider()
    st.success("💳 Bank Info (Bankalik / Attijari)")
    st.code("RIB: 007450000972130040048374\nSWIFT: BCWAMA BX", language="text")
    st.write("*Name:* ILHAM AMEZZARGOU")
    
    # رابط واتساب ديناميكي
    plan_id = plan.split(":")[0]
    wa_link = f"https://wa.me/212607573180?text={t['wa_msg']}{plan_id}"
    st.link_button("Pay & Send Receipt ✅", wa_link)
    
    st.divider()
    key = st.text_input("Enter License Key:", type="password")
    if st.button("Activate PRO"):
        if key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.balloons()

# 4. الواجهة الرئيسية
st.title(t["title"])

tabs = st.tabs(t["tabs"])

# ميزات فابور
with tabs[0]:
    st.subheader(t["tabs"][0])
    st.text_input("Competitor Website or Product Name:")
    st.button("Scan Ads")

with tabs[1]:
    st.subheader(t["tabs"][1])
    st.text_area("Describe your product:")
    st.button("Write High-Converting Copy")

# ميزة صانع صفحات Temu (The "Wow" Feature)
with tabs[2]:
    st.header(t["builder_head"])
    if st.session_state.is_pro:
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            name = st.text_input("Product Name:")
            price = st.text_input("Price ($):")
        with col_in2:
            img_url = st.text_input("Image URL (Direct Link):")
            old_price = st.text_input("Old Price ($):")
            
        if st.button(t["builder_btn"]):
            st.divider()
            # تصميم احترافي يشبه تطبيقات التجارة العالمية
            st.markdown(f"""
            <div style="border: 2px solid #ff4b4b; padding: 20px; border-radius: 15px; background-color: #fff9f9;">
                <div style="display: flex; gap: 20px;">
                    <img src="{img_url if img_url else 'https://via.placeholder.com/300'}" width="250" style="border-radius: 10px;">
                    <div>
                        <h1 style="color: #333;">{name}</h1>
                        <h2 style="color: #ff4b4b;">${price} <span style="text-decoration: line-through; color: gray; font-size: 15px;">${old_price}</span></h2>
                        <p style="background-color: #ffefef; color: #ff4b4b; padding: 5px; display: inline-block; border-radius: 5px;">🔥 Best Seller | Free Delivery</p>
                        <p style="color: #555;">⭐⭐⭐⭐⭐ (2,450 Reviews)</p>
                        <button style="background-color: #ff4b4b; color: white; border: none; padding: 15px 30px; border-radius: 25px; cursor: pointer; font-weight: bold;">ADD TO CART</button>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("🔒 This tool is locked. Only for PRO members.")
        st.image("https://via.placeholder.com/1000x400?text=Temu+Store+Design+Preview")
        st.link_button("Get PRO Access Now", wa_link)

# ميزة فيديو إعلاني
with tabs[3]:
    st.header(t["tabs"][3])
    if st.session_state.is_pro:
        st.write("Generating high-converting scripts and visual directions...")
        st.button("Generate Video Script")
    else:
        st.warning("🔒 Video Ads Automation is a PRO feature.")

st.divider()
st.caption(f"AdSpy Global v35.0 | Developed by Ilham Amezzargou | FST Marrakech")
