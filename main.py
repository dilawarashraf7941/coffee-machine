import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Create a Streamlit app
st.set_page_config(page_title="Coffee Machine for Izza Muhterma", page_icon=":coffee:", layout="wide")

# Add a title and an icon to the app
st.title(":coffee: Coffee Machine for Izza Muhterma")

# Create a sidebar
st.sidebar.header("Select Your Coffee")

# Add a dropdown menu to select a coffee type
coffee_type = st.sidebar.selectbox('Select a coffee type', ['Espresso', 'Cappuccino', 'Latte', 'Mocha'])

# Add a slider to select the coffee strength
coffee_strength = st.sidebar.slider('Select the coffee strength', 1, 10, 5)

# Add a checkbox to select if you want whipped cream
whipped_cream = st.sidebar.checkbox('Add whipped cream')

# Create a dataframe to store the coffee data
data = {
    'Coffee Type': [coffee_type],
    'Coffee Strength': [coffee_strength],
    'Whipped Cream': [whipped_cream]
}

df = pd.DataFrame(data)

# Create an interactive bar chart using Plotly
fig = go.Figure(data=[go.Bar(x=df['Coffee Type'], y=df['Coffee Strength'], text=df['Coffee Strength'], textposition='auto')])
fig.update_layout(title_text='Coffee Machine for Izza Muhterma', xaxis_title='Coffee Type', yaxis_title='Coffee Strength')

# Add a hovertemplate to display the coffee type and strength
fig.update_traces(hovertemplate='Coffee Type: %{x}<br>Coffee Strength: %{y}<extra></extra>')
fig.update_layout(hovermode='x unified')

# Display the chart
st.plotly_chart(fig, use_container_width=True)

# Add a button to brew the coffee
if st.button('Brew Coffee'):
    st.write('Brewing your coffee...')
    st.write('Your coffee is ready!')