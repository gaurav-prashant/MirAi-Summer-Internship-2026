import streamlit as st
import json
import requests
from io import BytesIO
from gtts import gTTS
from groq import Groq
import os

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Visual Novel Engine",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="expanded",
)

from dotenv import load_dotenv
load_dotenv()

# ── Inject Modern Minimalist CSS ──────────────────────────────────────────────
def _load_css(filename: str) -> None:
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

_load_css("style5.css")

# ── Securely Cache Groq Client ────────────────────────────────────────────────
@st.cache_resource
def get_groq_client():
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))

client = get_groq_client()

# ============================================================
#  SIDEBAR — Story Controls
# ============================================================

with st.sidebar:
    st.markdown("<div class='sidebar-title'>⚙️ Story Settings</div>", unsafe_allow_html=True)
    st.markdown("<hr class='sb-divider'>", unsafe_allow_html=True)

    # Active Progress Card
    chapter = len([
        m for m in st.session_state.get("chat_history", [])
        if m["role"] == "assistant"
    ])
    st.markdown(
        f"""
        <div class='progress-card'>
            <span class='progress-label'>Scenes Progress</span>
            <span class='progress-value'>#{chapter}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Genre
    st.markdown("<div class='sidebar-label'>Story Genre</div>", unsafe_allow_html=True)
    genre = st.selectbox(
        "Genre",
        ["Cyberpunk", "Fantasy", "Sci-Fi", "Mystery", "Post-Apocalyptic", "Horror", "Steampunk"],
        label_visibility="collapsed",
    )

    # Art Style
    st.markdown("<div class='sidebar-label'>Art Style</div>", unsafe_allow_html=True)
    art_style = st.selectbox(
        "Art Style",
        ["Anime", "Digital Art", "Pixel Art", "Cinematic Realism", "Oil Painting", "Watercolor", "Dark Fantasy"],
        label_visibility="collapsed",
    )

    st.markdown("<hr class='sb-divider'>", unsafe_allow_html=True)

    # Features Toggles
    st.markdown("<div class='sidebar-label'>Audio & Visuals</div>", unsafe_allow_html=True)
    enable_tts = st.toggle("Voice Narration", value=True)
    enable_images = st.toggle("Scene Artwork", value=True)

    st.markdown("<hr class='sb-divider'>", unsafe_allow_html=True)

    # Reset Button
    if st.session_state.get("current_scene") is not None:
        if st.button("🔄 Start New Story", key="reset_btn"):
            st.session_state.chat_history = []
            st.session_state.current_scene = None
            st.rerun()

# ── System Prompt ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = f"""
You are a master interactive story writer for a visual novel.
Genre: {genre}
Art Style: {art_style}

You MUST ALWAYS reply in strict, valid JSON without Markdown wrapping or extra text.
The JSON object must have these EXACT keys:
1. "story_text": A compelling narrative paragraph (2-4 sentences) written in second-person.
2. "image_prompt": A highly detailed prompt tailored for an image generator (style: {art_style}).
3. "options": A JSON array containing 2 to 3 distinct string options for the player's next move.

Example format:
{{
  "story_text": "You stand before the dark citadel, its obsidian spires piercing a blood-red sky.",
  "image_prompt": "A towering dark obsidian citadel under a red sky, {art_style} style, dramatic lighting",
  "options": ["Enter the main gate boldly", "Search for a hidden side entrance", "Turn back and flee"]
}}
"""

# ── Session State Init ────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_scene" not in st.session_state:
    st.session_state.current_scene = None

# ============================================================
#  HELPER FUNCTIONS
# ============================================================

def get_next_scene(user_input: str = None):
    """Fetch next story node from Groq."""
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for turn in st.session_state.chat_history:
            messages.append(turn)

        if user_input:
            messages.append({"role": "user", "content": f"Player chose: {user_input}"})
            st.session_state.chat_history.append(
                {"role": "user", "content": f"Player chose: {user_input}"}
            )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            response_format={"type": "json_object"},
            temperature=0.9,
        )
        response_text = response.choices[0].message.content
        parsed_data = json.loads(response_text)
        st.session_state.current_scene = parsed_data
        st.session_state.chat_history.append(
            {"role": "assistant", "content": response_text}
        )
    except Exception as e:
        st.error(f"⚠️ Error generating story: {e}")


def generate_image(prompt: str):
    """Fetch scene image from Pollinations AI."""
    try:
        encoded_prompt = requests.utils.quote(prompt)
        url = (
            f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            f"?width=840&height=480&nologo=true&model=flux"
        )
        res = requests.get(url, timeout=15)
        if res.status_code == 200:
            return res.content
        else:
            st.toast("Image generator busy — skipping visual.", icon="⚠️")
            return None
    except Exception:
        st.toast("Network issue with image generator.", icon="⚠️")
        return None


def generate_tts(text: str):
    """Generate TTS audio narration."""
    try:
        tts = gTTS(text=text, lang="en", slow=False)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        return mp3_fp
    except Exception:
        st.toast("Audio narration unavailable.", icon="⚠️")
        return None

# ============================================================
#  APP HEADER
# ============================================================

st.markdown(
    """
    <div class='app-header'>
        <h1 class='app-title-main'>AI Visual Novel Engine</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
#  START / LAUNCH CARD
# ============================================================

if st.session_state.current_scene is None:
    st.markdown(
        f"""
        <div class='start-card'>
            <div class='start-card-title'>Ready to begin your journey?</div>
            <div class='start-card-desc'>
                Select your favorite genre and art style in the sidebar, then hit start.
            </div>
            <div class='start-pills'>
                <span class='start-pill'>Genre: {genre}</span>
                <span class='start-pill'>Style: {art_style}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='start-btn-wrap'>", unsafe_allow_html=True)
        if st.button("🚀 Start Adventure", key="start_btn", use_container_width=True):
            with st.spinner("Generating opening scene…"):
                get_next_scene("Begin the adventure with an exciting opening scene.")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
#  ACTIVE SCENE DISPLAY
# ============================================================

scene = st.session_state.current_scene
if scene:
    st.markdown("<div class='scene-wrapper'>", unsafe_allow_html=True)

    # Narrative Card
    story_text = scene.get("story_text", "")
    if story_text:
        st.markdown(
            f"""
            <div class='narrative-card'>
                <p class='narrative-text'>{story_text}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Audio Narration
    if enable_tts and story_text:
        audio_data = generate_tts(story_text)
        if audio_data:
            st.audio(audio_data, format="audio/mp3", autoplay=True)

    # Scene Image
    if enable_images:
        image_prompt = scene.get("image_prompt", "")
        if image_prompt:
            with st.spinner("Rendering scene artwork…"):
                img_bytes = generate_image(image_prompt)
            if img_bytes:
                st.markdown("<div class='scene-img-box'>", unsafe_allow_html=True)
                st.image(img_bytes, use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

    # Choice Options
    options = scene.get("options", [])
    if options:
        st.markdown("<div class='choice-label'>Select your next action</div>", unsafe_allow_html=True)

        for idx, choice in enumerate(options):
            if st.button(
                f"→  {choice}",
                key=f"choice_{idx}",
                use_container_width=True,
            ):
                with st.spinner("Crafting next scene…"):
                    get_next_scene(choice)
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)