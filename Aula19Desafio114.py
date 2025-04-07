def verificarSite(url):
    import requests
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print('Site acessado com sucesso!')
        
    except:
        print('O site não está acessível.')
    

verificarSite('https://www.pudim.com.br')