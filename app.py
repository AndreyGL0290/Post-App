from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv

from DB.posts.pull_posts import pull_posts
from DB.posts.push_post import push_post
from DB.posts.delete_post import delete_post

app = Flask(__name__)

@app.get('/')
def homePage():
    data = pull_posts()
    return render_template('index.html', data=data)

@app.post('/createPost')
def createPost():
    data = request.form.to_dict()
    push_post(data['new-post-text'])
    return redirect('/')

@app.post('/deletePost')
def deletePost():
    data = request.form.to_dict()
    delete_post(int(data['post-id']))
    return redirect('/')

@app.get('/newPost')
def postPage():
    return render_template('newPost.html')

if __name__ == '__main__':
    load_dotenv()
    app.run(host='127.0.0.1', port=8000)