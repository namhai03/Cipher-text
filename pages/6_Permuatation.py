import streamlit as st
import pandas as pd
import Permuatation

st.title("Mã hóa Hoán vị")
st.info("Bạn có thể nhập bản rõ hoặc chọn file .txt")

with st.form("Form 1"): 
    text = st.text_input("Có thể nhập kí tự có dấu và sử dụng space. Khóa K là số tự nhiên tối thiểu là 2")
    m = st.number_input("Khóa K:", step= 1, min_value= 2)
    key = Permuatation.take_key(m)
    submit = st.form_submit_button("Submit")
    if submit:
        st.write(pd.Series(key,name="Giá trị", index=["π", "π^(-1)"]))
        tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])
        with tab1:
            st.write("Bản mã hóa : " )
            st.code(Permuatation.encrypt(text= text, key= key)) 
        with tab2:
            st.write("Bản giải mã : " )
            st.code(Permuatation.decrypt(text= text,key= key)) 
            
with st.form("Form 2"):
    file = st.file_uploader("Upload file", type=["txt"])
    m = st.number_input("Khóa K:", step= 1, min_value= 2)
    key = Permuatation.take_key(m)
    st.selectbox(label="Chọn phương pháp", options=["Encrypt", "Decrypt"], key="options")
    submit = st.form_submit_button("Submit")
    if submit:
        st.write(pd.Series(key,name="Giá trị", index=["π", "π^(-1)"]))
        if st.session_state["options"] == "Encrypt":
            if file is not None:
                content_encrypted = file.read().decode("utf-8")
                content = Permuatation.encrypt(text= text,key= key)
        if st.session_state["options"] == "Decrypt":
            if file is not None:
                content_decrypted = file.read().decode("utf-8")
                content = Permuatation.decrypt(text= text,key= key)
        st.success("Mã hóa file thành công !!")
if submit:
    st.download_button(
    label="Download",
    data=content,
    file_name="ban_ma.txt",
    )
