from flask import Flask
app =Flask(__name__)

@app.route('/blog/<int:post_id>')
def show_blog(post_id):
    return 'blog_number %d!' %id

@app.route('/rev/<float:rev')
def revision(revNo):
    return 'Revision number %f' %revNo


if __name__ == '__main__':
   app.run()
