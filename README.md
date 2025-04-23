# Start Me Up

Start Me Up is a Python-based automation tool that:

- Launches Google Chrome
- Opens multiple user-defined tabs (Gmail, JIRA, GitHub, etc.)
- Moves the window to a specific monitor
- Maximizes the window for immediate productivity

It’s built for users with multi-monitor setups who want a fast, repeatable workspace launcher — especially useful at the beginning of the workday.

Features:

- Launches Chrome with multiple tabs in one window
- Moves the window to a specific monitor using screen coordinates
- Maximizes the window for a clean layout
- Frozen .exe version available — no Python needed
- Fully versioned with Git and ready for extension

Requirements:

If running from source:
pip install -r requirements.txt

This project uses:
- pyautogui
- pygetwindow
- pyinstaller (for freezing)
- subprocess (built-in)
- time (built-in)

Usage:

Run from Python:
python start_me_up.py
(Make sure your venv is active.)

Run as a standalone app:
dist/start_me_up.exe
Just double-click — no Python required.

Freezing into an .exe:

If you'd like to freeze it again later:
pyinstaller --onefile --windowed start_me_up.py
Your .exe will appear in the dist/ folder.

Version:
Current: v1.2

License:
MIT, because freedom.

Credits:
Built by https://github.com/tigloki, with help from coffee and a talking machine.
(Created by the author with collaborative input from ChatGPT.)
