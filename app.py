import streamlit as st
import time

# Page configuration for a premium, clean look
st.set_page_config(
    page_title="Interactive Greeting App",
    page_icon="✨",
    layout="centered"
)

# Premium modern styling
st.markdown("""
+<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .header-container {
        text-align: center;
        padding: 2.5rem 1.5rem;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    }
    
    .app-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .app-subtitle {
        font-size: 1.1rem;
        color: #718096;
        font-weight: 400;
    }
    
    .interactive-card {
        padding: 2rem;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
    }
    
    .greeting-banner {
        padding: 1.5rem;
        border-radius: 16px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        font-size: 1.5rem;
        font-weight: 600;
        text-align: center;
        margin-top: 1rem;
        box-shadow: 0 4px 15px rgba(118, 75, 162, 0.3);
        animation: fadeIn 0.8s ease-in-out;
    }
    
    .age-badge {
        display: inline-block;
        padding: 0.35rem 1rem;
        border-radius: 50px;
        background-color: rgba(118, 75, 162, 0.15);
        color: #764ba2;
        font-weight: 600;
        font-size: 1.1rem;
        margin-top: 0.5rem;
        border: 1px solid rgba(118, 75, 162, 0.2);
    }

    /* Custom button styling */
    div.stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        transition: all 0.3s ease !important;
        width: 100%;
        box-shadow: 0 4px 15px rgba(118, 75, 162, 0.2) !important;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(118, 75, 162, 0.4) !important;
    }
    
    div.stButton > button:active {
        transform: translateY(0) !important;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# Title Header Card
st.markdown("""
<div class="header-container">
    <div class="app-title">✨ Interactive Playground</div>
    <div class="app-subtitle">Enter your details and let's celebrate together!</div>
</div>
""", unsafe_allow_html=True)

# Main interactive area
st.markdown("<div class='interactive-card'>", unsafe_allow_html=True)

# Text Input for Name
name = st.text_input("👤 Enter your name:", placeholder="Type your name here...")

# Age Slider
age = st.slider("🎂 Select your age:", min_value=1, max_value=120, value=25)

st.markdown("</div>", unsafe_allow_html=True)

# Greeting message
if name.strip():
    st.markdown(f"""
    <div class="greeting-banner">
        👋 Hello, {name}! Welcome to the app!
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-top: 1rem;">
        You have selected age: <span class="age-badge">{age} years young</span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("💡 Please enter your name in the text box above to get greeted!")

# Celebration Section
st.write("")
st.write("")
if st.button("🎉 Click to Celebrate! 🎉"):
    st.balloons()
    st.snow()
    if name.strip():
        st.success(f"Cheers to {name} (Age {age})! Let's party! 🥳")
    else:
        st.success("Cheers to you! Let's party! 🥳")