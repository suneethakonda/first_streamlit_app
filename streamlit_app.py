
import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner') 

streamlit.header('BF Menu')
streamlit.title('oats')
streamlit.title('Smoothie')
streamlit.title('Egg')
streamlit.header('Build your own smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
