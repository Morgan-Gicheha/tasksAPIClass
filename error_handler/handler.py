
from main import app
# error handling
@app.errorhandler(400)
def bad_request(error):
    return {"message": "Bad request"}, 400


@app.errorhandler(401)
def Unauthorized(error):
    return {"message": "Unauthorized"}, 401


@app.errorhandler(403)
def forbidden(error):
    return {"message": "Forbidden"}, 403

@app.errorhandler(404)
def not_foud(error):
    return {"message": "Request not found"}, 404


@app.errorhandler(405)
def bad_request(error):
    return {"message": "Request method is not allowed"}, 405