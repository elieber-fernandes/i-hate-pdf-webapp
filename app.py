from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os
from src.pdf_converter import pdf_para_jpg
import zipfile
import io

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and file.filename and file.filename.endswith('.pdf'):
        pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(pdf_path)
        pdf_para_jpg(pdf_path, OUTPUT_FOLDER)
        # Após converter, redireciona para a página de output
        return redirect(url_for('output_files'))
    return "Invalid file type", 400

@app.route('/output')
def output_files():
    files = os.listdir(OUTPUT_FOLDER)
    file_links = [url_for('download_file', filename=f) for f in files]
    zip_link = None
    if len(files) > 1:
        zip_link = url_for('download_zip')
    return render_template('output.html', files=zip(files, file_links), zip_link=zip_link)

@app.route('/output/all.zip')
def download_zip():
    files = os.listdir(OUTPUT_FOLDER)
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for filename in files:
            file_path = os.path.join(OUTPUT_FOLDER, filename)
            zf.write(file_path, arcname=filename)
    memory_file.seek(0)
    return send_from_directory(
        directory=OUTPUT_FOLDER,
        filename='all.zip',
        as_attachment=True,
        mimetype='application/zip'
    ) if False else (
        # Serve o arquivo zip diretamente da memória
        (lambda f: (f, 200, {
            'Content-Type': 'application/zip',
            'Content-Disposition': 'attachment; filename=all.zip'
        }))(memory_file)
    )

@app.route('/output/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == '__main__':
    app.run()