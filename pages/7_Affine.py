import streamlit as st
import Affine

st.title("Mã hóa Affine")
st.info("Bạn có thể nhập bản rõ hoặc chọn file .txt")

with st.form("Form 1"): 
    text = st.text_input("Nhập không dấu. Khóa là 2 số tự nhiên a và b.")
    a, b = st.columns(2)
    with a:
        a_value = st.number_input("Nhập số a:",step= 1,min_value=0, key= "key_a")
    with b:
        b_value = st.number_input("Nhập số b:",step= 1,min_value=0, key= "key_b")
        
    st.selectbox(label="Chọn phương pháp", options=["Encrypt", "Decrypt"], key="options")
    submit = st.form_submit_button("Submit")
    if submit:
        if st.session_state["options"] == "Encrypt":
            st.write("Bản giải mã : " )
            st.code(Affine.encrypt(text= text, a= a_value, b= b_value))
        if st.session_state["options"] == "Decrypt":
            st.write("Bản giải mã : " )
            st.code(Affine.decrypt(text= text, a= a_value, b= b_value))
        
            
    

# with st.form("Form 2"):
#     file = st.file_uploader("Upload file", type=["txt"])
#     key = st.number_input("Khóa K :", step=1, min_value=1, max_value=256)
#     st.selectbox(label="Chọn phương pháp", options=["Encrypt", "Decrypt"], key="options")
#     submit = st.form_submit_button("Submit")
#     if submit:
#         if st.session_state["options"] == "Encrypt":
#             if file is not None:
#                 content_encrypted = file.read().decode("utf-8")
#                 content = Affine.encrypt(text= text, a= a, b= b)
#         if st.session_state["options"] == "Decrypt":
#             if file is not None:
#                 content_decrypted = file.read().decode("utf-8")
#                 content = Affine.decrypt(text= text,a= a, b= b)
#         st.success("Mã hóa file thành công !!")
# if submit:
#     st.download_button(
#     label="Download",
#     data=content,
#     file_name="ban_ma.txt",
#     )




