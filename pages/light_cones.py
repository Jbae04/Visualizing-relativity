
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.header("🔦 Light Cones and Causality")
st.write("Speed of light forms a 45° cone in spacetime diagrams.")

x = np.linspace(-10, 10, 400)
t = x  # light path

fig, ax = plt.subplots()
ax.plot(x, t, 'r--', label='Light cone (+c)')
ax.plot(x, -t, 'b--', label='Light cone (-c)')
ax.axvline(0, color='gray', linestyle='--')
ax.axhline(0, color='gray', linestyle='--')
ax.set_xlabel("Space")
ax.set_ylabel("Time")
ax.legend()
ax.set_title("Spacetime Light Cones")
ax.grid(True)
st.pyplot(fig)
