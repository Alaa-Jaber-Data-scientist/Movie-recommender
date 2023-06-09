import spacy
nlp = spacy.load('en_core_web_md')

def recommend(description, movies_file):
    """
    Recommends the most similar movie based on a provided description.

    Args:
        description (str): The description of a movie.
        movies_file (str): The path to the file containing movie lines.

    Returns:
        str: The most similar movie based on the description.
            Returns "No similar movie found." if no similar movie is found.
    """

    # Tokenize the description using spaCy.
    description = nlp(description)

    # Read the movie lines from the file.
    with open(movies_file, 'r') as file:
        movie_lines = file.readlines()

    # List to hold similarity scores for each movie line.
    similarity_scores = []

    # List to hold movie names and their similarity scores.
    movie_list = []

    # Calculate similarity between the description and each movie line.
    for line in movie_lines:
        line = nlp(line)

        # Split the line into movie name and description.
        line_text = line.text.split(":")
        movie_name = line_text[0]
        
        # Calculate similarity between the provided description and the current movie line.
        similarity = line.similarity(description)
        similarity_scores.append(similarity)
        
        # Create a list of the movie name and its similarity with the description.
        movie_similarity = [movie_name, similarity] 
        movie_list.append(movie_similarity)

    # Find the highest similarity score.
    highest_similarity = max(similarity_scores)
    recommended_movies = []

    # Retrieve movies with the highest similarity score.
    for entry in movie_list:
        if entry[1] == highest_similarity:
            recommended_movies.append(entry[0])

    if recommended_movies:
        return f"The most similar movie(s) is/are: {', '.join(recommended_movies)}"
    else:
        return "No similar movie found."


# Example description and movies file path.
description = """Will he save their world or destroy it? When the Hulk becomes 
too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""
movies_file = "movies.txt"  

# Call the recommend function and print the result.
result = recommend(description, movies_file)
print(result)