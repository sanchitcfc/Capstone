import streamlit as st
import pandas as pd


    

def Page_1():
    st.subheader("Page 1")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")

def Page_2():   
    st.subheader("Page 2")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")

def Page_3():
    st.subheader("Page 3")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")

def Page_4():
    st.subheader("Page 4")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")


def Page_5():
    st.subheader("Page 5")
    sub_page = st.sidebar.selectbox("Select a sub-page", ["Sub-page 1", "Sub-page 2"])
    if sub_page == "Sub-page 1":
        st.write("This is sub-page 1.")
    elif sub_page == "Sub-page 2":
        st.write("This is sub-page 2.")



def main():
    st.set_page_config(page_title="Malware Mavericks", page_icon=":guardsman:", layout="wide")
    st.title("Malware Mavericks")
    # Adding a logo
    logo_url = 'https://images.unsplash.com/photo-1501594907352-04cda38ebc29?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80'
    st.sidebar.image(logo_url, width=50)
    pages = {"Page 1":Page_1,"Page 2":Page_2,"Page 3":Page_3,"Page 4":Page_4,"Page 5":Page_5}
    choice = st.sidebar.selectbox("Select a page", list(pages.keys()))
    pages[choice]()

if __name__ == '__main__':
    main()
