---
layout: post
title: 'Study checklist for a budding data-scientist'
scripts: [toggle]
lang: en
ref: data-science-checklist
permalink: /data-science-checklist/
thumbnail: "images/data-science-checklist/I_know_data_science.jpg
tags:
 - "vselico"
 - "programovanie"
excerpt: ""
---

<style>
span .red {background-color: red;}
span .blue {background-color: blue;}
span .green {background-color: green;}
</style>


<img alt="Neo saying: 'I know data science'" src="{{site.baseurl}}/images/data-science-checklist/I_know_data_science.jpeg" />

I recently met someone who wants to learn data science- like I did years ago!
This blog post is for you, dear future data scientist.

When I look back at my data-science career, I had no problem finding all the learning resources I might need freely accessible on the internet. The problem was actually the opposite - every blog, book, tutorial or tool tried to look like the most important thing in the universe that you definitely need to know. The hardest thing was to correctly prioritize all the topics.
So to help you I came up with this list of topics a budding data scientist should learn. It is not the only possible learning path, but it is a good compromise between being exhaustive and concise. It is a springboard to data science studies, before you learn enough to guide your studies yourself.


### Legend

<span class=red>Red</span>
 : Know this well, it will be your bread and butter.

<span class=green>Green</span>
 :Know this well enough so that at worst you need to look up some specifics.

<span class=blue>Blue</span>
 :Know that this exists and what it is, you will learn the details later as you need them.

## Basic tools

- :small_blue_diamond::small_blue_diamond::small_blue_diamond:Visual Studio Code- code editor (IDE -Integrated development environment- used to edit code, run it, and other useful things) other IDE of your choice. They are usually packed with features - learn the basic ones you need, you will learn more advanced ones as you go.
- :small_blue_diamond::small_blue_diamond::small_blue_diamond:jupyter notebooks- code format and IDE useful for interactive data exploration and visualization. Compatible with both vscode and Google Colab
- :small_blue_diamond::small_blue_diamond::small_blue_diamond:basics of work with Linux terminal (or Windows command line)- change directory, list its contents, run a command, display help for the command
- :small_blue_diamond::small_blue_diamond:git
- :small_blue_diamond::small_blue_diamond:GitHub (or GitLab, Gitea or similar)

## Programming

- :small_blue_diamond::small_blue_diamond::small_blue_diamond:Python
- :small_blue_diamond:SQL

## Data formats

- :small_blue_diamond::small_blue_diamond::small_blue_diamond:CSV - basic format for tabular data, compatible with Excel 
- :small_blue_diamond::small_blue_diamond:JSON -  widespread format, can handle non-tabular data. A great tool for JSON exploration is jq.

## Python packages and tools

- :small_blue_diamond::small_blue_diamond::small_blue_diamond:Pandas - general, high level work with tables, python equivalent of Excel. Learn to load data, transform it and select some parts of it, the rest is optional.

- :small_blue_diamond::small_blue_diamond::small_blue_diamond:Matplotlib - most widespread data plotting package, used also by Pandas and Scikit-learn. Learn how to do basic plots, the rest is optional.

- :small_blue_diamond:Seaborn - very useful extension of matplotlib capabilities, it's a good idea to get used to it for basic plots instead of matplotlib.

- :small_blue_diamond::small_blue_diamond:Numpy - matrix multiplication and other linear algebra, work with numerical arrays

- :small_blue_diamond::small_blue_diamond::small_blue_diamond:Scikit-learn - a huge collection of models and tools for model evaluation, from basic to advanced. Learn where the model performance evaluation tools are, learn what the model interface looks like, treat the list of available models as a learning checklist for further study.

- :small_blue_diamond:Scipy - advanced mathematics, statistics and optimization

- :small_blue_diamond:Pytorch and/or Tensorflow - python packages for neural networks

- :small_blue_diamond::small_blue_diamond:pip - package manager, you will need it to install all these packages anyway

- :small_blue_diamond:conda package manager and virtual environment

## Math

- :small_blue_diamond::small_blue_diamond::small_blue_diamond:linear algebra - :small_blue_diamond::small_blue_diamond::small_blue_diamond:vectors, :small_blue_diamond::small_blue_diamond::small_blue_diamond:matrix multiplication, :small_blue_diamond:geometric interpretation
- :small_blue_diamond::small_blue_diamond::small_blue_diamond:basics of statistics - :small_blue_diamond::small_blue_diamond::small_blue_diamond:probability, :small_blue_diamond::small_blue_diamond::small_blue_diamond:probability distribution, :small_blue_diamond::small_blue_diamond:conditional probability,:small_blue_diamond::small_blue_diamond:confidence interval, :small_blue_diamond:what is a statistical test, :small_blue_diamond::small_blue_diamond::small_blue_diamond:normal distribution, :small_blue_diamond::small_blue_diamond:binomial distribution , :small_blue_diamond::small_blue_diamond:Poisson distribution, :small_blue_diamond::small_blue_diamond:correlation, :small_blue_diamond::small_blue_diamond::small_blue_diamond:categorical distribution
- :small_blue_diamond::small_blue_diamond:Simpson's paradox, :small_blue_diamond::small_blue_diamond:selection bias, :small_blue_diamond::small_blue_diamond:survivor bias, :small_blue_diamond::small_blue_diamond::small_blue_diamond:confounding variable and spurious correlation 
- :small_blue_diamond:unintuitive properties of high dimensional spaces
- :small_blue_diamond:Intro to Bayesian statistics - Bayes rule, apriori and aposteriori probability distribution. Maximum likelihood and maximum aposteriori probability estimates.

## Modeling

- :small_blue_diamond::small_blue_diamond::small_blue_diamond:difference between regression and classification
- :small_blue_diamond::small_blue_diamond::small_blue_diamond:linear regression and logistic regression
- :small_blue_diamond::small_blue_diamond::small_blue_diamond:overfitting and strategies against it - :small_blue_diamond::small_blue_diamond::small_blue_diamond:train/test/validation split or :small_blue_diamond::small_blue_diamond:cross-validation, :small_blue_diamond::small_blue_diamond:regularization, :small_blue_diamond:data augmentation
- :small_blue_diamond::small_blue_diamond:data normalization - which models need it, which are immune
- :small_blue_diamond::small_blue_diamond::small_blue_diamond:confusion matrix - recall (sensitivity), precision, specificity, accuracy and tradeoffs between them.
- :small_blue_diamond::small_blue_diamond:roc curve, roc auc score (perhaps also precision-recall curve)
- :small_blue_diamond:data imbalance - impact on both training and model evaluation metrics
- :small_blue_diamond::small_blue_diamond:decision boundary, linear vs. non linear models - what is linearly separable data?
- :small_blue_diamond:Feature engineering for turning linear models non-linear, also see "kernel trick".
- :small_blue_diamond::small_blue_diamond:decision tree
- :small_blue_diamond:neural networks for classification
- :small_blue_diamond:bias Vs variance tradeoff
- :small_blue_diamond:ensemble models
- :small_blue_diamond:clustering
- :small_blue_diamond:topic modeling
- :small_blue_diamond:dimensionality reduction
- :small_blue_diamond:autencoders and embeddings

## Ethics

- Biased data leads to  biased models
- Misinterpretation of model output meaning - The user doesn't understand the math as you do.
- Overestimation of model output reliability - The user doesn't understand the limitations of the model as you do.
- Unintended use - users do whatever they want, sometimes it's great, but sometimes it's stupid and sometimes it's evil.
- Automated decision making - Don't do it, it's better to assist human decision makers, but keep in mind previous bullet points.
- When not to do machine learning - Good UI and good math are often a better solution than a good model.



## What does usual data-scientist workflow look like?

- Load data
- Explore it - what does it look like, how much is there, what data is missing, is it biased in some way? What data do you actually need? Are there outliers? Visualize it to get a better feel for it.
- Compute metrics you care about (means, medians, variance, correlation and rank correlation).
- Remove duplicates, deal with missing data, decide what to do with outliers.
- Model the data - understand what answer you want and what type of model can give you that.
- Evaluate your model - does it do what you want? If not, return to previous step.
- Visualise and clearly communicate the conclusions of your modeling - what do they mean? How certain are you?
- If needed, deploy the model for repeated use.






