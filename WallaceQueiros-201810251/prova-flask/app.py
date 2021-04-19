from flask import Flask, render_template, json
from os import path

app = Flask(__name__, static_folder='static')

@app.context_processor
def export_categorias():
    json_path = path.join(app.static_folder, 'categorias.json')
    with open(json_path) as json_file:
        categorias = json.load(json_file)
    return dict(categorias=categorias)


@app.route('/video/<categoria>/<video>')
def video_player(categoria=None, video=None):
    return render_template('video_page.html', cid=int(categoria), vid=int(video))

@app.route('/')
def tela_inicial():
    return render_template('tela_inicial.html')


if __name__ == '__main__':
    app.run()
