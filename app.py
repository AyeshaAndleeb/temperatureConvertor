import streamlit as st

# Set Page Configuration
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="wide",
)

# Sidebar
st.sidebar.title("Temperature Conversion App")
st.sidebar.markdown("Easily convert temperatures between Celsius, Fahrenheit, and Kelvin.")

# Main Layout
st.title("🌡️ Temperature Converter")
st.markdown("### Convert temperatures between **Celsius**, **Fahrenheit**, and **Kelvin**.")

# Input Section
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        temp_input = st.number_input(
            "Enter the temperature to convert:", 
            format="%.2f", 
            help="Input the temperature value to convert."
        )

    with col2:
        conversion_type = st.radio(
            "Select conversion type:",
            (
                "Celsius to Fahrenheit",
                "Fahrenheit to Celsius",
                "Celsius to Kelvin",
                "Kelvin to Celsius",
                "Fahrenheit to Kelvin",
                "Kelvin to Fahrenheit",
            ),
            help="Choose the conversion type.",
        )

# Conversion Logic
with st.container():
    st.markdown("### Result")
    if conversion_type == "Celsius to Fahrenheit":
        converted_temp = (temp_input * 9/5) + 32
        st.success(f"{temp_input:.2f}°C is equal to {converted_temp:.2f}°F.")
    elif conversion_type == "Fahrenheit to Celsius":
        converted_temp = (temp_input - 32) * 5/9
        st.success(f"{temp_input:.2f}°F is equal to {converted_temp:.2f}°C.")
    elif conversion_type == "Celsius to Kelvin":
        converted_temp = temp_input + 273.15
        st.success(f"{temp_input:.2f}°C is equal to {converted_temp:.2f} K.")
    elif conversion_type == "Kelvin to Celsius":
        converted_temp = temp_input - 273.15
        st.success(f"{temp_input:.2f} K is equal to {converted_temp:.2f}°C.")
    elif conversion_type == "Fahrenheit to Kelvin":
        converted_temp = (temp_input - 32) * 5/9 + 273.15
        st.success(f"{temp_input:.2f}°F is equal to {converted_temp:.2f} K.")
    elif conversion_type == "Kelvin to Fahrenheit":
        converted_temp = (temp_input - 273.15) * 9/5 + 32
        st.success(f"{temp_input:.2f} K is equal to {converted_temp:.2f}°F.")

# Footer Section
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit. Explore more on [Hugging Face Spaces](https://huggingface.co/spaces).")
