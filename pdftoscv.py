import PyPDF2
import pandas as pd

def pdf_to_csv(pdf_file):
  """
  Converte um arquivo PDF para CSV, salvando o CSV com o mesmo nome do PDF.

  Args:
    pdf_file: Caminho para o arquivo PDF.
  """

  # Abre o arquivo PDF
  with open(pdf_file, 'rb') as pdf_fileobj:
    pdf_reader = PyPDF2.PdfReader(pdf_fileobj)

    # Cria uma lista para armazenar as linhas do CSV
    rows = []

    # Itera sobre cada página do PDF
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]

      # Extrai o texto da página
      text = page.extract_text()

      # Divide o texto em linhas
      lines = text.splitlines()

      # Adiciona as linhas à lista de linhas
      rows.extend(lines)

  # Cria um DataFrame Pandas a partir das linhas
  df = pd.DataFrame(rows)

  # Extrai o nome do arquivo PDF sem a extensão
  csv_file = pdf_file[:-4] + '.csv'

  # Salva o DataFrame como um arquivo CSV
  df.to_csv(csv_file, index=False, header=False)

# Pede ao usuário para inserir o nome do arquivo PDF
pdf_file = input("Digite o nome do arquivo PDF (incluindo a extensão): ")

# Chama a função para converter o PDF para CSV
pdf_to_csv(pdf_file)

print(f"Arquivo CSV '{pdf_file[:-4]}.csv' criado com sucesso!")