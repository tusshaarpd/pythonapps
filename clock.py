import subprocess
import sys

# Install necessary libraries dynamically
required_libraries = ["pytz", "plotly"]
for lib in required_libraries:
    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Import libraries after installation
import streamlit as st
import pytz
from datetime import datetime
import plotly.graph_objects as go
import math

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

# Function to create an analog clock using Plotly
def create_analog_clock(time, timezone_label):
    # Get current hour, minute, and second
    hours = time.hour % 12
    minutes = time.minute
    seconds = time.second

    # Calculate angles for clock hands
    hour_angle = (hours * 30) + (minutes * 0.5) - 90  # 30 degrees per hour
    minute_angle = (minutes * 6) - 90  # 6 degrees per minute
    second_angle = (seconds * 6) - 90  # 6 degrees per second

    # Base circle for the clock
    fig = go.Figure()

    # Add clock face
    fig.add_trace(go.Scatterpolar(
        r=[1] * 12,
        theta=[i * 30 for i in range(12)],
        mode='markers+text',
        marker=dict(size=10),
        text=[str(i if i != 0 else 12) for i in range(12)],
        textposition="top center",
        hoverinfo="none"
    ))

    # Add hour hand
    fig.add_trace(go.Scatterpolar(
        r=[0, 0.5],
        theta=[0, hour_angle],
        mode='lines',
        line=dict(color='black', width=6),
        hoverinfo="none"
    ))

    # Add minute hand
    fig.add_trace(go.Scatterpolar(
        r=[0, 0.7],
        theta=[0, minute_angle],
        mode='lines',
        line=dict(color='blue', width=4),
        hoverinfo="none"
    ))

    # Add second hand
    fig.add_trace(go.Scatterpolar(
        r=[0, 0.9],
        theta=[0, second_angle],
        mode='lines',
        line=dict(color='red', width=2),
        hoverinfo="none"
    ))

    # Layout adjustments
    fig.update_layout(
        polar=dict(
            angularaxis=dict(showline=False, tickmode='array', ticks='', showgrid=False),
            radialaxis=dict(visible=False)
        ),
        showlegend=False,
        margin=dict(l=20, r=20, t=30, b=20),
        title=dict(text=f"Time in {timezone_label}<br>{time.strftime('%Y-%m-%d %H:%M:%S')}", x=0.5),
    )

    return fig

# Streamlit app
st.title("World Time Analog Clocks")

st.write("### Analog clocks for different time zones across continents")

# Loop through time zones and display clocks
for label, tz_name in time_zones.items():
    current_time = datetime.now(pytz.timezone(tz_name))
    fig = create_analog_clock(current_time, label)
    st.plotly_chart(fig)
