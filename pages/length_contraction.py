
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header("📏 Length Contraction")
st.latex(r"L = L_0 \sqrt{1 - \frac{v^2}{c^2}}")

v = st.slider("Velocity as fraction of light speed (v/c)", 0.01, 0.99, 0.5, key="length_v")
L0 = st.number_input("Rest Length (L₀)", value=10.0)
L = L0 * np.sqrt(1 - v**2)

st.write(f"Contracted Length: {L:.2f} units")

fig, ax = plt.subplots()
v_range = np.linspace(0.01, 0.99, 100)
L_range = L0 * np.sqrt(1 - v_range**2)
ax.plot(v_range, L_range)
ax.set_xlabel("Velocity (v/c)")
ax.set_ylabel("Contracted Length (L)")
ax.set_title("Length Contraction vs Velocity")
ax.grid(True)
st.pyplot(fig)
