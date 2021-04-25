from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyser = SentimentIntensityAnalyzer()

# 関数例
def sentiment_analyzer_scores(sentence):
    analysis = TextBlob(sentence)
    text = analysis.translate(to='en')
    score = analyser.polarity_scores(text)
    print(text, "\n", str(score))
    return score 


if __name__ == '__main__':
    sentiment_analyzer_scores("今日はいい天気だ.")
