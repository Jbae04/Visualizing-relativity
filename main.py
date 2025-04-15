import streamlit as st
st.set_page_config(page_title="Relativity Lab", layout="centered")

from pages import time_dilation, length_contraction, light_cones, spacetime_curvature, black_hole

st.sidebar.title("Relativity Lab")
st.sidebar.info("Interactive visualizations of Einstein's Theory of Relativity")

st.title("Relativity Lab: Explore Einstein's Universe")
st.markdown("""
Welcome to **Relativity Lab** — a visual and mathematical journey through Special and General Relativity.

Use the sidebar to navigate:
- Time Dilation
- Length Contraction
- Light Cones
- Spacetime Curvature
- Black Holes
""")
