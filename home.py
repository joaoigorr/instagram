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
follow_min = int(df['followers'].min())
follow_max = int(df['followers'].max())
df_nt = df[df['username'] == 'cs2nicetry']
follow_nt = int(df_nt['followers'].max())
col1, col2, col3 = st.columns(3)
with col1:    
    st.metric(label='Seguidores', value=follow_nt)
with col2:
    st.metric(label='Distancia para 50k', value=follow_nt-50000)
with col3:
    st.metric(label='Distancia para Fallendadepre', value=follow_nt - follow_max)
#Grafico de barras
df_atual = df.sort_values(by='date')
df_atual = df_atual.tail(6)

# #Imagens
# df_atual['link_image'] = df_atual['url_photo'].apply(lambda x: x + '.png')
# df_editor = df_atual[['followers',
#                       'username',
#                       'link_image']].sort_values(by='followers',ascending=False)



# st.data_editor(
#     df_editor,
#     column_config= {
#         "followers": st.column_config.ProgressColumn(
#             "Followers",
#             format="%f",
#             min_value = follow_min,
#             max_value = follow_max
#             )
#     ,
#      "link_image": st.column_config.ImageColumn(
#             'Logo', help='test2'
#     )
# },
#     hide_index=True,
# )


# #st.bar_chart(df_atual.sort_values('followers'), x='username', y='followers')

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
st.line_chart(df_line, x='date', y='followers', color='username')
