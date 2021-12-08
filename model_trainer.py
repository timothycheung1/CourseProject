import pandas as pd
import nltk
import string
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def main():
    training_data = pd.read_csv('data.csv', index_col=0).to_dict()
    while(True):
        print("Input review or type \"EXIT\" to quit")
        with open('test.txt') as f:
            to_predict = f.read()
        to_predict = str(input())
        if to_predict == "EXIT":
            break
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(to_predict)
        print("Input rating:")
        rating_input = int(input())
        rating = '0'
        if rating_input == 1:
            rating = '1'
        elif rating_input == 2:
            rating = '2'
        elif rating_input == 3:
            rating = '3'
        elif rating_input == 4:
            rating = '4'
        elif rating_input == 5:
            rating = '5'
        else:
            print("Invalid rating")
            continue

        for word in word_tokens:
            word = word.lower()
            if word not in stop_words and word not in string.punctuation:
                if word not in training_data['1']:
                    training_data['1'][word] = 0
                    training_data['2'][word] = 0
                    training_data['3'][word] = 0
                    training_data['4'][word] = 0
                    training_data['5'][word] = 0
                training_data[rating][word] = training_data[rating][word] + 1

    df = pd.DataFrame.from_dict(training_data)
    df.to_csv(r'data.csv')

if __name__ == "__main__":
    main()