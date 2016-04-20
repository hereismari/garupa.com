from flask import Flask, redirect
import controller
import logging

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/site/')

@app.route('/site/')
@app.route('/site/<path:url>')
def render_view(url=None):
    return serve_static('index.html')

@app.route('/<path:url>')
def serve_static(url):
    return app.send_static_file(url)

@app.route('/api/exemplo')
def api_exemple():
    return controller.example()

if __name__ == '__main__':
    logging.basicConfig(filename='info.log',level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8000, debug=True)
