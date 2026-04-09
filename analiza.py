import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Wczytanie danych (upewnij się, że plik jest w tym samym folderze)
df = pd.read_csv('tmdb_5000_movies.csv')

# 2. Czyszczenie danych
# Usuwamy filmy, które mają budżet lub przychód równy 0 (błędne dane)
df_clean = df[(df['budget'] > 0) & (df['revenue'] > 0)].copy()

# 3. Tworzenie wykresu 1: Budżet vs Przychód
plt.figure(figsize=(10, 6))
sns.regplot(data=df_clean, x='budget', y='revenue', 
            scatter_kws={'alpha':0.3, 'color':'blue'}, 
            line_kws={'color':'red'})
plt.title('Korelacja między budżetem a przychodem filmu')
plt.xlabel('Budżet (USD)')
plt.ylabel('Przychód (USD)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('wykres_korelacji.png')
plt.show()

# 4. Statystyki do raportu
print(f"Liczba przeanalizowanych filmów: {len(df_clean)}")
print(f"Korelacja Pearsona: {df_clean['budget'].corr(df_clean['revenue']):.2f}")
