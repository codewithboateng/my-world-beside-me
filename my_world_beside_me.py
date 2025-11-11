import requests
import streamlit as st
from datetime import datetime

# --- Page setup ---
st.set_page_config(
    page_title="My World Beside Me",
    page_icon="♥️",
    layout="centered",
    initial_sidebar_state="collapsed"
)
def increment_and_get_views():
    try:
        res = requests.get("https://api.counterapi.dev/v1/my-world-beside-me/views/up")
        if res.status_code == 200:
            data = res.json()
            return data.get("count", 0)
        else:
            return 0
    except Exception as e:
        print("Counter API error:", e)
        return 0

    
views = increment_and_get_views()

if views is not None:
        st.markdown(
            f"<p style='text-align:center;color:#9b8e7c;'>👁️ {views:,} visits</p>",
            unsafe_allow_html=True
        )
else:
        st.markdown(
            "<p style='text-align:center;color:#9b8e7c;'>👁️ Visitors: —</p>",
            unsafe_allow_html=True
        )


# --- Session state ---
if "revealed_sections" not in st.session_state:
    st.session_state.revealed_sections = set()
if "ending_revealed" not in st.session_state:
    st.session_state.ending_revealed = False
if "selected_mood" not in st.session_state:
    st.session_state.selected_mood = None

# --- Styling ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;600&family=Poppins:wght@300;500&display=swap');

.stApp {
    background: radial-gradient(circle at top, #0e0e10 0%, #1b1b1e 50%, #000000 100%);
    color: #f2ede7;
    font-family: 'EB Garamond', serif;
}

/* Headings */
h1, h2, h3 {
    font-family: 'Poppins', sans-serif;
    text-align: center;
    color: #d8cbb6;
}

/* Title */
.main-title {
    font-size: 3.3em;
    margin: 40px 0 10px 0;
    color: #e9e1d1;
    text-shadow: 0 0 12px rgba(233,225,209,0.2);
}

/* Subtitle */
.subtitle {
    font-size: 1.1em;
    color: #c5b59a;
    letter-spacing: 2px;
    margin-bottom: 40px;
}

/* Divider */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #6e604e, transparent);
    margin: 40px 0;
}

/* Poem lines */
.poem-line {
    opacity: 0;
    animation: fadeInUp 1.5s ease forwards;
    text-align: center;
    font-size: 20px;
    line-height: 1.8;
    color: #f2ede7;
    margin: 15px 0;
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(25px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Buttons */
div.stButton > button {
    width: 100%;
    height: 65px;
    border-radius: 12px;
    font-family: 'Poppins', sans-serif;
    font-size: 17px;
    letter-spacing: 0.5px;
    color: #f2ede7;
    background: linear-gradient(135deg, #2d2620, #4d4034);
    border: 1px solid #6e604e;
    transition: all 0.3s ease;
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #3b3228, #5e4d3d);
    transform: translateY(-4px);
}

/* Response box */
.response-box {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 25px;
    margin: 25px 0;
    box-shadow: 0 0 30px rgba(255, 255, 255, 0.05);
    animation: fadeIn 1s ease;
}
@keyframes fadeIn {
    from { opacity: 0; transform: scale(0.97); }
    to { opacity: 1; transform: scale(1); }
}

/* Ending box */
.ending-box {
    background: linear-gradient(135deg, rgba(30,25,20,0.8), rgba(55,45,35,0.8));
    border-radius: 20px;
    border: 1px solid rgba(200,180,150,0.3);
    padding: 45px;
    text-align: center;
    box-shadow: 0 0 25px rgba(180,150,120,0.2);
}
.glow-text {
    font-family: 'Poppins', sans-serif;
    color: #f2d9a6;
    font-size: 1.3em;
    text-shadow: 0 0 12px rgba(242,217,166,0.4);
}

/* Footer */
.footer {
    margin-top: 70px;
    text-align: center;
    font-size: 14px;
    color: #9b8e7c;
    padding-bottom: 30px;
}
#MainMenu, header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 class='main-title'>My World Beside Me</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>An Interactive Poem for Her</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Intro ---
st.markdown("""
<div class='poem-line'>It's 1:40 am.</div>
<div class='poem-line'>The night exhales; vast, patient, unbothered by the noise of my mind.</div>
<div class='poem-line'>The cursor in VS Code flickers like a heartbeat that refuses to quit,</div>
<div class='poem-line'>each blink echoing the spaces I fill with thought and longing.</div>
<div class='poem-line'>Every line I write reaches for logic but collapses into feeling.</div>
<div class='poem-line'>Syntax can’t contain the truth of you.</div>
""", unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)

# --- Interactive words ---
st.markdown("<h3 style='text-align:center;'>✨ Touch the word that might tell you what I can’t say out loud</h3>", unsafe_allow_html=True)

cols = st.columns(4)
labels = [("💞 Love", "love"), ("🤫 Silence", "silence"), ("🌍 World", "world"), ("😴 Dream", "dream")]

for i, (label, key) in enumerate(labels):
    with cols[i]:
        if st.button(label, key=f"{key}_btn"):
            st.session_state.revealed_sections.add(key)

responses = {
    "love": "Love is the quiet architecture beneath everything I build. It’s the reason every system finds its rhythm.",
    "silence": "Silence is where I hear you most clearly; your breath, your trust, your peace brushing against my chaos.",
    "world": "The world asks for speed. You remind me that depth is a kind of arrival too.",
    "dream": "Dreams are just places my heart visits to keep you company while you sleep."
}

for key in st.session_state.revealed_sections:
    st.markdown(f"""
    <div class='response-box'>
        <p style='font-size:20px;'>{responses[key]}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Mood selector (messages to her) ---
st.markdown("<h3 style='text-align:center;'>💭 If you only knew how I’ve always felt and always will...</h3>", unsafe_allow_html=True)

mood = st.radio(
    "mood_selector",
    ["Peace", "Wonder", "Gratitude", "Longing"],
    label_visibility="collapsed",
    horizontal=True
)

if mood:
    messages = {
        "Peace": "You are my calm in every season. Even when years pass and noise fills the world, I will still find silence in you.",
        "Wonder": "Every time I see you, I fall into awe all over again. Time may move forward but my heart never moves past you.",
        "Gratitude": "If I could thank the universe for one thing, it would be the miracle of finding you and the grace of being allowed to stay.",
        "Longing": "Even when distance or years stretch between us, I will still ache for you in the softest parts of my soul. That ache is love that refuses to fade."
    }

    st.markdown(f"""
    <div class='response-box'>
        <p style='font-size:20px; font-style:italic;'>{messages[mood]}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


# --- Ending ---
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
if st.button("💌 Reveal the Ending"):
    st.session_state.ending_revealed = True
st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.ending_revealed:
    st.markdown("""
<div class='ending-box'>
    <p style='font-size:22px;'>
        I’ve spent my life as a software engineer chasing purpose through patterns and precision.
    </p>
    <p style='font-size:20px;'>
        Yet nothing I’ve ever built has run as flawlessly as the memory of you.
    </p>
    <p style='font-size:20px;'>
        Tonight, I silence the code and let the algorithms sleep.
    </p>
    <p style='font-size:20px;'>
        The world can keep its deadlines. I’m already home.
    </p>
    <p class='glow-text'>
        Because my universe begins and ends here, folded in the quiet of you.
    </p>
</div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown(f"""
<div class='footer'>
With all my love from: <a href='https://twitter.com/koboateng' target='_blank' style='color:#d8cbb6; text-decoration:none; font-weight:500;'>@koboateng</a>  
<span style='display:block; margin-top:6px; color:#9b8e7c;'>Built in the dark, for the light that is you.</span>
</div>
""", unsafe_allow_html=True)

