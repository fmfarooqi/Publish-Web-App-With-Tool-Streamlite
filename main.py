import streamlit as st
import pandas

data = {
  'series_1':[1, 4, 13, 24, 45],
  'series_2':[10, 30, 40, 100, 250]
}


df = pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit in Automate Every Thing With python')
st.write('''This is our first web app.
Learn it and enjoy it!
''')
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('celsius')
st.write(myslider, 'in fahrenheit is', myslider * 9/5 + 32)