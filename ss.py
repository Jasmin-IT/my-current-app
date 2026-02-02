import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    data = option_menu(
        menu_title="my project",
        options=["Home","About","contact"]
    )
if data == "Home":
    st.header("home page")
    st.title("welcome to the home page")
    name = st.text_input("Name")
    id = st.number_input("ID",min_value=1)
    gender = st.radio("Gender",options=["Male","Female"])
    city = st.selectbox("City",options=["Madurai","Chennai","Bangalore"])
    dob = st.date_input("Pic A Date")
    age = st.slider("Age",20,35)
    skills = st.multiselect("Skills",options=["Html","css","js","Python","java"])
    if st.button("Click"):
        st.write(name)
        st.success("Data Print Successfully")
elif data == "About":
    st.header("About page")
    col1,col2 = st.columns(2)
    with col1:
        st.write("Over 4.2 million+ royalty-free stock photos shared by our talented community.Over 4.2 million+ royalty-free stock photos shared by our talented community.Over 4.2 million+ royalty-free stock photos shared by our talented community.")
        # name = st.text_input("Name")
    with col2:
        # name = st.text_input("Name1")
        st.image("https://images.pexels.com/photos/210186/pexels-photo-210186.jpeg?cs=srgb&dl=cascade-clouds-cool-wallpaper-210186.jpg&fm=jpg")
elif data == "contact":

    st.header("contact page")
    name=st.text_input("name")
    number = st.text_input("enter number")
    mail = st.text_input("enter mail:")
    queries = st.text_area("enter queries:")
    if st.button("submit"):
        st.success("queries sent successfully")
