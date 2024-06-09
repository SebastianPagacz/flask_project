from website import create_app

app = create_app()

if __name__ == '__main__':
#debug = True means that after every chnage site will be reloaded
    app.run(debug=True)
