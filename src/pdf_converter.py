from pdf2image import convert_from_path
import os

def pdf_para_jpg(caminho_pdf, pasta_saida=None, dpi=300):
    if pasta_saida is None:
        pasta_saida = os.path.dirname(caminho_pdf)
    os.makedirs(pasta_saida, exist_ok=True)

    paginas = convert_from_path(caminho_pdf, dpi=dpi)
    base = os.path.splitext(os.path.basename(caminho_pdf))[0]

    image_paths = []
    for i, pagina in enumerate(paginas, 1):
        nome_arquivo = os.path.join(pasta_saida, f'{base}_pagina_{i}.jpg')
        pagina.save(nome_arquivo, 'JPEG')
        image_paths.append(nome_arquivo)

    return image_paths