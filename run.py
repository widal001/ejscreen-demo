from mapper import create_app

app = create_app()
app.config["TESTING"] = True

if __name__ == "__main__":
    app.run(debug=True)
