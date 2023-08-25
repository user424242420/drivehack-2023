import pandas as pd
from tqdm import tqdm
from datetime import date, datetime
import numpy as np
from holidays import country_holidays
from get_all_station_id import get_station_id
import get_weather

df_weather = get_weather.transform_weather()
import swifter
tqdm.pandas()
columns = ["date", "hour", "line", "station", "num_val"]

ru_holidays = country_holidays("RU")
class HourCome:
    number_hour: int # 0 to 24
    number_week: int # 0 to 6
    number_year: int # 0 to 365 (если 366 то тупо ставим 365)
    type_holiday: int # 0 - нет 1 - федеральный 2 - попущенный
    count_people: int # количество людей
    #event_people: int # сколько людей планируется на мероприятии # идея

    # weather в теории из openweather map

def load_model(passengers_csv="../data/ds_passengers_circle.csv"):
    df = pd.read_csv(passengers_csv)
    out_df = pd.DataFrame(df, columns=columns)

    def func_(x):
        _date = datetime(*map(int, x["date"].split("-")), x["hour"])
        
        return pd.concat([x, pd.Series([int(_date in ru_holidays),
                                        _date.weekday(), _date.timetuple().tm_yday, get_station_id(x["station"])],
                                       index=["type_holiday", "number_week", "number_year", "station_id"]),
                          get_weather.get_weather(df_weather,_date)
                          ])
    out_df = out_df.swifter.apply(func_, axis=1)
    return out_df

if __name__ == "__main__":
    df = load_model()

    df.to_csv("../data/ds_passengers_prepared_small.csv")
