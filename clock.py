import tkinter as tk
import pytz
from datetime import datetime
import math
from threading import Thread
import time

# List of time zones with their labels
time_zones = {
    "Asia": "Asia/Tokyo",
    "Europe": "Europe/London",
    "Africa": "Africa/Johannesburg",
    "North America": "America/New_York",
    "South America": "America/Sao_Paulo",
    "Australia": "Australia/Sydney",
    "Antarctica": "Antarctica/Palmer"
}

# Clock dimensions
CLOCK_RADIUS = 50
WINDOW_WIDTH = 300
WINDOW_HEIGHT = len(time_zones) * 150

# Function to create and update analog clock
def draw_clock(canvas, x, y, timezone):
    def update_clock():
        while True:
            # Get current time
            current_time = datetime.now(pytz.timezone(timezone))
            hours, minutes, seconds = current_time.hour % 12, current_time.minute, current_time.second

            # Calculate angles for clock hands
            sec_angle = math.radians(seconds * 6 - 90)
            min_angle = math.radians(minutes * 6 - 90)
            hour_angle = math.radians((hours * 30) + (minutes * 0.5) - 90)

            # Draw clock face
            canvas.delete("clock_" + timezone)
            canvas.create_oval(x - CLOCK_RADIUS, y - CLOCK_RADIUS, x + CLOCK_RADIUS, y + CLOCK_RADIUS, fill="white", outline="black", tags="clock_" + timezone)

            # Draw hour hand
            canvas.create_line(
                x, y, x + CLOCK_RADIUS * 0.5 * math.cos(hour_angle), y + CLOCK_RADIUS * 0.5 * math.sin(hour_angle),
                width=4, fill="black", tags="clock_" + timezone
            )

            # Draw minute hand
            canvas.create_line(
                x, y, x + CLOCK_RADIUS * 0.7 * math.cos(min_angle), y + CLOCK_RADIUS * 0.7 * math.sin(min_angle),
                width=3, fill="blue", tags="clock_" + timezone
            )

            # Draw second hand
            canvas.create_line(
                x, y, x + CLOCK_RADIUS * 0.9 * math.cos(sec_angle), y + CLOCK_RADIUS * 0.9 * math.sin(sec_angle),
                width=2, fill="red", tags="clock_" + timezone
            )

            # Show time below the clock
            canvas.create_text(x, y + CLOCK_RADIUS + 20, text=current_time.strftime("%Y-%m-%d %H:%M:%S"), tags="clock_" + timezone)
            canvas.create_text(x, y + CLOCK_RADIUS + 40, text=timezone, tags="clock_" + timezone)

            # Pause for smooth updates
            time.sleep(1)

    # Run the clock update in a thread
    Thread(target=update_clock, daemon=True).start()


# Main application window
def create_app():
    root = tk.Tk()
    root.title("World Time Analog Clocks")
    canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="lightgray")
    canvas.pack()

    # Draw clocks for each time zone
    y_offset = 80
    for idx, (label, tz) in enumerate(time_zones.items()):
        x, y = WINDOW_WIDTH // 2, y_offset + idx * 150
        draw_clock(canvas, x, y, tz)

    root.mainloop()


# Run the application
create_app()
