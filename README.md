# PDF to Image Web Application

This project is a web application that allows users to upload PDF files, convert them to images, and download the converted images. It is built using Flask and utilizes the `pdf2image` library for the conversion process.

## Project Structure

```
pdf-img-webapp
├── app.py                # Main entry point of the web application
├── requirements.txt      # Lists the dependencies required for the project
├── src
│   ├── pdf_converter.py   # Contains the PDF to JPG conversion logic
│   └── templates
│       └── index.html     # HTML template for the main page
│   └── static
│       └── README.md      # Information about static assets (currently empty)
├── README.md              # Documentation for the project
```

## Requirements

To run this project, you need to have Python installed on your machine. You can install the required dependencies by running:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory.
2. Run the application using the following command:

```
python app.py
```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

- Upload a PDF file using the provided interface.
- Click the convert button to convert the PDF to images.
- Download the converted images from the provided links.

## License

This project is licensed under the MIT License.