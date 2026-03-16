import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles.csv')

st.header('Análise de Anúncios de Veículos nos EUA')

st.write(f'Dataset com **{df.shape[0]}** veículos e **{df.shape[1]}** colunas.')

if st.checkbox('Mostrar histograma de preços'):
    st.subheader('Distribuição de Preços')
    fig = px.histogram(df, x='price', nbins=50,
                       title='Distribuição de Preços dos Veículos',
                       labels={'price': 'Preço (USD)'})
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Mostrar gráfico de dispersão: Odômetro vs Preço'):
    st.subheader('Odômetro vs Preço')
    fig = px.scatter(df, x='odometer', y='price', color='condition',
                     title='Odômetro vs Preço por Condição do Veículo',
                     labels={'odometer': 'Odômetro (milhas)', 'price': 'Preço (USD)', 'condition': 'Condição'})
    st.plotly_chart(fig, use_container_width=True)
