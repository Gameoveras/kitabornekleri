from flask import Flask, render_template, request, flash
import openai

app = Flask(__name__)

openai.api_key = "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"


@app.route("/", methods=['POST', 'GET'])
def anasayfa():
    if request.method == 'POST':
        soru = request.form['soru']
        response = openai.Completion.create(
        model="text-davinci-001",
        prompt=f"{soru}:",
        temperature=0,
        max_tokens=150)
        return render_template('index.html',response=response)
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)