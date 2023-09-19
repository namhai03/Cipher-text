import streamlit as st
import Substitution

key_pi = Substitution.key_pi
key = Substitution.key
st.title("Mã hóa Thay thế")
st.info("Bạn có thể nhập bản rõ hoặc chọn file .txt")

with st.form("Form 1"): 
    text = st.text_input("Nhập không dấu và không kí tự space. Khóa K là là hoán vị bảng chữ cái")
    st.write("Khóa K:")
    st.code(key)
    submit = st.form_submit_button("Submit")  
    if submit:
        tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])
        with tab1:
            st.write("Bản mã hóa : " )
            st.code(Substitution.encrypt(text= text,key=key, key_pi=key_pi)) 
        with tab2:
            st.write("Bản giải mã : " )
            st.code(Substitution.decrypt(text= text, key_pi=key_pi, key=key)) 
            
key_pi = Substitution.key_pi
key = Substitution.key

with st.form("Form 2"):
    file = st.file_uploader("Upload file", type=["txt"])
    st.write("Khóa K:")
    st.code(key)
    st.selectbox(label="Chọn phương pháp", options=["Encrypt", "Decrypt"], key="options")
    submit = st.form_submit_button("Submit")
    if submit:
        if st.session_state["options"] == "Encrypt":
            if file is not None:
                content_encrypted = file.read().decode("utf-8")
                content = Substitution.encrypt(text= text,key=key, key_pi=key_pi)
        if st.session_state["options"] == "Decrypt":
            if file is not None:
                content_decrypted = file.read().decode("utf-8")
                content = Substitution.decrypt(text= text, key_pi=key_pi, key=key)
        st.success("Mã hóa file thành công !!")
if submit:
    st.download_button(
    label="Download",
    data=content,
    file_name="ban_ma.txt",
    )



