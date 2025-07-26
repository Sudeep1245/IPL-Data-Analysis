# import streamlit as st

# # Custom Title
# st.markdown("""
#     <h1 style='text-align: center; font-size: 60px; color: #fcfbf9;'>
#         🏏 IPL DETAILED ANALYSIS
#     </h1>
#     <hr style='border:1px solid #fcfbf9;'/>
# """, unsafe_allow_html=True)

# # Unified Button Styling
# st.markdown("""
#     <style>
#     div.stButton > button {
#         font-size: 40px !important;
#         padding: 25px 120px !important;
#         border-radius: 100px !important;
#         background-color: #1f77b4 !important;
#         color: white !important;
#         font-weight: bold !important;
#         font-family: 'Arial', sans-serif !important;
#         transition: background-color 0.3s ease;
#     }
#     div.stButton > button:hover {
#         background-color: #104e7d !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Buttons Section
# st.markdown("### 🔍 Choose Your Analysis", unsafe_allow_html=True)
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     st.button("📊 All Seasons Analysis")

# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     st.button("📅 Each Season Analysis")

import streamlit as st

# Custom Title
st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #fcfbf9;'>
        🏏 IPL DETAILED ANALYSIS
    </h1>
    <hr style='border:1px solid #fcfbf9;'/>
""", unsafe_allow_html=True)

# Unified Button Styling
st.markdown("""
    <style>
    div.stButton > button {
        font-size: 40px !important;
        padding: 25px 120px !important;
        border-radius: 100px !important;
        background-color: #1f77b4 !important;
        color: white !important;
        font-weight: bold !important;
        font-family: 'Arial', sans-serif !important;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #104e7d !important;
    }
    </style>
""", unsafe_allow_html=True)

# Buttons Section
st.markdown("### 🔍 Choose Your Analysis", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.button("📊 All Seasons Analysis")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.button("📅 Each Season Analysis")

