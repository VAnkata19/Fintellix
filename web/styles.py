import streamlit as st


SIDEBAR_CSS = """
<style>
    /* Force sidebar to always be visible and fixed width */
    [data-testid="stSidebar"] {
        min-width: 300px !important;
        max-width: 300px !important;
        position: relative !important;
    }
    
    /* Ensure sidebar is always displayed, whether expanded or collapsed */
    [data-testid="stSidebar"][aria-expanded="false"] {
        display: block !important;
        min-width: 300px !important;
        max-width: 300px !important;
        margin-left: 0 !important;
        visibility: visible !important;
    }
    
    [data-testid="stSidebar"][aria-expanded="true"] {
        display: block !important;
        min-width: 300px !important;
        max-width: 300px !important;
    }
    
    /* Allow the collapse/expand button to work */
    [data-testid="collapsedControl"] {
        display: block !important;
    }
</style>
"""


def apply_custom_styles():
    """Apply custom CSS styles to the app."""
    st.markdown(SIDEBAR_CSS, unsafe_allow_html=True)
