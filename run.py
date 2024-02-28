from app import create_app

app = create_app(use_auth=True)

if __name__ == "__main__":
    app.run(debug=True)