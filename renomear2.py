import os

# para cria uma função em python iremos utilizar o comando def(definição)
def mudarNome(ar_or,nv_ar):
    """ 
    A função mudar nome,altera o nome de um arquivo.
    O usario deseja trocar ,do antigo para o novo
    Args:
        ar_or(srt):o nome original do arquivo 
        nv_or(srt):o nome do novo arquivo 
    Returns:
        Retorna uma mensagem de confirmação    
    """
    os.rename(ar_or,nv_ar)
    msg = "O nome do arquivo foi alterado "
    return msg


arquivo_original = input("Digite o nome do arquivo que sera renomeado:")
novo_arquivo = input("Digite o novo nome do arquivo ")



rs = mudarNome(arquivo_original,novo_arquivo)
print(rs)

