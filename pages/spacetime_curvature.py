
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header("🌌 Spacetime Curvature")
mass = st.slider("Mass of Object", 0.1, 10.0, 1.0)

x, y = np.meshgrid(np.linspace(-5, 5, 400), np.linspace(-5, 5, 400))
r = np.sqrt(x**2 + y**2)
z = -mass / (r + 1e-3)

fig, ax = plt.subplots()
c = ax.contourf(x, y, z, levels=100, cmap='plasma')
fig.colorbar(c, ax=ax, label="Gravitational Potential")
ax.set_title("Curvature of Spacetime Around Mass")
ax.axis('equal')
st.pyplot(fig)
