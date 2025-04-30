import pandas as pd
import plotly.express as px
import streamlit as st

final_df = pd.read_csv('india.csv')
list_of_state = list(final_df['State'].unique())
list_of_state.insert(0,'overall india')

st.set_page_config(layout='wide')
st.title('INDIA CENSUS ANALYSIS')

st.sidebar.title('India data visulaization')
selected_state = st.sidebar.selectbox('Select state',list_of_state)

primary = st.sidebar.selectbox('select Primary parameter ',sorted(final_df.columns[5:]))
secondary = st.sidebar.selectbox('select secondary parameter ',sorted(final_df.columns[5:]))

plot = st.sidebar.button('Plot')


if plot:
    st.text(f'size represent {primary}')
    st.text(f'color represent {secondary}')
    if selected_state == 'overall india':
        fig = px.scatter_map(final_df, lat="Latitude", lon="Longitude", color=secondary, size=primary,
                             color_continuous_scale=px.colors.cyclical.IceFire, zoom=3.5,width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

    else:
        state_df = final_df[final_df['State'] == selected_state]
        fig = px.scatter_map(state_df, lat="Latitude", lon="Longitude", color=secondary, size=primary,
                             color_continuous_scale=px.colors.cyclical.IceFire, zoom=5.5, width=1200, height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)