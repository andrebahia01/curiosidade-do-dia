import requests

def main():
    url = "http://numbersapi.com/today/date"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        print("Curiosidade do dia:")
        print(resposta.text)
    except Exception as e:
        print("Erro ao buscar curiosidade:", e)

if __name__ == "__main__":
    main()
