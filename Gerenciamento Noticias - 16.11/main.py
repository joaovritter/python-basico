import os
import csv

# Classe Noticia
class Noticia:
    def __init__(self, titulo, categoria, texto, palavras_chave):
        self.titulo = titulo
        self.categoria = categoria
        self.texto = texto
        self.palavras_chave = palavras_chave

# Classe SistemaGestaoNoticias
class SistemaGestaoNoticias:
    def __init__(self):
        self.noticias = []

    def cadastrar_noticia(self, noticia):
        self.noticias.append(noticia)
        self.salvar_noticias_arquivo('noticias.csv')

    def salvar_noticias_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Título', 'Categoria', 'Texto', 'Palavras-chave'])
            for noticia in self.noticias:
                writer.writerow([noticia.titulo, noticia.categoria, noticia.texto, ', '.join(noticia.palavras_chave)])

    def carregar_noticias_arquivo(self, nome_arquivo):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    titulo = row['Título']
                    categoria = row['Categoria']
                    texto = row['Texto']
                    palavras_chave = row['Palavras-chave'].split(', ')
                    noticia = Noticia(titulo, categoria, texto, palavras_chave)
                    self.noticias.append(noticia)

    def pesquisar_noticia(self, termo_pesquisa):
        resultados = []
        for noticia in self.noticias:
            if (termo_pesquisa.lower() in noticia.titulo.lower() or
                termo_pesquisa.lower() in noticia.categoria.lower() or
                termo_pesquisa.lower() in noticia.texto.lower() or
                termo_pesquisa.lower() in ' '.join(noticia.palavras_chave).lower()):
                resultados.append(noticia)
        return resultados


    def alterar_noticia(self, termo_pesquisa, novo_titulo, nova_categoria, novo_texto, novas_palavras_chave):
        noticia_encontrada = None
        for noticia in self.noticias:
            if (termo_pesquisa.lower() in noticia.titulo.lower() or
                termo_pesquisa.lower() in noticia.categoria.lower() or
                termo_pesquisa.lower() in noticia.texto.lower() or
                termo_pesquisa.lower() in ' '.join(noticia.palavras_chave).lower()):
                noticia_encontrada = noticia
                break
        
        if noticia_encontrada:
            noticia_encontrada.titulo = novo_titulo
            noticia_encontrada.categoria = nova_categoria
            noticia_encontrada.texto = novo_texto
            noticia_encontrada.palavras_chave = novas_palavras_chave
            
            # Salvar as notícias alteradas no arquivo CSV imediatamente após a alteração
            self.salvar_noticias_arquivo('noticias.csv')
            
            return True
        else:
            return False

    def remover_noticia(self, termo_pesquisa):
        for noticia in self.noticias:
            if (termo_pesquisa.lower() in noticia.titulo.lower() or
                termo_pesquisa.lower() in noticia.categoria.lower() or
                termo_pesquisa.lower() in noticia.texto.lower() or
                termo_pesquisa.lower() in ' '.join(noticia.palavras_chave).lower()):
                self.noticias.remove(noticia)
                self.salvar_noticias_arquivo('noticias.csv')
                return True
        return False
    # Restante dos métodos do SistemaGestaoNoticias permanecem igual ao exemplo anterior

 
# Adicione a criação do objeto SistemaGestaoNoticias
sistema_noticias = SistemaGestaoNoticias()

# Carregar notícias do arquivo CSV
def carregar_noticias_csv():
    if os.path.exists('noticias.csv'):
        with open('noticias.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                titulo = row['Título']
                categoria = row['Categoria']
                texto = row['Texto']
                palavras_chave = row['Palavras-chave'].split(', ')
                noticia = Noticia(titulo, categoria, texto, palavras_chave)
                sistema_noticias.cadastrar_noticia(noticia)

# Carregar notícias do arquivo CSV ao iniciar o programa
carregar_noticias_csv()

# Restante do código para a conexão base, entrada e saída permanecem igual ao exemplo fornecido

while True:
    os.system('cls')
    print('MENU')
    print('1 - Inscrever noticia')
    print('2 - Pesquisar noticia')
    print('3 - Remover noticia')
    print('4 - Alterar noticia')
    print('5 - Finalizar')
    op = input('Opções: ')

    if op == '1':
        print('Inscrever noticia')
        # Receber dados para cadastrar a notícia
        titulo = input('Título da notícia: ')
        categoria = input('Categoria da notícia: ')
        texto = input('Texto da notícia (máximo 400 letras): ')[:400]
        palavras_chave = input('Palavras-chave da notícia (separadas por vírgula): ').split(',')
        # Verificação se há pelo menos 3 palavras-chave
        if len(palavras_chave) >= 3:
            noticia = Noticia(titulo, categoria, texto, palavras_chave)
            sistema_noticias.cadastrar_noticia(noticia)
            print('Notícia cadastrada com sucesso!')
        else:
            print('Erro: É necessário fornecer pelo menos 3 palavras-chave.')

    elif op == '2':
        print('Pesquisar noticia')
        termo_pesquisa = input('Digite o termo de pesquisa: ')
        resultados_pesquisa = sistema_noticias.pesquisar_noticia(termo_pesquisa)
        if resultados_pesquisa:
            for noticia_encontrada in resultados_pesquisa:
                print(f'Título: {noticia_encontrada.titulo}, Categoria: {noticia_encontrada.categoria}')
        else:
            print('Nenhuma notícia encontrada.')

    elif op == '3':
        print('Remover noticia')
        termo_pesquisa = input('Digite o termo para remover a notícia: ')
        if sistema_noticias.remover_noticia(termo_pesquisa):
            print('Notícia removida com sucesso!')
        else:
            print('Nenhuma notícia encontrada para remover.')

    elif op == '4':
        print('Alterar noticia')
        termo_pesquisa = input('Digite o termo para alterar a notícia: ')
        novo_titulo = input('Novo título da notícia: ')
        nova_categoria = input('Nova categoria da notícia: ')
        novo_texto = input('Novo texto da notícia (máximo 400 letras): ')[:400]
        novas_palavras_chave = input('Novas palavras-chave da notícia (separadas por vírgula): ').split(',')
        if sistema_noticias.alterar_noticia(termo_pesquisa, novo_titulo, nova_categoria, novo_texto, novas_palavras_chave):
            print('Notícia alterada com sucesso!')
        else:
            print('Nenhuma notícia encontrada para alterar.')

    elif op == '5':
        print('Obrigado por usar o sistema')
        # Salvar notícias antes de finalizar o programa
        sistema_noticias.salvar_noticias_arquivo('noticias.csv')
        break

    else:
        print('Opção inválida!')

    os.system('pause')