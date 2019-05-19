import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def recommendations(id):
    df = pd.read_csv('post_data.csv')

    df = df[['id','title', 'tags']]

    count = CountVectorizer()
    count_matrix = count.fit_transform(df['tags'])

    indices = pd.Series(df.id)

    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    
    recommended_article = []
    print(indices[indices == id])
    idx = indices[indices == id].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    top_3_indexes = list(score_series.iloc[1:5].index)
    for i in top_3_indexes:
        
        recommended_article.append(list(df.id)[i])
        
    return recommended_article
