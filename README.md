# 🐦 Flappy Bird Game - Streamlit App

A customizable Flappy Bird game built with Streamlit, featuring custom image and sound uploads.

## Features

- 🎮 Classic Flappy Bird gameplay
- 🖼️ Custom bird image upload
- 🎵 Custom sound effects (flap, score, game over)
- 📊 Score tracking
- 🎨 Beautiful UI with Streamlit

## Installation

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

To run the app locally:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Deployment to Streamlit Cloud

### Step 1: Push to GitHub

1. Create a new repository on GitHub
2. Push your code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Flappy Bird Streamlit app"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository and branch
5. Set the main file path to: `app.py`
6. Click "Deploy"

Your app will be live at: `https://YOUR_USERNAME-streamlit-app.streamlit.app`

## File Structure

```
flappy/
├── app.py                 # Main Streamlit application
├── flappybird.html        # Game HTML/JavaScript code
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml        # Streamlit configuration
└── README.md             # This file
```

## How to Play

1. Click "Start Game" to begin
2. Press **SPACE** or **Click** on the canvas to make the bird flap
3. Navigate through the pipes without hitting them
4. Score points by passing through pipes
5. Upload custom images and sounds from the sidebar to personalize your game!

## Customization

- **Bird Image**: Upload a PNG, JPG, or GIF file to replace the default bird
- **Flap Sound**: Upload an MP3, WAV, or OGG file for the flapping sound
- **Score Sound**: Upload an MP3, WAV, or OGG file for the scoring sound
- **Game Over Sound**: Upload an MP3, WAV, or OGG file for the game over sound

## Requirements

- Python 3.7+
- Streamlit 1.28.0+

## Notes

- The game uses HTML5 Canvas for rendering
- Custom files are loaded via base64 encoding
- All game logic runs client-side in the browser
- The game works best in modern browsers (Chrome, Firefox, Edge, Safari)

## Troubleshooting

If you encounter issues:

1. **Game not loading**: Ensure `flappybird.html` is in the same directory as `app.py`
2. **Files not uploading**: Check file size limits (Streamlit has a default limit)
3. **Sounds not playing**: Ensure your browser allows autoplay for audio

## License

Feel free to use and modify this project as you like!

---

Enjoy playing Flappy Bird! 🎮

