from flask import Flask, jsonify, request

app =Flask(__name__)

@app.route("/")
def root():
    return "root"


@app.route("/users/<id>")
def get_user(id):
    user= {"id":id, "name": "test", "telefono": "999-666-333"}
    query = request.args.get('query')
    if query:
        user["query"] = query
    return jsonify(user), 200

#/users/123?query=query_test


if __name__ == '__main__':
    app.run(debug=True)
