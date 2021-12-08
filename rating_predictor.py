import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def main():
    print("Welcome to Interactive Yelp Predictor")
    print("Preparing....")
    nltk.download('stopwords')
    nltk.download('punkt')

    print("Training model....")
    training_data = pd.read_csv('data.csv', index_col=0).to_dict()

    while(True):
        print("Type \'n\' to create a new prediction")
        print("Type \'q\' to quit")
        command = str(input())
        if command == "n":
            print("Input review to predict")
            to_predict = str(input())
            predict(to_predict, training_data)
        elif command == "q":
            break
        else:
            print("Invalid command")

def predict(to_predict, training_data):
    print("Predicting....")
    
    stop_words = set(stopwords.words('english'))
    
    word_tokens = word_tokenize(to_predict)
    score_1 = 0
    score_2 = 0
    score_3 = 0
    score_4 = 0
    score_5 = 0

    for word in word_tokens:
        if word not in stop_words:
            if word in training_data['1']:
                score_1 += training_data['1'][word]
                score_2 += training_data['2'][word]
                score_3 += training_data['3'][word]
                score_4 += training_data['4'][word]
                score_5 += training_data['5'][word]
    
    max_score = max(score_1, score_2, score_3, score_4, score_5)
    
    if max_score == score_1:
        print("Rating prediction: 1")
    elif max_score == score_2:
        print("Rating prediction: 2")
    elif max_score == score_3:
        print("Rating prediction: 3")
    elif max_score == score_4:
        print("Rating prediction: 4")
    elif max_score == score_5:
        print("Rating prediction: 5")

if __name__ == "__main__":
    main()