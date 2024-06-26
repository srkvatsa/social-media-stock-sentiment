# Evaluating Differences in Public Sentiment Surrounding the Nvidia Stock Across Politically-Divergent Social Media Platforms

The paper is entitled `paper.pdf`.

### Guide to Repository

- `data/`: Contains all Data Files
    - `demo_generations/`: All data files generated in this demo will automatically be placed here in order to prevent any effect on the original data files.
    - `raw/`: All raw scraped JSON files generated by the scrapers in the `scrapers/` directory.
    - `sentiments/`: Text data that has been split by sentiment (for topic modeling), as generated by by the sentiment analysis scripts in `data-processing/`. 
    - `text_extract/`: Text data that has been extracted from the JSON files using the respective scripts in the `data-processing/` directory
- `data-processing/`: Contains all scripts for processing the raw data files into text data. Also, contains scripts for sentiment analysis.
- `scrapers/`: Contains all scripts for scraping data from social media platforms.
- `topic-modeling/`: Contains all scripts for topic modeling.
- `visualizations/`: Contains visualizations that appear in the paper. 

### Guide to Running the Demo


All the scripts can be run without any changes to the code, provided the necessary libraries are installed.
The necessary libraries are specified in the `requirements.txt` file. 

PLEASE NOTE: For both topic model scripts, the Python interpreter must be on version 3.9. Even so, there may be errors with versions of libraries used in the script, as the `gensim` package is no longer being updated and is therefore causing dependency errors. 

Additionally, for `twitterscraper.py` to work, `twscrape` must be properly set up with account credentials. Instructions are linked in the file itself.

