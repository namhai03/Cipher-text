import streamlit as st
import Vigenere

st.title("Mã hóa Vigenère")
st.info("Bạn có thể nhập bản rõ hoặc chọn file .txt")

with st.form("Form 1"): 
    text = st.text_input("Nhập không dấu và không có kí tự space. Khóa K là một chuỗi kí tự")
    key = st.text_input("Khóa K:")
    m = len(key)
    key = Vigenere.take_key(key)
    submit = st.form_submit_button("Submit")
    if submit:
        tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])
        with tab1:
            st.write("Bản mã hóa : " )
            st.code(Vigenere.encrypt(text= text,m=m, k=key)) 
        with tab2:
            st.write("Bản giải mã : " )
            st.code(Vigenere.decrypt(text= text,m=m, k=key)) 
            
    

with st.form("Form 2"):
    file = st.file_uploader("Upload file", type=["txt"])
    key = st.text_input("Khóa K:")
    m = len(key)
    key = Vigenere.take_key(key)
    st.selectbox(label="Chọn phương pháp", options=["Encrypt", "Decrypt"], key="options")
    submit = st.form_submit_button("Submit")
    if submit:
        if st.session_state["options"] == "Encrypt":
            if file is not None:
                content_encrypted = file.read().decode("utf-8")
                content = Vigenere.encrypt(text= text,m=m, k=key)
        if st.session_state["options"] == "Decrypt":
            if file is not None:
                content_decrypted = file.read().decode("utf-8")
                content = Vigenere.decrypt(text= text,m=m, k=key)
        st.success("Mã hóa file thành công !!")
if submit:
    st.download_button(
    label="Download",
    data=content,
    file_name="ban_ma.txt",
    )




