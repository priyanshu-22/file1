import streamlit as st
st.title ("Find the largest among the 3 numbers")
num1 = st.number_input("Enter number 1")
num2 = st.number_input("Enter number 2")
num3 = st.number_input("Enter number 3")
calculate = st.button("Find largest number")

def largest number (a, b, c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b 
  else:
    return c
if calculate:
   largest_Num=largest_number(num1,num2,num3)
   st.write('the largest no. is",largest_num)
