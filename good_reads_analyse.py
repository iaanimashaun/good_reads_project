import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('data/analyse_this.csv')

def my_best_book(author):
    autors_books = df[df['author']== author]
    rating = autors_books.loc[autors_books['norm_max_min'].idxmax()]
    return rating.title

my_best_book('Jane Austen')
