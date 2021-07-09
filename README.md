# Is it a Rumour
In this project I have created a model to classify the tweets as Rumour or Non Rumour. Further more the model was used to classify tweets based around Covid-19.The project has been done as a part of Natural Language Processing(NLP) Course at University of Melbourne.  
### Dataset
The dataset was divided into three portions-train,development and test set.In each of the set the the data was in the form of list of tweet objects in each line .The first tweet in each line is the target tweet followed by the tweets that follow it in the thread.  Labels for the target tweet were available for the train and development set.  
### Feature Tecniques explored
In this project the following techniques to generate a representation of tweets and their replies have been explored:  
-GLoVe.  
-Sentence Transformers.  
-BERTweet. 
### ML TECHNIQUES explored
In this project the following ML techniques have been explored:  
-Random Forest.  
-LightGBM.  
-LSTM.  
-BERT with softmax. 
### Results
It was found that the BERTweet with a softmax layer with a modified input architecture(please refer to the project report for the implementation details) performs the best and achieves an F1 score of 0.835 and a rank of 55 out 345 on the online platform hosting the intra class competition.


For details of the implementation details and the models please refer to the project report:Project_Report.pdf. 



