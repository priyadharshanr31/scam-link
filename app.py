import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine", layout="centered")


def b64_file(path: str) -> str:
    data = Path(path).read_bytes()
    return base64.b64encode(data).decode("utf-8")


# Assets (make sure these exist)
CAT_PATH = "assets/cat.png"
GIF_PATH = "assets/yay.gif"

cat_b64 = b64_file(CAT_PATH)
gif_b64 = b64_file(GIF_PATH)

# Change the name here:
name = "Priyan"
# Optional URL-based name:
# name = st.query_params.get("name", "Priyan")

name_lower = name.lower()

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<style>
  /* FULL SCREEN PINK BACKGROUND */
  html, body {{
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
  }}

  body {{
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
    background: #f6c7d2;
  }}

  /* Center the card perfectly */
  .page {{
    min-height: 100vh;
    width: 100vw;
    display: grid;
    place-items: center;
    padding: 0;
  }}

  /* White card */
  .card {{
    width: min(860px, 92vw);
    background: #f2f2f2;
    border-radius: 18px;
    padding: 34px 22px 26px;
    box-shadow: 0 18px 40px rgba(0,0,0,0.14);
    position: relative;
    overflow: hidden; /* keep No inside */
  }}

  /* Subtle confetti dots overlay (inside the card) */
  .card::before {{
    content: "";
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(rgba(0,0,0,0.06) 1px, transparent 1px),
      radial-gradient(rgba(0,0,0,0.04) 1px, transparent 1px);
    background-size: 22px 22px, 28px 28px;
    background-position: 0 0, 10px 14px;
    opacity: 0.35;
    pointer-events: none;
  }}

  /* Ensure content stays above overlay */
  .content {{
    position: relative;
    z-index: 2;
  }}

  .icon {{
    display: grid;
    place-items: center;
    margin-bottom: 10px;
  }}

  .cat {{
    width: 86px;
    height: 86px;
    object-fit: contain;
    display: block;
  }}

  .title {{
    text-align: center;
    font-size: clamp(22px, 3.0vw, 42px);
    margin: 10px 0 26px;
    font-weight: 900;
    color: #111;
    letter-spacing: -0.02em;
  }}

  .name {{
    font-weight: 950;
  }}

  /* Buttons area */
  .buttonsArea {{
    position: relative;
    height: 92px;
    display: grid;
    place-items: center;
    margin-top: 6px;
  }}

  .btn {{
    border: none;
    cursor: pointer;
    font-weight: 800;
    padding: 12px 26px;
    border-radius: 999px;
    font-size: 16px;
    box-shadow: 0 10px 22px rgba(0,0,0,0.10);
    user-select: none;
    transition: transform 0.10s ease, box-shadow 0.25s ease, filter 0.25s ease;
    -webkit-tap-highlight-color: transparent;
  }}

  .btn:active {{
    transform: scale(0.98);
  }}

  .yes {{
    background: #ff2f6d;
    color: white;
    position: absolute;
    left: 50%;
    transform: translateX(10px);
  }}

  .no {{
    background: #ededed;
    color: #111;
    position: absolute;
    left: 50%;
    transform: translateX(-110px);
  }}

  .hint {{
    text-align: center;
    margin: 14px 0 0;
    font-size: 14px;
    color: rgba(0,0,0,0.55);
  }}

  .hidden {{ display: none; }}

  .yay {{
    text-align: center;
    font-weight: 950;
    font-size: clamp(28px, 4vw, 54px);
    margin: 6px 0 18px;
  }}

  .gifWrap {{
    display: grid;
    place-items: center;
    padding-bottom: 10px;
  }}

  .gifWrap img {{
    width: min(420px, 85%);
    border-radius: 12px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.12);
  }}

  /* -------------------------
     Floating Hearts Animation
     ------------------------- */
  .heartsLayer {{
    position: absolute;
    inset: 0;
    overflow: hidden;
    pointer-events: none;
    z-index: 3; /* above content */
  }}

  .heart {{
    position: absolute;
    bottom: -30px;
    font-size: 22px;
    opacity: 0.95;
    animation: floatUp linear forwards;
    filter: drop-shadow(0 6px 10px rgba(0,0,0,0.12));
  }}

  @keyframes floatUp {{
    0%   {{ transform: translateY(0) scale(0.9); opacity: 0; }}
    10%  {{ opacity: 1; }}
    100% {{ transform: translateY(-520px) scale(1.25); opacity: 0; }}
  }}

  /* -------------------------
     YES button pulse/glow (mobile)
     - We enable it when the device likely has no mouse (touch)
       OR when the screen is small.
     ------------------------- */
  @keyframes pulseGlow {{
    0%   {{ transform: translateX(10px) scale(1);   box-shadow: 0 10px 22px rgba(0,0,0,0.10); filter: brightness(1); }}
    50%  {{ transform: translateX(10px) scale(1.06); box-shadow: 0 0 0 10px rgba(255,47,109,0.18), 0 18px 34px rgba(0,0,0,0.14); filter: brightness(1.05); }}
    100% {{ transform: translateX(10px) scale(1);   box-shadow: 0 10px 22px rgba(0,0,0,0.10); filter: brightness(1); }}
  }}

  /* Touch devices (common mobile case) */
  @media (hover: none) and (pointer: coarse) {{
    .yes {{
      animation: pulseGlow 1.25s ease-in-out infinite;
    }}
  }}

  /* Also pulse on small screens just in case */
  @media (max-width: 520px) {{
    .yes {{
      animation: pulseGlow 1.25s ease-in-out infinite;
    }}
    .card {{
      width: min(560px, 92vw);
      padding: 28px 18px 22px;
    }}
  }}
</style>
</head>

<body>
  <div class="page">
    <div class="card" id="card">
      <div class="heartsLayer" id="heartsLayer"></div>

      <div class="content">
        <div class="icon">
          <img class="cat" src="data:image/png;base64,{cat_b64}" alt="cat" />
        </div>

        <!-- QUESTION SCREEN -->
        <div id="questionState">
          <div class="title"><span class="name">{name_lower}</span> will you be my valentine?</div>

          <div class="buttonsArea" id="buttonsArea">
            <button class="btn yes" id="yesBtn">Yes</button>
            <button class="btn no" id="noBtn">No</button>
          </div>

          <div class="hint">"No" seems a bit shy 😈</div>
        </div>

        <!-- YAY SCREEN -->
        <div id="yayState" class="hidden">
          <div class="title"><span class="name">{name_lower}</span> will you be my valentine?</div>
          <div class="yay">YAY! 🎉</div>

          <div class="gifWrap">
            <img src="data:image/gif;base64,{gif_b64}" alt="yay gif" />
          </div>
        </div>
      </div>
    </div>
  </div>

<script>
  const buttonsArea = document.getElementById("buttonsArea");
  const noBtn = document.getElementById("noBtn");
  const yesBtn = document.getElementById("yesBtn");

  const questionState = document.getElementById("questionState");
  const yayState = document.getElementById("yayState");

  const heartsLayer = document.getElementById("heartsLayer");
  const card = document.getElementById("card");

  function moveNoButton() {{
    const areaRect = buttonsArea.getBoundingClientRect();
    const btnRect = noBtn.getBoundingClientRect();
    const padding = 10;

    const maxX = areaRect.width - btnRect.width - padding * 2;
    const maxY = areaRect.height - btnRect.height - padding * 2;

    const x = padding + Math.random() * Math.max(0, maxX);
    const y = padding + Math.random() * Math.max(0, maxY);

    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
    noBtn.style.transform = "none";
  }}

  // Run away when cursor approaches "No" (desktop/mouse)
  noBtn.addEventListener("mouseenter", moveNoButton);

  buttonsArea.addEventListener("mousemove", (e) => {{
    const r = noBtn.getBoundingClientRect();
    const dx = e.clientX - (r.left + r.width / 2);
    const dy = e.clientY - (r.top + r.height / 2);
    const dist = Math.sqrt(dx*dx + dy*dy);
    if (dist < 95) moveNoButton();
  }});

  // If someone manages to click it, still move
  noBtn.addEventListener("click", (e) => {{
    e.preventDefault();
    moveNoButton();
  }});

  // Floating hearts
  function spawnHeart() {{
    const heart = document.createElement("div");
    heart.className = "heart";

    const hearts = ["💗","💖","💕","💘","💝","❤️"];
    heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];

    const cardRect = card.getBoundingClientRect();
    const x = Math.random() * (cardRect.width - 30);
    heart.style.left = x + "px";

    const size = 18 + Math.random() * 18;
    heart.style.fontSize = size + "px";

    const duration = 1.6 + Math.random() * 1.4;
    heart.style.animationDuration = duration + "s";

    heartsLayer.appendChild(heart);
    setTimeout(() => heart.remove(), (duration + 0.1) * 1000);
  }}

  function heartsBurst() {{
    let count = 0;
    const interval = setInterval(() => {{
      spawnHeart();
      count++;
      if (count >= 24) clearInterval(interval);
    }}, 60);

    let count2 = 0;
    const interval2 = setInterval(() => {{
      spawnHeart();
      count2++;
      if (count2 >= 18) clearInterval(interval2);
    }}, 120);
  }}

  // Vibrate ~5 seconds (mostly works on Android; iOS is limited by browser rules)
  function vibrateForFiveSeconds() {{
    if (!navigator.vibrate) return;

    // Pattern totals ~5 seconds (vibrate/pause repeated)
    navigator.vibrate([
      300, 200,
      300, 200,
      300, 200,
      300, 200,
      300, 200,
      300, 200,
      300, 200
    ]);
  }}

  // YES => show gif + hearts + vibration
  yesBtn.addEventListener("click", () => {{
    questionState.classList.add("hidden");
    yayState.classList.remove("hidden");
    heartsBurst();
    vibrateForFiveSeconds();
  }});

  // Initial setup
  noBtn.style.position = "absolute";
  noBtn.style.top = "22px";
  setTimeout(moveNoButton, 60);
</script>
</body>
</html>
"""

components.html(html, height=720, scrolling=False)
