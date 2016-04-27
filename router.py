import json, logging, validation
from distutils.util import strtobool

from flask import Flask, request, redirect
from flask_digest import Stomach
from flask_digest.hasher import hash_all

from core import Controller
from core.mailing import Email
from core.generator import Generator

#----------------------------------CONFIG---------------------------------------

app = Flask(__name__)
stomach = Stomach('garupa.com')

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USERNAME = 'sitegarupa@gmail.com',
    MAIL_PASSWORD = 'garupa.com',
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_DEFAULT_SENDER = 'sitegarupa@gmail.com',

    MAX_CONTENT_LENGTH = 1024 * 1024,
    DEBUG = True
)

email_manager = Email(app)
controller = Controller()
generator = Generator()

@app.after_request
def add_header(response):
    headers = response.headers

    if 'WWW-Authenticate' in headers:
        headers['WWW-Authenticate'] = \
        headers['WWW-Authenticate'].replace('Digest', 'X-Digest')

    headers['Cache-Control'] = 'max-age=0'
    return response

#--------------------------------STATUS-CODES-----------------------------------

CONFLICT       = 'Aborted due to conflict.', 409
CREATED        = 'Resource created.'       , 200
UPDATED        = 'Resource updated.'       , 200
NOT_FOUND      = 'Resource not found.'     , 404
BAD_REQUEST    = 'Bad arguments provided.' , 400
UNAUTHORIZED   = 'Not authorized.'         , 401

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

#-------------------------------AUTHENTICATION----------------------------------

@stomach.access
def get_credentials(uid):
    try: uid = int(uid)
    except: return None
    return controller.get_credentials(uid)

@stomach.register
def register_credentials(uid, passwd, name, email):
    return controller.register_user(uid, passwd, name, email)

def logged_user():
    return int(request.authorization.username)

#------------------------------------API----------------------------------------

@app.route('/api/users', methods=['POST'])
def register_user():
    try:
        args = request.json
        assert validation.complete('user', args)

        for attr, value in args.iteritems():
            assert validation.check(attr, value)
    except:
        return BAD_REQUEST

    uid, name, email = args['uid'], args['name'], args['email']
    passwd = args['passwd'] or generator.password()

    user = register_credentials(uid, passwd, name, email)
    if user: email_manager.send_welcome(user, passwd)
    return CREATED if user else CONFLICT

@app.route('/api/users/<int:uid>', methods=['GET'])
@stomach.protect
def view_user(uid):
    vuid = logged_user()
    view = controller.view_user(uid, vuid)

    if view == None: return NOT_FOUND
    return json.dumps(view)

@app.route('/api/users/<int:uid>/<string:attr>', methods=['PUT'])
@stomach.protect
def update_user(uid, attr):
    try:
        value = request.json['value']
        assert validation.check(attr, value)
    except:
        return BAD_REQUEST

    if uid != logged_user(): return UNAUTHORIZED

    success = controller.update_user(uid, attr, value)
    return UPDATED if success else NOT_FOUND

@app.route('/api/users/<int:uid>/password-reset', methods=['POST'])
def recover_passwd(uid):
    new_passwd = generator.password()
    hashed_passwd = hash_all(uid, stomach.realm, new_passwd)
    user = controller.get_user(uid)

    success = controller.recover_passwd(uid, hashed_passwd)
    if success: email_manager.send_recover_passwd(user, new_passwd)
    return UPDATED if success else NOT_FOUND

@app.route('/api/users/<int:uid>/friends', methods=['POST'])
@stomach.protect
def add_friend(uid):
    try: fuid = request.json['fuid']
    except: return BAD_REQUEST

    if uid != logged_user(): return UNAUTHORIZED

    success = controller.add_friend(uid, fuid)
    return UPDATED if success else NOT_FOUND

@app.route('/api/users/<int:uid>/friends/<int:fuid>', methods=['DELETE'])
@stomach.protect
def remove_friend(uid, fuid):
    if uid != logged_user(): return UNAUTHORIZED

    success = controller.remove_friend(uid, fuid)
    return UPDATED if success else NOT_FOUND

@app.route('/api/users/<int:uid>/notifications', methods=['GET'])
@stomach.protect
def get_notifications(uid):
    if uid != logged_user(): return UNAUTHORIZED

    notifications = controller.get_notifications(uid)
    print notifications
    print 'ok'

    if notifications == None: return NOT_FOUND
    return json.dumps(notifications)

@app.route('/api/rides', methods=['POST'])
@stomach.protect
def register_ride():
    try:
        args = request.json
        assert validation.complete('ride', args)

        for attr, value in args.iteritems():
            assert validation.check(attr, value)
    except:
        return BAD_REQUEST

    args['driver'] = logged_user()

    success = controller.register_ride(**args)
    return CREATED if success else NOT_FOUND

@app.route('/api/users/<int:uid>/rides', methods=['POST'])
@stomach.protect
def join_ride(uid):
    try:
        rid = request.json['rid']
        district = request.json['district']
        complement = request.json['complement']
    except:
        return BAD_REQUEST

    if uid != logged_user(): return UNAUTHORIZED

    success = controller.join_ride(uid, rid, district, complement)
    return UPDATED if success else NOT_FOUND

@app.route('/api/users/<int:uid>/rides/<int:rid>', methods=['DELETE'])
@stomach.protect
def cancel_ride(uid, rid):
    if uid != logged_user(): return UNAUTHORIZED

    success = controller.cancel_ride(uid, rid)
    return UPDATED if success else NOT_FOUND

@app.route('/api/rides', methods=['GET'])
@stomach.protect
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

        page, limit = int(page), int(limit)
        weekly, date = strtobool(weekly), long(date)
    except:
        return BAD_REQUEST

    result = controller.search_rides(dest, district, date, weekly, logged_user())

    return json.dumps({
        'results': result[(page-1)*limit:page*limit],
        'pages': (len(result) + limit - 1) / limit
    })

#-----------------------------------MAIN----------------------------------------

if __name__ == '__main__':
    logging.basicConfig(filename='info.log', level=logging.DEBUG)
    register_credentials(114110428, "123" , "casfasfh", "safsafasf@gmail.com")
    register_credentials(114110429, "123", "casfsadfsaf", "safsafgfgfdsf@gmail.com")
    app.run(host='0.0.0.0', port=8000)
