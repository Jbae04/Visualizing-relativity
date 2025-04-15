
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header("🕳️ Black Hole Horizon")
r_s = st.slider("Schwarzschild Radius (Rs)", 0.1, 5.0, 2.0)

r = np.linspace(0.1, 10, 500)
phi = -1 / (r - r_s)

fig, ax = plt.subplots()
ax.plot(r, phi)
ax.axvline(r_s, color='red', linestyle='--', label='Event Horizon')
ax.set_xlabel("Distance from Center (r)")
ax.set_ylabel("Potential")
ax.set_title("Gravitational Well of a Black Hole")
ax.legend()
ax.grid(True)
st.pyplot(fig)
