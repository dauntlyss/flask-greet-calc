from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = add(a, b)
    return str(sum)

@app.route('/sub')
def sub_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    difference = sub(a, b)
    return str(difference)

@app.route('/mult')
def mult_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    product = mult(a, b)
    return str(product)

@app.route('/div')
def div_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    quoitent = div(a, b)
    return str(quoitent)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)


