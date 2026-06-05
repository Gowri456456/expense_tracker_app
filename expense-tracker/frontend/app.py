"""
Smart Finance Manager — Premium Streamlit Frontend
Main entry point with updated luxury dark-cyber navigation, authentication, and page routing.
"""

import streamlit as st
import sys
import os

# Add project root to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from frontend.utils.auth import (
    init_session_state,
    is_authenticated,
    show_auth_page,
    do_logout,
)

# ─────────────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────────────

st.set_page_config(
    page_title="EXPENSE TRACKER APP",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────
# Custom Luxury UI CSS
# ─────────────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

/* Base Typography */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Luxury Sidebar Gradient */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617 0%, #0B1329 100%) !important;
    border-right: 1px solid rgba(56, 189, 248, 0.15) !important;
}

/* Glassmorphism Metric Cards */
[data-testid="stMetric"] {
    background: linear-gradient(
        135deg,
        rgba(30, 41, 59, 0.7) 0%,
        rgba(15, 23, 42, 0.9) 100%
    ) !important;
    border: 1px solid rgba(56, 189, 248, 0.2) !important;
    border-radius: 16px !important;
    padding: 1.2rem !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25) !important;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-4px) scale(1.01);
    border-color: rgba(34, 211, 238, 0.5) !important;
    box-shadow: 0 10px 25px rgba(34, 211, 238, 0.15) !important;
    transition: all 0.3s ease-in-out;
}

/* Premium Curved Buttons */
.stButton > button {
    border-radius: 12px !important;
    font-weight: 700 !important;
    background: linear-gradient(90deg, #06B6D4 0%, #3B82F6 100%) !important;
    color: white !important;
    border: none !important;
    padding: 0.5rem 1rem !important;
    box-shadow: 0 4px 12px rgba(6, 182, 212, 0.2) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(6, 182, 212, 0.4) !important;
    background: linear-gradient(90deg, #22D3EE 0%, #60A5FA 100%) !important;
    transition: all 0.2s ease;
}

/* Input Fields Style */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 12px !important;
    background-color: #0F172A !important;
    border: 1px solid #334155 !important;
    color: #F8FAFC !important;
}

.stTextInput input:focus {
    border-color: #06B6D4 !important;
}

/* Elegant Custom Card */
.card {
    background: #0F172A;
    border-radius: 16px;
    padding: 24px;
    border: 1px solid #1E293B;
}

/* Cyber Metallic Gradient Text */
.gradient-text {
    background: linear-gradient(
        135deg,
        #38BDF8 0%,
        #34D399 50%,
        #22D3EE 100%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    letter-spacing: -0.5px;
}

/* Hide Unwanted UI Elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────
# Session State
# ─────────────────────────────────────────────────────

init_session_state()
st.write("✨ SYSTEM UPDATE SUCCESSFUL - PREMIUM LOOK LOADING... ✨")

# ─────────────────────────────────────────────────────
# Authentication
# ─────────────────────────────────────────────────────

if not is_authenticated():
    show_auth_page()
    st.stop()

# ─────────────────────────────────────────────────────
# Sidebar Layout
# ─────────────────────────────────────────────────────

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding:15px 0px;">
            <h2 class="gradient-text" style="font-size: 26px;">
                ⚡ Quantum Finance
            </h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<hr style='border-color: rgba(255,255,255,0.05);' />", unsafe_allow_html=True)

    # Logged In User Badge
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, rgba(56,189,248,0.08) 0%, rgba(52,211,153,0.05) 100%);
            padding: 14px;
            border-radius: 14px;
            margin-bottom: 20px;
            border: 1px solid rgba(56,189,248,0.15);
        ">
            <span style="color: #94A3B8; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">Active Session</span><br>
            <span style="color: #F8FAFC; font-weight: 600; font-size: 15px;">🔒 {st.session_state.username}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Modern Navigation
    page = st.radio(
        "Navigation Menu",
        [
            "🏠 Overview Dashboard",
            "💸 Log New Expense",
            "💵 Log New Income",
            "📊 Financial Analytics",
            "📜 Ledger History"
        ],
        label_visibility="collapsed",
    )

    st.markdown("<hr style='border-color: rgba(255,255,255,0.05);' />", unsafe_allow_html=True)

    # Sleek Red Logout Button
    if st.button("🚪 Terminate Session", use_container_width=True):
        do_logout()
        st.rerun()

    st.markdown(
        """
        <div style="text-align:center; padding-top:40px; font-size:11px; color:#475569; letter-spacing: 0.5px;">
            © 2026 Gowri K <br>
            <span style="color: #06B6D4;">Quantum System Engine</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────────────
# Main Dashboard Header
# ─────────────────────────────────────────────────────

st.markdown("""
<div style="padding-bottom: 10px;">
    <h1 class="gradient-text" style="font-size: 36px; font-weight: 800;">
        📊 Control Center Dashboard
    </h1>
    <p style="color: #64748B; margin-top: -10px; font-size: 15px;">
        Real-time financial analytics and smart asset tracking.
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────
# Secure Page Router
# ─────────────────────────────────────────────────────

if page == "🏠 Overview Dashboard":
    from frontend.views.dashboard import render_dashboard
    render_dashboard()

elif page == "💸 Log New Expense":
    from frontend.views.add_expense import render_add_expense
    render_add_expense()

elif page == "💵 Log New Income":
    from frontend.views.add_income import render_add_income
    render_add_income()

elif page == "📊 Financial Analytics":
    from frontend.views.budgets import render_budgets
    render_budgets()

elif page == "📜 Ledger History":
    from frontend.views.history import render_history
    render_history()
