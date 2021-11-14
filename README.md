# Bullying-The-Bully (Bot)

## Overview

This project aims towards conserving anti-bullying rights on social media. It is built with the objective that users of social media are not a victim of cyberbullying or trolls online. A study led by Microsoft Corporation in 2012, spread over 25 nations positioned India third in the quantity of internet cyberbullying cases. As indicated by the 2014 investigation led by the Internet security organization, McAfee, “Half of the young in India have had some experience with cyberbullying”. Cyberbullying can be intimidating, dangerous, invasive and very real to the people who go through it.  In this scenario, when there is an effort to destroy someone’s reputation online, the effect ripples into people’s lives and their relationships. Therefore, cyber bullying is a grave concern in contemporary times. Many leading companies are taking the aid of ML and AI related models for prevention of harassment online. We have taken a small initiative towards this issue by creating an NLP-based model that classifies comments into offensive and non-offensive. We have also created a bot on discord  that reports such users and blocks them. We can only teach people to protect their well-being, to say enough. Cyberbullying leads to cyberhacking, which leads to real life stalking. We need to enforce the criminal code by ensuring the law enforcement puts hackers behind bars. It’s causes loss of economic activity, loss of life, etc. Hence, let us strive together towards taking precautions against this abhorrent and criminalized activity.

We created a NLP based discord bot using the dataset we collected from [Kaggle](https://www.kaggle.com/surekharamireddy/malignant-comment-classification), that takes the recent texted message from the server, runs analysis and predicts if the text is offensive to any person on the server or not. If it finds the text offensive then it deletes the text and messages the Administrator of the server to block the person that sent the message. This is how it looks when someone texts something bad:

![image](https://user-images.githubusercontent.com/78687109/141666424-fb768d22-e431-4346-b79c-1a46c6382ff5.png)

## How to use
[Click here to add Bot to your server.](https://discord.com/api/oauth2/authorize?client_id=908627254387568670&permissions=8&scope=bot)

**If you find the bot offline, feel free to contact us at +91 9337070750**

Give Administrator access and then it good to go.

This bot can only run for the person who created the bot, so it **"cannot run on any-other local machine"**.

When someone Texts something offensive, then Bot deleted the message and creates a poll to ban the user. If the number of votes reaches the threashold, then the user that texted it, gets banned.

## Technologies Used

We used discord.py, scikit-learn, and other minor libraries for making the whole project, from modeeling the NLP model to deploying it to a discord Bot.
