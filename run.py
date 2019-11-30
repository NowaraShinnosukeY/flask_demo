from app import app

@app.route('/')
def hello_world():
    print(app.url_map)

    return 'Hello World!'



if __name__ == '__main__':
    app.run()
