from flask import Flask, render_template, request
import temp_helper


@app.route('/weather/', methods = ['GET', 'POST'])
def show_weather():
    if request.method == 'POST':
        city_name = request.form['city']

        temperature = temp_helper.get_current_temp(city_name)

        return render_template('weather-result.html', city = city_name, temperature = temperature)
    else:
        return render_template('weather-form.html')