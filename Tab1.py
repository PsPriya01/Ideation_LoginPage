import streamlit as st

# Get the user input
amount = st.number_input('Enter an amount')

# Calculate the percentages
savings = amount * 0.10
growth = amount * 0.20
expenditure = amount * 0.70

# Display the calculated values
st.write('Savings: ', savings)
st.write('Growth: ', growth)
st.write('Expenditure: ', expenditure)
