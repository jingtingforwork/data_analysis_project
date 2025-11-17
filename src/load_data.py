
def load_data():
    '''
    利用kaggle API下載最新dataset，並自動轉成dataframe
    '''
    import os
    import pandas as pd
    from kaggle.api.kaggle_api_extended import KaggleApi

    # 初始化 Kaggle API
    api = KaggleApi()
    api.authenticate()

    # 資料集 ID
    #dataset = "nadeemajeedch/fitness-tracker-dataset"
    dataset = "valakhorasani/gym-members-exercise-dataset"


    # 指定下載路徑
    raw_data_path = "/Users/jingting/Documents/GitHub/data_analysis_project/data/raw"
    os.makedirs(raw_data_path, exist_ok=True) # 若資料夾不存在就建立

    # 下載資料集並解壓到 data/raw/
    api.dataset_download_files(dataset, path=raw_data_path, unzip=True)

    # 找出 CSV 檔案
    csv_files = [f for f in os.listdir(raw_data_path) if f.endswith(".csv")]

    if csv_files:
        # 讀取第一個 CSV 檔案
        csv_path = os.path.join(raw_data_path, csv_files[0])
        df = pd.read_csv(csv_path, engine="python") # engine="python" 對於換行字元的容忍度更高
        return df
    else:
        print("找不到 CSV 檔案")