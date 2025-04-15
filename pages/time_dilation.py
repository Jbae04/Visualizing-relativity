
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header("⏳ Time Dilation")
st.latex(r"t' = \frac{t}{\sqrt{1 - \frac{v^2}{c^2}}}")

v = st.slider("Velocity as fraction of light speed (v/c)", 0.01, 0.99, 0.5, key="time_v")
gamma = 1 / np.sqrt(1 - v**2)

st.write(f"Time Dilation Factor (γ): {gamma:.3f}")

fig, ax = plt.subplots()
v_range = np.linspace(0.01, 0.99, 100)
gamma_range = 1 / np.sqrt(1 - v_range**2)
ax.plot(v_range, gamma_range)
ax.set_xlabel("Velocity (v/c)")
ax.set_ylabel("Time Dilation γ")
ax.set_title("Time Dilation vs Velocity")
ax.grid(True)
st.pyplot(fig)
