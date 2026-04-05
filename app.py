import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AdSpy AI Global", page_icon="🚀", layout="wide")

# 2. اللغات
lang = st.selectbox("🌐 Choose Language / اختر اللغة", ["العربية", "English", "Français"])

if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# 3. ترجمة النصوص مع المهارات الجديدة
translations = {
    "العربية": {
        "title": "AdSpy AI: منصة النجاح الشاملة",
        "offer": "🔥 عرض خاص: احصل على ميزات الـ AI المتقدمة بخصم 50% اليوم!",
        "free_tabs": ["🔍 تحليل الإعلانات", "✍️ كاتب المحتوى", "💡 أفكار منتجات"],
        "pro_tabs": ["🏗️ صانع المواقع", "🎬 سيناريو فيديو (Viral)", "🕵️ تجسس المنافسين", "📈 سيو (SEO)"],
        "sidebar_title": "تفعيل الاشتراك الممتاز",
        "price": "250 درهم فقط/شهر (بدل 500 درهم)",
        "rib_msg": "التحويل إلى RIB: 007450000972130040048374",
        "wa_btn": "تواصل لتفعيل حسابك ✅",
        "key_label": "كود التفعيل:",
    },
    "English": {
        "title": "AdSpy AI: All-in-One Success Platform",
        "offer": "🔥 Special Offer: Get Advanced AI Features at 50% OFF Today!",
        "free_tabs": ["🔍 Ad Analysis", "✍️ AI Copywriter", "💡 Product Ideas"],
        "pro_tabs": ["🏗️ Web Builder", "🎬 Video Scripts", "🕵️ Competitor Spy", "📈 SEO Tools"],
        "sidebar_title": "Unlock Premium Access",
        "price": "$25/Month (was $50)",
        "rib_msg": "RIB: 007450000972130040048374",
        "wa_btn": "Contact to Activate ✅",
        "key_label": "License Key:",
    }
}

t = translations.get(lang, translations["English"])

# 4. القائمة الجانبية
with st.sidebar:
    st.header(t["sidebar_title"])
    st.success(f"💎 {t['price']}")
    st.info(f"🏦 {t['rib_msg']}")
    st.write("*Name:* ILHAM AMEZZARGOU")
    
    wa_url = f"https://wa.me/212607573180?text=I_want_to_activate_AdSpy_Pro"
    st.link_button(t["wa_btn"], wa_url)
    
    st.divider()
    license_key = st.text_input(t["key_label"], type="password")
    if st.button("Activate PRO"):
        if license_key == "GLOBAL_PRO_2026":
            st.session_state.is_pro = True
            st.balloons()
            st.success("PRO Active! ✅")
        else:
            st.error("Invalid Code")

# 5. الواجهة الرئيسية
st.title(t["title"])
st.error(t["offer"])

# التبويبات: نجمع الفابور والمدفوع
all_tabs_names = t["free_tabs"] + t["pro_tabs"]
tabs = st.tabs(all_tabs_names)

# عرض التبويبات المجانية
for i in range(len(t["free_tabs"])):
    with tabs[i]:
        st.subheader(t["free_tabs"][i])
        st.text_area("Input:", key=f"free_in_{i}")
        st.button("Run Free", key=f"free_btn_{i}")

# عرض التبويبات المدفوعة (PRO)
for i in range(len(t["free_tabs"]), len(all_tabs_names)):
    with tabs[i]:
        if st.session_state.is_pro:
            st.header(f"✅ {all_tabs_names[i]}")
            st.write("This tool is now unlocked for you!")
            st.text_input("Enter Details:", key=f"pro_in_{i}")
        else:
            st.warning(f"🔒 {all_tabs_names[i]} is a PRO Feature")
            st.write("Upgrade to unlock this professional skill and scale your business.")
            st.image("https://via.placeholder.com/600x200?text=PRO+Skill+Locked")

st.divider()
st.caption(f"AdSpy Global v22.0 | Dev: Ilham Amezzargou")
