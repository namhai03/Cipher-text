import streamlit as st

st.set_page_config(
    page_title="An toàn thông tin",
    page_icon="🙄"
)
st.title("Trang chủ")
st.info("""Bạn có thể mã hóa văn bản với các khóa có sẵn trong mỗi phương pháp.  
        Đối với mỗi phương pháp sẽ có yêu cầu input khác nhau. """)
st.success("Hãy vào trang để được hướng dẫn chi tiết")
st.snow()
st.sidebar.success("Hãy chọn các phương pháp mã hóa")