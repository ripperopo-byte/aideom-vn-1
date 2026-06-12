# AIDEOM-VN — Dashboard Streamlit

## Cách chạy (local)
```bash
pip install -r requirements.txt
streamlit run app.py
```
Mở trình duyệt tại http://localhost:8501

## Đưa lên Streamlit Community Cloud (miễn phí)
1. Đẩy toàn bộ thư mục này lên một GitHub repo (Public).
2. Vào share.streamlit.io → New app → chọn repo → Main file = `app.py` → Deploy.

## Cấu trúc
- `app.py` — trang chủ (tổng quan + 4 chỉ số + biểu đồ bong bóng)
- `pages/` — 12 bài + trang Tổng hợp & Kết luận (thanh điều hướng bên trái)
- `aideom_lib.py` — toàn bộ nội dung phân tích + bố cục dùng chung
- `charts/` — 20 biểu đồ PNG


