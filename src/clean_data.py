def clean_data(df):
    '''
    填補 dataframe 缺失值
    '''
    import pandas as pd

    ## 填補 float 缺失值

    # 先把 “Max_BPM” 轉 float
    df['Max_BPM'] = pd.to_numeric(df['Max_BPM'], errors='coerce')
    
    # 將 dtype='int' 轉 'float64'
    int_cols = df.select_dtypes(include=['int']).columns
    df[int_cols] = df[int_cols].astype(float)

    # 找到所有dtype='float64'的column
    numeric_cols = df.select_dtypes(include=['float64']).columns
    # 用「平均數」填補缺失值
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean()).round(2)


    ## 填補 object 缺失值

    # 找出欄位'Gender'中最常出現的值
    new_Gender = df['Gender'].mode()[0]
    # 找出欄位'Workout_Type'中最常出現的值
    new_Workout_Type = df['Workout_Type'].mode()[0]
    # 用「眾數」填補缺失值
    df['Gender'] = df['Gender'].fillna(new_Gender)
    df['Workout_Type'] = df['Workout_Type'].fillna(new_Workout_Type)

    df['Workout_Type'] = df['Workout_Type'].str.replace('\\n', '').str.replace('\\t', '')

    # 只保留合法值
    # valid_types = ["Strength", "Cardio", "Yoga", "HIIT"]
    # df = df[df['Workout_Type'].isin(valid_types)].reset_index(drop=True)


    return df


