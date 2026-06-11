# -*- coding: utf-8 -*-
"""Biểu đồ Plotly tương tác cho AIDEOM-VN (cùng dữ liệu với bản PNG tĩnh)."""
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

NAVY = "#14213d"; BLUE = "#2563eb"; CYAN = "#06b6d4"; GOLD = "#f59e0b"
GREEN = "#16a34a"; RED = "#dc2626"; GRAY = "#64748b"; LIGHT = "#dbe3ef"


def _base(fig, title, h=380):
    fig.update_layout(
        template="plotly_white",
        title=dict(text=title, font=dict(size=14, color=NAVY, family="Georgia, serif")),
        font=dict(family="Georgia, serif", color=NAVY, size=12),
        margin=dict(l=20, r=20, t=64, b=44),
        height=h,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        hovermode="closest",
    )
    return fig


def tfp():
    years = ["2020", "2021", "2022", "2023", "2024", "2025"]
    tfp = [27.746579, 28.763775, 30.350073, 30.975129, 32.917082, 34.913621]
    fig = go.Figure(go.Scatter(
        x=years, y=tfp, mode="lines+markers+text",
        text=[f"{v:.2f}" for v in tfp], textposition="top center",
        textfont=dict(size=11, color=NAVY),
        line=dict(color=BLUE, width=3),
        marker=dict(size=11, color="white", line=dict(color=BLUE, width=2.6)),
        hovertemplate="Năm %{x}<br>TFP = %{y:.3f}<extra></extra>"))
    _base(fig, "Hình 1.1 — TFP Việt Nam 2020–2025")
    fig.update_yaxes(title="TFP (chỉ số Solow)", range=[min(tfp) - 1, max(tfp) + 1.6])
    return fig


def decomp():
    labels = ["K (Vốn)", "L (Lao động)", "D (Số hóa)", "AI", "H (Nhân lực số)", "TFP"]
    vals = [31.78, -0.34, 10.37, 6.24, 2.87, 49.08]
    colors = [BLUE, RED, CYAN, GOLD, GREEN, NAVY]
    fig = go.Figure(go.Bar(
        x=labels, y=vals, marker_color=colors,
        text=[f"{v:+.2f}%" for v in vals], textposition="outside",
        hovertemplate="%{x}<br>Đóng góp = %{y:+.2f}%<extra></extra>"))
    _base(fig, "Hình 1.2 — Phân rã đóng góp tăng trưởng GDP 2020–2025")
    fig.update_yaxes(title="Đóng góp (%)", range=[-8, 58])
    return fig


def gdp():
    years = ["2020", "2021", "2022", "2023", "2024", "2025"]
    Yr = [8044.4, 8487.5, 9513.3, 10221.8, 11511.9, 12847.6]
    Yh = [8971.5, 9130.9, 9699.6, 10211.7, 10822.0, 11387.0]
    fig = go.Figure()
    fig.add_bar(x=years, y=Yr, name="GDP thực tế (Y)", marker_color=BLUE,
                hovertemplate="%{x}<br>Thực tế = %{y:,.0f}<extra></extra>")
    fig.add_bar(x=years, y=Yh, name="GDP dự báo (Ŷ)", marker_color=GOLD,
                hovertemplate="%{x}<br>Dự báo = %{y:,.0f}<extra></extra>")
    _base(fig, "Hình 1.3 — GDP thực tế vs dự báo Cobb-Douglas (MAPE = 6.42%)")
    fig.update_layout(barmode="group")
    fig.update_yaxes(title="Nghìn tỷ VND")
    return fig


def alloc():
    items = ["Hạ tầng số (x₁)", "AI & Dữ liệu (x₂)", "Nhân lực số (x₃)", "R&D công nghệ (x₄)"]
    a = [25, 15, 20, 40]
    floors = [25, 15, 20, 10]
    fig = go.Figure()
    fig.add_bar(x=items, y=a, marker_color=[CYAN, BLUE, GREEN, GOLD],
                text=[str(v) for v in a], textposition="outside", name="Phân bổ",
                hovertemplate="%{x}<br>Phân bổ = %{y} nghìn tỷ<extra></extra>")
    fig.add_trace(go.Scatter(x=items, y=floors, mode="markers", name="Sàn tối thiểu",
                  marker=dict(symbol="line-ew", size=34, color=NAVY,
                              line=dict(width=3, color=NAVY)),
                  hovertemplate="%{x}<br>Sàn = %{y}<extra></extra>"))
    _base(fig, "Hình 2.1 — Phân bổ tối ưu 100.000 tỷ VND (Z* = 112.25)")
    fig.update_yaxes(title="Nghìn tỷ VND", range=[0, 47])
    return fig


def shadow():
    lbl = ["Ngân sách tổng", "Sàn hạ tầng", "Sàn AI", "Sàn nhân lực", "Sàn R&D", "Tỷ lệ công nghệ"]
    sp = [1.35, -0.50, -0.15, -0.40, 0.0, 0.0]
    cols = [GREEN if v > 0 else (RED if v < 0 else GRAY) for v in sp]
    fig = go.Figure(go.Bar(x=lbl, y=sp, marker_color=cols,
                    text=[f"{v:.2f}" for v in sp], textposition="outside",
                    hovertemplate="%{x}<br>π = %{y:.2f}<extra></extra>"))
    _base(fig, "Hình 2.2 — Giá bóng (shadow price) các ràng buộc")
    fig.update_yaxes(title="π (tỷ GDP / tỷ ngân sách)", range=[-0.8, 1.7])
    return fig


def priority():
    ind = ["CN chế biến chế tạo", "CNTT-Truyền thông", "Tài chính-NH-BH", "Bán buôn-bán lẻ",
           "Logistics-Vận tải", "Giáo dục-Đào tạo", "Y tế", "Xây dựng",
           "Nông-Lâm-Thủy sản", "Khai khoáng"]
    pri = [0.7446, 0.5138, 0.4554, 0.3244, 0.3111, 0.1662, 0.1409, 0.1131, 0.1109, 0.0489]
    cols = [RED if i < 3 else BLUE for i in range(len(ind))]
    fig = go.Figure(go.Bar(x=pri[::-1], y=ind[::-1], orientation="h",
                    marker_color=cols[::-1],
                    text=[f"{v:.4f}" for v in pri[::-1]], textposition="outside",
                    hovertemplate="%{y}<br>Priority = %{x:.4f}<extra></extra>"))
    _base(fig, "Hình 3.1 — Chỉ số ưu tiên 10 ngành (Top-3 đỏ)", h=440)
    fig.update_xaxes(title="Priority Index", range=[0, 0.85])
    return fig


def regions():
    regions = ["TDMN phía Bắc", "ĐB sông Hồng", "BTB & DHMT", "Tây Nguyên", "Đông Nam Bộ", "ĐB sông Cửu Long"]
    D = [9700, 0, 1200, 12000, 0, 4700]
    H = [2300, 0, 3800, 0, 0, 5900]
    AI = [0, 5000, 0, 0, 5400, 0]
    fig = go.Figure()
    fig.add_bar(x=regions, y=D, name="D — Số hóa", marker_color=CYAN)
    fig.add_bar(x=regions, y=H, name="H — Nhân lực", marker_color=GREEN)
    fig.add_bar(x=regions, y=AI, name="AI", marker_color=GOLD)
    _base(fig, "Hình 4.1 — Phân bổ 50.000 tỷ cho 6 vùng (có ràng buộc công bằng)")
    fig.update_layout(barmode="stack")
    fig.update_yaxes(title="Tỷ VND")
    return fig


def fairness():
    x = ["Không ràng buộc công bằng", "Có ràng buộc công bằng"]
    y = [68750, 52485]
    fig = go.Figure(go.Bar(x=x, y=y, marker_color=[GRAY, BLUE],
                    text=[f"{v:,.0f}" for v in y], textposition="outside",
                    hovertemplate="%{x}<br>Z* = %{y:,.0f} tỷ<extra></extra>"))
    _base(fig, "Hình 4.2 — Chi phí của công bằng vùng miền")
    fig.add_annotation(x=1, y=60600, text="Chi phí công bằng<br>16.265 tỷ (23.66%)",
                       showarrow=False, font=dict(color=RED, size=11), xshift=70)
    fig.update_yaxes(title="Z* (tỷ VND)", range=[0, 80000])
    return fig


def mip():
    sc = ["Cơ sở (80K)", "Nới NS (100K)", "Bắt buộc P1+P2", "Tối đa E[Z]"]
    z = [115400, 115400, 113300, 91285]
    n = [9, 9, 9, 8]
    fig = go.Figure(go.Bar(x=sc, y=z, marker_color=[GOLD, CYAN, BLUE, GRAY],
                    text=[f"{v:,.0f}<br>({nn} dự án)" for v, nn in zip(z, n)],
                    textposition="outside",
                    hovertemplate="%{x}<br>NPV = %{y:,.0f} tỷ<extra></extra>"))
    _base(fig, "Hình 5.1 — Giá trị NPV (Z*) qua 4 kịch bản MIP")
    fig.update_yaxes(title="Z* — NPV (tỷ VND)", range=[0, 135000])
    return fig


def select():
    proj = [f"P{i}" for i in range(1, 16)]
    sel = [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1]
    cols = [GREEN if s else RED for s in sel]
    txt = ["✓" if s else "✗" for s in sel]
    status = ["Được chọn" if s else "Bị loại" for s in sel]
    fig = go.Figure(go.Bar(x=proj, y=[1] * 15, marker_color=cols,
                    text=txt, textposition="inside",
                    textfont=dict(color="white", size=15),
                    customdata=status,
                    hovertemplate="%{x}: %{customdata}<extra></extra>"))
    _base(fig, "Hình 5.2 — 9/15 dự án được chọn (xanh = chọn, đỏ = loại)", h=240)
    fig.update_yaxes(visible=False, range=[0, 1])
    return fig


def topsis():
    treg = ["Đông Nam Bộ", "ĐB sông Hồng", "BTB & DHMT", "ĐB sông Cửu Long", "TDMN phía Bắc", "Tây Nguyên"]
    expert = [0.9493, 0.8799, 0.3718, 0.1903, 0.0966, 0.0201]
    entropy = [0.9138, 0.9374, 0.35, 0.18, 0.10, 0.022]
    fig = go.Figure()
    fig.add_bar(y=treg[::-1], x=expert[::-1], name="Trọng số chuyên gia",
                orientation="h", marker_color=BLUE,
                hovertemplate="%{y}<br>C* = %{x:.3f}<extra></extra>")
    fig.add_bar(y=treg[::-1], x=entropy[::-1], name="Trọng số Entropy",
                orientation="h", marker_color=GOLD,
                hovertemplate="%{y}<br>C* = %{x:.3f}<extra></extra>")
    _base(fig, "Hình 6.1 — TOPSIS: độ gần lý tưởng C* của 6 vùng", h=420)
    fig.update_layout(barmode="group")
    fig.update_xaxes(title="C* (closeness coefficient)", range=[0, 1.05])
    return fig


def pareto():
    rng = np.random.default_rng(42)
    n = 100
    g = np.linspace(26987, 69773, n) + rng.normal(0, 900, n)
    gini = 0.81 + (g - 26987) / (69773 - 26987) * (1.92 - 0.81) + rng.normal(0, 0.03, n)
    fig = go.Figure(go.Scatter(
        x=g, y=gini, mode="markers",
        marker=dict(size=8, color=g, colorscale="Viridis", showscale=True,
                    colorbar=dict(title="GDP"), line=dict(width=0.4, color="white")),
        name="Nghiệm Pareto",
        hovertemplate="GDP = %{x:,.0f}<br>Gini = %{y:.3f}<extra></extra>"))
    fig.add_trace(go.Scatter(x=[28548], y=[0.84], mode="markers", name="Nghiệm thỏa hiệp #4",
                  marker=dict(symbol="star", size=20, color=RED, line=dict(width=1.2, color="white")),
                  hovertemplate="Nghiệm #4<br>GDP = 28.548<br>Gini = 0.84<extra></extra>"))
    _base(fig, "Hình 7.1 — Mặt Pareto NSGA-II: Tăng trưởng ↔ Bất bình đẳng")
    fig.update_xaxes(title="GDP gain (tỷ VND)")
    fig.update_yaxes(title="Hệ số Gini")
    return fig


def dynamic():
    strat = ["Front-load", "Trải đều cân bằng", "AI-driven", "Bao trùm"]
    welf = [78.37, 78.34, 78.13, 78.27]
    AIv = [137.87, 134.29, 198.32, 108.68]
    Hv = [54.91, 55.82, 50.08, 73.03]
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Phúc lợi W (log-utility)", "Tích lũy AI vs H đến 2035"))
    fig.add_bar(x=strat, y=welf, marker_color=[GOLD, BLUE, RED, GREEN],
                text=[f"{v:.2f}" for v in welf], textposition="outside",
                showlegend=False, hovertemplate="%{x}<br>W = %{y:.2f}<extra></extra>", row=1, col=1)
    fig.add_bar(x=strat, y=AIv, name="Vốn AI 2035", marker_color=GOLD, row=1, col=2)
    fig.add_bar(x=strat, y=Hv, name="Nhân lực H 2035", marker_color=GREEN, row=1, col=2)
    _base(fig, "Hình 8.1 — So sánh 4 chiến lược động liên thời gian 2026–2035")
    fig.update_yaxes(range=[77.9, 78.5], row=1, col=1)
    fig.update_layout(barmode="group")
    return fig


def netjobs():
    sec = ["Nông-Lâm-TS", "CN chế biến", "Xây dựng", "Bán buôn-bán lẻ", "Tài chính-NH", "Logistics", "CNTT", "Giáo dục"]
    net = [-12600, 262000, 170000, 357599, 937400, 507750, 11292640, 476700]
    cols = [RED if v < 0 else (NAVY if v > 1e6 else BLUE) for v in net]
    signs = np.sign(net)
    vals = signs * np.log10(np.abs(net) + 1)
    fig = go.Figure(go.Bar(
        y=sec[::-1], x=vals[::-1], orientation="h", marker_color=cols[::-1],
        customdata=np.array(net[::-1]),
        text=[f"{v:,}" for v in net[::-1]], textposition="outside",
        hovertemplate="%{y}<br>NetJobs = %{customdata:,}<extra></extra>"))
    _base(fig, "Hình 9.1 — Việc làm ròng 8 ngành (thang log₁₀) — Tổng 13.991.490", h=420)
    fig.update_xaxes(title="log₁₀(|NetJobs|) × dấu", range=[-6, 9])
    return fig


def sp():
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Phân bổ giai đoạn 1 (here-and-now)", "Giá trị thông tin (EVPI = 1.567,5)"))
    lbl = ["I Hạ tầng", "D Số hóa", "AI", "H Nhân lực"]
    val = [8000, 8000, 41000, 8000]
    fig.add_bar(x=lbl, y=val, marker_color=[CYAN, BLUE, GOLD, GREEN],
                text=[f"{v:,}" for v in val], textposition="outside",
                showlegend=False, hovertemplate="%{x}<br>%{y:,} tỷ<extra></extra>", row=1, col=1)
    lbl2 = ["Z_SP (stochastic)", "EEV (kỳ vọng)", "WS (wait-and-see)"]
    val2 = [92185, 92185, 93752.5]
    fig.add_bar(x=lbl2, y=val2, marker_color=[BLUE, GRAY, GOLD],
                text=[f"{v:,.0f}" for v in val2], textposition="outside",
                showlegend=False, hovertemplate="%{x}<br>%{y:,.0f} tỷ<extra></extra>", row=1, col=2)
    _base(fig, "Hình 10.1 — Stochastic Programming 2 giai đoạn (4 kịch bản)")
    fig.update_yaxes(range=[0, 46000], row=1, col=1)
    fig.update_yaxes(range=[90000, 94500], row=1, col=2)
    return fig


def qlearn():
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Đường cong học (5.000 episodes)", "π* so với chiến lược cố định"))
    ep = [0, 250, 500, 1000, 1500, 2000, 3000, 4000, 5000]
    rw = [5, 11, 16, 19.5, 22, 23.2, 24.5, 25.2, 25.56]
    fig.add_trace(go.Scatter(x=ep, y=rw, mode="lines+markers", name="Q-learning",
                  line=dict(color=BLUE, width=2.6),
                  marker=dict(size=7, color="white", line=dict(color=BLUE, width=2)),
                  hovertemplate="Episode %{x}<br>Reward %{y:.2f}<extra></extra>"), row=1, col=1)
    fig.add_hline(y=21.32, line_dash="dash", line_color=GRAY, row=1, col=1)
    pol = ["π* Q-learning", "Luôn a₁ (Cân bằng)", "Random", "Luôn a₃ (AI-driven)"]
    pv = [26.11, 22.17, 21.32, 17.02]
    fig.add_bar(x=pol, y=pv, marker_color=[GREEN, BLUE, GRAY, RED],
                text=[f"{v:.2f}" for v in pv], textposition="outside",
                showlegend=False, hovertemplate="%{x}<br>%{y:.2f}<extra></extra>", row=1, col=2)
    _base(fig, "Hình 11.1 — Q-learning chính sách thích nghi (MDP 81×5)")
    fig.update_yaxes(range=[0, 29], row=1, col=2)
    return fig


def pie():
    acts = ["a₂ Số hóa (25)", "a₁ Cân bằng (21)", "a₄ Bao trùm (19)", "a₃ AI-driven (12)", "a₀ Truyền thống (4)"]
    cnt = [25, 21, 19, 12, 4]
    fig = go.Figure(go.Pie(labels=acts, values=cnt,
                    marker=dict(colors=[CYAN, BLUE, GREEN, GOLD, GRAY], line=dict(color="white", width=1.5)),
                    textinfo="percent", hovertemplate="%{label}<br>%{value} trạng thái (%{percent})<extra></extra>"))
    _base(fig, "Hình 11.2 — Phân bố hành động tối ưu π* trên 81 trạng thái")
    return fig


def scenarios():
    sc = ["S1 Truyền thống", "S2 Số hóa nhanh", "S3 AI dẫn dắt", "S4 Bao trùm số", "S5 Tối ưu cân bằng"]
    g = [20133.54, 18970.96, 18026.91, 20082.49, 20205.52]
    cols = [BLUE, CYAN, RED, GREEN, GOLD]
    fig = go.Figure(go.Bar(x=sc, y=g, marker_color=cols,
                    marker_line=dict(color=[NAVY if i == 4 else "rgba(0,0,0,0)" for i in range(5)],
                                     width=[2.4 if i == 4 else 0 for i in range(5)]),
                    text=[f"{v:,.0f}" for v in g], textposition="outside",
                    hovertemplate="%{x}<br>GDP 2030 = %{y:,.0f}<extra></extra>"))
    _base(fig, "Hình 12.1 — GDP 2030 theo 5 kịch bản (S5 thắng)")
    fig.update_yaxes(title="GDP 2030 (nghìn tỷ VND)", range=[17000, 21000])
    return fig


def ready():
    secfull = ["Nông-Lâm", "CN chế biến", "Xây dựng", "Khai khoáng", "Bán lẻ", "Tài chính", "Logistics", "CNTT", "Giáo dục", "Y tế"]
    rd = [15, 55, 20, 30, 48, 72, 42, 88, 38, 45]
    risk = [18, 42, 25, 55, 38, 52, 35, 28, 22, 18]
    fig = go.Figure()
    fig.add_bar(x=secfull, y=rd, name="AI Readiness", marker_color=BLUE)
    fig.add_bar(x=secfull, y=risk, name="Rủi ro tự động hóa (%)", marker_color=GOLD)
    _base(fig, "Hình 12.2 — Sẵn sàng AI và Rủi ro tự động hóa của 10 ngành")
    fig.update_layout(barmode="group")
    fig.update_yaxes(title="Điểm / %")
    return fig


def bubble():
    secfull = ["Nông-Lâm", "CN chế biến", "Xây dựng", "Khai khoáng", "Bán lẻ", "Tài chính", "Logistics", "CNTT", "Giáo dục", "Y tế"]
    rd = [15, 55, 20, 30, 48, 72, 42, 88, 38, 45]
    risk = [18, 42, 25, 55, 38, 52, 35, 28, 22, 18]
    labor = [13.2, 11.5, 4.8, 0.3, 7.8, 0.55, 1.95, 0.62, 2.15, 0.75]
    cols = [BLUE, CYAN, GOLD, GREEN, RED, NAVY, GRAY, BLUE, CYAN, GOLD]
    fig = go.Figure(go.Scatter(
        x=rd, y=risk, mode="markers+text", text=secfull, textposition="middle center",
        textfont=dict(size=9, color="white"),
        marker=dict(size=[l * 6 + 14 for l in labor], color=cols, opacity=0.7,
                    line=dict(color=NAVY, width=1)),
        customdata=labor,
        hovertemplate="%{text}<br>AI Readiness = %{x}<br>Rủi ro = %{y}%<br>Lao động = %{customdata} triệu<extra></extra>"))
    fig.add_vline(x=50, line_dash="dot", line_color=GRAY)
    fig.add_hline(y=40, line_dash="dot", line_color=GRAY)
    _base(fig, "Bản đồ 10 ngành: Sẵn sàng AI × Rủi ro × Quy mô lao động", h=440)
    fig.update_xaxes(title="AI Readiness (0–100)")
    fig.update_yaxes(title="Rủi ro tự động hóa (%)")
    return fig


FIGS = {
    "b01_tfp": tfp, "b01_decomp": decomp, "b01_gdp": gdp,
    "b02_alloc": alloc, "b02_shadow": shadow,
    "b03_priority": priority,
    "b04_regions": regions, "b04_fairness": fairness,
    "b05_mip": mip, "b05_select": select,
    "b06_topsis": topsis,
    "b07_pareto": pareto,
    "b08_dynamic": dynamic,
    "b09_netjobs": netjobs,
    "b10_sp": sp,
    "b11_qlearn": qlearn, "b11_pie": pie,
    "b12_scenarios": scenarios, "b12_ready": ready,
    "ov_bubble": bubble,
}
