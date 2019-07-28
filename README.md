# CRISP-DM Example

This project follows the CRISP-DM (CRoss Industry Standard Process for Data Mining) and breaks down each of it's processes with the respect to the project

>CRISP-DM stands for cross-industry process for data mining. The CRISP-DM methodology provides a structured approach to planning a data mining project. It is a robust and well-proven methodology. [...] , its flexibility and its usefulness when using analytics to solve thorny business issues. It is the golden thread than runs through almost every client engagement. The CRISP-DM model is shown on the right.
This model is an idealised sequence of events. In practice many of the tasks can be performed in a different order and it will often be necessary to backtrack to previous tasks and repeat certain actions. The model does not try to capture all possible routes through the data mining process.
-- by ["Smart Vision Europe"](https://www.sv-europe.com/crisp-dm-methodology/)

These are the stated process in the methodoly:
  - Business Understanding
  - Data Understanding
  - Data Preparation
  - Modeling
  - Evaluation
  - Deployment

# Project Details

I have used a [dataset](https://raw.githubusercontent.com/S-Mann/hyperparameter_optimization/master/dataset/dataset.csv) that I have combined from multiple source like Wikipedia and Kaggle, I am trying to find strongly coupled attrbutes with respect to our output label. The focus of this project is to highlight how deployment would work in a Data Mining project and optimization of models.

# Process Breakdown

- **Business Understanding**: 
Our clients are trying to make cars for a certain category and they want to see if entering a certain category with a certain model yields them profit or not. They are trying to assess if the car model idea will give good enough profit.
We are trying to understand if there is a relationship between the happiness and other attributes. We would like to know which are these attrbutes and if given a set of inputs will we be able to predict the happiness ranking accurately.

- **Data Understanding**:
We are considering that we get the data from a data warehouse or we mine certain sites for certain attributes. We are given attributes like Ladder Index (life satisfaction), Positive Emotion, Negative Emotion, Social Support, Freedom, Life Expectance, Generosity, Government Corruption, GDP. Almost all these attributes are relative scores of numeric type, they are rankings ranging within 1-156 as we have 156 countries (regions) in total.

- **Data Preparation**:
Our dataset does have missing values which we will try to resolve. Since the dataset has attributes as numeric ranking, we can replace missing values with the last available index or a mean value of the rankings.

- **Modeling**:
We will use [RapidMiner](https://rapidminer.com/) to suggest us which algorithm would make the most sense to implement. There are few other methods to check which model would make sense but we would like to use RapidMiner as it's efficient and fast to test.

- **Evaluation**:
Our metric for worthiness of the model would be the accuracy. We would see the accurancy, time taken, standard deviation for each model and try to decide upon which model to use.

- **Deployment**:
All our efforts will come down to how we deploy our model, we would setup some sort of monitoring system to look for model anomly, but we would like that no such anomly occurs in the first place.
