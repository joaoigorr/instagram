import pandas as pd
import streamlit as  st
#import plotly.express as px
from datetime import datetime, timedelta
from data_pages import new_data

#Titulo
df = pd.read_excel('date_pages.xlsx')
st.header('Rivalidade no Cenário de Páginas de CS.')
hour_att = df['date'].max()
hora_atual = datetime.today()
next_att = hour_att + pd.Timedelta(hours=1)

if next_att < hora_atual:
    new_data()
else:
    pass

st.text(f'Atualizado em: {hour_att}')

#Grafico de barras
df_atual = df.sort_values(by='date', ascending=False).tail(6)
st.bar_chart(df_atual.sort_values('followers'), x='username', y='followers')

#fig_total.update_traces(textfont_size=12, textangle=0, cliponaxis=False)

#st.plotly_chart(fig_total)

#Grafico de linha
st.subheader('Evolução no tempo.')
df_line = df[['date','followers','username']]
st.line_chart(df_line, x='date', y='followers', color='username')


