"""
Smart Finance Manager — Streamlit Frontend
Main entry point with navigation, authentication, and page routing.
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
    page_title="Smart Finance Manager",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────
# Custom CSS
# ─────────────────────────────────────────────────────

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
    border-right: 1px solid rgba(0, 200, 83, 0.2);
}

/* Metric Cards */
[data-testid="stMetric"] {
    background: linear-gradient(
        135deg,
        rgba(0, 200, 83, 0.12) 0%,
        rgba(34, 197, 94, 0.08) 100%
    );
    border: 1px solid rgba(0, 200, 83, 0.2);
    border-radius: 15px;
    padding: 1rem;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    transition: 0.3s;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    font-weight: 600;
}

.stButton > button:hover {
    transform: translateY(-2px);
    transition: 0.2s;
}

/* Input Fields */
.stTextInput input,
.stNumberInput input {
    border-radius: 10px !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    font-weight: 600;
}

/* Custom Card */
.card {
    background: white;
    border-radius: 15px;
    padding: 20px;
    border: 1px solid #E5E7EB;
}

/* Gradient Text */
.gradient-text {
    background: linear-gradient(
        135deg,
        #00C853 0%,
        #22C55E 50%,
        #16A34A 100%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────
# Session State
# ─────────────────────────────────────────────────────

init_session_state()

# ─────────────────────────────────────────────────────
# Authentication
# ─────────────────────────────────────────────────────

if not is_authenticated():
    show_auth_page()
    st.stop()

# ─────────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────────

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center;padding:10px;">
            <h2 class="gradient-text">
                📈 Smart Finance Manager
            </h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown(
        f"""
        <div style="
            background:rgba(0,200,83,0.1);
            padding:12px;
            border-radius:10px;
            margin-bottom:15px;
        ">
            <small>Logged in as</small><br>
            <b>👨‍💻 {st.session_state.username}</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

    page = st.radio(
        "Navigate",
        [
            "🏠 Home",
            "💸 Expense Entry",
            "💵 Income Entry",
            "📊 Analytics",
            "📜 Transactions"
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")

    if st.button("🚪 Logout", use_container_width=True):
        do_logout()
        st.rerun()

    st.markdown(
        """
        <div style="text-align:center;padding-top:20px;font-size:12px;color:gray;">
            © 2026 Gowri K <br>
            Smart Finance Manager
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────────────
# Main Header
# ─────────────────────────────────────────────────────

st.markdown("""
<h1 class="gradient-text">
📊 Personal Finance Dashboard
</h1>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────
# Page Router
# ─────────────────────────────────────────────────────

if page == "🏠 Home":
    from frontend.views.dashboard import render_dashboard
    render_dashboard()

elif page == "💸 Expense Entry":
    from frontend.views.add_expense import render_add_expense
    render_add_expense()

elif page == "💵 Income Entry":
    from frontend.views.add_income import render_add_income
    render_add_income()

elif page == "📊 Analytics":
    from frontend.views.budgets import render_budgets
    render_budgets()

elif page == "📜 Transactions":
    from frontend.views.history import render_history
    render_history()
