import streamlit as st
import time
import webbrowser as wb
st.title('Đăng nhập')
username = st.text_input('Username', '')
password = st.text_input('Password', '', type='password')
if st.button('Đăng nhập'):
    if username == '21520703' and password == '2003':
        st.success('Đăng nhập thành công')
        time.sleep(2)
        wb.open('http://www.uit.edu.vn/')
    else:
        st.error('Sai username hoặc password')

# Link web: https://21520703-cau2-2.streamlit.app/
