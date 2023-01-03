from app import create_app

app = create_app()

def run():
    app.run(host="0.0.0.0", debug=True, port=80)

if __name__ == "__main__":
    run()
