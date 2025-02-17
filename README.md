# BT5153_Applied_Machine_Learning_Group18

Head off Toxic comments in social media

## Getting Started

These README will give you an idea on what each code documents is and what commands you need to run

### Prerequisites

* Python 3.x
* Tensorflow 2.2.0-rc3

### Datasets 

1. Toxic_comment.csv - Main dataset for this project, **We removed the id column due to github file size limitation**. It is the training data for Toxic Comment Classification Challenge in Kaggle Competition (https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data)

2. Scrape data - It contains the ten raw csv file, we get from scraping historical tweets between 01 April 2020 to 10 April 2020 that were discussing the topic of ‘coronavirus’, with GetOldTweets3 python package.

3. data_augmentation_cn.csv - It contains the text after the original tweets being translated to **chinese** then back to engish

4. data_augmentation_fr.csv - It contains the text after the original tweets being translated to **French** then back to engish 

### Code Documents

1. Tweets_scraping.py - To scrape old tweets
2. EDA_Kaggle_Dataset.ipynb - Exploratory data analysis on the Toxic_comment dataset
3. LDA_Kaggle_Dataset.ipynb - Topic Modeling on the Toxic_comment dataset
4. LDA_Scraped_Dataset.ipynb - Topic Modeling on the combined scrap dataset
5. Data_Augmentation.ipynb - Data Augmentation on the non_toxic text in Toxic_comment dataset
6. Model_Feature_Engineering&Selection - Perform feature engineering followed by feature selection using Burota
6. Model_Preprocessing - Text pre-processing to clean input texts
7. Model_Classic_Models - Train four classic machine learning models as baseline models
8. Model_RNN - Train an RNN model (bidirectional LSTM + GRU)
9. Model_BERT - Leverage pre-train bert base model and fine-tune

### Python Dashboard

1. Dashboard.py - The main file and entry point to our dashboard
2. count_vect.pickel - The training data in vectorized form 
3. logreg_identity_hate_model.pkl 	- The trained logregression model for identity_hate category
4. logreg_insult_model.pkl - The trained logregression model for insult category
5. logreg_obscene_model.pkl - The trained logregression model for obscene category
6. logreg_severe_toxic_model.pkl - The trained logregression model for severe category
7. logreg_threat_model.pkl - The trained logregression model for threat category
7. logreg_toxic_model.pkl - The trained logregression model for toxic category
