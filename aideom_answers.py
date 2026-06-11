# -*- coding: utf-8 -*-
"""Goi y dap an cho tung cau hoi (yeu cau lap trinh va thao luan chinh sach)
cua 12 bai. Thu tu khop chinh xac voi DETAIL trong aideom_detail.py.
Bam sat so lieu phan tich cua bao cao AIDEOM-VN.
"""

ANS = {
 1: dict(
   yeucau=[
     "Giai nguoc ham san xuat: A_t = Y / (K^alpha . L^beta . D^gamma . AI^delta . H^theta). TFP tang deu tu ~27,7 (2020) len ~34,9 (2025) -> tang truong ngay cang dua vao hieu qua/cong nghe, khong chi von - lao dong.",
     "Lay A trung binh giai doan roi tinh san luong du bao; so voi Y thuc te cho MAPE ~ 6,42% - sai so nho, mo hinh bam du lieu tot va du tin cay de du bao.",
     "Phan ra tang truong binh quan nam: TFP ~49,1%, Von K ~31,8%, So hoa D ~10,4%, AI ~6,2%, Von nhan luc H ~2,9%, Lao dong L ~ -0,3%. TFP va K la hai tru cot; nhom yeu to moi (D+AI+H) ~19,5%.",
     "Kich ban 2030 (D=30%, AI=100 nghin DN, H=35%, K&L +6%/nam, TFP +1,2%/nam): GDP du bao ~12.847 nghin ty, cao hon ro ret kich ban nen.",
   ],
   thaoluan=[
     "TFP tang lien tuc -> chat luong tang truong cai thien, dich chuyen tu tham dung von sang tham dung hieu qua va cong nghe.",
     "So hoa D dong gop lon nhat trong nhom moi (~10,4%), vuot AI va H, vi nen tang du lieu/so hoa da lan rong trong khi AI va nhan luc so con o giai doan dau.",
     "Kha thi co dieu kien: phai giu TFP tang >=1,2%/nam va day dong thoi H; vi delta va theta nho nen dau tu AI don le khong du - 'AI khong co H la von chet'.",
   ]),
 2: dict(
   yeucau=[
     "linprog cho nghiem toi uu Z* = 112,25 voi phan bo x = (25; 15; 20; 40) - ngan sach don toi da vao linh vuc he so cao nhat (1,35) sau khi thoa cac san.",
     "PuLP cho cung nghiem; gia doi ngau cua rang buoc ngan sach = 1,35 (moi don vi ngan sach them -> +1,35 GDP). Cac san 25/15/20 la rang buoc chat nen co shadow price.",
     "Tang ngan sach 100 -> 120 -> 140: Z* tang theo doc 1,35 (~125,8 roi ~139,3) cho den khi gap rang buoc khac -> duong Z*(B) la duong gap khuc doc giam dan.",
     "Them x3 >= 30: van kha thi nhung buoc doi von khoi linh vuc he so cao -> Z* giam nhe (xuong ~110), the hien chi phi cua viec uu tien nhan luc so.",
   ],
   thaoluan=[
     "Theo gia doi ngau, +1 ty ngan sach -> +1,35 ty GDP; day la can tren hop ly cua chi phi co hoi von cong - du an sinh loi duoi muc nay khong nen uu tien.",
     "R&D he so cao nhung san thap vi do tre va rui ro lon, kho hap thu von nhanh; san thap tranh dan trai khi nang luc trien khai con han che.",
     "35% cho cong nghe chien luoc la tham vong khi 2025 uu tien ha tang va an sinh; can lo trinh tang dan va huy dong von tu nhan thay vi don ngan sach cong.",
   ]),
 3: dict(
   yeucau=[
     "Chuan hoa min-max dua 7 cot ve [0,1], dao dau Risk (1 - gia tri) de rui ro cao thanh diem thap; ma tran chuan hoa la dau vao tinh Priority.",
     "Priority_i = tong (trong so x gia tri chuan hoa); xep hang cho diem tu 0,7446 (cao nhat) xuong 0,0489 - nhom CNTT-TT va Tai chinh dan dau.",
     "Tang a6 (AI Readiness) tu 0,05 den 0,40 va chuan hoa lai: Top-3 ve co ban on dinh, chi dao vi tri trong nhom; heatmap cho thay thu hang it nhay voi a6 o hai dau.",
     "Bo 'tang truong' day nganh dong gop GDP lon len dau; bo 'bao trum' nang nganh nhieu lao dong/vung kho - Top-3 lech nhau 1-2 vi tri.",
   ],
   thaoluan=[
     "Ba nganh uu tien: CNTT-Truyen thong, Tai chinh-Ngan hang, Cong nghiep che bien che tao - khop dinh huong dong luc so cua Nghi quyet 57-NQ/TW.",
     "Khai khoang nang suat cao nhung diem AI Readiness va lan toa thap, rui ro moi truong cao (bi dao dau) -> tong hop lai khong vao nhom uu tien.",
     "Trong so nen qua doi thoai cong khai co hoi dong chinh sach tham dinh: vua dam bao tinh ky tri, vua co tinh chinh danh va tranh thien lech nhom loi ich.",
   ]),
 4: dict(
   yeucau=[
     "PuLP/CBC cho ma tran phan bo x_{j,r} 6x4 va Z* = 68.750 (khi chua siet cong bang toi da); von tap trung vao vung hieu qua cao.",
     "CVXPY cho cung nghiem Z* va cung phan bo (lech <0,1%) -> xac nhan mo hinh tuyen tinh, hai solver nhat quan.",
     "Heatmap: Dong Nam Bo va DB Song Hong nhan nhieu ngan sach nhat; moi vung uu tien hang muc co he so cao nhat cua vung do.",
     "Bo rang buoc cong bang (C5): Z* len 68.750 so voi 52.485 khi siet toi da -> chi phi cua cong bang vung mien ~ 16.265 ty (23,66% GDP gain).",
   ],
   thaoluan=[
     "Bo cong bang -> von don ve Dong Nam Bo va DB Song Hong (hieu suat cao); dai han lam gian khoang cach vung, di cu va bat on xa hoi.",
     "Tran ngan sach vung (C3) lam giam Z* vai % nhung doi lai phan quyen va can bang vung - muc giam chap nhan duoc neu uu tien bao trum.",
     "Tay Nguyen he so AI thap (0,45) -> mo hinh khuyen nghi dau tu H va ha tang (I) truoc de tao nen, roi moi mo rong AI.",
   ]),
 5: dict(
   yeucau=[
     "PuLP/CBC chon tap du an trong ngan sach 80.000 cho tong loi ich Z* ~ 115.400; NPV bien (Z*/chi phi) cao cho thay danh muc hieu qua.",
     "Noi ngan sach len 100.000: them duoc du an co ty suat loi ich/chi phi thap hon, tong loi ich tang nhung loi ich bien giam dan (duong cong lom).",
     "Bat buoc ca P1 va P2: van kha thi, nhung chiem cho du an hieu qua hon -> Z* giam nhe (xuong ~113.300).",
     "Them xac suat hoan thanh p_i va toi da E[Z] = tong p_i.B_i.y_i: danh muc dich sang du an chac chan hon, Z ky vong giam con ~91.285.",
   ],
   thaoluan=[
     "Bo qua P15 (Open Data) du ty suat cao co the do vuong rang buoc tien quyet/ngan sach nam; ve chinh sach day la ket qua KHONG mong muon -> nen go rang buoc hoac tach giai doan.",
     "Bat buoc P14 (an ninh mang) lam giam Z* chut it nhung hop ly: an ninh la dieu kien nen, khong nen danh doi lay loi ich kinh te ngan han.",
     "Hieu ung cong huong P8 x P13: them bien tuong tac (loi ich bo sung khi cung chon) hoac rang buoc 'chon P8 thi khuyen khich P13' de mo hinh hoa.",
   ]),
 6: dict(
   yeucau=[
     "TOPSIS voi trong so chuyen gia: C_i* xep hang 6 vung, Dong Nam Bo (0,949) va DB Song Hong (0,880) dan dau, thap nhat la vung mien nui (0,020).",
     "Entropy gan trong so theo do phan tan du lieu; xep hang doi o nhom giua nhung top-2 van giu nguyen -> ket luan robust voi cach chon trong so.",
     "Tang/giam w_AI tu 0,10 den 0,40: Top-3 on dinh, chi hoan doi trong nhom -> quyet dinh khong qua nhay voi trong so AI.",
     "AHP don gian (scikit-criteria) cho thu hang tuong dong TOPSIS (tuong quan Spearman cao) -> cung co do tin cay cua ket qua.",
   ],
   thaoluan=[
     "Dong Nam Bo dan dau -> ung vien hang dau dat trung tam AI quoc gia dau tien nho ha tang, nhan luc va mat do doanh nghiep.",
     "Vung doi hang lon nhat khi dung Entropy thuong la nhom giua, do trong so dich sang tieu chi co do phan tan cao ma vung do manh/yeu bat thuong.",
     "AI Readiness va Internet penetration tuong quan cao gay trung lap thong tin -> nen gop thanh mot nhan to (PCA) hoac giam trong so de tranh dem trung.",
     "Theo QD 127, chon Dong Nam Bo, DB Song Hong va mot vung trung tam (Bac Trung Bo/Da Nang) de can bang; nen them tieu chi dia - chinh tri va an ninh.",
   ]),
 7: dict(
   yeucau=[
     "pymoo ElementwiseProblem 24 bien, 4 muc tieu; NSGA-II pop_size=100, n_gen=200 hoi tu ve tap Pareto da dang.",
     "Mat truoc Pareto: GDP trai tu ~26.987 den ~69.773, di kem Gini tang 0,81 -> 1,92; scatter 3D va parallel coordinates cho thay danh doi ro giua tang truong va bao trum.",
     "TOPSIS tren Pareto voi trong so (0,40; 0,25; 0,20; 0,15) chon nghiem thoa hiep GDP ~ 28.548, Gini ~ 0,84 - can bang tot.",
     "Nghiem GDP cao nhat (69.773) hi sinh bao trum rat lon (Gini 1,92 so 0,84): GDP tang ~144% nhung bat binh dang tang hon gap doi so voi nghiem thoa hiep.",
   ],
   thaoluan=[
     "Danh doi tang truong - bao trum rat ro tren Pareto -> co cau kinh te con dua vao vai cuc tang truong, de gian bat binh dang neu chay theo GDP.",
     "Trong so uu tien tang truong (0,40) phu hop Dai hoi XIII; de bam COP26 va QD 127 nen nang trong so moi truong va bao trum.",
     "NSGA-II dua ra ca mat danh doi de con nguoi chon, khac LP chi cho mot nghiem; no ho tro chu khong thay quyet dinh chinh tri.",
   ]),
 8: dict(
   yeucau=[
     "(A) log-linearize giai bang CVXPY va (B) SLSQP cho cung quy dao toi uu -> xac nhan loi giai; CVXPY nhanh va on dinh hon cho bai loi.",
     "Quy dao 2026-2035: K, D, AI, H tang, dau tu don ve dau ky (front-load), Y va C tang dan - phuc loi chiet khau ~78,4.",
     "Cu soc 2028 (Y -8%): mo hinh tam giam tieu dung C, giu dau tu H/AI de khong pha vo tich luy dai han roi phuc hoi nhanh sau soc.",
     "Front-load cho phuc loi tong cao hon trai deu (78,37 so 78,13) vi loi ich tich luy som duoc huong lau hon duoi rho = 0,97.",
   ],
   thaoluan=[
     "Quy dao front-loaded vi rho cao khien loi ich tuong lai it bi chiet khau -> dau tu som sinh loi dai.",
     "Ty le AI/H kha on dinh va mo hinh de xuat dao tao nhan luc DI TRUOC hoac dong thoi voi dau tu AI, khong de H tut lai.",
     "rho = 0,90 day ve back-load va giam dau tu dai han -> dung la ly do chinh phu thuong 'duoi dau tu' R&D khi qua chu trong ngan han.",
   ]),
 9: dict(
   yeucau=[
     "PuLP/CVXPY: phan bo (x_AI, x_H) moi nganh; NetJob rong toan nen ~ +13,99 trieu, CNTT dan dau (+11,29 trieu), Nong-Lam am nhe (-12.600).",
     "Nguong x_H toi thieu o CN che bien de NetJob2 >= 0 ngay ca khi AI toi da: can dau tu dao tao du bu so lao dong bi thay the (diem hoa von viec lam).",
     "Sankey cho thay lao dong dich tu nganh de ton thuong (1,3,4) sang dich vu/CNTT; nhom nay can ho tro chuyen doi manh nhat.",
     "Rang buoc 'khong nganh nao mat qua 5% lao dong': van kha thi nhung phai ham toc do AI o vai nganh -> tong NetJob giam chut, doi lay on dinh xa hoi.",
   ],
   thaoluan=[
     "Nganh can dao tao lai nhieu nhat la CN che bien che tao va ban le - khop thuc te Viet Nam khi tu dong hoa lan nhanh o khu vuc nay.",
     "Tai chinh - Ngan hang thay the 52% nhung tao viec moi cao -> khuyen nghi reskilling tai cho sang nghiep vu so thay vi cat giam.",
     "Han che dau tu x_AI vao Nong - Lam - Thuy san (he so tao viec AI thap, dich chuyen lon); uu tien co gioi hoa va H truoc.",
     "'Toc do tu dong hoa <= nang luc dao tao lai' bieu dien bang rang buoc DisplacedJob_i <= nang luc reskilling; nen bo sung rang buoc tro cap/an sinh toi thieu.",
   ]),
 10: dict(
   yeucau=[
     "Pyomo + GLPK/CBC: quyet dinh first-stage toi uu ~ (8.000; 8.000; 41.000; 8.000) - don vao hang muc it rui ro giua cac kich ban.",
     "So EV va SP: loi giai ky vong (EV) thieu du phong, SP dau tu H/du phong nhieu hon de chiu duoc kich ban xau.",
     "VSS duong (loi ich cua tu duy bat dinh) va EVPI = 1.567,5 (gia tri thong tin hoan hao) -> lap ke hoach co xac suat dang gia.",
     "Robust (min regret kich ban xau nhat) cho quyet dinh than trong hon SP, hi sinh ky vong de giam rui ro duoi.",
   ],
   thaoluan=[
     "SP dau tu H NHIEU hon loi giai xac dinh, vi nhan luc so la 'dem' linh hoat giup thich ung moi kich ban.",
     "VSS duong cho thay tu duy xac suat tao gia tri thuc trong hoach dinh - Viet Nam nen the che hoa lap ke hoach theo kich ban.",
     "COVID-19 va bao Yagi cho thay ta dang 'duoi dau tu' nhan luc so nhu mot hang hoa bao hiem; can tang du phong va dao tao.",
   ]),
 11: dict(
   yeucau=[
     "Moi truong gymnasium (reset/step/action_space/observation_space), 1 episode = 10 nam; trang thai gom GDP, D, AI, H, U.",
     "Q-learning alpha=0,1, gamma=0,95, epsilon giam 1,0 -> 0,05 qua 10.000 episode -> bang Q hoi tu on dinh.",
     "pi*(s) = argmax_a Q(s,a): tai VN 2026 uu tien hanh dong dau tu can doi AI+H; cac trang thai gia dinh cho hanh dong khac nhau theo GDP/U.",
     "Phan thuong tich luy pi* (~26,1) vuot rule-based luon a1 (~22,2), luon a3 (~21,3) va ngau nhien (~17,0); learning curve di len roi bao hoa.",
     "DQN (stable-baselines3, 2 lop an 64) khai quat hoa tot hon o khong gian trang thai lon, nhung tabular du tot cho bai toan roi rac nho nay.",
   ],
   thaoluan=[
     "GDP thap, D thap, U cao -> pi* chon dau tu tao viec/quick win nhanh de tao da, dung tinh than 'quick win'.",
     "GDP cao, AI cao, U thap -> pi* chuyen sang cung co (consolidation), giu on dinh va dau tu chieu sau - phu hop.",
     "Tich hop pi* nhu cong cu tham muu/canh bao trong quy trinh hoach dinh, ket qua van do con nguoi quyet de khong vi pham nguyen tac 'AI khong thay quyet dinh chinh tri'.",
   ]),
 12: dict(
   yeucau=[
     "Moi module la file .py doc lap co docstring va unit test pytest, tai su dung dung ky thuat Bai 1-11 (ham san xuat, LP, MIP, da muc tieu, ngau nhien).",
     "Dashboard Streamlit/Plotly >=4 tab (Tong quan, Phan bo, So sanh kich ban, Canh bao rui ro) - chinh la web AIDEOM-VN nay.",
     "Chay S1, S3, S5 va lap bang so sanh KPI 2030: GDP cac kich ban dao quanh ~18.000-20.200, S5 (can bang) cho tong hop tot nhat.",
     "Ma >= 1.500 dong tren GitHub kem README + requirements.txt, bao cao 15-25 trang va slide/video demo.",
   ],
   thaoluan=[
     "So sanh 5 kich ban - Truyen thong (S1), So hoa nhanh (S2), AI dan dat (S3), Bao trum so (S4), Toi uu can bang (S5); GDP 2030 lan luot ~20.134; 18.971; 18.027; 20.082; 20.206.",
     "Kich ban GDP cao (S5/S1) danh doi ap luc an ninh du lieu va moi truong; S3 AI dan dat manh nhung kem bao trum -> can can nhac cai gia xa hoi.",
     "Khuyen nghi chon S5 (Toi uu can bang): vua giu GDP cao nhat (~20.206), vua dam bao bao trum - phu hop uu tien phat trien nhanh va ben vung cua Viet Nam.",
   ]),
}
