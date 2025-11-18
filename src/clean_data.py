def clean_data(df):
    '''
    填補 dataframe 缺失值
    '''
    import pandas as pd

    ## 填補 float 缺失值

    # 找到所有dtype='float64'的column
    float_cols = df.select_dtypes(include=['float64']).columns
    # 用「平均數」填補缺失值
    df[float_cols] = df[float_cols].fillna(df[float_cols].mean()).round(2)

    ## 填補 int 缺失值

    # 找到所有dtype='int64'的column
    int_cols = df.select_dtypes(include=['int64']).columns
    # 用「平均數」填補缺失值
    df[int_cols] = df[int_cols].fillna(df[int_cols].mean())

    ## 填補 object 缺失值

    # 找出欄位'Gender'中最常出現的值
    new_Gender = df['Gender'].mode()[0]
    # 找出欄位'Workout_Type'中最常出現的值
    new_Workout_Type = df['Workout_Type'].mode()[0]
    # 用「眾數」填補缺失值
    df['Gender'] = df['Gender'].fillna(new_Gender)
    df['Workout_Type'] = df['Workout_Type'].fillna(new_Workout_Type)
    # 去除特殊符號
    df['Workout_Type'] = df['Workout_Type'].str.replace('\\n', '').str.replace('\\t', '')


    return df


