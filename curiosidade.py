import requests
from datetime import datetime

def main():
    hoje = datetime.now()
    mes = hoje.month
    dia = hoje.day

    url = f"http://numbersapi.com/{mes}/{dia}/date"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        print("🧠 Curiosidade do dia:")
        print(resposta.text)
    except Exception as e:
        print("Erro ao buscar curiosidade:", e)

if __name__ == "__main__":
    main()
