import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_csv('vehicles_us.csv')
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df.dropna(subset=['price'])  
df['price'] = df['price'].astype(int)  
st.header('Market of Used Vehicles in the US')
st.write('Filter the data by selecting the columns you want to see.')
model_choice=df['model'].unique()
make_choice_man=st.selectbox('Select Model:',model_choice)
min_year,max_year=int(df['model_year'].min()),int(df['model_year'].max())
year_range=st.slider("Choose Years",
                     value=(min_year,max_year),min_value=min_year,max_value=max_year)
filtered_df=df[(df.model==make_choice_man) & (df.model_year>=year_range[0])&(df.model_year<=year_range[1])]
st.table(filtered_df)
st.header('Price Analysis')
st.write('We will analyze how the distribution of price varies dependind on transmission,engine type or body type')
list_for_hist=['transmission','fuel','body_type']
choice_for_hist=st.selectbox('Split for Price Distribution',list_for_hist)
fig1=px.histogram(df,x='price',color=choice_for_hist)
fig1.update_layout(title="<b> Split of Price by {} </b>".format(choice_for_hist))
st.plotly_chart(fig1)
fig1.show()
df['age']=2019-df['model_year']
def age_category(x):
    if x<5:
        return '<5'
    if x>=5 and x<=10:
        return '5-10'
    if x>10 and x<20:
        return '10-20'
    else:
        return '>20'

df['age_category']=df['age'].apply(age_category)
st.write('How price is affected by odometer and engine capacity')
list_for_scatter=['odometer','cylinders','condition']
choice_for_scatter=st.selectbox('Price Dependency on',list_for_scatter)
fig2=px.scatter(df,x='price',y=choice_for_scatter,)
fig2.update_layout(title="<b>  Price vs {} </b>".format(choice_for_scatter))
st.plotly_chart(fig2)
