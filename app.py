import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Tiêu đề Web App
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 2. Tạo dữ liệu mẫu và tính toán (Giống các phần trước)
data = {
    'Họ và tên': ['An', 'Bình', 'Cường', 'Hà', 'Lan', 'Linh', 'Nhi', 'Minh', 'Nhựt','Quyết'],
    'Điểm chuyên cần': [8.0, 8.5, 7.0, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.0],
    'Điểm giữa kỳ': [7.5, 8.0, 6.5, 8.5, 7.0, 5.5, 8.0, 6.5, 7.0, 8.5],
    'Điểm cuối kỳ': [8.0, 8.5, 6.5, 9.5, 7.5, 6.0, 8.5, 7.0, 7.5, 9.0]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết
df['Tong_ket'] = (
    0.2 * df['Điểm chuyên cần'] + 
    0.3 * df['Điểm giữa kỳ'] + 
    0.5 * df['Điểm cuối kỳ']
).round(2)

# Xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# 3. Hiển thị bảng điểm của 10 sinh viên
st.subheader("📊 Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

# 4. Hiển thị thông tin thống kê
st.subheader("📈 Thông tin thống kê chung")
diem_tb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

st.write(f"- **Điểm tổng kết trung bình của lớp:** {diem_tb_lop:.2f}")
st.write(f"- **Sinh viên có điểm cao nhất:** {sv_max['Họ và tên']} ({sv_max['Tong_ket']} điểm)")
st.write(f"- **Sinh viên có điểm thấp nhất:** {sv_min['Họ và tên']} ({sv_min['Tong_ket']} điểm)")
st.write(f"- **Số sinh viên đạt (>= 5.0):** {so_sv_dat} sinh viên")

# 5. Danh sách xổ xuống (Selectbox) để chọn sinh viên
st.subheader("🔍 Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Họ và tên'])

# Lọc thông tin sinh viên được chọn
student_info = df[df['Họ và tên'] == selected_student].iloc[0]

st.info(f"""
- **Họ và tên:** {student_info['Họ và tên']}
- **Điểm chuyên cần:** {student_info['Điểm chuyên cần']}
- **Điểm giữa kỳ:** {student_info['Điểm giữa kỳ']}
- **Điểm cuối kỳ:** {student_info['Điểm cuối kỳ']}
- **Điểm tổng kết:** **{student_info['Tong_ket']}**
- **Xếp loại:** **{student_info['Xep_loai']}**
""")

# 6. Hiển thị biểu đồ cột điểm tổng kết
st.subheader("📊 Biểu đồ điểm tổng kết của lớp")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df['Họ và tên'], df['Tong_ket'], color='skyblue', edgecolor='black')
ax.set_title('Biểu đồ điểm tổng kết của 10 sinh viên')
ax.set_xlabel('Họ và tên')
ax.set_ylabel('Điểm tổng kết')
ax.set_ylim(0, 10)
for i, txt in enumerate(df['Tong_ket']):
    ax.text(i, txt + 0.1, str(txt), ha='center', fontsize=9)

st.pyplot(fig)

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: small; color: gray;'>Người tạo: [Họ và tên của bạn] - MSSV: [Mã số sinh viên của bạn]</p>", unsafe_allow_html=True)
