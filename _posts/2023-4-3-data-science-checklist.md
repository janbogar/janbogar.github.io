---
layout: post
title: 'Study checklist for a budding data scientist'
scripts: [toggle]
lang: en
ref: data-science-checklist
thumbnail: "images/data-science-checklist/datascience.webp"
tags:
 - "this and that"
 - "programming"
excerpt: "I recently met someone who wants to learn data science - just like I did years ago!
This blog post is for you, dear future data scientist.

When I look back at my data science career, I had no problem finding all the learning resources I might need freely accessible on the internet. The problem was actually the opposite - every blog, book, tutorial or tool tried to look like the most important thing in the universe that you definitely need to know. The hardest thing was to correctly prioritize all the topics.
So to help you I came up with this list of topics a budding data scientist should learn."
---

<img alt="Tom (from Tom & Jerry) haphazardly mixing food ingredients labeled as data, Pytorch, Numpy, etc." src="{{site.baseurl}}/images/data-science-checklist/datascience.webp" />

I recently met someone who wants to learn data science- just like I did years ago!
This blog post is for you, dear future data scientist.

When I look back at my data science career, I had no problem finding all the learning resources I might need freely accessible on the internet. The problem was actually the opposite - every blog, book, tutorial or tool tried to look like the most important thing in the universe that you definitely need to know. The hardest thing was to correctly prioritize all the topics.

So to help you, I came up with this list of topics a budding data scientist should know. It is not the only possible learning path or the only flavour of data science (it is a very vaguely defined job), but it is a good compromise between being exhaustive and concise. Use it as a springboard, to guide you before you learn enough to guide yourself.


### Legend

- <span style="color:red">Red</span> - Know this well, it will be your bread and butter.
- <span style="color:green">Green</span> - Know this well enough so that at worst you need to look up some specifics.
- <span style="color:blue">Blue</span> - Know that this exists and what it is, you will learn the details later as you need them.

## Basic tools

 - <span style="color:red">Visual Studio Code</span> - I recommend this code editor (more specifically IDE - Integrated Development Environment - used to edit code, run it, and other useful things). IDEs are usually packed with features, but you don't need to learn how to use all of them, just learn the basics for now. There are also many good choices other than VS Code, e.g. Spyder. Try a few, pick one and stick with it.

- <span style="color:red">Jupyter Notebook</span> - This is a code format and IDE useful for interactive data exploration and visualization. It's compatible with both VS Code and Google Collab.

 - <span style="color:red">Basic work with Linux terminal (or Windows command line)</span> - Learn how to change directory, list its contents, run a command, display help for the command.

 - <span style="color:green">Git</span>
 - <span style="color:green">GitHub</span> - or GitLab, Gitea or similar Git hosting service. 

## Programming

- <span style="color:red">Python</span>
- <span style="color:green">SQL</span>

## Data formats

- <span style="color:red">CSV</span> - Basic format for tabular data, compatible with Excel. 
- <span style="color:green">JSON</span> -  Widespread format, can handle non-tabular data. A great tool for JSON exploration is jq.

## Python packages and tools

- <span style="color:red">Pandas</span> - General, high level work with tables, Python equivalent of Excel. Learn to load data, transform it and select some parts of it, learn the rest as you go.
- <span style="color:red">Matplotlib</span> - Most widespread data plotting package, used also by Pandas, Seaborn and Scikit-learn for their plotting. Learn how to do basic plots, formatting (set title, rename axis, change range) and how to save the plot to file.
- <span style="color:blue">Seaborn</span> - Very useful extension of matplotlib capabilities, it is a good idea to get used to it for basic plots instead of matplotlib.
- <span style="color:green">Numpy</span> - Matrix multiplication and other linear algebra, anything to do with numerical arrays.
- <span style="color:red">Scikit-learn</span> - A huge collection of models and tools for model evaluation, from basic to advanced. Learn about evaluation tools, what the model interface looks like and treat the list of available models as a learning checklist for further study.
- <span style="color:blue">Scipy</span> - Advanced mathematics, statistics and optimization.
- <span style="color:blue">Pytorch and/or Tensorflow</span> - Python packages for neural networks.
- <span style="color:green">Pip</span> - Package manager, you will need it to install all these packages anyway.
- <span style="color:blue">Conda</span> - Package manager and virtual environment.

## Math

- <span style="color:red">Linear algebra:</span>
  - <span style="color:red">Vectors</span> and their <span style="color:red">dot product</span>
  - <span style="color:red">Matrix multiplication</span>
  - <span style="color:green">Geometric interpretation</span>
- <span style="color:red">Statistics:</span>
  - <span style="color:red">Probability</span>
  - <span style="color:red">Probability distribution</span> and difference between probability and probability density
    - <span style="color:red">Normal (a.k.a gaussian) distribution</span>
    - <span style="color:red">Categorical distribution</span>
    - <span style="color:green">Binomial distribution</span>
    - <span style="color:green">Poisson distribution</span>
  - <span style="color:green">Correlation</span> and <span style="color:green">rank correlation</span>
  - <span style="color:green">Confidence interval</span>
  - <span style="color:blue">Concept of statistical test</span>
  - <span style="color:blue">P-value</span>
  - <span style="color:blue"> P-hacking</span> (as something to avoid)
- <span style="color:green">Conditional probability</span>
- Cognitive biases and statistical fallacies:
  - <span style="color:green">Simpson's paradox</span>
  - <span style="color:green">Selection bias</span>
  - <span style="color:green">Survivorship bias</span>
  - <span style="color:red">Confounding variable and spurious correlation</span>
- <span style="color:blue">Unintuitive properties of high dimensional spaces</span>
- <span style="color:blue">Introduction to Bayesian statistics:</span>
  - Bayes rule
  - Prior and posterior probability distributions
  - Difference between maximum likelihood estimate and maximum posterior probability estimate

## Visualization and descriptive statistics
 - <span style="color:red">Lineplot</span>
 - <span style="color:red">Scatterplot</span>
 - <span style="color:red">Histogram</span>
 - <span style="color:blue">Boxplot</span>
 - <span style="color:blue">KDE (kernel density estimate, a method to smooth out histograms)</span>
 - <span style="color:green">Quantiles</span>
 - <span style="color:red">Mean, mode, median, variance and standard deviation</span>

## Modeling

- Difference between <span style="color:red">regression</span> and <span style="color:red">classification</span>
- <span style="color:red">Linear regression</span> and <span style="color:red">logistic regression</span>
- <span style="color:red">Overfitting</span> and strategies against it:
  - <span style="color:red">Train/test/validation split</span>
  - <span style="color:green">Cross-validation</span>
  - <span style="color:green">Regularization</span>
  - <span style="color:blue">Data augmentation</span>
- <span style="color:green">Data normalization</span> - which models need it and which don't
- <span style="color:red">Confusion matrix</span> - recall (sensitivity), precision, specificity, accuracy and tradeoffs between them
- <span style="color:green">ROC curve</span> -  ROC AUC score (perhaps also precision-recall curve)
- Impact of <span style="color:blue">data imbalance</span> on training and model evaluation metrics
- <span style="color:green">Decision boundary</span> - linear vs. non linear models, concept of linearly separable data
- <span style="color:blue">Feature engineering</span>, especially for turning linear models non-linear, also see "kernel trick"
- <span style="color:green">Decision tree</span>
- <span style="color:blue">Neural networks</span> for classification
- <span style="color:blue">Bias Vs variance tradeoff</span>
- <span style="color:blue">Ensemble models</span>
- <span style="color:blue">Clustering</span>
- <span style="color:blue">Topic modeling</span>
- <span style="color:blue">Dimensionality reduction</span>
- <span style="color:blue">Autoencoders and embeddings</span>

## Ethics

- Biased data leads to biased models.
- Misinterpretation of model output meaning - the user doesn't understand the math as you do.
- Overestimation of model output reliability - the user doesn't understand the limitations of the model as you do.
- Unintended use - users do whatever they want, sometimes it is great, but sometimes it is stupid and sometimes it is evil.
- Automated decision making - don't do it, it is better to assist human decision makers, but keep in mind previous bullet points.
- When not to do machine learning - good UI and good math are often a better solution than a good model.

## What does the usual data science workflow look like?

In addition to thinking about business needs, hypothesis forming and testing, communication and other tasks, the "manual" part of data-science usually consists of these steps:

- Load data.
- Explore it - what does it look like, how much is there, what data is missing, is it biased in some way? Is it representative of the real world? What data do you actually need? Are there outliers?
- Use descriptive statistics and visualization to summarize data properties.
- Clean the data - remove duplicates and deal with missing data and outliers.
- Model the data - understand what answer you want and what type of model can give it to you.
- Evaluate your model - does it do what you want? If not, return to previous step.
- Visualize and clearly communicate the conclusions of your modeling - what do they mean? How certain are you?
- If needed, deploy the model for repeated use.

## Conclusion
Good luck!