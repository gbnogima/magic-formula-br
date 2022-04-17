import requests

DOWNLOAD_URL = 'https://api-cotacao-b3.labdo.it/api/empresa'
CSV_FILE = 'setor.csv'

r = requests.get(DOWNLOAD_URL)
if r.status_code != 200:
    raise Exception("Couldn't download file.")
else:
    print("Success")

data = r.json()

fin = open(CSV_FILE, "wt")
fin.write(f"code;name;sector;segment\n")

for company in data:
    fin.write(f"{company['cd_acao_rdz']};{company['nm_empresa']};{company['setor_economico']};{company['segmento']}\n")

fin.close()
