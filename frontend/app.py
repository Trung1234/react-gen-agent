# frontend/app.py
import streamlit as st
import json

# Import các thành phần
from ui.design_section import render_design_section
from ui.code_section import render_code_section
from ui.test_section import render_test_section
from services.api_service import generate_react_code

# Cấu hình trang
st.set_page_config(
    page_title="AI React Agent Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI React Code Generator (Figma-like)")

# Sidebar
with st.sidebar:
    st.title("Cài đặt")
    st.write("Backend đang chạy ở: ``")

# Main Layout: Chia 2 cột
col1, col2 = st.columns([1, 1])

with col1:
    # --- CỘT TRÁI: INPUT ---
    prompt, visual_json_str = render_design_section()
    
    # Nút Generate
    if st.button("🚀 Generate Code", type="primary", use_container_width=True):
        if not prompt:
            st.warning("Vui lòng nhập mô tả!")
        else:
            # Cố gắng parse JSON visual
            try:
                visual_context = json.loads(visual_json_str)
            except json.JSONDecodeError:
                st.error("Dữ liệu Visual JSON không hợp lệ!")
                visual_context = {}
            
            # Gọi API Service
            with st.spinner("AI đang suy nghĩ và viết code..."):
                result = generate_react_code(prompt, visual_context)
                
                # Lưu kết quả vào session_state để hiển thị ở cột phải
                st.session_state['last_result'] = result

with col2:
    # --- CỘT PHẢI: OUTPUT ---
    # Kiểm tra xem có kết quả trong session không
    if 'last_result' in st.session_state:
        render_code_section(st.session_state['last_result'])
        render_test_section()
    else:
        st.info("Nhập thông tin và bấm Generate để xem kết quả.")