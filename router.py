import json, logging, validation
from distutils.util import strtobool
from flask import Flask, request, redirect
from core import Controller
from emails import Email

#----------------------------------CONFIG---------------------------------------

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['DEBUG'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465 
app.config['MAIL_USERNAME'] = 'sitegarupa@gmail.com'
app.config['MAIL_PASSWORD'] = 'garupa.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True 
app.config['MAIL_DEFAULT_SENDER'] = 'sitegarupa@gmail.com'

controller = Controller()
emailHelper = Email(app)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'max-age=0'
    return response

#--------------------------------STATUS-CODES-----------------------------------

CONFLICT       = 'Aborted due to conflict.', 409
CREATED        = 'Resource created.'       , 200
UPDATED        = 'Resource updated.'       , 200
NOT_FOUND      = 'Resource not found.'     , 404
BAD_REQUEST    = 'Bad arguments provided.' , 400

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
def register_user():
    try:
        
        args = request.json.copy()
        assert set(args) == validation.REQUIRED

        for attr, value in args.iteritems():
            assert validation.check(attr, value)

        for attr, value in args.iteritems():
            args[attr] = validation.cast(attr, value)

    except: return BAD_REQUEST
    else: success = controller.register_user(**args)

    if success:
        print args
        print args['uid']
        emailHelper.send_welcome(controller.get_user(args['uid']))
        return CREATED
    return CONFLICT

@app.route('/api/users/<int:uid>', methods=['GET'])
def view_user(uid):
    try: vuid = int(request.args['vuid'])
    except: vuid = uid
    view = controller.view_user(uid, vuid)

    if view != None: return json.dumps(view)
    return NOT_FOUND

@app.route('/api/users/<int:uid>/<string:attr>', methods=['PUT'])
def update_user(uid, attr):
    try:
        value = request.data
        assert validation.check(attr, value)
        assert attr in validation.EDITABLE

    except: return BAD_REQUEST
    else: success = controller.update_user(uid, attr, value)

    if success: return UPDATED
    return NOT_FOUND

@app.route('/api/recover/', methods=['PUT'])
def recover_passwd():
    try:
        args = request.json.copy()
        assert set(args) == validation.REQUIRED

        for attr, value in args.iteritems():
            assert validation.check(attr, value)

        for attr, value in args.iteritems():
            args[attr] = validation.cast(attr, value)

    except: return BAD_REQUEST
    else: success = controller.recover_passwd(**args)

    if success: 
        emailHelper.send_passwd(controller.get_user(get_uid_from_email(args['email'])))
        return UPDATED
    return NOT_FOUND

@app.route('/api/users/<int:uid>/friends', methods=['POST'])
def add_friend(uid):
    try: fuid = int(request.data)
    except: return BAD_REQUEST
    else: success = controller.add_friend(uid, fuid)

    if success: return UPDATED
    return NOT_FOUND

@app.route('/api/users/<int:uid>/friends/<int:fuid>', methods=['DELETE'])
def remove_friend(uid, fuid):
    success = controller.remove_friend(uid, fuid)
    if success: return UPDATED
    return NOT_FOUND

@app.route('/api/rides', methods=['POST'])
def register_ride():
    try:
        args = request.json.copy()
        # Missing validation

    except: return BAD_REQUEST
    else: success = controller.register_ride(**args)

    if success: return CREATED
    return NOT_FOUND

@app.route('/api/users/<int:uid>/rides', methods=['POST'])
def join_ride(uid):
    try:
        rid = int(request.json['rid'])
        district = request.json['district']
        complement = request.json['complement']

    except: return BAD_REQUEST
    else: success = controller.join_ride(uid, rid, district, complement)

    if success: return UPDATED
    return NOT_FOUND

@app.route('/api/users/<int:uid>/rides/<int:rid>', methods=['DELETE'])
def cancel_ride(uid, rid):
    success = controller.cancel_ride(uid, rid)
    if success: return UPDATED
    return NOT_FOUND

@app.route('/api/rides', methods=['GET'])
def search_ride():
    try:
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 10)

        assert 1 <= page
        assert 1 <= limit

        dest = request.args['dest']
        district = request.args['district']
        date = request.args['date']
        weekly = request.args['weekly']
        uid = request.args['uid']

        page, limit = int(page), int(limit)
        date, uid = int(date), int(uid)
        weekly = strtobool(weekly)

    except: return BAD_REQUEST
    else: result = controller.search_rides(dest, district, date, weekly, uid)

    return json.dumps({
        'results': result[(page-1)*limit:page*limit],
        'pages': (len(result) + limit - 1) / limit
    })

#-----------------------------------MAIN----------------------------------------

if __name__ == '__main__':
    #logging.basicConfig(filename='info.log',level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8000)
