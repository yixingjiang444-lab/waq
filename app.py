import streamlit as st
st.title("test")
st.write("hello")
name =st.text_input("name?")
if st.button("CLICK"):
    st.success(f"안녕하세요,{name}님!")

