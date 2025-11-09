from src.load_data import load_data
from src.clean_data import clean_data

def main():
    import os

    print("開始資料下載...")
    df_raw = load_data()
    print(f"下載完成，筆數：{len(df_raw)}")

    print("開始資料清理...")
    df_clean = clean_data(df_raw)
    print("資料清理完成")

    print("儲存清理後資料...")
    # output_path = '/Users/jingting/Documents/GitHub/data_analysis_project/data/cleaned_data.csv'
    output_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "data/cleaned_data.csv")
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df_clean.to_csv(output_path, index=False)
    print(f"清理後資料已儲存：{output_path}")

if __name__ == "__main__":
    main()
