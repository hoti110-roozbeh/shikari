# streamlit_app.py
import streamlit as st
from PIL import Image
import io
import random

# تنظیمات اولیه
st.set_page_config(page_title="شکارچی", page_icon="🦅", layout="centered")

# عنوان و توضیحات برنامه
st.title("🦅 شکارچی — تحلیل تصویر چارت")
st.markdown("""
این نسخه‌ی آزمایشی شکارچی است.  
کافی است تصویر چارت خود را از گالری انتخاب کنید تا شکارچی به شما پیشنهاد دهد چه باید کرد.
""")

# آپلود فایل تصویر
uploaded_file = st.file_uploader("📸 عکس چارت را انتخاب کنید", type=["png","jpg","jpeg"])

def fake_analyze(img: Image.Image):
    """
    تحلیل آزمایشی برای دمو.
    در نسخه‌ی نهایی، هوش مصنوعی واقعی به‌جای این قسمت قرار می‌گیرد.
    """
    width, height = img.size
    base_price = int((width + height) * 1.3)
    direction = random.choice(["لانگ", "شورت"])
    entry = base_price + random.randint(-2000, 2000)
    stop = entry - (random.randint(1000, 4000) if direction=="لانگ" else -random.randint(1000,4000))
    target = entry + (random.randint(2000, 8000) if direction=="لانگ" else -random.randint(2000,8000))
    confidence = random.uniform(0.45, 0.97)
    return {
        "direction": direction,
        "entry": entry,
        "stop": stop,
        "target": target,
        "confidence": confidence
    }

# تحلیل و نمایش نتیجه
if uploaded_file is not None:
    try:
        image = Image.open(io.BytesIO(uploaded_file.read()))
        st.image(image, caption="📊 چارت انتخاب‌شده", use_column_width=True)
        st.info("در حال تحلیل تصویر... (نسخه آزمایشی)")
        result = fake_analyze(image)

        st.markdown("---")
        st.subheader(f"📈 پیشنهاد شکارچی: **{'لانگ کن' if result['direction']=='لانگ' else 'شورت کن'}**")
        st.markdown(f"- **ورود:** {result['entry']:,}")
        st.markdown(f"- **حد ضرر:** {result['stop']:,}")
        st.markdown(f"- **تارگت:** {result['target']:,}")
        st.markdown(f"- **اعتماد تحلیل:** {result['confidence']:.2%}")

        # هشدار صوتی در نسخه بعدی اضافه می‌شود
        st.markdown("---")
        st.caption("نسخهٔ آزمایشی ۱.۰ — توسعه‌دهنده: حسین 🧿")
    except Exception as e:
        st.error("❌ مشکلی در خواندن تصویر پیش آمد. لطفاً تصویر دیگری انتخاب کنید.")
else:
    st.warning("برای شروع، تصویر چارت خود را از گالری انتخاب کنید.")
