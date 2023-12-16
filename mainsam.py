import streamlit as st
import pandas as pd

# Import the login page buttons and Tab1 Python files
import login_page
import button 
import Tab1
import Savings

# Define a main() function
def main():
  # Call the functions from the login page buttons and Tab1 Python files
  login_page.login_page()
  button.button()
  Tab1.Tab1()
  Savings.Savings()

# Execute the main() function
if __name__ == '__main__':
  main()
