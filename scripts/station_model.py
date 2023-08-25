import csv
import pandas as pd
from dataclasses import dataclass, astuple
import people
import swifter


@dataclass
class Station:
    input_doors_total_bandwidth: int
    input_turnstile_total_bandwidth: int
    input_stairs_total_bandwidth: int
    input_escalator_total_bandwidth: int


def load_model(file_csv="../data/ds_bandwidth_circle.csv"):
    df = pd.read_csv(file_csv).dropna(axis=1,how='all')
    out_df = pd.DataFrame(df, columns=["line_id", "line_name", "station_name",
                                       "station_id",
                                       "input_doors_total_bandwidth",
                                       "input_turnstile_total_bandwidth",
                                       "input_stairs_total_bandwidth",
                                       "input_escalator_total_bandwidth"])
    perehvat_df = pd.read_csv("../data/perehvat_id.csv").set_index("id")

    def _func(x):
        try:
            parking_count = perehvat_df.loc[[x["station_id"]]].sum()["Количество парковочных мест"]
        except:
            parking_count = 0
        return pd.concat([x, pd.Series([people.get_people_by_station_id(x["station_id"]), parking_count], index=["count_people", "parking_count"])])


    out_df = out_df.apply(_func, axis=1)
    return out_df

if __name__ == "__main__":
    df = load_model()
    df.to_csv("../data/ds_bandwidth_prepared_park.csv")