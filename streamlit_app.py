import streamlit as sl
import pandas 

sl.header('Breakfast Favorites')
sl.text('🥣 Omega 3 & Blueberry Oatmeal')
sl.text('🥗 Kale, Spinach & Rocket Smoothie')
sl.text('🐔 Hard-Boiled Free-Range Egg')
sl.text('🥑🍞 Avocado Toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt").set_index('Fruit')

# To select the desired fruits in the smoothie
sl.multiselect("Pick some fruits", list(my_fruit_list.index), ['Strawberry', 'Banana'])

# Displays table with fruit list
sl.dataframe(my_fruit_list)
