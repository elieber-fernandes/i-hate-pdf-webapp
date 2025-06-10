# I HATE PDF ☠️ – Conversor PDF para JPG

Conversor web simples e moderno para transformar arquivos PDF em imagens JPG.  
Permite upload de múltiplos PDFs, converte todas as páginas e gera um arquivo ZIP para download.

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Flask** – Framework web
- **pdf2image** – Conversão de PDF para imagens (JPG/PNG)
- **pdfminer.six** – Extração de texto de PDFs
- **pdf2docx** – Conversão de PDF para DOCX
- **python-pptx** – Geração de apresentações PowerPoint
- **Pillow** – Manipulação de imagens
- **Bootstrap 4** – Interface moderna e responsiva
- **Jinja2** – Templates HTML

## 💻 Como rodar localmente

1. Clone o repositório:
    ```bash
    git clone https://github.com/elieber-fernandes/pdf-img-webapp
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # ou venv\Scripts\activate no Windows
    pip install -r requirements.txt
    ```

3. Execute o app:
    ```bash
    python app.py
    ```

4. Acesse em [http://localhost:5000](http://localhost:5000)

## 📦 Deploy

- Suporta deploy fácil no [PythonAnywhere](https://www.pythonanywhere.com/), [Render](https://render.com/) ou qualquer serviço compatível com Flask.


## 🛠️ Funcionalidades

- **PDF → JPG**: Converte cada página do PDF em uma imagem JPG.
- **PDF → PNG**: Converte cada página do PDF em uma imagem PNG.
- **PDF → TXT**: Extrai todo o texto do PDF para um arquivo .txt.
- **PDF → DOCX**: Converte o PDF para um arquivo Word editável (.docx).
- **PDF → PowerPoint (PPTX)**: Cada página do PDF vira um slide com a imagem da página.


## 👨‍💻 Autor

- [LinkedIn](https://www.linkedin.com/in/eliebermartins/)
- [GitHub](https://github.com/elieber-fernandes)

---

> Desenvolvido por Elieber Martins
