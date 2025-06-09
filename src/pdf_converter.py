from pdf2image import convert_from_path
import os

def pdf_para_jpg(caminho_pdf, pasta_saida=None, dpi=300):
    if pasta_saida is None:
        pasta_saida = os.path.dirname(caminho_pdf)
    os.makedirs(pasta_saida, exist_ok=True)

    paginas = convert_from_path(caminho_pdf, dpi=dpi)

    image_paths = []
    for i, pagina in enumerate(paginas):
        nome_arquivo = os.path.join(pasta_saida, f'pagina_{i+1}.jpg')
        pagina.save(nome_arquivo, 'JPEG')
        image_paths.append(nome_arquivo)

    return image_paths