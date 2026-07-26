import requests

def consulta_cep(cep="01001000"):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    cep = input("Digite o CEP (apenas números), exemplo 01001000: ").strip() or "01001000"
    try:
        dados = consulta_cep(cep)
        print("Resultado da API:")
        for k, v in dados.items():
            print(f"{k}: {v}")
    except Exception as e:
        print("Erro ao consultar API:", e)
