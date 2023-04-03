---
layout: post
title: 'Study checklist for a budding data scientist'
scripts: [toggle]
lang: en
ref: data-science-checklist
thumbnail: "images/data-science-checklist/datascience.webp"
tags:
 - "this-and-that"
 - "programming"
excerpt: "I recently met someone who wants to learn data science - like I did years ago!
This blog post is for you, dear future data scientist.

When I look back at my data science career, I had no problem finding all the learning resources I might need freely accessible on the internet. The problem was actually the opposite - every blog, book, tutorial or tool tried to look like the most important thing in the universe that you definitely need to know. The hardest thing was to correctly prioritize all the topics.
So to help you I came up with this list of topics a budding data scientist should learn."
---

<img alt="Tom (from Tom & Jerry) haphazardly mixing food ingredients labeled as data, Pytorch, Numpy, etc." src="{{site.baseurl}}/images/data-science-checklist/datascience.webp" />

I recently met someone who wants to learn data science- like I did years ago!
This blog post is for you, dear future data scientist.

When I look back at my data science career, I had no problem finding all the learning resources I might need freely accessible on the internet. The problem was actually the opposite - every blog, book, tutorial or tool tried to look like the most important thing in the universe that you definitely need to know. The hardest thing was to correctly prioritize all the topics.

So to help you, I came up with this list of topics a budding data scientist should know. It is not the only possible learning path or the only flavour of data science (it is a very vaguely defined job), but it is a good compromise between being exhaustive and concise. Use it as a springboard, to guide you before you learn enough to guide yourself.


### Legend

- <span style="color:red">Red</span> - Know this well, it will be your bread and butter.
- <span style="color:green">Green</span> - Know this well enough so that at worst you need to look up some specifics.
- <span style="color:blue">Blue</span> - Know that this exists and what it is, you will learn the details later as you need them.

## Basic tools

 - <span style="color:red">Visual Studio Code</span> - code editor (IDE, i.e. Integrated development environment, used to edit code, run it, and other useful things) or other IDE of your choice. They are usually packed with features, don't worry about them, just learn the basics for now.

- <span style="color:red">Jupyter Notebook</span> - code format and IDE useful for interactive data exploration and visualization. Compatible with both vscode and Google Collab.

 - <span style="color:red">basic work with Linux terminal (or Windows command line)</span> - change directory, list its contents, run a command, display help for the command

 - <span style="color:green">Git</span>
<span style="color:green">GitHub</span> (or GitLab, Gitea or similar)

## Programming

- <span style="color:red">Python</span>
- <span style="color:green">SQL</span>

## Data formats

- <span style="color:red">CSV</span> - basic format for tabular data, compatible with Excel 
- <span style="color:green">JSON</span> -  widespread format, can handle non-tabular data. A great tool for JSON exploration is jq.

## Python packages and tools

- <span style="color:red">Pandas</span> - general, high level work with tables, Python equivalent of Excel. Learn to load data, transform it and select some parts of it, learn the rest as you go.
- <span style="color:red">Matplotlib</span> - most widespread data plotting package, used also by Pandas, Seaborn and Scikit-learn for their plotting. Learn how to do basic plots, formatting (set title, rename axis, change range) and how to save the plot to file.
- <span style="color:blue">Seaborn</span> - very useful extension of matplotlib capabilities, it is a good idea to get used to it for basic plots instead of matplotlib.
- <span style="color:green">Numpy</span> - matrix multiplication and other linear algebra, anything to do with numerical arrays.
- <span style="color:red">Scikit-learn</span> - a huge collection of models and tools for model evaluation, from basic to advanced. Learn about evaluation tools are, what the model interface looks like, treat the list of available models as a learning checklist for further study.
- <span style="color:blue">Scipy</span> - advanced mathematics, statistics and optimization
- <span style="color:blue">Pytorch and/or Tensorflow</span> - python packages for neural networks
- <span style="color:green">Pip</span> - package manager, you will need it to install all these packages anyway
- <span style="color:blue">Conda</span> package manager and virtual environment

## Math

- <span style="color:red">linear algebra</span>
  - <span style="color:red">vectors</span>
  - <span style="color:red">matrix multiplication</span>
  - <span style="color:green">geometric interpretation</span>
- <span style="color:red">statistics</span>
  - <span style="color:red">probability</span>
  - <span style="color:red">probability distribution</span> and difference between probability and probability density
    - <span style="color:red">normal (a.k.a gaussian) distribution</span>
    - <span style="color:red">categorical distribution</span>
    - <span style="color:green">binomial distribution</span>
    - <span style="color:green">Poisson distribution</span>
  - <span style="color:green">correlation</span> and <span style="color:green">rank correlation</span>
  - <span style="color:green">confidence interval</span>
  - <span style="color:blue">what is a statistical test</span>
  - <span style="color:blue">p-value</span>
  - <span style="color:blue"> p-hacking</span> (as something to avoid)
- <span style="color:green">conditional probability</span>
- <span style="color:green">Simpson's paradox</span>, <span style="color:green">selection bias</span>, <span style="color:green">survivor bias</span>, <span style="color:red">confounding variable and spurious correlation</span>
- <span style="color:blue">unintuitive properties of high dimensional spaces</span>
- <span style="color:blue">introduction to Bayesian statistics</span>
  - Bayes rule
  - prior and posterior probability distribution
  - maximum likelihood and maximum posterior probability estimates

## Visualization and descriptive statistics
 - <span style="color:red">lineplot</span>
 - <span style="color:red">scatterplot</span>
 - <span style="color:red">histogram</span>
 - <span style="color:blue">boxplot</span>
 - <span style="color:blue">KDE (kernel density estimate, basically a method to smooth out histograms)</span>
 - <span style="color:green">quantiles</span>
 - <span style="color:red">mean, mode, median, variance, standard deviation</span>

## Modeling

- difference between <span style="color:red">regression</span> and <span style="color:red">classification</span>
- <span style="color:red">linear regression</span> and <span style="color:red">logistic regression</span>
- <span style="color:red">overfitting</span> and strategies against it - <span style="color:red">train/test/validation split</span>, <span style="color:green">cross-validation</span>, <span style="color:green">regularization</span>, <span style="color:blue">data augmentation</span>
- <span style="color:green">data normalization</span> - which models need it, which are immune
- <span style="color:red">confusion matrix</span> - recall (sensitivity), precision, specificity, accuracy and tradeoffs between them
- <span style="color:green">roc curve</span> -  roc auc score (perhaps also precision-recall curve)
- <span style="color:blue">data imbalance</span> - impact on both training and model evaluation metrics
- <span style="color:green">decision boundary</span> - linear vs. non linear models, concept of linearly separable data
- <span style="color:blue">feature engineering</span>, especially for turning linear models non-linear, also see "kernel trick"
- <span style="color:green">decision tree</span>
- <span style="color:blue">neural networks</span> for classification
- <span style="color:blue">bias Vs variance tradeoff</span>
- <span style="color:blue">ensemble models</span>
- <span style="color:blue">clustering</span>
- <span style="color:blue">topic modeling</span>
- <span style="color:blue">dimensionality reduction</span>
- <span style="color:blue">autoencoders and embeddings</span>

## Ethics

- Biased data leads to  biased models.
- Misinterpretation of model output meaning - the user doesn't understand the math as you do.
- Overestimation of model output reliability - the user doesn't understand the limitations of the model as you do.
- Unintended use - users do whatever they want, sometimes it is great, but sometimes it is stupid and sometimes it is evil.
- Automated decision making - don't do it, it is better to assist human decision makers, but keep in mind previous bullet points.
- When not to do machine learning - good UI and good math are often a better solution than a good model.

## What does the usual data science workflow look like?

- Load data
- Explore it - what does it look like, how much is there, what data is missing, is it biased in some way? Is it representative of the real world? What data do you actually need? Are there outliers? Visualize it to get a better feel for it.
- Use descriptive statistics to summarize data properties.
- Remove duplicates, deal with missing data, decide what to do with outliers.
- Model the data - understand what answer you want and what type of model can give it to you.
- Evaluate your model - does it do what you want? If not, return to previous step.
- Visualize and clearly communicate the conclusions of your modeling - what do they mean? How certain are you?
- If needed, deploy the model for repeated use.

## Conclusion
Good luck!