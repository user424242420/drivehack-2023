from flask import Flask, render_template, make_response, request
from forms import DataForm
import pandas as pd
from get_all_station_id import get_station_id
from stations_info import stations_info
from catboost import CatBoostRegressor


model = CatBoostRegressor()
model.load_model("out_model.cbm")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kellogg'


@app.route("/", methods=('GET', 'POST'))
def main_page():
    form = DataForm(request.form)
    if request.method == 'POST' and form.validate():
        data = dict()

        idd = int(get_station_id(form.stations.data))

        data['station_id'] = idd
        data['count_people'] = form.humans.data
        data['parking_count'] = form.parking.data
        data['hour'] = form.time.data.hour
        data['type_holiday'] = int(form.weekend.data)
        data['number_week'] = form.date.data.timetuple().tm_yday
        data['number_year'] = form.date.data.year

        data['T'] = form.temp.data
        data['U'] = form.humidity.data
        data['N'] = form.cloudiness.data
        data['RRR'] = form.puddles.data
        data['sss'] = form.snow.data

        data['line_id'] = int(stations_info[idd][0])
        data['input_doors_total_bandwidth'] = stations_info[idd][1]
        data['input_turnstile_total_bandwidth'] = stations_info[idd][2]
        data['input_stairs_total_bandwidth'] = stations_info[idd][3]
        data['input_escalator_total_bandwidth'] = stations_info[idd][4]
        data['count_people'] = stations_info[idd][5]
        data['parking_count'] = stations_info[idd][6]

        x = pd.Series(data=data, index=['hour',
                                        'type_holiday',
                                        'number_week',
                                        'number_year',
                                        'station_id',
                                        'T', 'U', 'N',
                                        'RRR', 'sss', 'line_id',
                                        'input_doors_total_bandwidth',
                                        'input_turnstile_total_bandwidth', 'input_stairs_total_bandwidth',
                                        'input_escalator_total_bandwidth', 'count_people', 'parking_count'])
        print(x)
        return make_response(render_template('index.html', form=form, predict=int(model.predict(x))))
    return make_response(render_template('index.html', form=form, predict=0))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
