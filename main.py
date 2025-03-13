import streamlit as st
import secrets
import string
import random
from password_strength import PasswordStats

st.set_page_config(page_title="🔥 Ultimate PassGen & Strength Checker", page_icon="🔒")

st.markdown(
    """
    <style>
    .stApp {
        background: rgb(2,0,36);
        background: radial-gradient(circle, rgba(2,0,36,1) 0%, rgba(0,0,0,1) 100%);
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        color: white;
    }
    .stButton>button {
        background: linear-gradient(135deg, #ff0000, #ff7300);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        color: white;
        transform: scale(1.05);
        background: linear-gradient(135deg, #ff7300, #ff0000);
    }
    .stButton>button:active {
    background: linear-gradient(135deg, #ff7300, #ff0000) !important;
    color: white !important;
    transform: scale(1.05) !important;
    }
    .stButton>button:focus {
    outline: none !important;
    box-shadow: none !important;
    background: linear-gradient(135deg, #ff0000, #ff7300) !important;
    color: white !important;
    }
    .stProgress>div>div>div {
        background: linear-gradient(135deg, #ff0000, #ff7300);
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        font-size: 14px;
        color: rgba(255, 255, 255, 0.8);
    }
    </style>
    """,
    unsafe_allow_html=True
)

def ai_generate_password():
    words = ["Sh4d0w", "Hun73r", "Dr@g0n", "R0gu3", "N!nja", "Cyb3r", "M@trix", "St0rm", "Qu@ntum", "N30n", 
             "Ph4nt0m", "Gh0st", "Bl@de", "H4v0c", "Xtr3me", "V1per", "Sn!p3r", "Gl!tch", "H@ck3r", "T3rm1n@l",
             "R3b00t", "D3c0d3", "F1rew@ll", "D@rkNet", "Crypt0", "Neural", "Titan", "Fury", "Warp", "Cosm0s", 
             "Nebul@", "QuantumX", "ZeroDay", "Vortex", "Eclipse", "Cipher", "Zenith", "Gr!ff0n", "Str!k3r",
             "Galax!s", "Hyperion", "Ax!s", "Tundra", "Saber", "Stormbringer", "Eon", "Horizon", "Orion", "Nova"]
    numbers = ''.join(random.choices(string.digits, k=3))
    special_chars = ''.join(random.choices("@#$%&*!?", k=2))
    word1, word2 = random.sample(words, 2)
    password = f"{word1}{numbers}{special_chars}{word2}"
    return password

def generate_password(length, use_uppercase, use_digits, use_special, start_with_letter, exclude_similar, exclude_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if exclude_similar:
        characters = characters.translate(str.maketrans('', '', "O0I1l"))
    if exclude_chars:
        characters = characters.translate(str.maketrans('', '', exclude_chars))
    password = ''.join(secrets.choice(characters) for _ in range(length))
    if start_with_letter:
        password = secrets.choice(string.ascii_letters) + password[1:]
    return password

def check_password_strength(password):
    stats = PasswordStats(password)
    strength = round(stats.strength() * 10, 1)
    if strength < 2:
        feedback = "🔴 A toddler could guess this!"
    if strength < 3:
        feedback = "🔴 Bro, this password softer than a marshmallow. Ain't nobody safe with this!"
    elif strength < 5:
        feedback = "🟡 Meh, this got some weight, but a hacker gonna crack it like an egg!"
    elif strength < 7:
        feedback = "🟡 This pass ain't bad, but I bet a bored teenager could guess it in a lunch break!"
    elif strength < 8.5:
        feedback = "🟢 Yo, this password built like a tank. No one's touchin' it!"
    else:
        feedback = "🟢 Bruh, this password built like a bunker! Even a supercomputer gonna struggle!"
    return strength, feedback

st.title("🔒 Ultimate PassGen & Strength Checker 💥🔥")

tabs = st.tabs(["💀 Password Generator 🔥", "🛡️ Strength Checker 🛡️"])

with tabs[0]:
    st.header("🔑 Yo, let’s cook up a fire password! 🔥🔥")
    password_length = st.slider("🚀 How long you want this banger to be? 🎯", 8, 32, 12)
    smart_mode = st.checkbox("🤖 Let AI bless you with a strong pass! 🤯")
    
    disable_options = smart_mode
    use_uppercase = st.checkbox("🔥 Wanna flex with uppercase? 🔠", True, disabled=disable_options)
    use_digits = st.checkbox("💰 Need dem digits? 🔢", True, disabled=disable_options)
    use_special = st.checkbox("💀 Throw in some spicy symbols? 💥", True, disabled=disable_options)
    start_with_letter = st.checkbox("📝 Start with a letter? ✏️", True, disabled=disable_options)
    exclude_similar = st.checkbox("🚫 No confusing chars (O, 0, I, 1, l)? ❌", False, disabled=disable_options)
    exclude_chars = st.text_input("💔 Any characters you HATE? 😡 (Type them here)", disabled=disable_options)

    if st.button("🔥 Cook it up! 🚀💨"):
        if smart_mode:
            password = ai_generate_password()
        else:
            password = generate_password(password_length, use_uppercase, use_digits, use_special, start_with_letter, exclude_similar, exclude_chars)
        st.session_state.generated_password = password

    if "generated_password" in st.session_state:
        st.subheader("💾 Yo, here’s your new key to the vault! 🔐✨")
        st.code(st.session_state.generated_password, language="text")

        strength, feedback = check_password_strength(st.session_state.generated_password)
        st.progress(strength / 10)
        st.write(f"⚡ **{strength}/10** - {feedback} 🚀")

with tabs[1]:
    st.header("🛡️ How tough is your password?")
    user_password = st.text_input("🧐 Drop a password to check its toughness!", placeholder="Type your password here...")

    if user_password:
        strength, feedback = check_password_strength(user_password)
        st.progress(strength / 10)
        st.write(f"⚡ **{strength}/10** - {feedback} 🚀")

st.markdown("<div class='footer'>Made by HUXAIFA | Powered by Streamlit</div>", unsafe_allow_html=True)