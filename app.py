from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<name>', methods=['GET'])
def get_user(name=None):

    return 'Hello, World! Hello {name}.'.format(name=name)

@app.route('/search', methods=['GET'])
def get_search(name=''):
    query = request.args.get('q')
    return 'No matches were found for "{query}".'.format(query=query)

if __name__ == "__main__":
    app.run(debug=True)