import json, validation
from flask import Flask, request, redirect
from logic import Controller

#----------------------------------CONFIG---------------------------------------

app = Flask(__name__)
controller = Controller()

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['DEBUG'] = True

#--------------------------------STATUS-CODES-----------------------------------

UID_TAKEN      = 'User ID taken.'         , 409
USER_CREATED   = 'User created.'          , 200
USER_UPDATED   = 'User updated.'          , 200
USER_NOT_FOUND = 'User does not exist.'   , 404
BAD_REQUEST    = 'Bad arguments provided.', 400

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

@app.route('/api/users', methods=['POST'])
def register():
    try:
        args = request.json.copy()
        assert set(args) == validation.REQUIRED

        for attr, value in args.iteritems():
            assert validation.check(attr, value)

        args['uid'] = int(args['uid'])

    except: return BAD_REQUEST
    else: success = controller.register(**args)

    if success: return USER_CREATED
    return UID_TAKEN

@app.route('/api/users/<int:uid>', methods=['GET'])
def view_user(uid):
    try: vuid = int(request.args['vuid'])
    except: return BAD_REQUEST
    else: view = controller.view_user(uid, vuid)

    if view != None: return json.dumps(view)
    return USER_NOT_FOUND

@app.route('/api/users/<int:uid>/<string:attr>', methods=['PUT'])
def update_user(uid, attr):
    try:
        value = request.data
        assert validation.check(attr, value)
        assert attr in validation.EDITABLE

    except: return BAD_REQUEST
    else: success = controller.update_user(uid, attr, value)

    if success: return USER_UPDATED
    return USER_NOT_FOUND

@app.route('/api/users/<int:uid>/friends', methods=['POST'])
def add_friend(uid):
    try: fuid = int(request.data)
    except: return BAD_REQUEST
    else: success = controller.add_friend(uid, fuid)

    if success: return USER_UPDATED
    return USER_NOT_FOUND

@app.route('/api/users/<int:uid>/friends/<int:fuid>', methods=['DELETE'])
def remove_friend(uid, fuid):
    success = controller.remove_friend(uid, fuid)

    if success: return USER_UPDATED
    return USER_NOT_FOUND

#-----------------------------------MAIN----------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
