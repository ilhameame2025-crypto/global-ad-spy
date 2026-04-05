import streamlit as st

# 1. Page Configuration (Keep at very top)
st.set_page_config(page_title="AdSpy AI Global", page_icon="🚀", layout="wide")

# 2. Complete Language Dictionary (The brain of the site)
translations = {
    "English": {
        "title": "AdSpy AI: The #1 Hub for Global E-com Success",
        "scarcity": "🔥 URGENT: 50% OFF - Only 7 Licenses Left Today!",
        "sidebar": {
            "title": "Unlock Success Now",
            "price": "SPECIAL: $25/Month (Real Value: $500)",
            "proof": "Join 5,000+ Millionaire Entrepreneurs Worldwide",
            "rib_label": "Global Bank Transfer (SWIFT):",
            "get_code": "Get My Activation Code Now ✅",
            "key_label": "Enter License Key",
            "activate_btn": "Activate PRO"
        },
        "tabs": ["🔍 Ad Analysis", "✍️ AI Copywriter", "💡 Product Trends", "🏗️ Global Web Builder", "🎬 Viral Video Scripts"],
        "tab_msg": "Feature available in free version",
        "locked_msg": "This High-Income tool is Locked",
        "lock_info": "Upgrade to PRO and get instant access to viral skills."
    },
    "العربية": {
        "title": "AdSpy AI: المنصة العالمية الأولى لنجاح التجارة الإلكترونية",
        "scarcity": "🔥 عاجل: خصم 50% متبقي 7 حسابات فقط لهذا اليوم!",
        "sidebar": {
            "title": "تفعيل الاشتراك الممتاز",
            "price": "💎 همزة اليوم: 25 دولار فقط/شهر (بدل 50 دولار)",
            "proof": "✨ انضم لأكثر من 5000 مقاول ناجح حول العالم",
            "rib_label": "💳 التحويل البنكي الدولي (SWIFT):",
            "get_code": "الحصول على كود التفعيل الآن ✅",
            "key_label": "أدخل كود التفعيل هنا",
            "activate_btn": "تفعيل حساب PRO"
        },
        "tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "💡 أفكار منتجات", "🏗️ صانع المواقع", "🎬 سيناريو فيديو"],
        "tab_msg": "هذه الميزة متاحة مجاناً",
        "locked_msg": "هذه الأداة الاحترافية مقفولة بقفل",
        "lock_info": "Upgrade to PRO and get instant access to viral skills." # رسالة عالمية
    }
}

# 3. Choose Language
with st.sidebar:
    st.title("⚙️ Settings / الإعدادات")
    lang_choice = st.selectbox("🌐 Select Language", ["English", "العربية"])
    st.divider()

t = translations[lang_choice]

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 4. Attractive Sidebar with Scarcity
with st.sidebar:
    st.header(t["sidebar"]["title"])
    st.success(f"💎 {t['sidebar']['price']}")
    st.info(f"🏆 {t['sidebar']['proof']}")
    st.divider()
    
    st.write(t["sidebar"]["rib_label"])
    st.code("RIB: 007450000972130040048374\nSWIFT: BCMAMAMC", language="text")
    st.write("*Name:* ILHAM AMEZZARGOU")
    
    # WhatsApp activation
    wa_url = f"https://wa.me/212607573180?text=I_paid_for_AdSpy_Pro_Verification"
    st.link_button(t["sidebar"]["get_code"], wa_url)
    
    st.divider()
    
    license_key = st.text_input(t["sidebar"]["key_label"], type="password")
    if st.button(t["sidebar"]["activate_btn"]):
        if license_key == "GLOBAL_PRO_2026": # The activation code
            st.session_state.is_pro = True
            st.balloons()
            st.success("Access Granted! ✅")

# 5. Main Content Area
st.title(t["title"])
st.error(t["scarcity"])

# Tabs (4 فابور + 1 برو)
tabs = st.tabs(t["tabs"])

for i in range(3):
    with tabs[i]:
        st.subheader(t["tabs"][i])
        st.info(t["tab_msg"])
        st.text_area("Input:", height=100, key=f"f_in_{i}")
        st.button("Start Now", key=f"f_btn_{i}")

with tabs[3]: # صانع المواقع (PRO)
    if st.session_state.is_pro:
        st.header("🏗️ Global Web Builder")
        # كود بناء المواقع هنا
    else:
        st.warning(f"🔒 {t['locked_msg']}")
        st.write(t["lock_info"])
        st.markdown(f"### {t['sidebar']['price']}")
        st.image("https://via.placeholder.com/800x300?text=Premium+dashboard+preview")

with tabs[4]: # سيناريو فيديو (PRO)
    if st.session_state.is_pro:
        st.header("🎬 Viral Video Scripts")
        # كود سيناريو الفيديو هنا
    else:
        st.warning(f"🔒 {t['locked_msg']}")
        st.image("https://via.placeholder.com/800x300?text=PRO+dashboard+preview")

st.divider()
st.caption(f"AdSpy Global v26.0 | Success Path by Ilham (FST Marrakech)")
