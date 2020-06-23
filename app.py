from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import os
from inference import predict
import glob
app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        # remove static directory if it exists
        for files in glob.glob(os.path.join("static", "*")):
            os.remove(files)

        name, img, path = predict(text)
        img.save(os.path.join("static", "molecule.png"))
        path.save(os.path.join("static", "pathway.png"))

        result = {
            'mol_name': name,
            'mol_path': os.path.join("static", "molecule.png"),
            'pathway_path': os.path.join("static", "pathway.png")
        }
        return render_template('show.html', result=result)
    return render_template('index.html')  # by default it will look in templates folder


if __name__ == '__main__':
    app.run(debug=True)
