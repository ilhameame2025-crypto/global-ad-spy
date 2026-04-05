import streamlit as st

# 1. إعدادات الصفحة (ضرورية في أول سطر)
st.set_page_config(page_title="AdSpy AI Global", page_icon="🌎", layout="wide")

# 2. اللغات (الإنجليزية هي الواجهة للعالم)
lang = st.selectbox("🌐 Select Language / اختر اللغة", ["English", "العربية", "Français"])

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 3. بنك الإغراءات والترجمة
translations = {
    "English": {
        "title": "AdSpy AI: The #1 Hub for Global E-com Success",
        "scarcity": "🔥 URGENT: 50% OFF - Only 7 Licenses Left Today!",
        "proof": "✨ Join 5,000+ Millionaire Entrepreneurs Worldwide",
        "free_tabs": ["🔍 Ad Insights", "✍️ AI Copywriter", "💡 Product Trends"],
        "pro_tabs": ["🏗️ Global Web Builder", "🎬 Viral Video Scripts", "🕵️ Competitor Spy", "📈 Global SEO"],
        "price": "💎 SPECIAL: $25/Month (Real Value: $500)",
        "sidebar_head": "🔐 Unlock Your Success Now",
        "rib_info": "💳 Global Bank Transfer (SWIFT):",
        "wa_btn": "Get My Activation Code Now ✅"
    },
    "العربية": {
        "title": "AdSpy AI: المنصة العالمية رقم #1 للنجاح",
        "scarcity": "🔥 عاجل: خصم 50% متبقي 7 حسابات فقط لهذا اليوم!",
        "proof": "✨ انضم لأكثر من 5000 مقاول ناجح حول العالم",
        "free_tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "💡 أفكار منتجات"],
        "pro_tabs": ["🏗️ صانع المواقع", "🎬 سيناريو فيديو", "🕵️ تجسس المنافسين", "📈 سيو عالمي"],
        "price": "💎 همزة اليوم: 25 دولار فقط (القيمة الأصلية 500 دولار)",
        "sidebar_head": "🔐 تفعيل حسابك الاحترافي",
        "rib_info": "💳 التحويل البنكي الدولي:",
        "wa_btn": "الحصول على كود التفعيل الآن ✅"
    }
}

t = translations.get(lang, translations["English"])

# 4. القائمة الجانبية (Sidebar) - مركز الإغراء والثقة
with st.sidebar:
    st.header(t["sidebar_head"])
    st.markdown(f"### {t['price']}")
    st.success(f"*{t['proof']}*")
    st.divider()
    st.write(t["rib_info"])
    # معلومات Bankalik العالمية
    st.code("RIB: 007450000972130040048374\nSWIFT: BCMAMAMC", language="text")
    st.write("*Account Name:* ILHAM AMEZZARGOU")
    
    # زر واتساب مباشر مع رسالة مغرية
    wa_url = f"https://wa.me/212607573180?text=I_want_the_50_percent_discount_AdSpy_Pro"
    st.link_button(t["wa_btn"], wa_url)
    
    st.divider()
    # خانة إدخال الكود (السر اللي كيحيد الأقفال)
    key = st.text_input("Enter License Key:", type="password")
    if st.button("Activate PRO"):
        if key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.balloons()
            st.success("Welcome to PRO Status! ✅")

# 5. الواجهة الرئيسية
st.title(t["title"])
st.error(t["scarcity"]) # إغراء "الندرة"

# التبويبات (مجانية + مقفولة للإغراء)
all_tabs = t["free_tabs"] + t["pro_tabs"]
tabs = st.tabs(all_tabs)

# عرض الميزات المجانية
for i in range(len(t["free_tabs"])):
    with tabs[i]:
        st.subheader(t["free_tabs"][i])
        st.info("Available for Free / متاح مجاناً")
        st.text_area("Input:", key=f"free_in_{i}")
        st.button("Run Now", key=f"free_btn_{i}")

# عرض ميزات الـ PRO (إغراء القفل)
for i in range(len(t["free_tabs"]), len(all_tabs)):
    with tabs[i]:
        if st.session_state.is_pro:
            st.header(f"✅ {all_tabs[i]} (Active)")
            st.write("Start using your professional tools now.")
        else:
            st.warning(f"🔒 {all_tabs[i]} is Locked")
            st.markdown(f"### Upgrade to unlock this *High-Income Skill*")
            st.write(f"This tool helps you scale to $10k+/month. Get it for only $25 today.")
            st.image("https://via.placeholder.com/800x200?text=Upgrade+to+Unlock+PRO+Feature")
            st.link_button("Unlock Now", wa_url, key=f"lock_btn_{i}")

st.divider()
st.caption(f"AdSpy Global v25.0 | Empowering Entrepreneurs by Ilham")
