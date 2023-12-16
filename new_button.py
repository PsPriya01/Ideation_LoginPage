import streamlit as st
import webbrowser

# Create three buttons
button1 = st.button('Category 1')
button2 = st.button('Category 2')
button3 = st.button('Category 3')

# Check which category button was pressed and open specific URLs based on sub-buttons
if button1:
    sub_button1 = st.button('Button 1.1')
    sub_button2 = st.button('Button 1.2')
    sub_button3 = st.button('Button 1.3')
    sub_button4 = st.button('Button 1.4')
    sub_button5 = st.button('Button 1.5')

    if sub_button1:
        webbrowser.open_new_tab('https://www.theinvestorspodcast.com/podcasts/20-best-business-podcasts/#section1')
    elif sub_button2:
        webbrowser.open_new_tab('https://www.theinvestorspodcast.com/podcasts/20-best-business-podcasts/#section3')
    elif sub_button3:
        webbrowser.open_new_tab('https://www.theinvestorspodcast.com/podcasts/20-best-business-podcasts/#section5')
    elif sub_button4:
        webbrowser.open_new_tab('https://www.theinvestorspodcast.com/podcasts/20-best-business-podcasts/#section7')
    elif sub_button5:
        webbrowser.open_new_tab('https://www.theinvestorspodcast.com/podcasts/20-best-business-podcasts/#section9')

if button2:
    sub_button1 = st.button('Button 2.1')
    sub_button2 = st.button('Button 2.2')
    sub_button3 = st.button('Button 2.3')

    if sub_button1:
        webbrowser.open_new_tab('https://www.entrepreneur.com/living/50-signs-you-might-be-an-entrepreneur/232451')
    elif sub_button2:
        webbrowser.open_new_tab('https://archive.nytimes.com/www.nytimes.com/interactive/business/ieconomy.html')
    elif sub_button3:
        webbrowser.open_new_tab('https://hbr.org/2016/03/dont-take-it-personally-is-terrible-work-advice')


if button3:
    sub_button1 = st.button('Button 3.1')
    sub_button2 = st.button('Button 3.2')
    sub_button3 = st.button('Button 3.3')

    if sub_button1:
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=5uaXq-xDp2g')
    elif sub_button2:
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=U7Ualuw1fqo')
    elif sub_button3:
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=l2mI-aqz4vo')

