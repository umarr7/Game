import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Page configuration
st.set_page_config(
    page_title="Horror Flappy - Nightmare Flight",
    page_icon="🦇",
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

# Helper functions (defined before use)
def load_default_file(filename, file_type):
    """Load default file from folder if it exists"""
    if os.path.exists(filename):
        try:
            with open(filename, 'rb') as f:
                file_bytes = f.read()
                base64_encoded = base64.b64encode(file_bytes).decode()
                
                # Get file extension
                ext = filename.split(".")[-1].lower()
                
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
                        'mp4': 'audio/mp4',  # MP4 audio support
                        'm4a': 'audio/mp4',
                        'aac': 'audio/aac'
                    }
                }
                
                mime_type = mime_types.get(file_type, {}).get(ext, f'{file_type}/{ext}')
                return f"data:{mime_type};base64,{base64_encoded}"
        except Exception as e:
            pass  # Silently fail if file can't be loaded
    return None

def get_default_file(possible_names, file_type):
    """Try to load default file with multiple possible names"""
    for name in possible_names:
        result = load_default_file(name, file_type)
        if result:
            return result
    return None

# Title
st.title("🦇 Horror Flappy - Nightmare Flight")
st.markdown("### 💀 Navigate through the darkness... if you dare!")
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
        type=['mp3', 'wav', 'ogg', 'mp4', 'm4a'],
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
    
    # Show which default files are loaded
    default_files_loaded = []
    if not bird_image_file:
        # Prioritize bird.png (user's file)
        default_bird = get_default_file(['bird.png', 'bird.jpg', 'bird.jpeg', 'bird.gif', 'default_bird.png'], 'image')
        if default_bird:
            default_files_loaded.append("✅ Default bird image loaded (bird.png)")
    if not flap_sound_file:
        # Prioritize flap.mp4 (user's file)
        default_flap = get_default_file(['flap.mp4', 'flap.mp3', 'flap.wav', 'jump.mp3', 'jump.wav', 'flap.ogg'], 'audio')
        if default_flap:
            default_files_loaded.append("✅ Default flap sound loaded (flap.mp4)")
    if not game_over_sound_file:
        default_gameover = get_default_file(['gameover.mp3', 'gameover.wav', 'die.mp3', 'die.wav', 'game_over.mp3'], 'audio')
        if default_gameover:
            default_files_loaded.append("✅ Default game over sound loaded")
    
    if default_files_loaded:
        st.markdown("### Default Files")
        for msg in default_files_loaded:
            st.markdown(msg)
        st.markdown("---")
    
    st.markdown("### ⚠️ Instructions")
    st.markdown("""
    - **Press SPACE** or **Click** to fly through the darkness
    - Navigate through the spiky obstacles to collect souls
    - Avoid the shadows... or face your doom!
    - Upload custom images and sounds to personalize your nightmare!
    
    **Default Files:**
    Place these files in the same folder to use as defaults:
    - `bird.png` (or bird.jpg/gif) - Default creature image ✅
    - `flap.mp4` (or flap.mp3/flap.wav/jump.mp3) - Default flap sound ✅
    - `gameover.mp3` (or die.mp3/gameover.wav) - Default death sound
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
                        'mp4': 'audio/mp4',  # MP4 audio support
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
    # Process uploaded files (custom uploads take priority)
    # If no custom upload, try to load default files
    bird_image_data = None
    if bird_image_file:
        bird_image_data = file_to_data_url(bird_image_file, 'image')
    else:
        # Try default bird image names
        bird_image_data = get_default_file(
            ['bird.png', 'bird.jpg', 'bird.jpeg', 'bird.gif', 'default_bird.png', 'default_bird.jpg'],
            'image'
        )
    
    flap_sound_data = None
    if flap_sound_file:
        flap_sound_data = file_to_data_url(flap_sound_file, 'audio')
    else:
        # Try default flap/jump sound names (prioritize flap.mp4)
        flap_sound_data = get_default_file(
            ['flap.mp4', 'flap.mp3', 'flap.wav', 'jump.mp3', 'jump.wav', 'flap.ogg', 'default_flap.mp3', 'default_jump.mp3'],
            'audio'
        )
    
    score_sound_data = None
    if score_sound_file:
        score_sound_data = file_to_data_url(score_sound_file, 'audio')
    else:
        # Try default score sound names (optional, can be None)
        score_sound_data = get_default_file(
            ['score.mp3', 'score.wav', 'point.mp3', 'default_score.mp3'],
            'audio'
        )
    
    game_over_sound_data = None
    if game_over_sound_file:
        game_over_sound_data = file_to_data_url(game_over_sound_file, 'audio')
    else:
        # Try default game over/die sound names
        game_over_sound_data = get_default_file(
            ['gameover.mp3', 'gameover.wav', 'die.mp3', 'die.wav', 'game_over.mp3', 'default_gameover.mp3', 'default_die.mp3'],
            'audio'
        )
    
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
    with st.expander("💀 About this Nightmare"):
        st.markdown("""
        **Horror Flappy - Nightmare Flight** is a dark, horror-themed side-scrolling game where you control a bat-like creature, attempting to fly through spiky obstacles in the darkness.
        
        **Features:**
        - 🦇 Horror-themed graphics with dark atmosphere
        - 🔴 Glowing red effects and spooky visuals
        - 💀 Custom creature images
        - 🎵 Custom sound effects
        - 🌙 Animated fog and blood-red moon
        - ⚡ Smooth gameplay with horror aesthetics
        
        **Controls:**
        - Press **SPACE** or **Click** on the canvas to make the creature fly
        - Avoid hitting the spiky obstacles or the ground
        - Collect souls by passing through obstacles
        - The darkness awaits... ⚠️
        """)

