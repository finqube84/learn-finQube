import streamlit as st

def run():

    st.header("📚 FinQube Learning Hub")

    st.subheader("🎓 Stock Market Basics")

    videos = {
        "1️⃣ What is Stock Market?": "https://youtu.be/3UF0ymVdYLA?si=JLMmOur9bdBGU5Ug",
        "2️⃣ What is NSE & BSE?": "https://youtu.be/GT_auP0fh90?si=npWCOKhPOcqgW0_a",
        "3️⃣ What is a Share?": "https://youtu.be/6zF7RAW7SfU?si=b1hiLkQNipO-LEUj",
        "4️⃣ What is Market Cap?": "https://youtu.be/Qjz90llPLi0?si=vQYXMjYJwyU1pC9f",
        "5️⃣ What is IPO?": "https://youtu.be/CP4aHOcuJbs?si=SfNbnJ3qdqACwL1o",
        "6️⃣ What is RSI?": "https://youtu.be/WZkXcfr4r3c?si=m8UyEtra0SEnZkjB",
        "7️⃣ What is Moving Average?": "https://youtu.be/7ASY4PtZUTQ?si=gxSrV0fMkKiCNM9G",
        "8️⃣ What is Portfolio?": "https://youtu.be/qcrtDOQxmkc?si=yDJhgBnKRqfkJ74L",
        "9️⃣ Risk Management Basics": "https://youtu.be/s7KApswForA?si=KK8NCgA3dyDTllDW",
        "🔟 Long Term vs Short Term Investing": "https://youtu.be/Y-Gzs2_kssE?si=n005Z5LnY0vBVFGA",
    }

    selected_video = st.selectbox("Select Topic", list(videos.keys()))

    st.video(videos[selected_video])
    
if __name__ == "__main__":
    run()
