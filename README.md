# 🏋️‍♂️ Fitness Behavior & Training Efficiency Analysis  
Exploratory Data Analysis (EDA) | Cardio, Intensity, Calories | 973 Individuals

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.5+-yellowgreen)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-orange)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 📑 Table of Contents
- [📘 1. Project Overview](#-project-overview)
- [📦 2. Dataset Info](#-dataset-info)
- [🎯 3. Project Objective](#-project-objective)
- [🧹 4. Data Cleaning Summary](#-eda-highlights)
- [🗂 5. Project Structure](#-key-insights)
- [📈 6. Key Visuals & Insights](#-project-structure)
- [🔍 7. Major Findings（整合洞察）](#️-environment-setup)
- [⚙️ 8. Environment Setup](#-how-to-run)

---

# 📘 1. Project Overview

本專案分析 **973 筆個人運動紀錄**，內容包含心率、運動時長、卡路里消耗、BMI、體脂等健身行為指標。  
透過資料清理、視覺化與解讀，探討：

- 不同運動類型運動效率
- 年齡、性別是否影響訓練結果  
- 心率強度、運動時長是否影響卡路里消耗  
- 怎麼做才能達到最好的燃脂效率

本專案著重 **Storytelling Data Analysis**，不包含模型訓練。

---

# 📦 2. Dataset Description

> 本資料為 *Fitness Tracker Dataset*，包含身體指標、運動習慣、心率行為等資訊。  
> 數據為合成資料，專為教育、分析教學所設計，不代表真實個體。

資料特色：

- 973 筆紀錄、15 個欄位  
- 運動類型（HIIT、Yoga、Strength、Cardio）  
- 心率數據（Max/Avg/Resting BPM）  
- 週運動天數、時長、卡路里  
- BMI / 體脂率  

---

# 🎯 3. Analysis Objective

本專案回答五個核心問題：

### 1 哪種運動最能燃脂？  
（從「卡路里 / 訓練時長 / 心率」多面向比較）

### 2 年齡與性別是否會影響訓練效率？  
（20–30 vs 31–45 vs 46–59，每個族群差異）

### 3 高心率＝高效率？  
（心率與卡路里消耗的關係）

### 4 持續越久＝ 燃脂越多？  
（運動時長與卡路里消耗的關係）

### 5 是否能找出「效率低落」的運動族群？  
（心率高但卡路里低 → 訓練方式不佳）

---

# 🧹 4. Data Cleaning Summary

完成以下清理：

- 缺失值補齊（float → 平均值 / int → 平均值 / object → 眾數）
- 移除雜訊字元（如 \t, \n）
- 產出乾淨資料 `cleaned_data.csv`
- 建立衍生欄位：
  - ** Calories_per_hour (%) = Calories_Burned / Session_Duration × 100 **
  - ** Calories_per_heartbeat (%) = Calories_Burned / Avg_BPM × 100 **

---

# 🗂 5. Project Structure
data_analysis_project
├── data
│   ├── cleaned_data.csv
│   └── raw
│       └── gym_members_exercise_tracking.csv
├── main.py
├── notebooks
│   ├── clean_data.ipynb
│   ├── report.ipynb
│   └── visualization.ipynb
├── src
│   ├── clean_data.py
│   ├── load_data.py
│   └── visualization.py
├── README.md
└── requirements.txt

---

# 📈 6. Key Visuals & Insights

## **6.1 卡路里 vs 平均心率（全體 + 分類）**
📌 *摘要：綜合比較各運動類型 心率影響卡路里消耗*  

**洞察：**

- 20–30 歲族群平均強度最高，表示能承受更高負荷  
- HIIT / Strength 心率提升更能拉高卡路里
- Cardio / Yoga 心率提高效果有限

---

## **6.2 卡路里 vs 運動時長（全體 + 分類）**
📌 *摘要：綜合比較各運動類型 運動時長影響卡路里消耗*  

**洞察：**

- 男性在 Strength、HIIT 中消耗較高  
- 女性在 Yoga、Cardio 中表現更穩定  
- HIIT 在兩性中皆呈現最高變異度 → 技術門檻高  
- HIIT 時長再拉長效率反而下降（疲勞效應）

---

## **6.3 Gender × Age_Group × 心率效率 **
📌 *摘要：綜合比較各性別年齡層 不同運動之運動效率(心率)*  

**洞察：**

- HIIT：最高心率、最高熱量，但變異度大 → 年輕族群效果最好
- Strength：中強度但平均卡路里不低 → 效率佳  
- Yoga：卡路里效率最低，顯示其能量輸出本質較低 
- Cardio：雖低效率，但穩定性高、能長時間維持

---

## **6.4 Gender × Age_Group × 時間效率 **
📌 *摘要：綜合比較各性別年齡層 不同運動之運動效率(運動時長)*  

**洞察：**

- 女性整體單位時間能量消耗略低於男性
- 年齡增加後，HIIT 與 Strength 的效率下降最明顯
- Strength 在青年組的單位時間能量消耗最高
- Cardio 在所有年齡層中的效率最穩定

---

# 🔍 7. Major Findings（整合洞察）

### 🟦 1. 年齡 × 運動類型
1. 青少年與壯年族群在 HIIT 的每心跳卡路里最高，顯示高強度訓練對年輕族群最有效。
2. 年齡增加後，HIIT 與 Strength 的效率下降最明顯，反映肌肉量、代謝率與心肺功能的自然衰退。

### 🟩 2. 性別差異
3. 女性整體單位時間能量消耗略低於男性，多與肌肉量、基礎代謝率及訓練強度選擇有關。
4. 男性在相同心率效率下，Yoga 的能量輸出最低；女性則是 Cardio 最低。

### 🟧 3. 運動類型特性
5. Yoga 在所有運動中每心跳卡路里最低，屬低負荷、低變異運動（穩定但效率低）。
6. Cardio 在各年齡層效率最穩定，是最適合長期維持且受年齡退化影響最小的類型。
7. Strength 在青年組的能量消耗最高，反映此階段的肌力與能量輸出最佳。

### 🟥 4. 整體效率觀察
8. 部分族群出現「高心率但低卡路里」的現象 → 可能訓練技術不佳或姿勢效率低。
9. 心率強度（Intensity %）與卡路里呈現明顯正相關，是解讀訓練效率的重要指標。

---

# 🚀 8. How to Run 

## **Step 1：下載 Raw Dataset**

本專案內建 Kaggle API，可自動下載資料：

```bash
python src/main.py

功能包含：
- 自動下載最新 Kaggle 資料
- 執行清理流程
- 產生 cleaned_data.csv
- 回傳 DataFrame

## **Step 2：執行 EDA Notebook**

```bash
jupyter notebook notebooks/visualization.ipynb

功能包含：
- 
- 執行清理流程
- 產生 cleaned_data.csv
- 回傳 DataFrame

## 📦 安裝套件

```bash
pip install -r requirements.txt
