import flask as flask
from flask import Flask
app = Flask(__name__)

@app.route("/createproject")
def createproject():
    return 'project_id %s' % "randomproject_id"


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id


if __name__ == "__main__":
    app.run()