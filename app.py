import flask

import logger

logger = logger.get_logger(__name__)

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<name>', methods=['GET'])
def get_user(name=None):
    logger.debug('name={name}'.format(name=name))

    return 'Hello, World! Hello {name}.'.format(name=name)


@app.route('/search', methods=['GET'])
def get_search():
    query = flask.request.args.get('q')
    logger.info('q={query}'.format(query=query))  # message:q=matsumoto
    logger.info(flask.request.args)  # message:ImmutableMultiDict([('q', 'hoge')])

    return 'No matches were found for "{query}".'.format(query=query)


if __name__ == "__main__":
    app.run(debug=True)
