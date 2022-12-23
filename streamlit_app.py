
import streamlit
#import pandas
#import requests
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("fruit load list:")
streamlit.dataframe(my_data_rows)
fruit_choice = streamlit.text_input('What fruit would you like to add?','JackFruit')
streamlit.write('Thanks for adding ', fruit_choice)
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values ('jackfruit', 'papaya', 'guava','kiwi')")
       return "Thanks for adding " + new_fruit
 
