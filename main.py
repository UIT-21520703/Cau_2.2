import streamlit as st
import time
import webbrowser as wb
st.title('Đăng nhập')
username = st.text_input('Username', '')
password = st.text_input('Password', '', type='password')
if st.button('Đăng nhập'):
    if username == '21520703' and password == '2003':
        st.success('Đăng nhập thành công')
        with st.spinner('Đang chuyển hướng...'):
            time.sleep(2)
        # Sử dụng st.markdown để chèn liên kết
        st.markdown('<meta http-equiv="refresh" content="0; url=http://www.uit.edu.vn/" />', unsafe_allow_html=True)
    else:
        st.error('Sai username hoặc password')

# Link web: https://21520703-cau2-2.streamlit.app/
