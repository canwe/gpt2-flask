from flask import Flask, render_template, request, flash
from config import Config
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from web_model_generator import run_model

DEBUG = True
app = Flask(__name__)
app.config.from_object(Config)

class ReusableForm(Form):
    prompt = TextField('', validators=[validators.required()])

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
        result_text = ''
        if request.method == 'POST':
            prompt = request.form['prompt']
            print(prompt)

            if form.validate():
                result_text = run_model(prompt)
                result_text = prompt + result_text
            else:
                flash('All Fields Are Required')

        return render_template('index.html', form=form, result_text=result_text)

if __name__ == "__main__":
    app.run()