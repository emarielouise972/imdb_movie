import pandas as pd


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

print(df['Date'])  # Affiche les valeurs uniques de la colonne Date

print(df.columns)  # Vérifie si 'Global_Rating' est bien dans la liste des colonnes
print("nombre de global_rating null : ", df['Global_Rating'].isnull().sum())  # Vérifie s'il y a des valeurs nulles


df['Date'] = df['Date'].str.extract(r'(\d{4})').astype(float)
df['Date'] = pd.to_numeric(df['Date'],errors = 'coerce')
df['Decennie'] = (df['Date'] // 10) * 10

print("nombre de date null : ", df['Date'].isnull().sum())  # Affiche le nombre de valeurs nulles


note_moyenne_decennie = df.groupby('Decennie')['Global_Rating'].mean()
print('rating par decennie: ', note_moyenne_decennie)

