import math
from datetime import datetime
import tkinter as tk
import time

WIDTH = 400
HEIGHT = 400
MARGIN = 10
CLOCK_RADIUS = (WIDTH - MARGIN * 2) // 2

root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#F5F5F5", highlightthickness=0)
canvas.pack()

# Draw the clock face
canvas.create_oval(MARGIN, MARGIN, WIDTH - MARGIN, HEIGHT - MARGIN, width=4, outline="#333")

# Draw the hour markers
for i in range(12):
    angle = math.pi / 6 * (i+1) - math.pi / 2
    x1 = CLOCK_RADIUS * math.cos(angle) + WIDTH // 2
    y1 = CLOCK_RADIUS * math.sin(angle) + HEIGHT // 2
    x2 = (CLOCK_RADIUS - 40) * math.cos(angle) + WIDTH // 2
    y2 = (CLOCK_RADIUS - 40) * math.sin(angle) + HEIGHT // 2
    canvas.create_text(x2, y2, text=str(i+1), font=('Arial', 12, 'bold'))

# Draw the hands
hour_hand = canvas.create_line(0, 0, 0, 0, width=6, fill="#333")
minute_hand = canvas.create_line(0, 0, 0, 0, width=8, fill="#333")
second_hand = canvas.create_line(0, 0, 0, 0, width=2, fill="red")

while True:
    # Get the current time
    now = datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    # Calculate the angles of the hands
    hour_angle = math.pi / 6 * hour + math.pi / 360 * minute - math.pi / 2
    minute_angle = math.pi / 30 * minute - math.pi / 2
    second_angle = math.pi / 30 * second - math.pi / 2

    # Set the coordinates of the hands
    hour_x = (CLOCK_RADIUS - 80) * math.cos(hour_angle) + WIDTH // 2
    hour_y = (CLOCK_RADIUS - 80) * math.sin(hour_angle) + HEIGHT // 2
    minute_x = CLOCK_RADIUS * math.cos(minute_angle) + WIDTH // 2
    minute_y = CLOCK_RADIUS * math.sin(minute_angle) + HEIGHT // 2
    second_x = CLOCK_RADIUS * math.cos(second_angle) + WIDTH // 2
    second_y = CLOCK_RADIUS * math.sin(second_angle) + HEIGHT // 2

    # Update the hands on the canvas
    canvas.coords(hour_hand, WIDTH // 2, HEIGHT // 2, hour_x, hour_y)
    canvas.coords(minute_hand, WIDTH // 2, HEIGHT // 2, minute_x, minute_y)
    canvas.coords(second_hand, WIDTH // 2, HEIGHT // 2, second_x, second_y)

    # Update the window
    root.update()

    # Wait for 1 second
    time.sleep(1)