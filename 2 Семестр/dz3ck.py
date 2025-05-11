import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import cdist

# Создаём датафрейм на основе таблицы из задания
data = {
    "Вид пингвина": ["Adelie", "Adelie", "Adelie", "Chinstrap", "Chinstrap", "Chinstrap", "Gentoo", "Gentoo", "Gentoo"],
    "Остров": ["Torgersen", "Torgersen", "Torgersen", "Dream", "Dream", "Dream", "Biscoe", "Biscoe", "Biscoe"],
    "Длина ласт, мм": [186, 193, 186, 195, 194, 193, 215, 210, 216],
    "Масса тела, г": [3800, 3400, 3300, 4400, 3600, 3800, 5000, 5050, 4100],
    "Пол": ["FEMALE", "FEMALE", np.nan, "MALE", "MALE", "MALE", "MALE", "FEMALE", np.nan]
}
df = pd.DataFrame(data)

# Шаг 1: Кодирование признаков "Вид пингвина" и "Остров"
df['Вид пингвина'] = df['Вид пингвина'].map({"Adelie": 0, "Chinstrap": 1, "Gentoo": 2})
df['Остров'] = df['Остров'].map({"Biscoe": 0, "Dream": 1, "Torgersen": 2})

# Шаг 2: Нормализация признаков "Длина ласт" и "Масса тела" с помощью MinMax
scaler = MinMaxScaler()
df[['Длина ласт, мм', 'Масса тела, г']] = scaler.fit_transform(df[['Длина ласт, мм', 'Масса тела, г']])
df[['Длина ласт, мм', 'Масса тела, г']] = df[['Длина ласт, мм', 'Масса тела, г']].round(1)

# Шаг 3: Заполнение пропущенных значений в столбце "Пол"
# Создаем маску для строк с пропущенными значениями в столбце "Пол"
mask_nan = df['Пол'].isna()

# Находим евклидово расстояние для пингвинов с пропущенными значениями
for index in df[mask_nan].index:
    # Извлекаем строку с пропуском
    penguin_with_nan = df.loc[index, ['Длина ласт, мм', 'Масса тела, г']].values.reshape(1, -1)
    
    # Извлекаем строки без пропусков
    df_no_nan = df[~mask_nan]
    penguins_no_nan = df_no_nan[['Длина ласт, мм', 'Масса тела, г']].values
    
    # Рассчитываем расстояния и находим ближайшего пингвина
    distances = cdist(penguin_with_nan, penguins_no_nan, metric='euclidean')
    nearest_index = distances.argmin()
    
    # Заполняем пропуск значением пола ближайшего пингвина
    df.at[index, 'Пол'] = df_no_nan.iloc[nearest_index]['Пол']

# Шаг 4: Кодирование признака "Пол"
df['Пол'] = df['Пол'].map({"FEMALE": 0, "MALE": 1})

# Выводим финальный результат
print(df)