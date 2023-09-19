import streamlit as st
import ASCII

st.title("Mã hóa ASCII")
st.info("Bạn có thể nhập bản rõ hoặc chọn file .txt")

with st.form("Form 1"): 
    text = st.text_input("Nhập không dấu. Khóa K là các số nguyên từ 1 đến 256")
    key = st.number_input("Khóa K", step=1, min_value=1, max_value=256)
    submit = st.form_submit_button("Submit")
    if submit:
        tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])
        with tab1:
            st.write("Bản mã hóa : " )
            st.code(ASCII.encrypt(text= text, k=key)) 
        with tab2:
            st.write("Bản giải mã : " )
            st.code(ASCII.decrypt(text= text, k=key)) 
            
    

with st.form("Form 2"):
    file = st.file_uploader("Upload file", type=["txt"])
    key = st.number_input("Khóa K :", step=1, min_value=1, max_value=256)
    st.selectbox(label="Chọn phương pháp", options=["Encrypt", "Decrypt"], key="options")
    submit = st.form_submit_button("Submit")
    if submit:
        if st.session_state["options"] == "Encrypt":
            if file is not None:
                content_encrypted = file.read().decode("utf-8")
                content = ASCII.encrypt(content_encrypted, key)
        if st.session_state["options"] == "Decrypt":
            if file is not None:
                content_decrypted = file.read().decode("utf-8")
                content = ASCII.decrypt(content_decrypted, key)
        st.success("Mã hóa file thành công !!")
if submit:
    st.download_button(
    label="Download",
    data=content,
    file_name="ban_ma.txt",
    )




