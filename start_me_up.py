# --- Imports ---
# subprocess: Launches external applications with command-line arguments (in this case, Chrome)
# time: Provides delays (important for waiting on slow app or network responses)
# pygetwindow: Lets us detect and manipulate OS-level application windows (like Chrome)
# pyautogui: Required by pygetwindow and useful for future mouse/keyboard/screen control
import subprocess
import time
import pygetwindow as gw  # Short alias for convenience in calling window-related functions
import pyautogui

# --- Configuration ---
# Absolute path to the Chrome executable — this may need to be changed based on your system setup
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# List of URLs to be opened as separate tabs in one Chrome window
# Order matters: the first URL becomes the active tab
urls_to_open = [
    "https://mail.google.com/mail/u/1/#inbox",       # Personal Gmail
    "https://mail.google.com/mail/u/0/#inbox",       # Work Gmail
    "http://puregeek.atlassian.net/jira/your-work",  # JIRA task board
    "https://github.com"                             # GitHub dashboard
]

# --- Step 1: Launch Chrome and open all tabs ---
# Passing all URLs in a single subprocess call ensures one window opens with all tabs
# "--new-window" ensures a new window is created instead of reusing an existing one
subprocess.Popen([chrome_path, "--new-window"] + urls_to_open)

# --- Step 2: Give Chrome time to load ---
# A short delay allows Chrome to finish launching and become the focused browser
# Gmail and JIRA are particularly heavy — adjust this if you notice issues
time.sleep(6)

# --- Step 3: Locate and control the Chrome window ---
# We're looping through all open windows that include " - Google Chrome" in the title
# Each Chrome tab becomes a separate window title in the format "[Tab Title] - Google Chrome"
for window in gw.getWindowsWithTitle(" - Google Chrome"):
    # We use 'endswith' to avoid matching other apps that might contain this phrase coincidentally
    if window.title.endswith(" - Google Chrome"):
        # Ensure the window is not minimized or hidden
        window.restore()

        # Move the window to the top-left corner of Monitor 2
        # Your Monitor 2 starts at (-1920, 0) relative to Monitor 3 (your main display)
        window.moveTo(-1920, 0)

        # Maximize the window — lets Windows handle the full-screen size
        window.activate()
        window.maximize()

        # Once we've handled the first matching Chrome window, we stop
        break
