#Importa a função responsável por criar a aplicação com o banco
from sqlalchemy import create_engine

#Importa tipos de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

#Importar a classe Base usada para criar os modelos de orm
from sqlalchemy.orm import declarative_base

#Importar a ferramenta para criar sessões de banco de dados
from sqlalchemy.orm import sessionmaker