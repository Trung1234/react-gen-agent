# frontend/ui/design_section.py
import streamlit as st

def render_design_section():
    st.header("1. Thiết kế & Yêu cầu")
    
    # Input yêu cầu text
    user_prompt = st.text_area(
        "Mô tả ý định (Prompt)", 
        placeholder="VD: Tạo một nút đăng nhập màu xanh, bo tròn, có icon...",
        height=100
    )
    
    st.subheader("Dữ liệu Visual (JSON)")
    st.caption("Đây là dữ liệu cấu trúc UI từ Canvas (giả lập)")
    
    # Giả lập visual context bằng một JSON mẫu
    default_visual = """{
    "component_type": "Button",
    "props": {
        "label": "Đăng Nhập",
        "color": "blue",
        "size": "large"
    },
    "layout": "center"
}"""
    
    visual_json = st.text_area(
        "Visual Context JSON",
        value=default_visual,
        height=150
    )
    
    return user_prompt, visual_json