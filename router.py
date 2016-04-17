import re, json

from werkzeug.exceptions import BadRequest
from flask import Flask, request, redirect
from logic import Controller

#----------------------------------CONFIG---------------------------------------

app = Flask(__name__)
controller = Controller()

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['DEBUG'] = True

#----------------------------------STATIC---------------------------------------

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

#------------------------------------API----------------------------------------

@app.route('/api/user/register', methods=['POST'])
def register():
    try:
        name = request.json['name']
        uid = request.json['uid']
        email = request.json['email']
        passwd = request.json['passwd']

        assert re.match('.{3,}', name)
        assert re.match('\d{9}$', uid)
        assert re.match('.+@.+\..+', email)
        assert re.match('.+', passwd)

        uid = int(uid)

    except: raise BadRequest()
    else: success = controller.register(name, uid, email, passwd)

    if success: return ('Account created.', 200)
    return ('User ID taken.', 409)

@app.route('/api/user/<int:uid>', methods=['GET'])
def user_view(uid):
    try:
        vid = request.args.get('vid', None)
        if vid != None: vid = int(vid)

    except: raise BadRequest()
    else: view = controller.user_view(uid, vid)

    if view != None: return json.dumps(view)
    return ('User does not exist.', 404)

@app.route('/api/user/<int:uid>', methods=['POST'])
def update_user(uid):
    try:
        print repr(request.json)
        attr, value = request.json

        if attr == 'name': assert re.match('.{3,}', value)
        if attr == 'email': assert re.match('.+@.+\..+', value)
        if attr == 'phone': assert re.match('\(\d\d\) \d{4,5}-\d{4}$', value)
        if attr == 'photo_url': assert re.match('data:image/.+;base64,[A-Za-z0-9+/]*={0,2}$', value)

    except: raise BadRequest()
    else: controller.update_user(uid, attr, value)

    return ('User info updated.', 200)

#-----------------------------------MAIN----------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
