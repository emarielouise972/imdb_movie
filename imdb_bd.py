import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Connexion à la base de données
DB_USER = "dutinfopw201691"
DB_PASSWORD = "bygydasa"
DB_HOST = "database-etudiants.iut.univ-paris8.fr"
DB_PORT = "3306"
DB_NAME = "dutinfopw201691"

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

#Charger les données des films
query = "SELECT * FROM movies"
df = pd.read_sql(query, engine)

#Relation entre le nombre de votes et la note globale
plt.figure(figsize=(8,5))
sns.scatterplot(x=df['voters'], y=df['global_rating'], alpha=0.6)
plt.xscale("log")
plt.xlabel("Nombre de Votes (échelle log)")
plt.ylabel("Note Globale")
plt.title("Relation entre le nombre de votes et la note globale")
plt.show()

#Évolution de la note moyenne par année
query = """
SELECT release_year, AVG(global_rating) AS avg_rating 
FROM movies 
GROUP BY release_year 
ORDER BY release_year ASC
"""
df_years = pd.read_sql(query, engine)

plt.figure(figsize=(10, 5))
sns.lineplot(x=df_years["release_year"], y=df_years["avg_rating"], marker="o", color="b")
plt.xlabel("Année de sortie")
plt.ylabel("Note Moyenne")
plt.title("Évolution de la note moyenne des films par année")
plt.show()

#Comparaison des notes selon la durée du film (court/moyen/long)
df["length_category"] = pd.cut(df["runtime"], bins=[0, 90, 150, 300], labels=["Court (<90 min)", "Moyen (90-150 min)", "Long (>150 min)"])

plt.figure(figsize=(8,5))
sns.boxplot(x="length_category", y="global_rating", data=df, palette="coolwarm")
plt.xlabel("Catégorie de Durée")
plt.ylabel("Note Globale")
plt.title("Comparaison des notes entre films courts, moyens et longs")
plt.show()



#Répartition des films bien notés par genre
query_genre_classification = """
SELECT g.name, 
    COUNT(CASE WHEN m.global_rating >= 8 THEN 1 END) AS films_bien_notes,
    COUNT(CASE WHEN m.global_rating < 5 THEN 1 END) AS films_mal_notes
FROM movie_genres mg
JOIN genres g ON mg.id_genre = g.id
JOIN movies m ON mg.id_movie = m.id_movie
GROUP BY g.name
"""
df_genre_class = pd.read_sql(query_genre_classification, engine)

plt.figure(figsize=(12,6))
df_genre_class.set_index("name").plot(kind="bar", stacked=True, figsize=(12,6), colormap="coolwarm")
plt.xlabel("Genre")
plt.ylabel("Nombre de Films")
plt.title("Nombre de films bien notés vs mal notés par genre")
plt.legend(["Films bien notés (≥8)", "Films mal notés (<5)"])
plt.xticks(rotation=90)
plt.show()
