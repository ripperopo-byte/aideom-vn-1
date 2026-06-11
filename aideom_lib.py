# -*- coding: utf-8 -*-
"""Thư viện nội dung + bố cục dùng chung cho dashboard AIDEOM-VN.
Giữ NGUYÊN cách phân tích/diễn đạt của báo cáo để không phải sửa bài luận."""
import os
import streamlit as st

CHART_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")

META = {
    "sv": "Trần Đình Hướng", "msv": "23050491", "lop": "QH-2023-E KTPT 3",
    "gv": "TS. Phạm Văn Khánh", "hp": "BSA3035 · 2026",
}

# ---- Nội dung 12 bài (đồng bộ với bản web/Word) ----
BAI = {
 1: dict(code="01", nav="Bài 1 · Cobb-Douglas + AI", cap="Cấp độ 1 · Nền tảng",
   tag="Hàm sản xuất Cobb-Douglas mở rộng", headline="Khi số lượng lao động hết vai trò",
   formula="Y = A · K^α · L^β · D^γ · AI^δ · H^θ",
   stats=[("TFP 2020 → 2025","27,75 → 34,91"),("Sai số dự báo (MAPE)","6,42%"),
          ("Đóng góp TFP","49,08%"),("Đóng góp lao động L","−0,34%"),("GDP dự báo 2030","14.472,4")],
   reading="Gần một nửa tăng trưởng đến từ hiệu quả (TFP), không từ việc bơm thêm đầu vào. Đáng nói hơn cả là đóng góp âm của lao động: thêm người không còn tạo thêm GDP — cỗ máy tăng trưởng dựa vào số đông đã chạm trần.",
   insight="Dư địa tăng trưởng giờ nằm ở chất lượng — AI, nhân lực số, số hóa — chứ không còn ở việc tuyển thêm lao động phổ thông.",
   caveat="Chuỗi 6 năm khá ngắn, dễ đa cộng tuyến giữa D, AI, H; mô hình chưa có số hạng tương tác AI×H nên hơi dự báo thấp hai năm cuối.",
   charts=[("b01_tfp","Hình 1 · Năng suất tổng hợp TFP leo dốc đều suốt 2020–2025."),
           ("b01_decomp","Hình 2 · Phân rã đóng góp — lao động đã chuyển sang âm."),
           ("b01_gdp","Hình 3 · GDP thực bám sát dự báo, lệch nhẹ hai năm cuối.")]),
 2: dict(code="02", nav="Bài 2 · LP ngân sách số", cap="Cấp độ 1 · Nền tảng",
   tag="Quy hoạch tuyến tính", headline="Ngân sách đi về đâu, và với giá nào",
   formula="max Z = 1.2·x₁ + 1.5·x₂ + 0.9·x₃ + 1.8·x₄    ( Σx ≤ 100 )",
   stats=[("GDP tối ưu Z*","112,25"),("R&D (x₄)","40 — gấp 4 lần sàn"),
          ("Giá bóng ngân sách","1,35"),("Giá bóng sàn nhân lực","−0,40")],
   reading="Mỗi đồng ngân sách tăng thêm sinh 1,35 đồng GDP — nghĩa là chưa bão hòa, vẫn nên đầu tư. Nhưng giá bóng âm của các sàn xã hội tiết lộ một sự thật khó chịu: tối ưu thuần tài chính luôn muốn cắt giảm sàn nhân lực để dồn tiền cho R&D.",
   insight="Các sàn đầu tư xã hội cần được giữ như ràng buộc chính trị — không để phép tính sinh lợi xoá bỏ chúng.",
   caveat=None,
   charts=[("b02_alloc","Hình 4 · R&D hút phần lớn ngân sách tối ưu."),
           ("b02_shadow","Hình 5 · Giá bóng: ngân sách dương, các sàn xã hội âm.")]),
 3: dict(code="03", nav="Bài 3 · Chỉ số ưu tiên ngành", cap="Cấp độ 1 · Nền tảng",
   tag="Chỉ số ưu tiên ngành", headline="Ba ngành mũi nhọn tách tốp",
   formula=None,
   stats=[("CN chế biến chế tạo","0,7446"),("CNTT – Truyền thông","0,5138"),
          ("Tài chính – Ngân hàng","0,4554"),("Khai khoáng (cuối bảng)","0,0489")],
   reading="Khoảng cách giữa hạng nhất và hạng nhì (0,23) lớn hơn tổng điểm của năm ngành cuối cộng lại. Công nghiệp chế biến không đơn thuần đứng đầu mà vượt trội; ba ngành dẫn đầu góp 58,5% tổng điểm ưu tiên.",
   insight="Ưu tiên vốn cho cụm mũi nhọn, nhưng nhóm cuối bảng cần chính sách chuyển đổi riêng thay vì ép tăng tốc AI.",
   caveat=None,
   charts=[("b03_priority","Hình 6 · Ba ngành mũi nhọn bỏ xa phần còn lại.")]),
 4: dict(code="04", nav="Bài 4 · LP phân bổ theo vùng", cap="Cấp độ 2 · Phân bổ",
   tag="LP phân bổ vùng + ràng buộc công bằng", headline="Công bằng vùng miền có giá 23,7%",
   formula=None,
   stats=[("Có ràng buộc công bằng","52.485"),("Không ràng buộc","68.750"),
          ("Chi phí công bằng","16.265"),("Tỷ lệ đánh đổi","23,66%")],
   reading="Bỏ ràng buộc công bằng, mô hình dồn hết vốn vào Đông Nam Bộ và ĐB sông Hồng. Giữ công bằng không miễn phí: giá của nó là 16.265 tỷ GDP bỏ lỡ, tương đương gần một phần tư tiềm năng.",
   insight="Con số 23,66% nên được công khai trong tranh luận ngân sách để quyết định dựa trên bằng chứng, không phải cảm tính.",
   caveat=None,
   charts=[("b04_regions","Hình 7 · Cơ cấu phân bổ vốn cho sáu vùng."),
           ("b04_fairness","Hình 8 · Cái giá phải trả cho công bằng vùng miền.")]),
 5: dict(code="05", nav="Bài 5 · MIP chọn dự án", cap="Cấp độ 2 · Phân bổ",
   tag="Quy hoạch nguyên hỗn hợp (MIP)", headline="Chọn 9 trong 15 dự án — và còn dư tiền",
   formula=None,
   stats=[("Tổng NPV (Z*)","115.400"),("Chi phí sử dụng","59.700"),
          ("NPV / chi phí","1,933"),("Ngân sách còn dư","20.300")],
   reading="Mỗi đồng bỏ ra sinh gần hai đồng giá trị hiện tại ròng. Việc còn dư 20.300 tỷ cho thấy điểm thắt không nằm ở ngân sách mà ở tính ‘không chia nhỏ’ của dự án — không thể mua nửa dự án.",
   insight="Nên bổ sung các dự án quy mô nhỏ để hấp thụ phần ngân sách còn dư thay vì để lãng phí.",
   caveat=None,
   charts=[("b05_select","Hình 9 · Chín trong mười lăm dự án được chọn."),
           ("b05_mip","Hình 10 · NPV qua các kịch bản MIP.")]),
 6: dict(code="06", nav="Bài 6 · TOPSIS xếp hạng vùng", cap="Cấp độ 2 · Phân bổ",
   tag="TOPSIS đa tiêu chí", headline="Thứ hạng đầu bảng phụ thuộc cách chọn trọng số",
   formula=None,
   stats=[("ĐNB (chuyên gia)","0,9493"),("ĐBSH (entropy)","0,9374"),("Tây Nguyên (cả hai)","~0,02")],
   reading="Hai vùng dẫn đầu đổi ngôi khi đổi bộ trọng số — dấu hiệu thứ hạng top không phải sự thật khách quan. Nhưng Tây Nguyên luôn cuối bảng ở cả hai cách tính: kết luận này mới thực sự vững.",
   insight="Chỉ những kết luận bền với trọng số mới nên dùng để ưu tiên đầu tư bù đắp cho vùng yếu.",
   caveat=None,
   charts=[("b06_topsis","Hình 11 · Xếp hạng vùng đảo ngôi khi đổi bộ trọng số.")]),
 7: dict(code="07", nav="Bài 7 · Pareto NSGA-II", cap="Cấp độ 3 · Đánh đổi",
   tag="Tối ưu đa mục tiêu NSGA-II", headline="Một trăm lời giải, không lời nào ‘đúng’ tuyệt đối",
   formula="max GDP · min Gini · min CO₂ · min Risk",
   stats=[("GDP trải từ","26.987 → 69.773"),("Gini trải từ","0,81 → 1,92"),
          ("Nghiệm thỏa hiệp #4","GDP 28.548 / Gini 0,84")],
   reading="Muốn GDP cao nhất phải chấp nhận Gini gấp hơn hai lần. Nghiệm #4 nằm đúng ở ‘khuỷu tay áo’ của đường cong — điểm mà mỗi điểm GDP tăng thêm bắt đầu phải trả giá bằng bất bình đẳng tăng nhanh.",
   insight="Mặt Pareto biến đánh đổi tăng trưởng–công bằng thành lựa chọn tường minh; quyết định cuối vẫn thuộc về ưu tiên chính trị.",
   caveat=None,
   charts=[("b07_pareto","Hình 12 · Mặt Pareto: đánh đổi giữa GDP và Gini.")]),
 8: dict(code="08", nav="Bài 8 · Tối ưu động", cap="Cấp độ 3 · Đánh đổi",
   tag="Tối ưu động 2026–2035", headline="Bằng chứng đầu tiên: AI đơn độc thua cuộc",
   formula=None,
   stats=[("Front-load","78,37"),("Trải đều","78,34"),("Bao trùm","78,27"),("AI-driven (thấp nhất)","78,13")],
   reading="Nghịch lý: chiến lược AI-driven tích lũy AI cao nhất (198 so với 108–138) nhưng phúc lợi thấp nhất, vì nó bỏ đói nhân lực (H chỉ 50). AI thiếu người vận hành thì không chuyển hóa được thành GDP.",
   insight="Đầu tư AI phải đi kèm đầu tư nhân lực số — đây là lần đầu con số nói thẳng: ‘AI không có H là vốn chết’.",
   caveat=None,
   charts=[("b08_dynamic","Hình 13 · Bốn chiến lược động — AI nhiều nhất nhưng phúc lợi thấp nhất.")]),
 9: dict(code="09", nav="Bài 9 · Dịch chuyển lao động", cap="Cấp độ 3 · Đánh đổi",
   tag="LP dịch chuyển lao động", headline="14 triệu việc mới, nhưng dồn vào một ngành",
   formula=None,
   stats=[("Tổng việc làm ròng","13.991.490"),("CNTT","11.292.640 (80,7%)"),
          ("Tài chính","937.400"),("Nông – Lâm – Thủy sản","−12.600")],
   reading="Hơn bốn phần năm việc làm mới tập trung vào CNTT — một rủi ro cơ cấu khi cả nền kinh tế dựa vào một ngành cho tăng trưởng việc làm. Riêng nông nghiệp mất việc ròng.",
   insight="Cần chương trình đào tạo lại có mục tiêu cho lao động nông nghiệp, không chỉ ăn mừng con số tổng dương.",
   caveat=None,
   charts=[("b09_netjobs","Hình 14 · Việc làm ròng dồn vào CNTT (thang log).")]),
 10: dict(code="10", nav="Bài 10 · Quy hoạch ngẫu nhiên", cap="Cấp độ 4 · Bất định",
   tag="Quy hoạch ngẫu nhiên 2 giai đoạn", headline="Đầu tư AI là quyết định vững trước mọi kịch bản",
   formula=None,
   stats=[("Nghiệm stochastic Z_SP","92.185"),("Wait-and-see Z_WS","93.752,5"),
          ("Giá trị thông tin EVPI","1.567,5 (1,7%)"),("Đầu tư AI giai đoạn 1","41.000")],
   reading="AI nhận phần lớn nhất ngay khi chưa biết tương lai (gấp năm lần mỗi hạng mục khác). EVPI chỉ 1,7% nghĩa là có dự báo hoàn hảo cũng không đáng giá bao nhiêu — bất định ở đây không đắt.",
   insight="Không cần chờ ‘hết mưa mới đi’: đầu tư AI nên triển khai ngay, không treo chờ thêm thông tin.",
   caveat=None,
   charts=[("b10_sp","Hình 15 · Phân bổ giai đoạn một và các giá trị thông tin.")]),
 11: dict(code="11", nav="Bài 11 · Q-learning", cap="Cấp độ 4 · Bất định",
   tag="Học tăng cường Q-learning", headline="Chính sách thích nghi đánh bại mọi công thức cố định",
   formula=None,
   stats=[("Chính sách tối ưu π*","26,11"),("Luôn cân bằng (a₁)","22,17"),
          ("Ngẫu nhiên","21,32"),("Luôn AI-driven (a₃)","17,02")],
   reading="π* vượt chiến lược cố định tốt nhất 17,8% vì nó đổi hành động theo từng trạng thái. Chiến lược AI cứng nhắc lại tệ hơn cả ngẫu nhiên. Với Việt Nam 2026, π* khuyên chọn hành động cân bằng.",
   insight="Chính sách nên điều chỉnh theo giai đoạn phát triển, không áp một công thức chung cho mọi thời điểm.",
   caveat=None,
   charts=[("b11_qlearn","Hình 16 · Đường cong học và so sánh chính sách."),
           ("b11_pie","Hình 17 · Phân bố hành động tối ưu trên 81 trạng thái.")]),
 12: dict(code="12", nav="Bài 12 · AIDEOM tích hợp", cap="Cấp độ 4 · Tích hợp",
   tag="Mô hình tích hợp AIDEOM-VN", headline="Kịch bản cân bằng thắng, AI đơn độc thua",
   formula=None,
   stats=[("S5 – Cân bằng (thắng)","20.205,52"),("S1 – Truyền thống","20.133,54"),
          ("S4 – Bao trùm","20.082,49"),("S3 – AI dẫn dắt (thấp nhất)","18.026,91")],
   reading="Kịch bản cân bằng cho GDP cao nhất; kịch bản AI đơn độc thấp hơn tới 10,8%. Kết luận này khớp chính xác với Bài 08 và Bài 11 — ba phương pháp độc lập cùng chỉ một hướng.",
   insight="Sự phối hợp đồng bộ AI – nhân lực – hạ tầng vượt trội mọi hướng đi chuyên biệt.",
   caveat=None,
   charts=[("b12_scenarios","Hình 18 · GDP 2030 — kịch bản cân bằng dẫn đầu."),
           ("b12_ready","Hình 19 · Sẵn sàng AI của 10 ngành.")]),
}

NGANH = [
  ("CN chế biến chế tạo","0,7446","55","Tự động hóa dây chuyền + nâng tay nghề; ưu tiên vốn hàng đầu"),
  ("CNTT – Truyền thông","0,5138","88","Đầu tàu tạo việc (80,7% NetJobs); mở rộng đào tạo lập trình"),
  ("Tài chính – NH – BH","0,4554","72","Sẵn sàng cao nhưng rủi ro 52%; kiểm soát tự động hóa"),
  ("Bán buôn – bán lẻ","0,3244","48","Số hóa chuỗi cung ứng; tái bố trí lao động"),
  ("Logistics – Vận tải","0,3111","42","Tối ưu tuyến bằng AI; đào tạo vận hành"),
  ("Giáo dục – Đào tạo","0,1662","38","Hạ tầng cung kỹ năng số cho toàn nền kinh tế"),
  ("Y tế","0,1409","45","AI hỗ trợ chẩn đoán; giữ người trong vòng quyết định"),
  ("Xây dựng","0,1131","20","Số hóa thiết kế và quản lý; rủi ro thấp"),
  ("Nông – Lâm – Thủy sản","0,1109","15","NetJobs âm (−12.600); ưu tiên đào tạo lại và nền số"),
  ("Khai khoáng","0,0489","30","Quy mô nhỏ; tự động hóa an toàn, không mở rộng"),
]

THESES = [
  "**AI không có nhân lực là vốn chết.** Ba bài dùng ba phương pháp khác nhau (tối ưu động, học tăng cường, mô phỏng kịch bản) cùng cho một kết quả: đầu tư AI đơn độc luôn thua chiến lược cân bằng.",
  "**Tăng trưởng đã chuyển từ lượng sang chất.** Lao động đóng góp âm, TFP chiếm gần một nửa — dư địa nằm ở năng suất và nhân tố số.",
  "**Công bằng có giá đo được.** 16.265 tỷ (23,7%) cho công bằng vùng; mặt Pareto cho đánh đổi GDP–Gini. Quyết định nên dựa trên con số.",
  "**Chính sách tốt là chính sách thích nghi.** Chính sách học theo trạng thái đánh bại mọi công thức cố định — nên điều chỉnh theo giai đoạn thay vì áp cứng.",
]

_CSS = """
<style>
:root{--accent:#b5482b;--accent2:#1f6f5c;--navy:#1b2a4a;}
.block-container{max-width:1050px;padding-top:2.2rem}
h1,h2,h3{font-family:Georgia,'Times New Roman',serif;color:#1b2a4a}
.tagchip{display:inline-block;font-size:12px;letter-spacing:.05em;text-transform:uppercase;
  color:#1f6f5c;border:1px solid #1f6f5c;border-radius:999px;padding:3px 12px;margin-bottom:6px}
.eyebrow{font-size:12.5px;letter-spacing:.2em;text-transform:uppercase;color:#b5482b;font-weight:700}
.formula{background:#1b2a4a;color:#eef3ff;border-radius:10px;padding:11px 15px;
  font-family:'JetBrains Mono',Consolas,monospace;font-size:15px;margin:6px 0 2px}
.reading{font-size:17px;line-height:1.7}
</style>
"""

def _sidebar():
    st.sidebar.markdown(
        "### 🇻🇳 AIDEOM-VN\n*Ra quyết định kinh tế trong kỷ nguyên AI*\n\n---\n"
        f"**SV:** {METuple()}\n\n📊 Dữ liệu: NSO · MoST · MIC · MPI · WB · GII 2025\n\n"
        "🛠️ Phân tích từ mã nguồn Google Colab (12 bài).")

def METuple():
    return f"{META['sv']} — {META['msv']} — {META['lop']}"

def _charts(charts):
    imgs = [c for c in charts]
    i = 0
    if len(imgs) % 2 == 1:
        f, cap = imgs[0]
        st.image(os.path.join(CHART_DIR, f + ".png"), caption=cap, use_container_width=True)
        i = 1
    while i < len(imgs):
        c1, c2 = st.columns(2)
        f1, cap1 = imgs[i]
        with c1:
            st.image(os.path.join(CHART_DIR, f1 + ".png"), caption=cap1, use_container_width=True)
        if i + 1 < len(imgs):
            f2, cap2 = imgs[i + 1]
            with c2:
                st.image(os.path.join(CHART_DIR, f2 + ".png"), caption=cap2, use_container_width=True)
        i += 2

def render_bai(n):
    m = BAI[n]
    st.set_page_config(layout="wide", page_title=f"AIDEOM-VN · {m['nav']}", page_icon="📊")
    st.markdown(_CSS, unsafe_allow_html=True)
    _sidebar()
    st.markdown(f"<div class='eyebrow'>{m['cap']}</div>", unsafe_allow_html=True)
    st.markdown(f"<span class='tagchip'>{m['tag']}</span>", unsafe_allow_html=True)
    st.markdown(f"## {m['code']} — {m['headline']}")
    if m.get("formula"):
        st.markdown(f"<div class='formula'>{m['formula']}</div>", unsafe_allow_html=True)
    st.write("")
    cols = st.columns(len(m["stats"]))
    for col, (lab, val) in zip(cols, m["stats"]):
        col.metric(lab, val)
    st.write("")
    _charts(m["charts"])
    st.markdown("#### Đọc con số")
    st.markdown(f"<div class='reading'>{m['reading']}</div>", unsafe_allow_html=True)
    st.success(f"**Hàm ý.** {m['insight']}")
    if m.get("caveat"):
        st.caption(f"⚠️ Giới hạn: {m['caveat']}")

def render_home():
    st.set_page_config(layout="wide", page_title="AIDEOM-VN", page_icon="📊")
    st.markdown(_CSS, unsafe_allow_html=True)
    _sidebar()
    st.markdown("<div class='eyebrow'>Báo cáo cuối kỳ · BSA3035</div>", unsafe_allow_html=True)
    st.title("Mô hình AIDEOM-VN")
    st.markdown("*Mười hai mô hình định lượng trả lời một câu hỏi: Việt Nam nên phân bổ "
                "nguồn lực thế nào trong kỷ nguyên trí tuệ nhân tạo?*")
    c = st.columns(4)
    c[0].metric("TFP tăng 2020–2025", "+25,8%")
    c[1].metric("GDP dự báo 2030", "14.472", "nghìn tỷ")
    c[2].metric("Việc làm ròng do AI", "14,0 triệu")
    c[3].metric("Giá của công bằng vùng", "23,7%")
    st.write("")
    st.image(os.path.join(CHART_DIR, "ov_bubble.png"),
             caption="Bản đồ sẵn sàng AI × rủi ro × quy mô lao động của 10 ngành.",
             use_container_width=True)
    st.markdown(
        "AIDEOM-VN không cố dự báo tương lai một cách tuyệt đối. Nó làm một việc khiêm tốn hơn "
        "nhưng hữu dụng hơn: biến những lựa chọn chính sách thường được tranh luận bằng cảm tính "
        "thành những con số có thể đặt lên bàn cân. Mười hai bài tập đi từ dễ đến khó, mỗi cấp độ "
        "bóc tách một lớp câu hỏi: đâu là động lực tăng trưởng, phân bổ ra sao cho công bằng, "
        "cân nhắc đánh đổi nào, và quyết định thế nào khi tương lai bất định.")
    st.info("👈 Chọn từng bài ở thanh điều hướng bên trái. Trang **Tổng hợp & Kết luận** ở cuối "
            "gói gọn bản đồ 10 ngành và bốn luận điểm.")

def render_ketluan():
    st.set_page_config(layout="wide", page_title="AIDEOM-VN · Kết luận", page_icon="📊")
    st.markdown(_CSS, unsafe_allow_html=True)
    _sidebar()
    st.markdown("<div class='eyebrow'>Tổng hợp chính sách</div>", unsafe_allow_html=True)
    st.title("Bản đồ chiến lược 10 ngành")
    st.markdown("Gộp ba lăng kính — ưu tiên (Bài 03), sẵn sàng AI (Bài 12) và việc làm ròng "
                "(Bài 09) — thành một khuyến nghị cho từng ngành.")
    import pandas as pd
    df = pd.DataFrame(NGANH, columns=["Ngành", "Priority", "Sẵn sàng AI", "Hướng chiến lược"])
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.success("**Điểm mấu chốt.** Ba ngành đầu bảng chiếm 58,5% tổng điểm ưu tiên. Nhưng "
               "Nông – Lâm, dù điểm thấp, lại cần can thiệp khẩn cấp nhất vì là ngành duy nhất "
               "mất việc ròng và đang nuôi 13,2 triệu lao động.")
    st.markdown("## Bốn điều 12 mô hình cùng nói")
    for i, t in enumerate(THESES, 1):
        st.markdown(f"**{i}.** {t}")
    st.caption("Về độ tin cậy: nhiều chênh lệch thắng–thua khá nhỏ (Bài 08 chênh 0,3%, Bài 12 "
               "chênh 0,36%) nằm trong biên sai số mô hình, nên hiểu là ‘không thua’ hơn là "
               "‘thắng rõ’. Điểm mạnh nằm ở tính nhất quán: cùng một kết luận xuất hiện độc lập "
               "qua nhiều phương pháp.")
