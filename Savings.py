import streamlit as st
import webbrowser

# Create four buttons
button1 = st.button('Savings 1')
button2 = st.button('Savings 2')
button3 = st.button('Savings 3')
button4 = st.button('Savings 4')

# Check which button was pressed and open a specific URL
if button1:
    webbrowser.open_new_tab('https://cleartax.in/s/elss')
elif button2:
    webbrowser.open_new_tab('https://cleartax.in/s/nsc-national-savings-certificate')
elif button3:
    webbrowser.open_new_tab('https://cleartax.in/s/kisan-vikas-patra')
elif button4:
    webbrowser.open_new_tab('https://cleartax.in/s/atal-pension-yojna')
