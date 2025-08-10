import streamlit as st

st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/e/e4/S%C6%A1n_T%C3%B9ng_M-TP_on_%22Sky_Decade%22_in_Hanoi_11.png", 
    use_column_width=True
)
st.sidebar.title("Sơn Tùng M-TP")
st.sidebar.write("**Họ và tên:** Nguyễn Thanh Tùng")
st.sidebar.write("**Nghệ danh:** Sơn Tùng M-TP")
st.sidebar.write("""
Nguyễn Thanh Tùng, được biết đến với nghệ danh Sơn Tùng M-TP,
là ca sĩ, nhạc sĩ, rapper và diễn viên nổi tiếng của Việt Nam.
Anh được mệnh danh là "Hoàng tử Vpop" và đã giành nhiều giải thưởng âm nhạc uy tín.
""")

st.header("Bài hát yêu thích")
st.subheader("Chạy Ngay Đi")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.header("MV yêu thích")
st.subheader("Hãy Trao Cho Anh")
st.video("https://www.youtube.com/watch?v=knW7-x7Y7RE")