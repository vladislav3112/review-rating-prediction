## Yepl reviews prediction
### **Dataset**: [yelp reviews](https://www.kaggle.com/datasets/yacharki/yelp-reviews-for-sa-finegrained-5-classes-csv)  
### About dataset: 
  * Data Fields:

    - 'text': The review texts are escaped using double quotes ("), and any internal double quote is escaped by 2 double quotes (""). New lines are escaped by a backslash followed with an "n" character, that is "\n".
    - 'class_index': Corresponds to the score associated with the review (between 1 and 5)
  * Data Splits

    - The Yelp reviews full star dataset is constructed by randomly taking 130,000 training samples and 50,000 testing samples for each review star from 1 to 5. In total there are 650,000 trainig samples and 650,000 testing samples.
### Best result: DeBERTa, 0.64 accuracy