movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def rating_imbd(movies, movie_name):
  for movie in movies:
      if movie['name'] == movie_name:
          return movie['imdb'] > 5.5
        
def rating_5(movies):
  sublist = []  
  for movie in movies:  
      if movie['imdb'] > 5.5:  
          sublist.append(movie['name'])  
  return sublist
    
def category(movies, category_name):
  category_movies = []
  for movie in movies:  
      if movie['category'] == category_name:  
          category_movies.append(movie['name'])
  return category_movies 

def average_rating(movies):
  total = 0
  for movie in movies:
    total += movie['imdb']
  return total / len(movies)

def average_rating_category(movies, category):
  total = 0
  count = 0
  for movie in movies:
    if movie['category'] == category:
      total += movie['imdb']
      count += 1
  return total / count

umovie = input("Enter a movie name: ")
print(rating_imbd(movies, umovie))
print(rating_5(movies))
print(category(movies, 'Romance'))
print(average_rating(movies))
print(average_rating_category(movies, 'Romance'))
