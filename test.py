import requests

url = "http://127.0.0.1:8000/processar_docx/"

payload = {
    "substituicoes": '{"substituicoes": {"{{nome}}": "João da Silva", "{{data}}": "01/08/2024", "{{empresa}}": "Empresa Exemplo Ltda."}}'
}
files = [
    (
        "file",
        (
            "C:\\tmp\\template.docx",
            open("C:\\tmp\\template.docx", "rb"),
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ),
    )
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

# Verifique se a resposta foi bem-sucedida
if response.status_code == 200:
    with open("resultado.docx", "wb") as f:
        f.write(response.content)
    print("PDF salvo como 'resultado.docx'")
else:
    print(f"Erro: {response.status_code}")
    print(response.text)
