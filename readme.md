# UROP 1100
---
## Week 1 (17/3 - 24/3)

### **To-Do:**
1. News Topic Classification

2. Deploy ML Model on cloud

### **Datasets:**

|                                 |                                                               |
|---------------------------------|---------------------------------------------------------------|
| *News_Category_Dataset_v2.json* | kaggle dataset which contains over 200k data with 41 categories                 |
| *AG_NEWS*                       | pytorch dataset which contains 120k train data with 4 classes |
| *20newsgroups*                  | sklearn dataset which contains 19k data with 20 classes       |


### **Tested Models:**
- TFIDF with sklearn models (SVM, Ridge Regression, Logistic Regression, CNB)
- **goals:** 
    * high accuracy with short testing time
- **results:** 
    * SVM, ridge regression and logistic regression shows the best results with low test time
    * for the whole text: ~0.9 accuracy
    * for the headline: ~0.6 accuracy
- **limitations:** 
    * without hyperparameters tuning
    * without preprocessing text
- **ongoing:** 
    * sentence transformer (pretrained word embeddings) + MLP/CNN/LSTM 

### **Amazon Sagemaker**
- looked into Amazon Sagemaker
- tried to use notebook instance and s3 buckets
- **in-built algorithms:**
    * [blazing text](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) 

### **Next week plan**
1. Continue to try pytorch sentence transformer + MLP/CNN/LSTM
2. Look into training and deploying models in Sagemaker
3. Try Amazon in-built algorithms

### **Questions**
1. Should the input of the topic classification be the headline or the whole text?
2. Do you prefer more traditional sklearn-type models or the state-of-the-art nn models? 
3. When should I move on to the next part?

---

## Week 2 (24/3 - 31/3)

### **To-Do:**
1. Finish Topic Classification


### **Tested Models:**
- **BlazingText Algo from Sagemaker**
    * training
    * deployment
- **Results:** 
    * validation score: 0.67 after 20 epoches
- **Improvements to be made:** 
    * current dimension of the embedding layer = 10, could set higher to get a more accurate result
    * merge 41 categories to a smaller number of categories
    * looking at the top k results?
- **Target**
    * 0.85 or above


### **Next week plan**
1. Improvements to the blazingtext algorithm
2. Distinguish the categories that are needed to be de-polarize
3. Looking into finding the polarity of the news article
4. Estimate the cost of SageMaker
5. Compute testing time


### **Questions**
1. Billing of AWS?
2. Suggestions on finding the polarity?

---

## Week 3 (31/3 - 7/4)

### **To-Do:**
1. Improvements on Topic Classification
2. Estimate testing time and the cost of SageMaker
3. Find Dataset with multiple sources and find the source bias