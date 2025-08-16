# GEELY AUTO Car Price Prediction for Market Penetration
## Problem Statement
A Chinese automobile company Geely Auto aspires to enter the US market by setting up their manufacturing unit there and producing cars locally to give competition to their US and European counterparts. They have contracted an automobile consulting company to understand the factors on which the pricing of cars depends. Specifically, they want to understand the factors affecting the pricing of cars in the American market, since those may be very different from the Chinese market. The company wants to know:


- Which variables are significant in predicting the price of a car
- How well those variables describe the price of a car

Based on various market surveys, the consulting firm has gathered a large data set of different types of cars across the America market. 

## Business Goals
We are required to model the price of cars with the available independent variables. It will be used by the management to understand how exactly the prices vary with the independent variables. They can accordingly manipulate the design of the cars, the business strategy etc. to meet certain price levels. Further, the model will be a good way for management to understand the pricing dynamics of a new market. 

# Disclaimer
**The dataset, modelling and deployment done here is for learning purpose only. Do not infer from this project.**

## Solution

+ Use Multiple Linear Regression as interpretable model
+ Use Recursive Feature Elimination with Cross Validation and Variance Inflation Factor to help reduce dimensionality and determine significant factors
+ Build a simple internal web-app for price prediction based on model for internal use

# System Overview Diagram / Architecture
![](https://github.com/brian-novp/dcampt25/blob/main/img/architecture%20diagram%20deploycamp%20team%2025.png)
## Tech Stack Table
![](img/tech_stack_table.png)
## Functionality
![](img/functionality.png)

# Executive Summary
## Purpose
This project aims to discover which significant factors affect pricing of cars in USA based on the observational data.

## Findings
We found that curb weight, horsepower, engine location, OHCV engine, number of cylinders and SPDI fuel system are significant factors in determining price of a car based on our project.

## Audience
This project is intended for Geely internal-use only to be used by marketing, data science and design department

## Recommendations
1. Use above-mentioned factors as keywords in marketing or in designing the car
2. Conduct further data collection to improve model

# DEMO 

## Live Web App
This web app lifetime will be terminated in early September 2025


private repo of team25 deploycamp
SLIDE HERE
https://docs.google.com/presentation/d/1_NQ5OA9zsNc8_GIWFv9xRdcuc4fw2ZlqQEprARMxJ3Q/edit?usp=sharing
