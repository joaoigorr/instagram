#%%
import pandas as pd
import streamlit as  st
from datetime import datetime
from data_pages import new_data_v2, new_data
import plotly.express as px
import requests

#Titulo
df = pd.read_excel('date_pages.xlsx')
st.header('Análise NiceTry e seus concorrentes.')
hour_att = df['date'].max()
hora_atual = datetime.today()
next_att = hour_att + pd.Timedelta(hours=6)


if next_att < hora_atual:
    new_data_v2()
else:
    pass

hour_att_new = hour_att.strftime("%d/%m/%Y, %H:%M")
st.text(f'Atualizado em: {hour_att_new}')

#Métricas
#Nicetry
df_nt = df[df['username'] == 'cs2nicetry'].sort_values(by='date')
df_nt = df_nt.tail(2)
follow_nt = int(df_nt['followers'].max())
follow_nt_last = int(df_nt['followers'].min())
#Fallen da depre
df_fd = df[df['username'] == 'fallendadepre'].sort_values(by='date')
df_fd = df_fd.tail(2)
follow_fd = int(df_fd['followers'].max())
follow_fd_last = int(df_fd['followers'].min())
delta_fd = (follow_fd - follow_nt ) - (follow_fd_last - follow_nt_last)
#Draft5gg
df_dt = df[df['username'] == 'draft5gg'].sort_values(by='date')
df_dt = df_dt.tail(2)
follow_dt = int(df_dt['followers'].max())
follow_dt_last = int(df_dt['followers'].min())
delta_dt = (follow_dt - follow_nt ) - (follow_dt_last - follow_nt_last)

df_tc = df[df['username'] == 'draft5gg']
follow_dt = int(df_tc['followers'].max())

col1, col2, col3, col4 = st.columns(4)
with col1:    
    st.metric(label='Seguidores', value=follow_nt, delta= follow_nt - follow_nt_last)
with col2:
    st.metric(label='Distancia para Fallendadepre', value= follow_fd - follow_nt , delta = delta_fd, delta_color='inverse')
with col3:
    st.metric(label='Distancia para Dratf5', value= follow_dt - follow_nt, delta = delta_dt, delta_color='inverse')
with col4:
    st.metric(label='Distancia para 50k', value=50000-follow_nt)
#Grafico de barras
df_atual = df.sort_values(by='date')
df_atual = df_atual.tail(6)

fig_total = px.bar(df_atual.sort_values("followers"), x='followers',y='username', 
                       title='Total seguidoress',
                        orientation='h',text_auto=True
                          )
fig_total.update_traces(textfont_size=12, textangle=0, cliponaxis=False)

st.plotly_chart(fig_total)

#Grafico de linha
st.subheader('Evolução no tempo.')
df_line = df[['date','followers','username']]
df_line = df_line.sort_values(by='date',ascending=False)
fig_line = px.line(df_line, x='date', y='followers', color='username',markers=True)
st.plotly_chart(fig_line)
