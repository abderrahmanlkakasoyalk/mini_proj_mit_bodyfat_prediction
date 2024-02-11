# Prediction of Body Fat Percentage using Different Regression Algorithms

## Introduction
This project aims to predict body fat percentage using various regression algorithms. The dataset used for this project is sourced from OpenML, and it contains information about different body measurements and body fat percentage.

## Project Details
- **Dataset**: [BodyFat Dataset from OpenML](https://openml.org/search?type=data&status=active&id=560&sort=runs)
- **Author**: Likram Abderrahman MIT_TAM
- **GitHub Repository**: [MiniProjetMl_MIT_TAM](https://github.com/abderrahmanlkakasoyalk/MiniProjetMl_MIT_TAM)

## Project Implementation

### Data Preprocessing
- Converted weight from pounds to kilograms and height from inches to meters.
- Calculated Body Mass Index (BMI) using weight and height.
- Removed non-important features such as id, ankle, wrist, and forearm.
- Renamed the 'class' column to 'BodyFat'.
- Created additional features like Abdomen/Chest ratio (ACratio) and Hip/Thigh ratio (HTratio).

### Exploratory Data Analysis (EDA)
- Plotted the correlation between body fat percentage and other features.
- Identified highly correlated features and dropped some redundant ones.

### Regression Algorithms
- Applied Linear Regression and Polynomial Regression.
- Implemented Lasso and Ridge regression for regularization.
- Utilized Support Vector Machine (SVM) and Random Forest Regression.

### Model Evaluation
- Evaluated models based on R-squared (R2) and Root Mean Squared Error (RMSE).
- Analyzed the performance of each algorithm and compared results.
- Identified Linear Regression as the most suitable model for this dataset.

### Conclusion
- Linear Regression demonstrated competitive performance with lower RMSE compared to other models.
- Polynomial features led to overfitting of the model.
- Random Forest Regression also showed promising results.
- Deployment of the Linear Regression model using Streamlit Cloud.

## Summary Table
The table below summarizes the performance of each algorithm:

| Algorithm                   | R2            | RMSE  |
|-----------------------------|---------------|-------|
| Linear Regression           | 0.7134        | 4.5802|
| Lasso Regression            | 0.7132        | 4.5820|
| Ridge Regression            | 0.7133        | 4.5816|
| Polynomial Regression       | -0.074        | 8.0700|
| Random Forest Regression    | 0.638         | 4.1000|
| Support Vector Machine (SVM)| 0.573         | 19.860|

## Conclusion and Deployment
Linear Regression emerged as the best choice due to its simplicity and competitive performance. The deployed app allows users to predict body fat percentage using the trained Linear Regression model.

[Link to the deployed app](https://bodyfat--proj-mit-tam.streamlit.app/?embed_options=dark_theme,show_colored_line,show_footer)

This README provides an overview of the project, its implementation, and the conclusions drawn from the analysis. For more detailed information, please refer to the code and documentation in the GitHub repository.
