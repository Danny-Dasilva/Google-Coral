from flask import Flask
from apps import run_server
from classify import add_render_gen_args, render_gen
import _thread as thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

def main():
    run_server(add_render_gen_args, render_gen)

if __name__ == "__main__":
    main
    thread.start_new_thread(main,())
    app.run(host='0.0.0.0', debug=True)