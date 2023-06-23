# Movie Suggestions
# By Ahmed AlAdl

# Import libraries
import spacy
import numpy as np

# Load the medium pre-trianed NLP data model
nlp = spacy.load('en_core_web_md')

# Funtion to check for similarity between the discription and the movies list
def get_most_similar_movie(description):
    
  # Create a document from the description.
  doc = nlp(description)

  # Calculate the similarity between the document and each movie description.
  similarities = []
  for movie in movies:
    movie_doc = nlp(movie)
    similarities.append(doc.similarity(movie_doc))

  # Find the movie with the highest similarity.
  max_index = np.argmax(similarities)

  # Return the title of the movie.
  return movies[max_index]


# Reading the movies file and displaying the list
f_movies = open('movies.txt', 'r')
while True:
  line = f_movies.readline()
  if not line:
    break
  print("Movies List: " + line)
  print(line)

# Read the movies.txt file.
with open('movies.txt') as f_movies:
 movies = f_movies.readlines()

# Get the most similar movie to the description of Planet Hulk.
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."""
most_similar_movie = get_most_similar_movie(description)

# Print the title of the most similar movie.
print ("The movie with the most similar title")
print(most_similar_movie)