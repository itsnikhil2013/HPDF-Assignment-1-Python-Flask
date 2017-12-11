from flask import Flask, render_template, request, jsonify, send_file, make_response
import requests
import json
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/authors')
def authors():
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url)
    url2 = 'https://jsonplaceholder.typicode.com/posts'
    posts = requests.get(url2)
    usersdata = users.json()
    postsdata = posts.json()
    return render_template('catalog.html',authors=usersdata, posts=postsdata)


@app.route('/setcookie')
def setcookie():
    resp = make_response('Setting cookie!')
    if 'name' not in request.cookies:
        resp.set_cookie('name', 'Nikhil')
    if 'age' not in request.cookies:
        resp.set_cookie('age', '22')
    else:
        resp = make_response('Cookie already set')
    return resp


@app.route('/getcookies')
def getcookies():
    name = str(request.cookies.get('name'))
    age = str(request.cookies.get('age'))
    return 'Name : '+name+"\tAge : "+age

@app.route('/robots.txt')
def robot():
    return send_file('robots.txt')

@app.route('/html')
def htmlrender():
    return render_template('samplehtmlrender.html')

@app.route('/image')
def imagerender():
    return send_file('image.jpg')

@app.route('/input')
def input():
    return render_template('forminput.html')


if(__name__=='__main__'):
    app.run(debug=True)
