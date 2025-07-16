from flask import Flask,request,jsonify

app = Flask(__name__)

#Creating an API-KEY
API_KEY="myapikey"

#Middleware/decorator to verify API-KEY
def require_api_key(func):
    def wrapper(*args,**kwargs):
        key = request.headers.get('x-api-key')

        if key and key == API_KEY:
            return func(*args, **kwargs)
        
        else:
            return jsonify({"Error: Unauthorized, Missing API_KEY"})
        
    return wrapper

@app.route('/',methods=["GET"])
def login():
    return "Login Here"

@app.route('/profile', methods=["GET"])
@require_api_key #Middleware/Guard
def profile():
    return "Welcome to the profile"

if __name__=='__main__':
    app.run(debug=True)