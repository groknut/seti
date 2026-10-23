import os
from bottle import Bottle, request, run, template, static_file

app = Bottle()
UPLOAD_DIR = './uploads'  # Папка для сохранения файлов

# Создаем папку, если её нет
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html>
    <body>
        <h2>Загрузка файла</h2>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="upload">
            <input type="submit" value="Загрузить">
        </form>
    </body>
    </html>
    '''

@app.route('/upload', method='POST')
def do_upload():
    upload = request.files.get('upload')
    if not upload:
        return "Файл не выбран."

    # Безопасное сохранение файла
    name, ext = os.path.splitext(upload.filename)
    # В реальном приложении здесь нужно очищать имя файла (secure_filename)
    save_path = os.path.join(UPLOAD_DIR, f"{name}{ext}")
    upload.save(save_path)

    return f"Файл сохранен: {save_path}"

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
