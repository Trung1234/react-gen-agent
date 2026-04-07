# backend/services/selenium_service.py
import os
import base64
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import io

# Template HTML cơ bản để chạy React code (sử dụng Babel để biên dịch JSX ngay trên trình duyệt)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <style>
        body {{ margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f3f4f6; }}
        #root {{ border: 1px solid #e5e7eb; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <div id="root"></div>
    <script type="text/babel">
        {code}
        
        // Tự động render component cuối cùng
        const root = ReactDOM.createRoot(document.getElementById('root'));
        
        // Cố gắng tìm component export default để render
        // (Đây là logic đơn giản hóa để demo)
        try {{
            root.render(<App />);
        }} catch (e) {{
            console.error("Render error:", e);
            document.getElementById('root').innerHTML = '<div style="color:red">Lỗi render: ' + e.message + '</div>';
        }}
    </script>
</body>
</html>
"""

def take_screenshot_of_react_code(react_code: str) -> str:
    """
    Chạy code React và chụp ảnh màn hình.
    Trả về chuỗi Base64 của ảnh.
    """
    # 1. Chuẩn bị nội dung HTML
    # Chúng ta bọc code trong một component App để đảm bảo nó chạy được
    wrapped_code = f"""
        const App = () => {{
            return (
                <div>
                    {react_code}
                </div>
            );
        }};
    """
    
    html_content = HTML_TEMPLATE.format(code=wrapped_code)
    
    # 2. Lưu file tạm
    temp_file = "temp_preview.html"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # 3. Cấu hình Chrome (Headless mode - không hiện cửa sổ)
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1024,768")
    
    driver = None
    try:
        # 4. Khởi tạo Driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # 5. Mở file
        file_path = os.path.abspath(temp_file)
        driver.get(f"file://{file_path}")
        
        # Chờ một chút để React render xong
        time.sleep(2) 
        
        # 6. Chụp màn hình
        screenshot = driver.get_screenshot_as_png()
        
        # 7. Convert sang Base64 để dễ gửi qua API
        img_base64 = base64.b64encode(screenshot).decode('utf-8')
        return img_base64
        
    except Exception as e:
        print(f"Lỗi Selenium: {e}")
        return ""
    finally:
        if driver:
            driver.quit()
        # Xóa file tạm (nếu muốn)
        # if os.path.exists(temp_file): os.remove(temp_file)