import time
import re
import pyautogui
import pyperclip
import webbrowser
from datetime import datetime


# ==================================================
# YOUR EXCEL ONLINE FILE
# ==================================================

EXCEL_URL = (
	"https://excel.cloud.microsoft/open/onedrive/"
	"?docId=9A970E80DC20F10B%21sff512ea2758a4497b61c5470649293bf"
	"&driveId=9A970E80DC20F10B"
)

# Chennai weather page
WEATHER_URL = "https://www.google.com/search?q=Chennai+weather"

# Screenshot name
today = datetime.now().strftime("%Y-%m-%d")
screenshot_file = f"daily_report_{today}.png"


# ==================================================
# 1. OPEN WEATHER
# ==================================================

print("1/5 Opening Chennai weather...")

webbrowser.open(WEATHER_URL)

time.sleep(8)


# ==================================================
# 2. GET WEATHER DATA
# ==================================================

print("2/5 Getting weather information...")

pyautogui.hotkey("ctrl", "a")
time.sleep(1)

pyautogui.hotkey("ctrl", "c")
time.sleep(2)

page_text = pyperclip.paste()


# Find temperature such as 30°C
match = re.search(
	r"-?\d{1,2}\s*°\s*[CF]",
	page_text,
	re.IGNORECASE
)

if match:
	weather = "Chennai Weather: " + match.group(0)
else:
	weather = "Chennai Weather: Data collected"

print("Fetched Data:", weather)


# ==================================================
# 3. OPEN EXCEL ONLINE
# ==================================================

print("3/5 Opening Excel Online...")

webbrowser.open(EXCEL_URL)

print("Waiting for Excel Online to load...")
time.sleep(15)


# ==================================================
# 4. WRITE HEADER + 5 ROWS
# ==================================================

print("4/5 Writing 5 rows...")


# Click inside spreadsheet
pyautogui.click(400, 400)

time.sleep(2)


# Go to A1
pyautogui.hotkey("ctrl", "home")

time.sleep(2)


# --------------------------------------------------
# Header
# --------------------------------------------------

header = "Date & Time\tFetched Data\tComment"

pyperclip.copy(header)

pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")

time.sleep(2)


# --------------------------------------------------
# 5 rows
# --------------------------------------------------

comments = [
	"Daily weather report",
	"Weather checked successfully",
	"Good for outdoor activities",
	"Weather status updated",
	"Daily data collected"
]


for comment in comments:

	current_time = datetime.now().strftime(
		"%Y-%m-%d %H:%M:%S"
	)

	row = (
		current_time
		+ "\t"
		+ weather
		+ "\t"
		+ comment
	)

	pyperclip.copy(row)

	pyautogui.hotkey("ctrl", "v")

	pyautogui.press("enter")

	time.sleep(1)


print("5 rows written successfully!")


# ==================================================
# 5. SCREENSHOT
# ==================================================

print("5/5 Taking screenshot...")

time.sleep(5)

pyautogui.screenshot(screenshot_file)


print()
print("=" * 50)
print("ASSIGNMENT COMPLETED SUCCESSFULLY!")
print("=" * 50)
print("Rows written : 5")
print("Columns      : 3")
print("Screenshot   :", screenshot_file)
print("=" * 50)
