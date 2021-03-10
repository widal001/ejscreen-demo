from mapper.app import create_app

app, db = create_app()
app.config["TESTING"] = True

if __name__ == "__main__":
    app.run(debug=True)
