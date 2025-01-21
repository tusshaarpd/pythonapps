import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Background Color Changer",
    page_icon="🎨",
    layout="centered"
)

# Title of the app
st.title("Background Color Changer")

# Sidebar for color selection
st.sidebar.header("Select a Background Color")
color = st.sidebar.color_picker("Pick a Color", "#ffffff")

# Apply the selected background color
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Display the selected color
st.write(f"The selected background color is: {color}")

# Footer
st.markdown(
    """
    <div style='text-align: center;'>
        <small>Built with ❤️ using Streamlit</small>
    </div>
    """,
    unsafe_allow_html=True
)
