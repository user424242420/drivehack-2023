from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, TimeField, DateField

with open('data/stations.txt') as file:
    data = list(map(lambda x: x.strip()[:-1], file.readlines()))


class DataForm(FlaskForm):
    stations = SelectField('Станция', choices=data)
    parking = IntegerField('Кол-во перехватывающих парковок')
    humans = IntegerField('Население района')
    time = TimeField('Время')
    date = DateField('Дата')
    weekend = BooleanField('Выходной')
    temp = IntegerField('Температура')
    humidity = IntegerField('Влажность (%)')
    cloudiness = IntegerField('Облачность (%)')
    puddles = IntegerField('Выпавшие осадки (мм)')
    snow = IntegerField('Снежный покров (см)')