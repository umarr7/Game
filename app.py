import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Page configuration
st.set_page_config(
    page_title="Flappy Bird Game",
    page_icon="🐦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main > div {
        padding-top: 2rem;
    }
    .stButton > button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🐦 Flappy Bird Game")
st.markdown("---")

# Sidebar for customization
with st.sidebar:
    st.header("🎨 Customization")
    
    # Bird Image Upload
    st.subheader("Bird Image")
    bird_image_file = st.file_uploader(
        "Upload Bird Image",
        type=['png', 'jpg', 'jpeg', 'gif'],
        key="bird_image",
        help="Upload a custom image for the bird"
    )
    
    # Sound Uploads
    st.subheader("🎵 Custom Sounds")
    
    flap_sound_file = st.file_uploader(
        "Flap Sound",
        type=['mp3', 'wav', 'ogg'],
        key="flap_sound",
        help="Upload a custom sound for flapping"
    )
    
    score_sound_file = st.file_uploader(
        "Score Sound",
        type=['mp3', 'wav', 'ogg'],
        key="score_sound",
        help="Upload a custom sound for scoring"
    )
    
    game_over_sound_file = st.file_uploader(
        "Game Over Sound",
        type=['mp3', 'wav', 'ogg'],
        key="game_over_sound",
        help="Upload a custom sound for game over"
    )
    
    st.markdown("---")
    st.markdown("### Instructions")
    st.markdown("""
    - **Press SPACE** or **Click** to make the bird flap
    - Navigate through the pipes to score points
    - Upload custom images and sounds to personalize your game!
    """)

# Read the HTML file
def get_game_html():
    """Read and return the game HTML content"""
    try:
        with open('flappybird.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error("Game file not found! Please ensure flappybird.html is in the same directory.")
        return None

# Convert uploaded files to base64 data URLs
def file_to_data_url(file, file_type):
    """Convert uploaded file to base64 data URL"""
    if file is not None:
        file_bytes = file.read()
        base64_encoded = base64.b64encode(file_bytes).decode()
        
        # Get file extension
        ext = file.name.split(".")[-1].lower()
        
        # Map extensions to MIME types
        mime_types = {
            'image': {
                'png': 'image/png',
                'jpg': 'image/jpeg',
                'jpeg': 'image/jpeg',
                'gif': 'image/gif',
                'webp': 'image/webp'
            },
            'audio': {
                'mp3': 'audio/mpeg',
                'wav': 'audio/wav',
                'ogg': 'audio/ogg',
                'm4a': 'audio/mp4',
                'aac': 'audio/aac'
            }
        }
        
        mime_type = mime_types.get(file_type, {}).get(ext, f'{file_type}/{ext}')
        return f"data:{mime_type};base64,{base64_encoded}"
    return None

# Get game HTML
game_html = get_game_html()

if game_html:
    # Process uploaded files
    bird_image_data = file_to_data_url(bird_image_file, 'image') if bird_image_file else None
    flap_sound_data = file_to_data_url(flap_sound_file, 'audio') if flap_sound_file else None
    score_sound_data = file_to_data_url(score_sound_file, 'audio') if score_sound_file else None
    game_over_sound_data = file_to_data_url(game_over_sound_file, 'audio') if game_over_sound_file else None
    
    # Inject file data into HTML using JavaScript
    # Inject before the closing body tag so it runs after the game script
    injection_script = f"""
    <script>
    // Store data URLs in window for the game to access
    {f"window.streamlitBirdImage = '{bird_image_data}';" if bird_image_data else ""}
    {f"window.streamlitFlapSound = '{flap_sound_data}';" if flap_sound_data else ""}
    {f"window.streamlitScoreSound = '{score_sound_data}';" if score_sound_data else ""}
    {f"window.streamlitGameOverSound = '{game_over_sound_data}';" if game_over_sound_data else ""}
    
    // Function to load Streamlit-provided assets
    function loadStreamlitAssets() {{
        // Load bird image
        if (window.streamlitBirdImage && typeof customBirdImage !== 'undefined') {{
            var img = new Image();
            img.onload = function() {{
                customBirdImage = img;
            }};
            img.src = window.streamlitBirdImage;
        }}
        
        // Load sounds
        if (window.streamlitFlapSound && typeof customFlapSound !== 'undefined') {{
            customFlapSound = new Audio(window.streamlitFlapSound);
            customFlapSound.volume = 0.5;
            if (document.getElementById('flapStatus')) {{
                document.getElementById('flapStatus').textContent = '✅';
                document.getElementById('flapStatus').className = 'sound-status';
            }}
        }}
        
        if (window.streamlitScoreSound && typeof customScoreSound !== 'undefined') {{
            customScoreSound = new Audio(window.streamlitScoreSound);
            customScoreSound.volume = 0.5;
            if (document.getElementById('scoreStatus')) {{
                document.getElementById('scoreStatus').textContent = '✅';
                document.getElementById('scoreStatus').className = 'sound-status';
            }}
        }}
        
        if (window.streamlitGameOverSound && typeof customGameOverSound !== 'undefined') {{
            customGameOverSound = new Audio(window.streamlitGameOverSound);
            customGameOverSound.volume = 0.5;
            if (document.getElementById('gameOverStatus')) {{
                document.getElementById('gameOverStatus').textContent = '✅';
                document.getElementById('gameOverStatus').className = 'sound-status';
            }}
        }}
    }}
    
    // Wait for game to initialize, then load assets
    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', function() {{
            setTimeout(loadStreamlitAssets, 1000);
        }});
    }} else {{
        setTimeout(loadStreamlitAssets, 1000);
    }}
    </script>
    """
    
    # Combine HTML with injection script
    final_html = game_html + injection_script
    
    # Display the game
    st.markdown("### 🎮 Play the Game")
    components.html(final_html, height=650, scrolling=False)
    
    # Info section
    with st.expander("ℹ️ About this Game"):
        st.markdown("""
        **Flappy Bird** is a classic side-scrolling game where you control a bird, attempting to fly between pipes without hitting them.
        
        **Features:**
        - Custom bird images
        - Custom sound effects
        - Smooth gameplay
        - Score tracking
        
        **Controls:**
        - Press **SPACE** or **Click** on the canvas to make the bird flap
        - Avoid hitting the pipes or the ground
        - Score points by passing through pipes
        """)

