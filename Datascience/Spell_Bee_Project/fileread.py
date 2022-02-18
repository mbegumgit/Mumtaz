# Importing Libraries
import numpy as np
import pandas as pd
def read():
    # Read Bee_words data
    dataset = pd.read_csv('Spell_Bee_fileV1.csv')
    return dataset

def Pick_Word(df_level):
    
    df=read()
    
    
    df=df.loc[df['Difficulty Level'] == df_level]
     
    #randomly select n number of rows out of the total existing row numbers from the dataframe df without replacement.
    n=1
    df_pick=df.take(np.random.permutation(len(df))[:n])

    print('Random Word ',df_pick)
    random_word = df_pick.iloc[0][2]
    
    return random_word
