# frontend/ui/code_section.py
import streamlit as st

def render_code_section(response_data):
    st.header("2. Kết quả Code & Test Case")

    if response_data.get("status") == "success":
        # Lấy dữ liệu từ response
        react_code = response_data.get("react_code", "")
        test_code = response_data.get("playwright_test_code", "")

        # --- Layout 2 cột ---
        col_react, col_test = st.columns([1, 1])

        # Cột trái: React Component
        with col_react:
            st.subheader("🧩 React Component")
            if react_code:
                st.code(react_code, language="jsx")
            else:
                st.warning("Không có React code nào được sinh ra.")

        # Cột phải: Playwright Test Case
        with col_test:
            st.subheader("🧪 Playwright Test Case")
            if test_code:
                st.code(test_code, language="typescript")
                
                # Nút tiện ích copy code test
                if st.button("📋 Copy Test Code", key="copy_test"):
                    st.toast("Đã copy code test vào clipboard!", icon="✅")
            else:
                st.info("Test Agent chưa tạo được test case.")

        # --- Logs Debug ---
        with st.expander("🔍 Xem Logs xử lý (Internal)"):
            for log in response_data.get("logs", []):
                st.text(log)

    else:
        st.error(f"Có lỗi xảy ra: {response_data.get('error_message')}")