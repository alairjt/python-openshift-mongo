from app import app

def run(host='0.0.0.0', port=8080, debug=False):
    app.debug = debug
    app.run(host=host, port=port)

if __name__ == "__main__":
    run(debug='-d' in sys.argv or '--debug' in sys.argv)