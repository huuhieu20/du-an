import streamlit as st

# Sidebar - Thông tin ca sĩ
with st.sidebar:
    st.image("sontung.jpg", use_container_width=True)  # Đổi thành ảnh của bạn
    st.header("Sơn Tùng M-TP")
    st.write("**Họ và tên:** Nguyễn Thanh Tùng")
    st.write("**Nghệ danh:** Sơn Tùng M-TP")
    st.write(
        "Nguyễn Thanh Tùng, được biết đến với nghệ danh Sơn Tùng M-TP, là ca sĩ, nhạc sĩ, rapper "
        "và diễn viên nổi tiếng của Việt Nam. Anh được mệnh danh là 'Hoàng tử Vpop' và đã giành "
        "nhiều giải thưởng âm nhạc uy tín."
    )

# Nội dung chính
st.title("Bài hát yêu thích")
st.subheader("Chạy Ngay Đi")
st.audio("chay_ngay_di.mp3")  # Đổi thành file nhạc của bạn

st.title("MV yêu thích")
st.subheader("Hãy Trao Cho Anh")
st.video("https://www.youtube.com/watch?v=knW7-x7Y7RE")
