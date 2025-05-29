import streamlit as st

def main():
    # Set the app title 
    st.title('My first Streamlit app') 
    # Add a header
    st.header('This is a header')
    # Add a markdown
    st.markdown('Esto es texto **markdown in bold**')
    # Add a welcome message 
    st.write('Welcome to my Streamlit app!') 
    # Create a text input 
    widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
    # Display the customized message 
    st.write('My Custom Message:', widgetuser_input)
    # st.subheader('Mensaje personalizado:', widgetuser_input)
    # Add a slider
    slider_value = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))

if __name__ == '__main__':
    main()
