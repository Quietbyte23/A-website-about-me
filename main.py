import streamlit as st

# Configurare pagină (titlu + iconiță în tab)
st.set_page_config(
    page_title="Alex | Personal Website",
    page_icon="👋",
    layout="centered"
)

# CSS personalizat pentru un look modern
st.markdown("""
    <style>
    /* Fundal general */
    .stApp {
        background-color: #0e1117;
    }
    /* Titluri */
    h1 {
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
    }
    h2, h3 {
        color: #e0e0e0;
        font-family: 'Segoe UI', sans-serif;
    }
    /* Text normal */
    p, li {
        color: #b0b0b0;
        font-family: 'Segoe UI', sans-serif;
        font-size: 16px;
    }
    /* Linia colorată sub titlu */
    .rainbow-line {
        height: 3px;
        background: linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #4b0082, #8f00ff);
        border-radius: 2px;
        margin-bottom: 30px;
    }
    /* Card pentru proiecte */
    .project-card {
        background-color: #1c1f26;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 4px solid #4b0082;
        transition: 0.3s;
    }
    .project-card:hover {
        border-left: 4px solid #8f00ff;
        background-color: #232733;
    }
    .project-card h4 {
        color: #ffffff;
        margin-top: 0;
    }
    .project-card p {
        color: #a0a0a0;
        margin-bottom: 0;
    }
    /* Butoane link */
    .stLinkButton a {
        background-color: #1c1f26 !important;
        color: #ffffff !important;
        border: 1px solid #4b0082 !important;
        border-radius: 8px !important;
        padding: 8px 18px !important;
        text-decoration: none !important;
        transition: 0.3s;
    }
    .stLinkButton a:hover {
        background-color: #4b0082 !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("<h1>Hello friend. 👋</h1>", unsafe_allow_html=True)
st.markdown('<div class="rainbow-line"></div>', unsafe_allow_html=True)

st.markdown("<h2>Welcome to my personal website.</h2>", unsafe_allow_html=True)

st.markdown("""
Hello, my name is **Alex**, I'm 15 years old and I made this website myself. 
I'm a programmer and a learner — I love to learn new things and build new projects. 
If you want to see more of my work, you can follow me on GitHub or Instagram.
""")

# ===== LINK-URI =====
col1, col2 = st.columns(2)
with col1:
    st.link_button("🐙 Follow me on GitHub", "https://github.com/Quietbyte23?")
with col2:
    st.link_button("📸 Follow me on Instagram", "https://www.instagram.com/777alexandrufoto/")

st.markdown("---")

# ===== DESPRE MINE =====
st.markdown("<h3>About me</h3>", unsafe_allow_html=True)
st.markdown("""
I'm a beginner programmer and I love learning new things. 
I've made some projects in the past and I'm proud to say I made them with mind and heart. 
Here's a link to my GitHub profile where you can see my projects and my work.
""")

st.markdown("---")

# ===== PROIECTE =====
st.markdown("<h3>My Projects</h3>", unsafe_allow_html=True)

projects = [
    {
        "name": "Project 1 - My first bot",
        "desc": "A Python bot made in python  that responds to commands."
    },
    {
        "name": "Project 2 - Personal Website",
        "desc": "This website! Made with Streamlit and Python."
    },
    {
        "name": "Project 3 - A website for my photography",
        "desc": "I made it this website to showcase my photography work."
    }
]

for p in projects:
    st.markdown(f"""
        <div class="project-card">
            <h4>{p['name']}</h4>
            <p>{p['desc']}</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ===== POZĂ (opțional) =====
st.markdown("<h3>Me</h3>", unsafe_allow_html=True)
# Decomentează linia de mai jos dacă ai o poză în folderul cu main.py
# st.image("poza_mea.jpg", caption="That's me!", width=400)

# Sau folosește o poză de pe internet:
st.image("https://picsum.photos/600/300", caption="Random photo")

# ===== FOOTER =====
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#666;'>Made with ❤️ by Alex • 2026</p>",
    unsafe_allow_html=True
)