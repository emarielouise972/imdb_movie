import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

#Connexion à la base de données
DB_USER = "dutinfopw201691"
DB_PASSWORD = "bygydasa"
DB_HOST = "database-etudiants.iut.univ-paris8.fr"
DB_PORT = "3306"
DB_NAME = "dutinfopw201691"

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


query = "SELECT * FROM movies"
df = pd.read_sql(query, engine)

plt.figure(figsize=(8,5))
sns.histplot(df['global_rating'], bins=20, kde=True, color='blue')
plt.xlabel("Note Globale")
plt.ylabel("Nombre de films")
plt.title("Répartition des notes des films")
plt.show()


plt.figure(figsize=(8,5))
sns.scatterplot(x=df['runtime'], y=df['global_rating'], alpha=0.6)
plt.xlabel("Durée du film (minutes)")
plt.ylabel("Note Globale")
plt.title("Corrélation entre la durée et la note")
plt.show()


query_genre = """
SELECT g.name, m.global_rating 
FROM movie_genres mg
JOIN genres g ON mg.id_genre = g.id
JOIN movies m ON mg.id_movie = m.id_movie
"""
df_genre = pd.read_sql(query_genre, engine)

plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel("Genre", fontsize=14)
plt.ylabel("Note Globale", fontsize=14)
plt.title("Répartition des notes par genre (trié par médiane)", fontsize=16)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
