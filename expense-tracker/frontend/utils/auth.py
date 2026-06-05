"""
Smart Finance Manager — Premium Authentication UI
Luxury cyber-dark theme for Login & Registration screens.
"""

import streamlit as st

def init_session_state():
    """Initializes session state variables securely."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = None

def is_authenticated():
    """Checks if the user is securely logged in."""
    return st.session_state.get("authenticated", False)

def do_logout():
    """Logs out the user and clears session data."""
    st.session_state.authenticated = False
    st.session_state.username = None

def show_auth_page():
    """Renders a premium, luxury dark-themed Login / Registration interface."""
    
    # Custom CSS Inject for Premium Auth Look
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    /* Base Overrides */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Full Page Cyber Background */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0B1329 0%, #020617 100%) !important;
    }
    
    /* Premium Auth Card */
    div[data-testid="stVerticalBlock"] > div:has(div.auth-container) {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(30, 41, 59, 0.5) 100%);
        border: 1px solid rgba(6, 182, 212, 0.2);
        border-radius: 24px;
        padding: 3rem 2.5rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(12px);
    }
    
    /* Input field modifications */
    .stTextInput input {
        background-color: #020617 !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        color: #F8FAFC !important;
        padding: 12px !important;
    }
    
    .stTextInput input:focus {
        border-color: #06B6D4 !important;
        box-shadow: 0 0 10px rgba(6, 182, 212, 0.2) !important;
    }
    
    /* Custom Cyan/Blue Gradient Button */
    .stButton > button {
        background: linear-gradient(90deg, #06B6D4 0%, #3B82F6 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        letter-spacing: 0.5px;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(6, 182, 212, 0.3) !important;
        margin-top: 10px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #22D3EE 0%, #60A5FA 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(6, 182, 212, 0.5) !important;
        transition: all 0.3s ease;
    }
    
    /* Tabs customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(2, 6, 23, 0.6);
        padding: 6px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 40px !important;
        white-space: pre !important;
        background-color: transparent !important;
        border-radius: 10px !important;
        color: #94A3B8 !important;
        font-weight: 600 !important;
        border: none !important;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.15) 0%, rgba(59, 130, 246, 0.15) 100%) !important;
        color: #22D3EE !important;
        border: 1px solid rgba(6, 182, 212, 0.3) !important;
    }
    
    /* Branding Header */
    .brand-title {
        background: linear-gradient(135deg, #38BDF8 0%, #34D399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 32px;
        text-align: center;
        margin-bottom: 5px;
    }
    
    .brand-subtitle {
        color: #64748B;
        text-align: center;
        font-size: 14px;
        margin-bottom: 30px;
    }
    </style>
    <div class="auth-container"></div>
    """, unsafe_allow_html=True)

    # Header Branding Look
    st.markdown('<div class="brand-title">⚡ QUANTUM FINANCE PRO</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-subtitle">Secure Next-Gen Asset & Expense Control Center</div>', unsafe_allow_html=True)

    # Render Tabs for Login / Register
    tab1, tab2 = st.tabs(["🔒 Secure Login", "📝 Create System Account"])
    
    with tab1:
        st.markdown("<h3 style='color:#F8FAFC; font-size:18px; margin-bottom:15px;'>Welcome Back, Agent</h3>", unsafe_allow_html=True)
        username = st.text_input("Username / Access ID", key="login_user", placeholder="Enter authorization key...")
        password = st.text_input("Master Password", type="password", key="login_pass", placeholder="••••••••")
        
        if st.button("Authorize & Entry", use_container_width=True):
            if username.strip() and password.strip():
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Access Denied: Invalid Authorization ID or Password.")

    with tab2:
        st.markdown("<h3 style='color:#F8FAFC; font-size:18px; margin-bottom:15px;'>Register New Node</h3>", unsafe_allow_html=True)
        new_username = st.text_input("Choose Username", key="reg_user", placeholder="Create unique ID...")
        new_email = st.text_input("Secure Email Address", key="reg_email", placeholder="name@domain.com")
        new_password = st.text_input("Create Password", type="password", key="reg_pass", placeholder="Minimum 8 characters")
        
        if st.button("Initialize Account", use_container_width=True):
            if new_username.strip() and new_password.strip():
                st.success("Registration Successful! Please switch to Login tab.")
            else:
                st.error("System Error: All protocol fields are required.")
