# Song Artist Predictor
*Predicting which artist sang lyrics based on their back catalogue*

## Design and Implementation
The project was split into three parts:
1. Data acquisition (scrape.ipynb) by scraping lyrics.com and parsing with BeautifulSoup. For this iteration, I chose David Bowie and Tina Turner.
2. Modeling with CountVectorizer and TfidtTransformer (model.ipynb). Three models were assessed for accuracy and the one with the best train and test accuracy (Naive Bayes) was pickled ().
3. Prediction (predictor_bayes.py) is a simple script that allows test data input and returns the prediction (which artist sang it) and probability.

## Next
- This was built step by step and only two artists chosen for it, if I were to expand upon it, the first thing would be replacing the code in scrape.ipynb with a function.
- Building a more complex/compound model, e.g. with voting classification, would be interesting to try to tweak it for accuracy.
- It would be quite fun to do something similar to build an author predictor/proofer, to check if text were likely written by e.g. Shakespeare or attributable to Homer or not.