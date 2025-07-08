import streamlit as st


st.markdown(
    "<h1 style='text-align: center; font-size: 60px; color: #fcfbf9;'>IPL DETAILED ANALYSIS</h1>",
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    div.stButton > button {
        font-size: 50px!important;
        padding: 30px 140px;
        border-radius: 200px;
        background-color: #1f77b4;
        color: white;
        font-weight: bold !important;
        font-family: 'Arial', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)


#align the button into the center
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.button("All Seasons Analysis")

st.markdown("""
    <style>
    div.stButton > button {
        font-size: 50px!important;
        padding: 30px 140px;
        border-radius: 200px;
        background-color: #1f77b4;
        color: white;
        font-weight: bold !important;
        font-family: 'Arial', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)


#align the button into the center
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.button("Each Season Analysis")
