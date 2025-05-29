import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Завантаження та очищення даних
df = pd.read_csv("car_price.csv")

# Очищення колонок і перетворення типів
df['Price (in USD)'] = pd.to_numeric(df['Price (in USD)'].str.replace(r'[\$]', '', regex=True), errors='coerce')
df['Horsepower'] = pd.to_numeric(df['Horsepower'].str.extract('(\d+)')[0], errors='coerce')
df['Torque (lb-ft)'] = pd.to_numeric(df['Torque (lb-ft)'].str.extract('(\d+)')[0], errors='coerce')
df['Engine Size (L)'] = pd.to_numeric(df['Engine Size (L)'].str.replace('L', '', regex=False), errors='coerce')

# Видалення пропусків, дублікатів, нереальних значень
df = df.dropna().drop_duplicates()
df = df[(df['Price (in USD)'] > 1000) & (df['Year'] <= 2025)]

# Середня ціна по бренду
brand_avg = df.groupby("Car Make")["Price (in USD)"].mean().sort_values(ascending=False)

# Візуалізації
sns.histplot(df['Price (in USD)'], kde=True)
plt.title("Розподіл цін на авто")
plt.xlabel("Ціна (USD)")
plt.ylabel("Кількість")
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=brand_avg.values, y=brand_avg.index)
plt.title("Середня ціна за брендом")
plt.xlabel("Ціна (USD)")
plt.ylabel("Бренд")
plt.show()

sns.scatterplot(x='Year', y='Price (in USD)', data=df)
plt.title("Залежність ціни від року випуску")
plt.xlabel("Рік")
plt.ylabel("Ціна (USD)")
plt.show()

# Статистика
print("Середня ціна:", round(df['Price (in USD)'].mean(), 2))
print("Медіана:", df['Price (in USD)'].median())
print("Мода:", df['Price (in USD)'].mode()[0])