import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer  
#TfidfVectorizer #basic idea to take  the text 
#and convert it to something that can be feaded to ML model


# "TF matrix : tearm frequency" and "IDF matrix : Inverse document frequency"

from sklearn.svm import LinearSVC

data = pd.read_csv("fake_or_real_news.csv")

data 