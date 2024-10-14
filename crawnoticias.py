# -*- coding: utf-8 -*-
"""crawnoticias.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z3LFjr8I26F-lcwtapINNe2xv5gDWTnd
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas_gbq

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
  # Título
  titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

  # print(titulo.text)
  # print(titulo['href']) # link da notícia

  # Subtítulo: div class="feed-post-body-resumo"
  subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

  if (subtitulo):
    # print(subtitulo.text)
    lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
  else:
    lista_noticias.append([titulo.text, '', titulo['href']])


news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

#Para gerar arquivo em excel descomentar abaixo
#news.to_excel('noticias.xlsx', index=False)

print(news)

#Para load em bigquery descomentar abaixo
#pandas_gbq.to_gbq(news, carga-noticias, project_id=igorgondim_9083408)