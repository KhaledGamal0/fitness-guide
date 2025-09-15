
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup
import importlib, inspect

app = Flask(__name__)

gen = importlib.import_module("fitness_guide_generator")

# Choose a generator function (first starting with 'generate')
def resolve_generator():
    for name in dir(gen):
        if name.lower().startswith("generate"):
            fn = getattr(gen, name)
            if callable(fn):
                return fn
    return getattr(gen, "generate_fitness_guide", None)

MAIN_FUNC = resolve_generator()

def run_generator(**kwargs):
    if not callable(MAIN_FUNC):
        return "<h2>Generator function not found.</h2>"
    try:
        sig = inspect.signature(MAIN_FUNC)
        accepted = {}
        for k,v in kwargs.items():
            if v in (None, ""): continue
            if k in sig.parameters:
                p = sig.parameters[k]
                try:
                    if p.annotation in (int, float):
                        accepted[k] = p.annotation(v)
                    else:
                        accepted[k] = v
                except Exception:
                    accepted[k] = v
        try:
            return MAIN_FUNC(**accepted)
        except TypeError:
            return MAIN_FUNC()
    except Exception as e:
        return f"<h3>Error:</h3><pre>{e}</pre>"

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/guide", methods=["POST"])
def guide():
    form = request.form.to_dict()
    if form.get("height") and not form.get("height_cm"):
        form["height_cm"] = form["height"]
    if form.get("weight") and not form.get("weight_kg"):
        form["weight_kg"] = form["weight"]
    html = run_generator(**form)
    return render_template("guide.html", result_html=Markup(html))
