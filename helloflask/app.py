from flask import Flask, render_template, request
from temp_helper import get_current_temp


@app.route('/weather/', methods = ['GET', 'POST'])
def show_weather():
    if request.method == 'POST':
        city_name = request.form['city']

        temperature = get_current_temp(city_name)

        return render_template('weather-result.html', city = city_name, temperature = temperature)
    else:
        return render_template('weather-form.html')
