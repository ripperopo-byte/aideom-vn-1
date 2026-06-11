# -*- coding: utf-8 -*-
# Khoi "Phan tich chuyen sau" + mo phong what-if cho 12 bai AIDEOM-VN
import streamlit as st
try:
    import plotly.graph_objects as go
    import numpy as np
    _OK = True
except Exception:
    _OK = False

NAVY = "#14213d"; BLUE = "#2563eb"; CYAN = "#06b6d4"; GOLD = "#f59e0b"
GREEN = "#16a34a"; RED = "#dc2626"; GRAY = "#64748b"; LIGHT = "#dbe3ef"


def _fig(fig, h=330):
    fig.update_layout(height=h, margin=dict(l=12, r=12, t=34, b=12),
                      paper_bgcolor="white", plot_bgcolor="white",
                      font=dict(family="Inter, system-ui", size=13, color=NAVY),
                      legend=dict(orientation="h", y=1.12, x=0))
    fig.update_xaxes(showgrid=True, gridcolor="#eef1f6", zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="#eef1f6", zeroline=False)
    return fig


def _norm(a):
    a = np.array(a, dtype=float)
    lo, hi = a.min(), a.max()
    if hi - lo < 1e-9:
        return np.ones_like(a)
    return (a - lo) / (hi - lo)


# =============================== MO PHONG ===============================
def _sim3():
    sec = ["CNTT-TT", "Tai chinh-NH", "Che bien CB", "Logistics", "Y te", "Giao duc"]
    ai = np.array([0.95, 0.80, 0.55, 0.45, 0.60, 0.50])
    gdp = np.array([0.70, 0.85, 0.90, 0.60, 0.50, 0.40])
    w = st.slider("Trong so cho TIEM NANG AI (con lai cho DONG GOP GDP)", 0.0, 1.0, 0.5, 0.05, key="d3w")
    comp = w * ai + (1 - w) * gdp
    order = np.argsort(-comp)
    names = [sec[i] for i in order]; vals = [comp[i] for i in order]
    cols_ = [GOLD if i == 0 else BLUE for i in range(len(names))]
    fig = go.Figure(go.Bar(x=vals, y=names, orientation="h", marker_color=cols_,
                           text=[f"{v:.3f}" for v in vals], textposition="outside"))
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(_fig(fig), use_container_width=True)
    st.metric("Nganh uu tien so 1", names[0], f"chi so {vals[0]:.3f}")
    st.caption("Tang trong so AI keo nhom cong nghe len; ha xuong thi nhom dong gop GDP truyen thong vuon len.")


def _sim4():
    lam = st.slider("Muc rang buoc CONG BANG vung (%)", 0, 100, 40, 5, key="d4l")
    base, fair = 68750.0, 52485.0
    welf = base - (base - fair) * (lam / 100.0)
    minshare = 8.0 + (20.0 - 8.0) * (lam / 100.0)
    xs = np.linspace(0, 100, 41)
    ys = base - (base - fair) * (xs / 100.0)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", line=dict(color=BLUE, width=3), name="Tong phuc loi"))
    fig.add_trace(go.Scatter(x=[lam], y=[welf], mode="markers", marker=dict(color=GOLD, size=14), name="Diem chon"))
    st.plotly_chart(_fig(fig), use_container_width=True)
    c1, c2 = st.columns(2)
    c1.metric("Tong phuc loi", f"{welf:,.0f}", f"{welf - base:,.0f} so voi khong rang buoc")
    c2.metric("Ty trong vung yeu nhat", f"{minshare:.1f}%")
    st.caption("Cang siet cong bang, tong phuc loi cang giam nhung khoang cach vung cang hep. Chi phi cong bang toi da ~23,7%.")


def _sim5():
    costs = np.array([12, 8, 15, 6, 10, 9, 14, 7, 11, 5, 13, 8, 10, 6, 9], dtype=float)
    vals = np.array([22, 14, 30, 9, 18, 15, 26, 11, 20, 7, 24, 13, 17, 8, 16], dtype=float)
    B = st.slider("Ngan sach dau tu (nghin ty dong)", 40, 130, 80, 5, key="d5b")
    ratio = vals / costs
    order = np.argsort(-ratio)
    rem, tot, cnt, chosen = float(B), 0.0, 0, []
    for i in order:
        if costs[i] <= rem:
            rem -= costs[i]; tot += vals[i]; cnt += 1; chosen.append(i)
    pick = np.zeros(len(costs))
    for i in chosen:
        pick[i] = 1
    labels = [f"P{i+1}" for i in range(len(costs))]
    cols_ = [GREEN if pick[i] else LIGHT for i in range(len(costs))]
    fig = go.Figure(go.Bar(x=labels, y=vals, marker_color=cols_))
    st.plotly_chart(_fig(fig), use_container_width=True)
    c1, c2 = st.columns(2)
    c1.metric("So du an duoc chon", f"{cnt}/15")
    c2.metric("Tong gia tri (diem)", f"{tot:.0f}")
    st.caption("Mo hinh balo 0/1: tang ngan sach mo khoa them du an nhung loi ich bien giam dan.")


def _sim6():
    reg = ["DB Song Hong", "Dong Nam Bo", "Bac Trung Bo", "Tay Nguyen", "DBSCL", "Trung du MN"]
    expert = np.array([0.9493, 0.8799, 0.3718, 0.1903, 0.0966, 0.0201])
    entropy = np.array([0.62, 0.91, 0.45, 0.30, 0.55, 0.10])
    a = st.slider("Pha tron: 0 = Entropy khach quan  ...  1 = Chuyen gia", 0.0, 1.0, 0.5, 0.05, key="d6a")
    final = a * expert + (1 - a) * entropy
    order = np.argsort(-final)
    names = [reg[i] for i in order]; vals = [final[i] for i in order]
    cols_ = [GOLD if i == 0 else CYAN for i in range(len(names))]
    fig = go.Figure(go.Bar(x=vals, y=names, orientation="h", marker_color=cols_,
                           text=[f"{v:.3f}" for v in vals], textposition="outside"))
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(_fig(fig), use_container_width=True)
    st.metric("Vung dan dau", names[0], f"diem {vals[0]:.3f}")
    st.caption("Khi nghieng ve Entropy, trong so doi theo do phan tan du lieu nen thu hang co the dao so voi chuyen gia.")


def _sim8():
    rho = st.slider("He so chiet khau rho (uu tien hien tai thap -> cao)", 0.90, 0.99, 0.97, 0.01, key="d8r")
    t = np.arange(5)
    u_front = np.array([30, 28, 22, 15, 10], dtype=float)
    u_back = np.array([8, 14, 22, 30, 34], dtype=float)
    disc = rho ** t
    wf = float((u_front * disc).sum()); wb = float((u_back * disc).sum())
    fig = go.Figure()
    fig.add_trace(go.Bar(x=["Front-load (dau tu som)", "Back-load (dau tu muon)"],
                         y=[wf, wb], marker_color=[GOLD if wf >= wb else GRAY, GOLD if wb > wf else GRAY],
                         text=[f"{wf:.1f}", f"{wb:.1f}"], textposition="outside"))
    st.plotly_chart(_fig(fig), use_container_width=True)
    win = "Front-load" if wf >= wb else "Back-load"
    st.metric("Chien luoc toi uu o muc rho nay", win, f"chenh {abs(wf - wb):.1f}")
    st.caption("rho cao (kien nhan) uu ai dau tu som vi loi ich tuong lai it bi chiet khau; rho thap day ve back-load.")


def _sim9():
    a = st.slider("Toc do ung dung AI trong nen kinh te (%)", 0, 100, 50, 5, key="d9a")
    sec = ["CNTT", "Tai chinh", "Che bien", "Ban le", "Nong-Lam"]
    base = np.array([11.29, 5.20, 3.10, 1.80, -0.20])
    created = base.clip(min=0) * (a / 50.0)
    displaced = np.array([1.2, 1.8, 1.4, 2.1, 0.6]) * (a / 50.0)
    net = created - displaced + base.clip(max=0) * (a / 50.0)
    cols_ = [GREEN if v >= 0 else RED for v in net]
    fig = go.Figure(go.Bar(x=sec, y=net, marker_color=cols_,
                           text=[f"{v:+.2f}" for v in net], textposition="outside"))
    st.plotly_chart(_fig(fig), use_container_width=True)
    st.metric("Viec lam rong toan nen (trieu)", f"{net.sum():+.2f}")
    if net.min() < 0:
        st.warning("Mot so nganh (vi du Nong-Lam, Ban le) chiu viec lam rong AM khi AI tang nhanh -> can dao tao lai.")


def _sim10():
    p = st.slider("Xac suat kich ban XAU xay ra (%)", 0, 60, 25, 5, key="d10p")
    c_here = 41.0
    base_cost = 78.0
    penalty = 90.0
    exp_cost = base_cost + (p / 100.0) * penalty
    vss = (p / 100.0) * penalty * 0.35
    xs = np.linspace(0, 60, 31)
    ys = base_cost + (xs / 100.0) * penalty
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", line=dict(color=RED, width=3), name="Chi phi ky vong"))
    fig.add_trace(go.Scatter(x=[p], y=[exp_cost], mode="markers", marker=dict(color=GOLD, size=14), name="Diem chon"))
    st.plotly_chart(_fig(fig), use_container_width=True)
    c1, c2 = st.columns(2)
    c1.metric("Chi phi ky vong", f"{exp_cost:.1f}")
    c2.metric("Gia tri loi giai ngau nhien (VSS)", f"{vss:.1f}")
    st.caption("Rui ro cang lon, gia tri cua viec lap ke hoach co tinh den bat dinh (VSS) cang cao -> nen mua bao hiem / du phong.")


def _sim12():
    b = st.slider("Pha tron muc tieu: 0 = BAO TRUM  ...  1 = TANG TRUONG", 0.0, 1.0, 0.5, 0.05, key="d12b")
    sc = ["S1", "S2", "S3", "S4", "S5"]
    gdp = np.array([20133.54, 18970.96, 18026.91, 20082.49, 20205.52])
    inc = np.array([0.55, 0.70, 0.82, 0.68, 0.78])
    score = b * _norm(gdp) + (1 - b) * inc
    order = np.argsort(-score)
    names = [sc[i] for i in order]; vals = [score[i] for i in order]
    cols_ = [GOLD if i == 0 else NAVY for i in range(len(names))]
    fig = go.Figure(go.Bar(x=names, y=vals, marker_color=cols_,
                           text=[f"{v:.2f}" for v in vals], textposition="outside"))
    st.plotly_chart(_fig(fig), use_container_width=True)
    st.metric("Kich ban thang", names[0], f"diem tong hop {vals[0]:.2f}")
    st.caption("Nghieng ve tang truong thi kich ban GDP cao thang; nghieng ve bao trum thi kich ban can bang (S3/S5) vuon len.")


SIMX = {3: _sim3, 4: _sim4, 5: _sim5, 6: _sim6, 8: _sim8, 9: _sim9, 10: _sim10, 12: _sim12}


# =============================== NOI DUNG CHUYEN SAU ===============================
# Moi bai: phuongphap, thamso[], buoc[], donhay (header + rows), chinhsach
DEEP = {
  1: dict(
    phuongphap="Ham san xuat Cobb-Douglas mo rong Y = A . K^alpha . L^beta . D^gamma . AI^delta . H^theta, lay logarit hai ve roi hoi quy OLS de uoc luong cac he so co gian, sau do dung hach toan tang truong (growth accounting) tach phan dong gop cua tung yeu to vao toc do tang GDP.",
    thamso=[
      "alpha, beta: do co gian cua von va lao dong truyen thong",
      "gamma: dong gop cua so hoa du lieu (D)",
      "delta: dong gop cua von AI; theta: dong gop cua von nhan luc (H)",
      "A (TFP): nang suat tong hop, phan tang truong khong giai thich duoc bang yeu to dau vao",
    ],
    buoc=[
      "Buoc 1 - Kiem tra TFP tang deu tu 27,7 len 34,9 cho thay tien bo cong nghe la dong luc nen.",
      "Buoc 2 - Phan ra cho thay TFP chiem ~49% tang truong, von vat chat ~32%, con AI va H cong lai ~9%.",
      "Buoc 3 - Du bao 2030: neu D=30, AI=100, H=35 thi GDP tien sat 12.847 (MAPE chi 6,42% nen du bao dang tin).",
    ],
    donhay=(["Kich ban", "Gia dinh", "Tac dong GDP 2030"],
            [["Co so", "TFP +1,2%/nam", "12.847"],
             ["Lac quan", "TFP +1,8%/nam", "~13.400"],
             ["Than trong", "TFP +0,6%/nam", "~12.300"]]),
    chinhsach="Vi delta va theta nho, dau tu AI ma khong dau tu nhan luc H se cho hieu qua thap: 'AI khong co H la von chet'. Nghi quyet 57-NQ/TW nen uu tien dong thoi ha tang AI va dao tao ky nang so.",
  ),
  2: dict(
    phuongphap="Quy hoach tuyen tinh (LP): toi da hoa Z = 0,85.x1 + 1,20.x2 + 0,95.x3 + 1,35.x4 voi rang buoc tong ngan sach = 100 va san toi thieu cho tung linh vuc. Giai bang scipy.optimize.linprog / PuLP va doc gia mo (shadow price) tu nghiem doi ngau.",
    thamso=[
      "x1..x4: ty trong ngan sach phan bo cho 4 linh vuc",
      "He so muc tieu: hieu qua bien cua moi dong von dau tu",
      "Gia mo (shadow price): GDP tang them khi noi long mot don vi rang buoc",
    ],
    buoc=[
      "Buoc 1 - Nghiem toi uu don ngan sach ve x4 (he so 1,35 cao nhat) cho toi khi cham tran/san khac.",
      "Buoc 2 - Z* = 112,25; gia mo cua ngan sach = 1,35 nghia la +1 don vi ngan sach -> +1,35 GDP.",
      "Buoc 3 - Cac san toi thieu (25/15/20) dang 'rang buoc chat', neu noi long se cai thien Z.",
    ],
    donhay=(["Thay doi", "Z* moi", "Nhan xet"],
            [["Ngan sach +10", "~125,8", "theo gia mo 1,35"],
             ["San x3 -5", "~116,0", "giai phong von hieu qua hon"],
             ["San x1 +5", "~106,5", "buoc von vao noi loi thap"]]),
    chinhsach="Linh vuc he so cao nhung bi giu san thap dang lam giam hieu qua tong. Khi phan bo 35% cho cong nghiep chien luoc can can nhac chi phi co hoi nay theo dung tinh than uu tien dong luc moi cua NQ57.",
  ),
  3: dict(
    phuongphap="Xay dung chi so uu tien tong hop bang chuan hoa min-max tung tieu chi roi cong co trong so. Xep hang nganh/linh vuc theo diem tong hop de dinh huong phan bo nguon luc.",
    thamso=[
      "Trong so tieu chi: phan anh uu tien chinh sach (AI vs dong gop GDP vs viec lam)",
      "Gia tri chuan hoa min-max: dua moi tieu chi ve thang 0-1 de so sanh cong bang",
    ],
    buoc=[
      "Buoc 1 - Chuan hoa moi tieu chi ve [0,1] de loai bo chenh lech don vi.",
      "Buoc 2 - Diem tong hop tu 0,7446 (cao nhat) xuong 0,0489 cho thay phan tang ro ret giua nhom dau va cuoi.",
      "Buoc 3 - Keo trong so AI len lam nhom cong nghe vuot len; nguoc lai nhom dong gop GDP truyen thong dan dau.",
    ],
    donhay=(["Trong so AI", "Nganh dan dau", "Ham y"],
            [["0,2", "Nhom dong gop GDP", "uu tien on dinh"],
             ["0,5", "Can bang", "trung dung"],
             ["0,8", "Nhom cong nghe AI", "uu tien dot pha"]]),
    chinhsach="Viec ai dat trong so la quyet dinh chinh tri - ky tri. Bo tieu chi va trong so nen cong khai, minh bach theo tinh than du lieu mo cua NQ57 de tranh thien lech nhom loi ich.",
  ),
  4: dict(
    phuongphap="LP phan bo nguon luc theo vung co them rang buoc cong bang (chenh lech giua vung cao nhat va thap nhat khong vuot nguong). Giai bang PuLP/CVXPY, danh doi giua tong phuc loi va do dong deu.",
    thamso=[
      "lambda: muc siet cong bang vung",
      "Tran nguon luc tung vung C3...",
      "Ty trong vung yeu nhat: thuoc do bao trum",
    ],
    buoc=[
      "Buoc 1 - Khong rang buoc cong bang: tong phuc loi dat 68.750 nhung lech vung lon.",
      "Buoc 2 - Siet cong bang toi da: phuc loi giam con 52.485, tuc chi phi cong bang 16.265 (23,66%).",
      "Buoc 3 - Quan he gan tuyen tinh: moi % cong bang tang doi mot phan phuc loi giam.",
    ],
    donhay=(["Muc cong bang", "Tong phuc loi", "Ty trong vung yeu"],
            [["0%", "68.750", "~8%"],
             ["40%", "~62.244", "~12,8%"],
             ["100%", "52.485", "~20%"]]),
    chinhsach="Bo rang buoc cong bang don von ve vung manh (Dong Nam Bo, DB Song Hong). Tay Nguyen va vung kho khan can suat dau tu AI/H rieng de khong bi bo lai - phu hop dinh huong phat trien bao trum.",
  ),
  5: dict(
    phuongphap="Quy hoach nguyen nhi phan (MIP) dang bai toan balo 0/1: chon tap du an toi da hoa gia tri trong gioi han ngan sach 80.000. Giai bang PuLP/OR-Tools; o day minh hoa bang heuristic theo ty le gia tri/chi phi.",
    thamso=[
      "Bien nhi phan: chon (1) hay khong (0) tung du an P1..P15",
      "Ngan sach B: rang buoc tong chi phi",
      "Ty le gia tri/chi phi: tieu chi xep uu tien greedy",
    ],
    buoc=[
      "Buoc 1 - Sap xep du an theo ty le loi ich/chi phi giam dan.",
      "Buoc 2 - Lan luot chon den khi het ngan sach; gia tri tang theo bac thang.",
      "Buoc 3 - Loi ich bien giam dan: moi lan tang ngan sach mo khoa du an kem hap dan hon.",
    ],
    donhay=(["Ngan sach", "So du an", "Tong gia tri"],
            [["60", "~7", "~115"],
             ["80", "~9", "~150"],
             ["100", "~11", "~178"]]),
    chinhsach="Cap ngan sach hop ly nam o vung loi ich bien con cao. P15 (Open Data) va P14 (an ninh) nen duoc uu tien vi tao cong huong he thong - dung tinh than ha tang du lieu quoc gia cua NQ57.",
  ),
  6: dict(
    phuongphap="TOPSIS ket hop trong so Entropy: Entropy do luong do phan tan thong tin de gan trong so khach quan, TOPSIS xep hang phuong an theo khoang cach toi giai phap ly tuong duong/am. So sanh voi trong so chuyen gia.",
    thamso=[
      "alpha: muc pha tron giua trong so chuyen gia va Entropy",
      "Diem TOPSIS: cang gan 1 cang tot",
      "Trong so Entropy: tu dong cao cho tieu chi phan biet manh",
    ],
    buoc=[
      "Buoc 1 - Tinh trong so Entropy tu ma tran quyet dinh chuan hoa.",
      "Buoc 2 - Theo trong so chuyen gia, Dong Nam Bo va DB Song Hong dan dau (0,95 va 0,88).",
      "Buoc 3 - Khi nghieng ve Entropy, thu hang co the dao do tieu chi nhieu thong tin duoc nhan manh.",
    ],
    donhay=(["Pha tron", "Vung dan dau", "Ham y"],
            [["Entropy (0)", "Theo do phan tan du lieu", "khach quan"],
             ["Can bang (0,5)", "Dong Nam Bo", "on dinh"],
             ["Chuyen gia (1)", "Dong Nam Bo", "theo kinh nghiem"]]),
    chinhsach="Ket hop Entropy giup giam thien lech chu quan khi chon 3 vung trong diem theo Quyet dinh 127. Nen cong bo ca hai cach tinh trong so de quyet dinh minh bach.",
  ),
  7: dict(
    phuongphap="Toi uu da muc tieu bang thuat toan tien hoa NSGA-II (pymoo) voi 4 muc tieu (tang truong, bao trum, ben vung, viec lam). Ket qua la mat truoc Pareto; dung TOPSIS de chon mot nghiem dai dien.",
    thamso=[
      "Mat truoc Pareto: tap nghiem khong bi tro troi",
      "Trong so muc tieu: phan anh uu tien Dai hoi XIII va cam ket COP26",
      "Gini/chi so bao trum: thuoc do cong bang",
    ],
    buoc=[
      "Buoc 1 - NSGA-II sinh quan the va tien hoa de phu mat truoc Pareto.",
      "Buoc 2 - GDP tren mat truoc trai tu 26.987 den 69.773 di kem Gini tang 0,81 -> 1,92 (danh doi ro).",
      "Buoc 3 - Nghiem can bang (GDP 28.548; Gini 0,84) duoc TOPSIS chon lam khuyen nghi.",
    ],
    donhay=(["Uu tien", "GDP", "Gini"],
            [["Tang truong", "~69.773", "1,92"],
             ["Can bang", "~28.548", "0,84"],
             ["Bao trum", "~26.987", "0,81"]]),
    chinhsach="Khong co nghiem 'tot nhat tuyet doi' - lua chon tren Pareto la quyet dinh gia tri. Trong so muc tieu nen bam sat dinh huong tang truong nhanh va ben vung, cong bang xa hoi cua Dai hoi XIII va COP26.",
  ),
  8: dict(
    phuongphap="Toi uu dong nhieu giai doan (dynamic optimization) bang CVXPY/SLSQP: chon lo trinh dau tu AI va H qua thoi gian de toi da phuc loi chiet khau theo he so rho.",
    thamso=[
      "rho: he so chiet khau (kien nhan voi tuong lai)",
      "Lo trinh front-load vs back-load",
      "Phuc loi chiet khau: tong l023 uu thoi gian",
    ],
    buoc=[
      "Buoc 1 - Voi rho cao (0,97), loi ich tuong lai it bi chiet khau -> uu tien dau tu som (front-load).",
      "Buoc 2 - Voi rho thap, hien tai duoc coi trong hon -> nghieng ve back-load.",
      "Buoc 3 - So sanh phuc loi hai lo trinh tai moi rho de chon diem chuyen.",
    ],
    donhay=(["rho", "Lo trinh toi uu", "Ghi chu"],
            [["0,90", "Can nhac back-load", "chiet khau manh"],
             ["0,97", "Front-load", "dau tu som"],
             ["0,99", "Front-load manh", "rat kien nhan"]]),
    chinhsach="Voi rho thuc te ~0,97, dau tu AI va H nen di som va dong thoi. Lui dau tu nhan luc lam giam phuc loi dai han - mot lan nua khang dinh 'AI khong co H la von chet'.",
  ),
  9: dict(
    phuongphap="Mo phong tac dong viec lam (NetJob) theo Muc 10: voi moi nganh, uoc luong viec lam tao moi tu AI tru di viec lam bi thay the, ra viec lam rong theo toc do ung dung AI.",
    thamso=[
      "Toc do ung dung AI: bien dieu khien chinh",
      "Viec tao moi vs viec bi thay the theo nganh",
      "Viec lam rong (net): tong tac dong",
    ],
    buoc=[
      "Buoc 1 - CNTT co viec lam rong duong rat lon (~11,29 trieu), keo tong toan nen len 13,99 trieu.",
      "Buoc 2 - Nong-Lam co viec lam rong am (~ -12.600) - nhom de bi ton thuong.",
      "Buoc 3 - Tang toc do AI khuech dai ca tao moi lan thay the; can nhin net tung nganh.",
    ],
    donhay=(["Toc do AI", "Viec lam rong", "Nganh am"],
            [["25%", "thap hon co so", "it ap luc"],
             ["50%", "~+14 trieu", "Nong-Lam"],
             ["100%", "cao nhung phan hoa", "Nong-Lam, Ban le"]]),
    chinhsach="Tai chinh co the mat ~52% viec lam thuong le, Nong-Lam chiu net am -> can chuong trinh dao tao lai (reskilling) va luoi an sinh truoc khi day nhanh ung dung AI.",
  ),
  10: dict(
    phuongphap="Quy hoach ngau nhien 2 giai doan (stochastic programming) bang Pyomo: quyet dinh giai doan 1 truoc khi biet kich ban, dieu chinh o giai doan 2. Tinh VSS va EVPI de luong gia tri thong tin.",
    thamso=[
      "p: xac suat kich ban xau",
      "VSS: gia tri cua loi giai ngau nhien so voi ke hoach tat dinh",
      "EVPI: gia tri ky vong cua thong tin hoan hao (= 1.567,5)",
    ],
    buoc=[
      "Buoc 1 - Quyet dinh giai doan 1 (stage1 = 8.000/8.000/41.000/8.000) duoc giu on dinh truoc bat dinh.",
      "Buoc 2 - Rui ro p cang cao, chi phi ky vong cang tang gan tuyen tinh.",
      "Buoc 3 - VSS duong cho thay tinh den bat dinh tot hon la gia dinh tat dinh.",
    ],
    donhay=(["p (kich ban xau)", "Chi phi ky vong", "VSS"],
            [["10%", "~87", "~3"],
             ["25%", "~100", "~7,9"],
             ["50%", "~123", "~15,8"]]),
    chinhsach="Voi cu soc kieu COVID-19 hay bao Yagi, gia tri du phong va bao hiem tang manh khi rui ro lon. Nen dau tu von nhan luc H lam 'dem giam soc' va lap quy du phong theo kich ban.",
  ),
  11: dict(
    phuongphap="Hoc tang cuong (Q-learning) tren mot MDP (gymnasium): tac nhan hoc chinh sach dau tu toi uu pi* qua thu-sai, toi da hoa phan thuong tich luy (GDP/phuc loi) dai han.",
    thamso=[
      "Trang thai: muc von AI, H, GDP hien tai",
      "Hanh dong: phan bo dau tu moi buoc",
      "Phan thuong tich luy: muc tieu hoc; episode: so vong huan luyen",
    ],
    buoc=[
      "Buoc 1 - Giai doan dau (GDP thap) chinh sach hoc duoc uu tien 'quick win' tao da.",
      "Buoc 2 - GDP cao chuyen sang consolidation (cung co, on dinh).",
      "Buoc 3 - Phan thuong hoi tu (tu ~17 len ~26) khi tang so episode huan luyen.",
    ],
    donhay=(["Episode", "Phan thuong", "Hanh vi chinh sach"],
            [["500", "thap, dao dong", "tham do"],
             ["2000", "~21", "on dinh dan"],
             ["5000", "~26", "hoi tu pi*"]]),
    chinhsach="pi* hoc duoc la cong cu tham chieu, khong thay the quyet dinh chinh tri. Ket hop bang chung tu RL voi muc tieu phat trien quoc gia giup dieu hanh thich ung theo tung giai doan.",
  ),
  12: dict(
    phuongphap="Do an tich hop 6 module M1-M6 (san xuat, phan bo, lua chon du an, da muc tieu, ngau nhien, dashboard) chay tren 5 kich ban S1-S5; danh gia bang phuc loi/GDP va do bao trum.",
    thamso=[
      "beta: pha tron giua muc tieu tang truong va bao trum",
      "GDP tung kich ban S1..S5",
      "Chi so bao trum: do dong deu/cong bang",
    ],
    buoc=[
      "Buoc 1 - GDP cac kich ban dao quanh 18.000-20.200; chenh lech khong qua lon ve quy mo.",
      "Buoc 2 - Khi can bang tang truong va bao trum, kich ban S5 thuong thang.",
      "Buoc 3 - Nghieng han ve tang truong co the day kich ban GDP cao nhat len dau bang.",
    ],
    donhay=(["Uu tien", "Kich ban thang", "Ghi chu"],
            [["Tang truong", "S5/S1", "GDP cao"],
             ["Can bang", "S5", "hai hoa"],
             ["Bao trum", "S3", "cong bang nhat"]]),
    chinhsach="Khuyen nghi chon kich ban can bang (S5): vua giu GDP cao vua dam bao bao trum. Bao cao 15-25 trang kem dashboard >=4 tab va ban giao GitHub theo dung yeu cau Phu luc.",
  ),
}


def _table(donhay):
    head, rows = donhay
    md = "| " + " | ".join(head) + " |\n"
    md += "|" + "|".join(["---"] * len(head)) + "|\n"
    for r in rows:
        md += "| " + " | ".join(str(x) for x in r) + " |\n"
    return md


def render_deep(n):
    d = DEEP.get(n)
    if not d and n not in SIMX:
        return
    st.write("")
    with st.expander("🔬 Phan tich chuyen sau", expanded=False):
        if d:
            st.markdown("**🧮 Phuong phap.** " + d["phuongphap"])
            st.markdown("**🔑 Y nghia tham so chinh**")
            for t in d["thamso"]:
                st.markdown("- " + t)
            st.markdown("**🪜 Doc ket qua theo buoc**")
            for b in d["buoc"]:
                st.markdown("- " + b)
            if d.get("donhay"):
                st.markdown("**📊 Bang do nhay (sensitivity)**")
                st.markdown(_table(d["donhay"]))
            st.markdown("**🏛️ Ham y chinh sach**")
            st.info(d["chinhsach"])
        if _OK and n in SIMX:
            st.markdown("---")
            st.markdown("**🎛️ Mo phong tuong tac (what-if)**")
            SIMX[n]()
        elif (not _OK) and n in SIMX:
            st.caption("Cai plotly va numpy de bat phan mo phong tuong tac.")
