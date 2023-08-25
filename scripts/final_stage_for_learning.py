import pandas as pd
from tqdm import tqdm
import swifter


tqdm.pandas()

def prepare(passengers_csv="../data/ds_passengers_prepared_small.csv", bandwidth_csv="../data/ds_bandwidth_prepared_park.csv"):
    df_ps = pd.read_csv(passengers_csv)
    df_bd = pd.read_csv(bandwidth_csv)
    print(df_ps.columns)


    df_ps = df_ps.drop(["date", "line", "station", "Unnamed: 0"], axis=1)



    def func_(x):
        ds = df_bd[df_bd.station_id == x["station_id"]].drop(["Unnamed: 0", "station_id"], axis=1).iloc[-1]
        return pd.concat([x,ds])
    out_df = df_ps.swifter.apply(func_, axis=1)
    return out_df



if __name__ == "__main__":
    df = prepare().drop(["line_name", "station_name"], axis=1)
    df.to_csv("../data/dataset_small.csv")