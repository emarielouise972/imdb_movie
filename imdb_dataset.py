import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#path = kagglehub.dataset_download("youssefamdouni/imbd-movie-rating")
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


df['Date'] = pd.to_numeric(df['Date'],errors = 'coerce')
df['Decennie'] = (df['Date'] // 10) * 10

note_moyenne_decennie = df.groupby('Decennie')['Global_Rating'].mean()
print('rating par decennie: ', note_moyenne_decennie)

sns.set(style="darkgrid")

plt.figure(figsize=(10, 5))
sns.countplot(y=df['Gender'], palette="viridis", order=df['Gender'].value_counts().index)
plt.xlabel("Nombre de films")
plt.ylabel("Genre")
plt.title("Répartition des genres de films")
plt.show()


plt.figure(figsize=(8, 5))
sns.histplot(df['Global_Rating'], bins=20, kde=True, color='blue')
plt.xlabel("Note Globale")
plt.ylabel("Nombre de Films")
plt.title("Distribution des Notes Globales")
plt.show()


plt.figure(figsize=(10, 5))
sns.countplot(x=df['Decennie'].dropna(), palette="coolwarm", order=sorted(df['Decennie'].dropna().unique()))
plt.xlabel("Décennie de sortie")
plt.ylabel("Nombre de films")
plt.title("Nombre de films par décennie")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Runtime'], y=df['Global_Rating'], alpha=0.5, color='purple')
plt.xlabel("Durée du film (minutes)")
plt.ylabel("Note Globale")
plt.title("Relation entre la durée et la note globale")
plt.show()


plt.figure(figsize=(10, 5))
sns.countplot(y=df['Review'], palette="viridis", order=df['Gender'].value_counts().index)
plt.xlabel("Nombre de films")
plt.ylabel("Genre")
plt.title("Répartition des genres de films")
plt.show()