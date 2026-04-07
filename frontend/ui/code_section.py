# frontend/ui/code_section.py
import streamlit as st
import base64

def render_code_section(response_data):
    st.header("2. Kết quả Code React & Preview")
    
    if response_data.get("status") == "success":
        # --- Layout 2 cột nhỏ trong section này ---
        col_code, col_img = st.columns([1, 1])
        
        with col_code:
            st.subheader("Source Code")
            code = response_data.get("code", "")
            st.code(code, language="jsx")
            
        with col_img:
            st.subheader("Live Preview (Selenium)")
            img_b64 = response_data.get("preview_image_base64")
            
            if img_b64:
                # Decode base64 và hiển thị
                st.image(f"data:image/png;base64,{img_b64}", use_container_width=True)
            else:
                st.warning("Không thể chụp ảnh (Lỗi Selenium)")

        # Logs
        with st.expander("Xem Logs xử lý"):
            for log in response_data.get("logs", []):
                st.text(log)
                
    else:
        st.error(f"Có lỗi xảy ra: {response_data.get('error_message')}")