# Movie Recommender

The Movie Recommender is a Python program that recommends the most similar movie based on a provided description. It uses the spaCy library for natural language processing to calculate the similarity between the description and a collection of movie lines.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation

1. Clone the repository:

```
git clone https://github.com/Alaa-Jaber-Data-scientist/finalCapstone.git
```

2. Navigate to the project directory:

```
cd movie-recommender
```

3. Install the required dependencies. Make sure you have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) installed, then run:

```
pip install -r requirements.txt
```

4. Prepare the movie lines file:

   - Create a text file containing movie lines.
   - Each line should follow the format: `movie_name: movie_description`.
   - Save the file as `movies.txt` in the project directory.

## Usage

1. Open the Python script file `watch_next.py` in a text editor.

2. Modify the `description` variable with the desired movie description.

3. Optionally, you can change the `movies_file` variable to point to a different movie lines file if needed.

4. Save the changes.

5. Run the script:

```
python watch_next.py
```

6. The program will display the most similar movie(s) based on the provided description. If no similar movie is found, it will show a corresponding message.

## Credits

This project was created by [Alaa Jaber](https://github.com/Alaa-Jaber-Data-scientist/) 
