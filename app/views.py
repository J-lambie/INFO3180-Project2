from app import app
from flask import Flask, abort, request, jsonify, g, url_for, render_template
import requests
from image_getter import image_dem
from models import User

@app.route('/')
def home():
    return "I'm home"

@app.route('/api/thumbnails/process', methods=['POST'])
def thumbnails():
    if request.method == 'POST' :
        url=request.form['url']
        r=requests.get(url)
        if r.status_code==200:
            thumbnails=image_dem(url)
            obj={'error': 'null','data':{'Thumbnail':thumbnails},'message':'success'}
            json=jsonify(obj)
            return json
        json=jsonify({'error':"1",'data':{},'message':'failure'})
        return json
    else:
        return "There is no get request"

@app.route('/api/user/register', methods=['POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        new_user=User(name=name,email=email,password=password)




if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)