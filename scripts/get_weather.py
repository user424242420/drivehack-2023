import pandas as pd
import swifter
import re
import time
from dateutil import parser
import datetime
import numpy as np

re_sub_n = r"([0-9]{0,3})%"


#Index(['Time', 'T', 'Po', 'P', 'Pa', 'U', 'DD', 'Ff', 'ff10', 'ff3', 'N', 'WW',
       # 'W1', 'W2', 'Tn', 'Tx', 'Cl', 'Nh', 'H', 'Cm', 'Ch', 'VV', 'Td', 'RRR',
       # 'tR', 'E', 'Tg', 'E'', 'sss'],

def transform_weather(file = "../data/weather.csv"):
    df = pd.DataFrame(pd.read_csv(file),
                      columns=["Time", "T", "U", "N", "RRR", "sss"]).fillna(0)

    def _func(x):
        try:
            r = re.findall(re_sub_n, x["N"])[0]
        except:
            r = 0
        x["Time"] = parser.parse(x["Time"].replace("2022", "2023"))
        x["N"] = int(r)
        x["sss"] = float(''.join(filter(lambda x: x in "1234567890.", str(x["sss"]))) or 0)
        x["RRR"] = float(''.join(filter(lambda x: x in "1234567890.", str(x["RRR"]))) or 0)
        return x


    r = df.swifter.apply(_func, axis=1).set_index("Time")


    return r


def get_weather(df, time=datetime.datetime.now()):
    i = np.argmin(np.abs(df.index.to_pydatetime() - time))

    return df.iloc[i]


if __name__ == "__main__":
    df = transform_weather()
    print(get_weather(df))