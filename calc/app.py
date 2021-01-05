from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/math/<operation>')
def math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    operations_dict = {
        'add': add(a, b),
        'sub': sub(a, b),
        'mult': mult(a, b),
        'div': div(a, b),
    }

    return str(operations_dict[operation])
