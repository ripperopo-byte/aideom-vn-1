# -*- coding: utf-8 -*-
"""Ba phần chuẩn theo ĐỀ BÀI cuối kỳ (BSA3035) cho 12 bài:
Mục tiêu học tập · Yêu cầu lập trình (Câu X.X.X) · Câu hỏi thảo luận chính sách.
Trích nguyên văn từ đề bài, không thay đổi số liệu phân tích của báo cáo.
"""

DETAIL = {
 1: dict(
   muctieu="Nắm vững dạng giải tích của hàm sản xuất Cobb-Douglas mở rộng (Mục 6 của bài báo), "
           "tính sản lượng kỳ vọng khi thêm các yếu tố mới là số hóa D, năng lực AI và vốn nhân lực số H, "
           "đồng thời thực hiện phân rã đóng góp tăng trưởng (growth accounting) trên dữ liệu Việt Nam 2020–2025.",
   yeucau=[
     "**Câu 1.4.1.** Đọc tệp `vietnam_macro_2020_2025.csv`; dùng numpy & pandas ước lượng TFP $A_t$ mỗi năm bằng cách giải ngược hàm sản xuất. Vẽ đồ thị $A_t$ theo năm và bình luận xu hướng.",
     "**Câu 1.4.2.** Lấy $A_t$ = trung bình A của 2020–2025, tính sản lượng dự báo $\\hat{Y}_t$ và so sánh với Y thực tế. Báo cáo MAPE.",
     "**Câu 1.4.3.** Phân rã tăng trưởng 2020–2025: trong tổng tăng trưởng GDP bình quân năm, K, L, D, AI, H và TFP đóng góp bao nhiêu %? Trình bày bảng và biểu đồ cột.",
     "**Câu 1.4.4.** Kịch bản 2030 (D = 30%, AI = 100 nghìn DN, H = 35%, K và L tăng đều 6%/năm, TFP tăng 1,2%/năm). Mô phỏng và dự báo GDP Việt Nam 2030.",
   ],
   thaoluan=[
     "**a)** TFP Việt Nam tăng hay giảm trong 2020–2025? Điều đó nói gì về chất lượng tăng trưởng?",
     "**b)** Trong các yếu tố mới D, AI, H, yếu tố nào đóng góp nhiều nhất cho tăng trưởng vừa qua? Vì sao?",
     "**c)** Mục tiêu 30% kinh tế số/GDP vào 2030 có khả thi theo mô hình này không? Cần ràng buộc gì?",
   ]),
 2: dict(
   muctieu="Xây dựng bài toán quy hoạch tuyến tính (LP) đơn giản với 4 biến quyết định và 5 ràng buộc, "
           "giải bằng `scipy.optimize.linprog` và `pulp`, đồng thời hiểu ý nghĩa của giá đối ngẫu (shadow price) trong phân tích chính sách.",
   yeucau=[
     "**Câu 2.4.1.** Giải bài toán bằng `scipy.optimize.linprog`. Báo cáo giá trị tối ưu và phân bổ tối ưu.",
     "**Câu 2.4.2.** Giải lại bằng `pulp` và in giá đối ngẫu (dual values) của từng ràng buộc; giải thích ý nghĩa chính sách của shadow price cho ràng buộc ngân sách tổng.",
     "**Câu 2.4.3.** Phân tích độ nhạy: tăng ngân sách tổng từ 100 lên 120, 140 nghìn tỷ. Vẽ đường cong $Z^*(B)$.",
     "**Câu 2.4.4.** Thêm ràng buộc ưu tiên nhân lực số $x_3 \\ge 30$. Bài toán còn khả thi không? $Z^*$ thay đổi thế nào?",
   ],
   thaoluan=[
     "**a)** Khi ngân sách tổng tăng 1 tỷ VND, GDP kỳ vọng tăng bao nhiêu? Đây có phải cận trên hợp lý của chi phí cơ hội vốn công?",
     "**b)** Vì sao R&D có hệ số tác động cao nhất nhưng lại có ràng buộc tối thiểu thấp nhất?",
     "**c)** Tỷ lệ 35% công nghệ chiến lược (AI + R&D) có khả thi khi ngân sách 2025 ưu tiên hạ tầng giao thông và an sinh xã hội?",
   ]),
 3: dict(
   muctieu="Áp dụng công thức chỉ số ưu tiên ngành (Mục 9 của bài báo), thực hành chuẩn hóa dữ liệu min-max, "
           "gán trọng số trên 10 ngành kinh tế Việt Nam và phân tích độ nhạy theo trọng số chính sách.",
   yeucau=[
     "**Câu 3.4.1.** Đọc dữ liệu, chuẩn hóa min-max cả 7 cột (lưu ý đảo dấu Risk). In ma trận đã chuẩn hóa.",
     "**Câu 3.4.2.** Tính $Priority_i$ với bộ trọng số mặc định; xếp hạng 10 ngành theo Priority giảm dần.",
     "**Câu 3.4.3.** Độ nhạy: thay đổi trọng số $a_6$ (AI Readiness) từ 0,05 đến 0,40 (chuẩn hóa lại tổng = 1). Top-3 có đổi không? Vẽ heatmap.",
     "**Câu 3.4.4.** So sánh hai bộ trọng số ‘Định hướng tăng trưởng’ và ‘Định hướng bao trùm’ — top-3 khác nhau thế nào?",
   ],
   thaoluan=[
     "**a)** Ba ngành nào nên ưu tiên chuyển đổi số và AI trước? Kết quả có phù hợp Nghị quyết 57-NQ/TW?",
     "**b)** Vì sao ngành Khai khoáng năng suất rất cao nhưng vẫn không nằm trong nhóm ưu tiên?",
     "**c)** Bộ trọng số nên do ai quyết định: chuyên gia kỹ thuật, hội đồng chính sách, hay đối thoại công khai? Thảo luận trên góc độ governance và tính chính danh chính sách.",
   ]),
 4: dict(
   muctieu="Xây dựng và giải bài toán LP cỡ vừa (~24–60 biến, 25 ràng buộc), biểu diễn ràng buộc công bằng vùng miền "
           "(Mục 7.3 của bài báo), thực hành PuLP và CVXPY để giải song song và đối chiếu kết quả.",
   yeucau=[
     "**Câu 4.4.1.** Cài đặt mô hình bằng PuLP, giải bằng solver CBC. In phân bổ tối ưu $x_{j,r}$ dạng ma trận 6×4 và $Z^*$.",
     "**Câu 4.4.2.** Cài đặt lại bằng CVXPY. So sánh kết quả với PuLP — hai phương pháp có giống nhau không?",
     "**Câu 4.4.3.** Vẽ heatmap phân bổ tối ưu. Vùng nào nhận nhiều ngân sách nhất? Hạng mục nào ưu tiên ở từng vùng?",
     "**Câu 4.4.4.** Đối chiếu với mô hình bỏ ràng buộc công bằng (bỏ C5). Chi phí kinh tế của công bằng vùng miền là bao nhiêu (tỷ VND GDP gain)?",
   ],
   thaoluan=[
     "**a)** Nếu bỏ ràng buộc công bằng, vốn chảy về vùng nào? Tại sao? Hậu quả xã hội dài hạn ra sao?",
     "**b)** Trần ngân sách mỗi vùng (C3) như một ‘chính sách phân quyền’ — làm giảm $Z^*$ bao nhiêu %? Mức giảm có chấp nhận được?",
     "**c)** Tây Nguyên có sàn 5.000 tỷ nhưng hệ số AI rất thấp (0,45). Nên đầu tư AI hay tập trung H và I trước? Mô hình trả lời thế nào?",
   ]),
 5: dict(
   muctieu="Xây dựng mô hình MIP với biến nhị phân (chọn dự án), biểu diễn ràng buộc loại trừ, ràng buộc tiên quyết "
           "(precedence) và ngân sách đa năm; dùng PuLP với CBC để giải bài toán knapsack tổng quát hóa.",
   yeucau=[
     "**Câu 5.4.1.** Cài đặt và giải bằng PuLP/CBC. Báo cáo dự án được chọn, tổng chi phí, tổng lợi ích, NPV biên ($Z^*$/chi phí).",
     "**Câu 5.4.2.** Nới ngân sách lên 100.000 tỷ. Tập dự án được chọn thay đổi thế nào?",
     "**Câu 5.4.3.** Quốc hội yêu cầu phải có cả P1 và P2 (redundancy). Bài toán còn khả thi không? $Z^*$ thay đổi ra sao?",
     "**Câu 5.4.4.** (Mở rộng) Thêm xác suất hoàn thành $p_i$ và tối đa hóa lợi ích kỳ vọng $E[Z]=\\sum p_i B_i y_i$.",
   ],
   thaoluan=[
     "**a)** Vì sao mô hình bỏ qua P15 (Open Data) dù tỷ suất lợi ích/chi phí rất cao? Đây có phải kết quả mong muốn về chính sách?",
     "**b)** Ràng buộc bắt buộc P14 (an ninh mạng) có làm giảm $Z^*$ không? Việc bắt buộc này có hợp lý?",
     "**c)** P8 (AI quốc gia) và P13 (bán dẫn) có lợi ích cộng hưởng — làm thế nào để mô hình hóa hiệu ứng này?",
   ]),
 6: dict(
   muctieu="Thành thạo ra quyết định đa tiêu chí (MCDM) – TOPSIS: chuẩn hóa ma trận quyết định, tính khoảng cách Euclide "
           "đến phương án lý tưởng tốt/xấu, và dùng phương pháp Entropy để xác định trọng số khách quan thay vì chủ quan.",
   yeucau=[
     "**Câu 6.4.1.** Cài đặt TOPSIS từ đầu bằng numpy với trọng số chuyên gia. Tính $C_i^*$ và xếp hạng 6 vùng.",
     "**Câu 6.4.2.** Tính lại với trọng số khách quan bằng phương pháp Entropy. So sánh xếp hạng với câu 6.4.1.",
     "**Câu 6.4.3.** Độ nhạy: tăng/giảm $w_{AI}$ từ 0,10 đến 0,40. Top-3 có ổn định không?",
     "**Câu 6.4.4.** (Mở rộng) Cài thêm AHP đơn giản để so sánh với TOPSIS (có thể dùng scikit-criteria).",
   ],
   thaoluan=[
     "**a)** Vùng nào dẫn đầu theo trọng số chuyên gia? Đây có phải vùng nên triển khai trung tâm AI quốc gia đầu tiên?",
     "**b)** Khi dùng trọng số Entropy, vùng nào thay đổi xếp hạng lớn nhất? Vì sao?",
     "**c)** TOPSIS giả định độc lập tuyến tính — AI Readiness và Internet penetration tương quan cao ảnh hưởng thế nào? Đề xuất cách xử lý.",
     "**d)** Theo QĐ 127/QĐ-TTg, chọn 3 vùng nào đặt trung tâm AI? Có cần thêm tiêu chí địa – chính trị?",
   ]),
 7: dict(
   muctieu="Hiểu khác biệt giữa tối ưu đơn và đa mục tiêu; dựng bài toán 4 mục tiêu xung đột (tăng trưởng, bao trùm, "
           "môi trường, an ninh dữ liệu), giải bằng NSGA-II của pymoo, vẽ và phân tích mặt Pareto, chọn nghiệm thỏa hiệp bằng TOPSIS/compromise programming.",
   yeucau=[
     "**Câu 7.4.1.** Cài bằng pymoo: lớp `ElementwiseProblem` với 24 biến, 4 mục tiêu; NSGA-II `pop_size=100`, `n_gen=200`.",
     "**Câu 7.4.2.** Trích quần thể Pareto cuối; vẽ scatter 3D ($f_1,f_2,f_3$) và biểu đồ song song (parallel coordinates) cho 4 mục tiêu.",
     "**Câu 7.4.3.** Áp TOPSIS lên tập Pareto để chọn một nghiệm thỏa hiệp với trọng số (0,40 tăng trưởng; 0,25 bao trùm; 0,20 môi trường; 0,15 an ninh).",
     "**Câu 7.4.4.** Phân tích chi phí cơ hội: nghiệm tăng trưởng cao nhất hi sinh bao nhiêu % bao trùm và môi trường so với nghiệm thỏa hiệp?",
   ],
   thaoluan=[
     "**a)** Đánh đổi giữa tăng trưởng và bao trùm có rõ không? Nó nói gì về cơ cấu kinh tế Việt Nam?",
     "**b)** Trọng số (0,40; 0,25; 0,20; 0,15) có phản ánh đúng ưu tiên hiện tại (Đại hội XIII)? Điều chỉnh thế nào cho phù hợp COP26 và QĐ 127?",
     "**c)** Vai trò của NSGA-II khác gì LP đơn mục tiêu? Nó có thay được quyết định chính trị?",
   ]),
 8: dict(
   muctieu="Xây dựng và giải bài toán quy hoạch phi tuyến động liên thời gian với phương trình động học của vốn, "
           "hàm Cobb-Douglas và ràng buộc tích lũy nhân lực số (Mục 7.2), bằng CVXPY (NLP convex) hoặc scipy.optimize, so sánh với phương trình Bellman.",
   yeucau=[
     "**Câu 8.3.1.** Hai lựa chọn: (A) log-linearize và giải bằng CVXPY (`geo_mean`/`log`); (B) giải bằng `scipy.optimize.minimize` (SLSQP).",
     "**Câu 8.3.2.** Vẽ quỹ đạo tối ưu của K, D, AI, H, Y, C theo thời gian 2026–2035.",
     "**Câu 8.3.3.** Phân tích cú sốc: 2028 $Y$ giảm 8% so kế hoạch (như bão Yagi 2024). Mô hình điều chỉnh phân bổ ra sao?",
     "**Câu 8.3.4.** So sánh ‘đầu tư trải đều’ và ‘đầu tư front-load’. Welfare tổng nào cao hơn? Vì sao?",
   ],
   thaoluan=[
     "**a)** Quỹ đạo K, D, AI, H ‘front-loaded’ hay ‘back-loaded’? Vì sao mô hình đề xuất như vậy?",
     "**b)** Tỷ lệ đầu tư AI/H theo thời gian có ổn định không? Mô hình ngụ ý đào tạo nhân lực nên đi trước hay đồng thời với đầu tư AI?",
     "**c)** $\\rho = 0,97$ ngụ ý quan tâm dài hạn. Nếu $\\rho = 0,90$ kết quả đổi thế nào? Đây có phải lý do chính phủ thường ‘dưới đầu tư’ R&D?",
   ]),
 9: dict(
   muctieu="Xây dựng mô hình mô phỏng cấu trúc việc làm Việt Nam dưới tác động tự động hóa và AI (Mục 10), "
           "tính NetJob ròng theo từng ngành, xác định ngưỡng đầu tư đào tạo lại tối thiểu để không mất việc ròng, và đề xuất chính sách lao động.",
   yeucau=[
     "**Câu 9.4.1.** Cài bằng PuLP/CVXPY (bài toán tuyến tính). In phân bổ tối ưu ($x_{AI}, x_H$) mỗi ngành; tính NetJob ròng từng ngành và tổng.",
     "**Câu 9.4.2.** Tìm ngưỡng đầu tư đào tạo $x_H$ tối thiểu ở ngành 2 (CN chế biến chế tạo) để $NetJob_2 \\ge 0$ ngay cả khi đầu tư AI tối đa.",
     "**Câu 9.4.3.** Mô phỏng tác động đến nhóm dễ tổn thương (ngành 1, 3, 4). Vẽ biểu đồ Sankey luồng dịch chuyển lao động.",
     "**Câu 9.4.4.** (Mở rộng) Thêm ràng buộc ‘không ngành nào mất quá 5% lao động’ ($DisplacedJob_i \\le 0,05 L_i$). Bài toán còn khả thi?",
   ],
   thaoluan=[
     "**a)** Ngành nào cần đầu tư đào tạo lại nhiều nhất theo kết quả tối ưu? Có khớp cảm nhận thực tế ở Việt Nam?",
     "**b)** Tài chính – Ngân hàng nguy cơ thay thế 52% nhưng tạo việc mới rất cao — mô hình khuyến nghị chiến lược gì?",
     "**c)** Có nên đầu tư $x_{AI}$ vào Nông – Lâm – Thủy sản không, khi hệ số tạo việc AI thấp (8,5) mà lao động dịch chuyển lại lớn?",
     "**d)** ‘Tốc độ tự động hóa không vượt quá năng lực đào tạo lại’ được biểu diễn bằng ràng buộc nào? Em đề xuất bổ sung ràng buộc an sinh nào?",
   ]),
 10: dict(
   muctieu="Xây dựng bài toán quy hoạch ngẫu nhiên hai giai đoạn (here-and-now + recourse), giải bằng scenario "
           "decomposition trên Pyomo + GLPK/CBC, và đánh giá Value of Stochastic Solution (VSS) cùng Expected Value of Perfect Information (EVPI).",
   yeucau=[
     "**Câu 10.5.1.** Cài bằng Pyomo (Set, Param, Var cho first-stage và second-stage). Giải bằng GLPK/CBC. Báo cáo quyết định first-stage tối ưu.",
     "**Câu 10.5.2.** Giải deterministic từng kịch bản. So sánh first-stage giữa lời giải kỳ vọng (EV) và lời giải stochastic (SP).",
     "**Câu 10.5.3.** Tính VSS và EVPI; giải thích ý nghĩa (VSS = lợi ích của tư duy bất định, EVPI = giá trị của thông tin hoàn hảo).",
     "**Câu 10.5.4.** (Mở rộng) Robust optimization (cực tiểu hóa regret kịch bản xấu nhất). So sánh quyết định với SP.",
   ],
   thaoluan=[
     "**a)** So với lời giải xác định, lời giải SP đầu tư H nhiều hơn hay ít hơn? Vì sao?",
     "**b)** VSS dương nói gì về giá trị của tư duy xác suất trong hoạch định chính sách Việt Nam?",
     "**c)** COVID-19 và bão Yagi là các cú sốc thực tế — liệu Việt Nam có đang ‘dưới đầu tư’ vào nhân lực số như một hàng hóa bảo hiểm?",
   ]),
 11: dict(
   muctieu="Hiểu và cài đặt mô hình học tăng cường tabular Q-learning (Mục 11) cho phân bổ ngân sách thích nghi, "
           "mô hình hóa nền kinh tế Việt Nam như một MDP, huấn luyện chính sách $\\pi^*$ qua nhiều episode và so sánh với chính sách rule-based.",
   yeucau=[
     "**Câu 11.3.1.** Cài môi trường gymnasium kế thừa `Env` (reset, step, action_space, observation_space). Một episode = 10 năm.",
     "**Câu 11.3.2.** Q-learning với $\\alpha=0,1$, $\\gamma=0,95$, epsilon-greedy giảm từ 1,0 xuống 0,05 qua 10.000 episodes.",
     "**Câu 11.3.3.** Trích $\\pi^*(s)=\\arg\\max_a Q(s,a)$. Báo cáo hành động tại các trạng thái khởi đầu (VN 2026 và 4 trạng thái giả định).",
     "**Câu 11.3.4.** So sánh phần thưởng tích lũy của $\\pi^*$ với 3 chính sách rule-based (luôn $a_1$; luôn $a_3$; ngẫu nhiên). Vẽ learning curve.",
     "**Câu 11.3.5.** (Mở rộng) Thay tabular bằng Deep Q-Network (stable-baselines3, 2 lớp ẩn 64 units). Có cải thiện?",
   ],
   thaoluan=[
     "**a)** Khi GDP thấp, D thấp, U cao — $\\pi^*$ chọn hành động gì? Có khớp ‘quick win’?",
     "**b)** Khi GDP cao, AI cao, U thấp — chính sách chọn gì? Có phù hợp ‘consolidation’?",
     "**c)** ‘AI không thay thế quyết định chính trị – xã hội’ — tích hợp $\\pi^*$ vào quy trình hoạch định chính sách thế nào để không vi phạm nguyên tắc này?",
   ]),
 12: dict(
   muctieu="Đồ án tổng kết: tích hợp các kỹ thuật Bài 1–11 thành hệ thống AIDEOM-VN đầy đủ 6 module (Mục 14) "
           "với một dashboard trực quan hỗ trợ ra quyết định trên 5 kịch bản chính sách (Mục 15).",
   yeucau=[
     "**M1–M5.** Mỗi module viết bằng Python thành file `.py` độc lập, có docstring và unit test (pytest).",
     "**M6 (Dashboard).** Web bằng Streamlit/Plotly Dash, tối thiểu 4 tab: Tổng quan · Phân bổ · Kịch bản so sánh · Cảnh báo rủi ro.",
     "**Bộ test.** Chạy được ít nhất 3 kịch bản (S1, S3, S5) và so sánh kết quả 2030 trên một bảng tổng hợp.",
     "**Bàn giao.** Mã nguồn ≥1.500 dòng trên GitHub (README + requirements.txt); báo cáo 15–25 trang; slide + video demo.",
   ],
   thaoluan=[
     "**S1–S5.** So sánh định lượng 5 kịch bản: Truyền thống · Số hóa nhanh · AI dẫn dắt · Bao trùm số · Tối ưu cân bằng.",
     "**Đánh đổi.** Kịch bản nào tối ưu GDP 2030? Cái giá về công bằng, môi trường, an ninh dữ liệu của mỗi kịch bản?",
     "**Khuyến nghị.** Từ bảng tổng hợp KPI, đề xuất hướng phân bổ nguồn lực phù hợp ưu tiên phát triển của Việt Nam.",
   ]),
}
