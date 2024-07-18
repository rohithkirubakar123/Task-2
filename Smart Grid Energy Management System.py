from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

energy_status = {
    "total_energy": 1000,  # in kWh
    "usage": 0,            # in kWh
    "threshold": 800       # in kWh
}

@app.route('/')
def index():
    return render_template('index.html', status=energy_status)

@app.route('/update', methods=['POST'])
def update_usage():
    new_usage = int(request.form.get('usage'))
    energy_status["usage"] = new_usage
    return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(debug=True)
