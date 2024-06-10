import streamlit as st
import time
st.title('Đăng nhập')
username = st.text_input('Username', '')
password = st.text_input('Password', '', type='password')
if st.button('Đăng nhập'):
    if username == '21520703' and password == '2003':
        st.success('Đăng nhập thành công')
        js = """
        <script type="text/javascript">
            setTimeout(function() {
                window.location.href = 'http://www.uit.edu.vn/';
            }, 2000);
        </script>
        """
        st.markdown(js, unsafe_allow_html=True)
    else:
        st.error('Sai username hoặc password')

# Link web: https://21520703-cau2-2.streamlit.app/
