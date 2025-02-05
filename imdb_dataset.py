import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

#connection bd 
DB_USER = "dutinfopw201691"
DB_PASSWORD = "bygydasa"
DB_HOST = "database-etudiants.iut.univ-paris8.fr"
DB_PORT = "3306"
DB_NAME = "dutinfopw201691"

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Charger les données
query = "SELECT * FROM movies"
df = pd.read_sql(query, engine)


path = 'IMBD_movie_rating.csv'
#load data
df = pd.read_csv(path)

#nb de lignes
print(f'Nombres de lignes : {df.shape[0]}')
#nb colonnes
print(f'Nombres de colonnes : {df.shape[1]}')

#detection valaeur manquante
'''
print(df['Title'])
print(df['Gender'])
print(df['Runtime'])
print(df['Voters'])
print(df['User_rate'])
print(df['Review'])
'''
print('\n')
'''
print('title', df['Title'].isnull().sum())
print('Gender', df['Gender'].isnull().sum())
print('Runtime', df['Runtime'].isnull().sum())
print('Voters', df['Voters'].isnull().sum())
print('User_rate', df['User_rate'].isnull().sum())
print('Review', df['Review'].isnull().sum())
'''

colonnes_a_check = ['Title', 'Gender', 'Global_Rating','Runtime', 'Date', 'Voters', 'User_rate', 'Review']
#Nombre de valeurs manquantes par colonne
for col in colonnes_a_check:
    print(f'{col} missing values:', df[col].isnull().sum())

#doublons
print('\n')
for col in colonnes_a_check:
    print(f'{col} duplicated:', df[col].duplicated().sum())



#Quel est le genre de film le plus fréquent ?
print('\n')
count_genre = df['Gender'].value_counts()

print('Genre le plus fréquent: ', count_genre.idxmax())
print(count_genre)

#note_moyenne films par décennie
print('\n')

print(df['Date'])#Affiche les valeurs uniques de la colonne Date

print(df.columns)#Vérifie si 'Global_Rating' est bien dans la liste des colonnes
print("nombre de global_rating null : ", df['Global_Rating'].isnull().sum())  # Vérifie s'il y a des valeurs nulles


df['Date'] = df['Date'].str.extract(r'(\d{4})').astype(float)
df['Date'] = pd.to_numeric(df['Date'],errors = 'coerce')
df['Decennie'] = (df['Date'] // 10) * 10

print("nombre de date null : ", df['Date'].isnull().sum())#Affiche le nombre de valeurs nulles


note_moyenne_decennie = df.groupby('Decennie')['Global_Rating'].mean()
print('rating par decennie: ', note_moyenne_decennie)


df['Gender'] = df['Gender'].astype(str).str.strip()


top_genres = df['Gender'].value_counts().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette="magma")

#Ajouter les labels et le titre
plt.xlabel("Nombre de films", fontsize=12)
plt.ylabel("Genre", fontsize=12)
plt.title("Top 10 des genres de films les plus fréquents", fontsize=14, fontweight="bold")

#Afficher les valeurs sur les barres
for index, value in enumerate(top_genres.values):
    plt.text(value + 1, index, str(value), va="center", fontsize=10)

#Afficher le graphique
plt.show()

sns.set(style="darkgrid")



plt.figure(figsize=(8, 5))
sns.histplot(df['Global_Rating'], bins=20, kde=True, color='blue')
plt.xlabel("Note Globale")
plt.ylabel("Nombre de Films")
plt.title("Distribution des Notes Globales")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Runtime'], y=df['Global_Rating'], alpha=0.5, color='purple')
plt.xlabel("Durée du film (minutes)")
plt.ylabel("Note Globale")
plt.title("Relation entre la durée et la note globale")
plt.show()


