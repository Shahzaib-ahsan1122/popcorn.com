from flask import Flask,  request, jsonify
from flask_cors import CORS 
from imdb import IMDb
from justwatch import JustWatch
import pandas as pd

app  = Flask(__name__)
CORS(app)
#load and reprocess imdb data
def load_imdb_data():
    titles = pd.read_csv('title.basics.tsv',sep ='\t', na_values = '\\N')
    ratings = pd.read_csv('title.ratings.tsv',sep='\t', na = '\\N')

# merge an dfilteirng the movies
    movies = titles.merge(ratings,on ='tconst' )
    movies = movies[movies['titleType']== 'movie']
    movies = movies [['primaryTitle','startYear','genres','averageRating']]
    return movies[['tconst','primaryTitle','startYear','genres','averageRating']]
    
#load  once at startup
IMDb_movies = load_imdb_data()
# search route
@app.route('/search')


def search():
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Missing the title parameter"}),400
    
    imdb_results = IMDb_movies[IMDb_movies['primaryTitle'].str.contains(title, case = False, na =False)]
    if imdb_results.empty:
        return jsonify({"error": "Movie not found "}),404
IMDb_data = imdb_results.iloc[0].to_dict()

try:
    JustWatch_data = fetch_Justwatch_data(IMDb_data['primaryTitle'])

    streaming_info = Justwatch_data.get('items',[])
    except Exception as e:
        streaming_info = []
        print(f"Justwatch error:{e}")

merged = {
    "Title": IMDb_data['primaryTitle'],
    "year": IMDb_data['startYear'],
    "genres": IMDb_data['genres'],
    "rating":IMDb_data['averageRating'],
    "streaming": streaming_info
}
    return jsonify(merged) 



def fetch_Justwatch_data(title):
    justwatch = Justwatch(country ='GB')
    results = JustWatch.search_for_item(query = title)
    return results

    


    #reccomendation route

app.route('/reccommend')
def reccommend ():
    mood = request.args.get('mood')
    platform = request.args.get('paltform')
    genere_map = {
        'Funny':'Comedy',
        'Thrilling':'Thriller',
        'dark':'Horror',
        'uplifting':'romance',
        'thoughtful':'Drama',
        'intense':'Action',
    }
    genre = genere_map.get(mood.lower()) if mood else None
    if genre:
        filtered = IMDb_movies[IMDb_movies['genres'].str.contains(genre, na =False)]
        return jsonify(filtered.head(10).to_dict(orient = 'records'))
    else:
        return jsonify({"error": "Mood not recognized"}),400
if __name__ == 'main':
    app.run(debug=True)
    