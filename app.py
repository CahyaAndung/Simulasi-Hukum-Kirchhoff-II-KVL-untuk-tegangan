
import streamlit as st
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Simulasi Hukum Kirchhoff II",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Simulasi Hukum Kirchhoff II (KVL)")
st.write(
    "Simulasi rangkaian resistor seri untuk membuktikan "
    "bahwa jumlah aljabar tegangan dalam satu loop tertutup adalah nol."
)

# =========================
# INPUT PARAMETER
# =========================
st.sidebar.header("Parameter Rangkaian")

Vs = st.sidebar.slider(
    "Tegangan sumber Vs (V)", 1, 30, 13
)
R1 = st.sidebar.slider(
    "Resistor R1 (Ω)", 10, 1000, 100, step=10
)
R2 = st.sidebar.slider(
    "Resistor R2 (Ω)", 10, 1000, 220, step=10
)
R3 = st.sidebar.slider(
    "Resistor R3 (Ω)", 10, 1000, 330, step=10
)

# =========================
# PERHITUNGAN KVL
# =========================
Rt = R1 + R2 + R3
I = Vs / Rt

V1 = I * R1
V2 = I * R2
V3 = I * R3

total_drop = V1 + V2 + V3
error = Vs - total_drop

# =========================
# NILAI UTAMA
# =========================
c1, c2, c3, c4 = st.columns(4)

c1.metric("Tegangan sumber", f"{Vs:.2f} V")
c2.metric("Resistansi total", f"{Rt} Ω")
c3.metric("Arus rangkaian", f"{I * 1000:.2f} mA")
c4.metric("Total jatuh tegangan", f"{total_drop:.2f} V")

st.divider()

# =========================
# DIAGRAM RANGKAIAN
# =========================
st.subheader("1. Diagram Rangkaian Seri")

circuit_svg = """
<svg viewBox="0 0 800 350"
     xmlns="http://www.w3.org/2000/svg"
     width="100%" role="img"
     aria-label="Rangkaian seri dengan sumber tegangan dan tiga resistor">

  <rect x="2" y="2" width="796" height="346"
        rx="18" fill="#101827" stroke="#334155"/>

  <g stroke="#60a5fa" stroke-width="4"
     fill="none" stroke-linecap="round"
     stroke-linejoin="round">
    <path d="M120 145 V80 H225"/>
    <path d="M315 80 H385"/>
    <path d="M475 80 H545"/>
    <path d="M635 80 H690 V270 H120 V215"/>
    <path d="M120 145 V155"/>
    <path d="M120 205 V215"/>
  </g>

  <!-- Battery -->
  <g stroke="#f8fafc" stroke-width="4">
    <line x1="88" y1="155" x2="152" y2="155"/>
    <line x1="103" y1="205" x2="137" y2="205"/>
  </g>
  <text x="160" y="151" fill="#f8fafc" font-size="17">+</text>
  <text x="143" y="211" fill="#f8fafc" font-size="17">−</text>
  <text x="35" y="183" fill="#f8fafc" font-size="18">Vs</text>

  <!-- Resistor 1 -->
  <rect x="225" y="61" width="90" height="38"
        rx="5" fill="#fde68a" stroke="#f59e0b" stroke-width="3"/>
  <text x="270" y="47" fill="#f8fafc" font-size="17"
        text-anchor="middle">R1</text>
  <text id="r1value" x="270" y="125" fill="#f8fafc"
        font-size="16" text-anchor="middle">100 Ω</text>

  <!-- Resistor 2 -->
  <rect x="385" y="61" width="90" height="38"
        rx="5" fill="#fde68a" stroke="#f59e0b" stroke-width="3"/>
  <text x="430" y="47" fill="#f8fafc" font-size="17"
        text-anchor="middle">R2</text>
  <text id="r2value" x="430" y="125" fill="#f8fafc"
        font-size="16" text-anchor="middle">220 Ω</text>

  <!-- Resistor 3 -->
  <rect x="545" y="61" width="90" height="38"
        rx="5" fill="#fde68a" stroke="#f59e0b" stroke-width="3"/>
  <text x="590" y="47" fill="#f8fafc" font-size="17"
        text-anchor="middle">R3</text>
  <text id="r3value" x="590" y="125" fill="#f8fafc"
        font-size="16" text-anchor="middle">330 Ω</text>

  <!-- Conventional current direction -->
  <path d="M170 80 H205 M345 80 H365 M505 80 H525
           M690 145 V190 M570 270 H530"
        stroke="#34d399" stroke-width="3" fill="none"/>
  <path d="M197 73 L207 80 L197 87
           M357 73 L367 80 L357 87
           M517 73 L527 80 L517 87
           M683 180 L690 192 L697 180
           M542 263 L530 270 L542 277"
        stroke="#34d399" stroke-width="3"
        fill="none" stroke-linejoin="round"/>

  <!-- Animated current dots following the complete loop -->
  <path id="currentPath"
        d="M120 215 H690 V80 H635
           M545 80 H475 M385 80 H315
           M225 80 H120 V145"
        fill="none" stroke="none"/>

  <g fill="#34d399">
    <circle r="5">
      <animateMotion dur="5s" repeatCount="indefinite"
        path="M120 215 H690 V80 H635
              M545 80 H475 M385 80 H315
              M225 80 H120 V145"/>
    </circle>
    <circle r="5">
      <animateMotion dur="5s" begin="-1.25s"
        repeatCount="indefinite"
        path="M120 215 H690 V80 H635
              M545 80 H475 M385 80 H315
              M225 80 H120 V145"/>
    </circle>
    <circle r="5">
      <animateMotion dur="5s" begin="-2.5s"
        repeatCount="indefinite"
        path="M120 215 H690 V80 H635
              M545 80 H475 M385 80 H315
              M225 80 H120 V145"/>
    </circle>
    <circle r="5">
      <animateMotion dur="5s" begin="-3.75s"
        repeatCount="indefinite"
        path="M120 215 H690 V80 H635
              M545 80 H475 M385 80 H315
              M225 80 H120 V145"/>
    </circle>
  </g>

  <text x="400" y="320" fill="#34d399"
        font-size="17" text-anchor="middle">
    Arah arus konvensional: dari terminal positif menuju terminal negatif
  </text>
</svg>
"""

components.html(circuit_svg, height=365)

st.caption(
    "Titik hijau menunjukkan arah arus konvensional. "
    "Diagram menunjukkan tiga resistor yang terhubung seri."
)

st.divider()

# =========================
# HASIL PERHITUNGAN
# =========================
st.subheader("2. Hasil Perhitungan")

left, right = st.columns(2)

with left:
    st.markdown("**Hukum Ohm**")
    st.latex(r"R_t = R_1 + R_2 + R_3")
    st.latex(
        rf"R_t = {R1} + {R2} + {R3} = {Rt}\ \Omega"
    )
    st.latex(r"I = \frac{V_s}{R_t}")
    st.latex(
        rf"I = \frac{{{Vs}}}{{{Rt}}}"
        rf" = {I:.6f}\ \text{{A}}"
    )

with right:
    st.markdown("**Jatuh Tegangan**")
    st.latex(r"V_R = I \times R")
    st.latex(rf"V_1 = {I:.6f}\times {R1} = {V1:.4f}\ V")
    st.latex(rf"V_2 = {I:.6f}\times {R2} = {V2:.4f}\ V")
    st.latex(rf"V_3 = {I:.6f}\times {R3} = {V3:.4f}\ V")

st.divider()

# =========================
# GRAFIK TEGANGAN
# =========================
st.subheader("3. Grafik Jatuh Tegangan")

fig, ax = plt.subplots(figsize=(8, 4))

labels = ["R1", "R2", "R3"]
voltages = [V1, V2, V3]

bars = ax.bar(labels, voltages)
ax.set_ylabel("Tegangan (V)")
ax.set_xlabel("Resistor")
ax.set_title("Jatuh Tegangan pada Setiap Resistor")
ax.grid(axis="y", linestyle="--", alpha=0.35)

ax.bar_label(bars, fmt="%.2f V", padding=4)
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.divider()

# =========================
# VERIFIKASI KVL
# =========================
st.subheader("4. Verifikasi Hukum Kirchhoff II")

st.latex(r"V_s - V_1 - V_2 - V_3 = 0")

st.code(
    f"{Vs:.4f} - {V1:.4f} - {V2:.4f} - {V3:.4f} "
    f"= {error:.10f} V",
    language="text"
)

if abs(error) < 1e-9:
    st.success(
        "KVL terpenuhi: jumlah aljabar tegangan dalam "
        "loop tertutup sama dengan nol."
    )
else:
    st.warning(
        "Terdapat selisih numerik. Periksa kembali "
        "parameter rangkaian."
    )

st.info(
    "Catatan: simulasi ini menggunakan model resistor ideal "
    "dan sumber tegangan DC ideal."
)

st.caption("Proyek Simulasi Hukum Kirchhoff II | Teknik Elektro")

