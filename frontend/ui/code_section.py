# frontend/ui/code_section.py
import streamlit as st

def render_code_section(response_data):
    st.header("2. Kết quả Code React")
    
    if response_data.get("status") == "success":
        code = response_data.get("code", "")
        
        # Hiển thị code
        st.code(code, language="jsx")
        
        # Nút copy (tính năng sẵn có của st.code khi bấm vào góc)
        
        # Hiển thị Logs (để debug quá trình AI)
        with st.expander("Xem Logs xử lý (AI Steps)"):
            for log in response_data.get("logs", []):
                st.text(log)
                
    else:
        st.error(f"Có lỗi xảy ra: {response_data.get('error_message')}")