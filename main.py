#Importa a função responsável por criar a aplicação com o banco
from sqlalchemy import create_engine

#Importa tipos de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

#Importar a classe Base usada para criar os modelos de orm
from sqlalchemy.orm import declarative_base

#Importar a ferramenta para criar sessões de banco de dados
from sqlalchemy.orm import sessionmaker

#Criar classe Base do ORM
Base = declarative_base()

#Classes = Tabelas
#Objeto = Linha Tabela
#Atributos = Colunas

#Classe Produto representando uma tabela no banco de dados
class Produto(Base):
    #Nome da Tabela no banco de dados
    __tablename__ = "produtos"

    #Colunas id
    #Integer > número inteiro
    #Primary_key = True
    id = Column(Integer, primary_key=True)

    #Nome do produto
    #String > texto
    nome = Column(String(100))

    #Preço do produto
    #Float > número decimal
    preco = Column(Float)

    #Quantidade em estoque
    estoque = Column(Integer)

    #Produto ativo ou não
    ativo = Column(Boolean)

    #Método construtor
    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo

    #Representação do objeto para imprimir
    def __repr__(self):
        return f"Produto(id={self.id}, nome='{self.nome}', preco={self.preco}, estoque={self.estoque}, ativo={self.ativo})"
    
#Criar conexão com o banco de dados SQLite
engine = create_engine("sqlite:///estoque.db", echo=False)

#Criar as tabelas no banco de dados, se ainda não existirem
Base.metadata.create_all(engine)

#Criar um fábrica de sessões, conectadas ao banco
Session = sessionmaker(bind=engine)

#Sessão atiiva - pense nela como carrinho de compras
session = Session()  


#Criar

#Criar objetos de produtos 
produto1 = Produto("Notebook", 5500, 6, True)
produto2 = Produto("Teclado", 500, 100, True)
produto3 = Produto("Mouse", 150, 55, True)

# #Adicionar os produtos na sessão (carrinho)
# session.add(produto1)
# session.add(produto2)
# session.add(produto3)

# #Confirmar a inserção no banco
# #Salvar no banco de dados
# session.commit()

#Listar
#Buscar todos os produtos do banco
produtos = session.query(Produto).all()

print(produtos)

for p in produtos:
    print( f"Produto(id={p.id}, nome='{p.nome}', preco={p.preco}, estoque={p.estoque}, ativo={p.ativo})")


# #UPDATE (Atualizar)

# #Buscar o produto com o id = 1
# produto_id = session.query(Produto).filter(Produto.id == 1).first()
# print(produto_id)

# #Produtos maior que 10
# num_estoque = session.query(Produto).filter(Produto.estoque > 10).all()
# for produto in num_estoque:
#  print(produto.estoque)

# produto_id2 = session.query(Produto). filter_by(id = 1).first()
# #print(produto_id2)

# #Podemos usar order by
# produtos_organizados = session.query(Produto).order_by(Produto.estoque).all()
# #for produto in produtos_organizados:
#    #print(f"Nome:{produto.nome}, Qtd_estoque: {produto.estoque}")

# #Podemos limitar a quantidade de resultado - top 5 mais caros
# produtos_mais_caros = session.query(Produto).order_by(Produto.preco.desc()).limit(3).all()
# for produto in produtos_mais_caros:
#    print(f"Nome:{produto.nome}, Valor: {produto.preco}")


#UPDATE - Atualizar
#Busquei o produo para atualizar
notebook = session.query(Produto).filter_by(id=1).first
notebook.preco =  6000

#Confirmar essa alteração
session.commit()

print("Preço atualizado com sucesso")

for p in produtos:
   print(  f"Produto(id={p.id}, nome='{p.nome}', preco={p.preco}, estoque={p.estoque}, ativo={p.ativo})")
