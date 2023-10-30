# Covid-19 Chatbot
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
One popular application of deep learning to NLP is the Chatbot. Many companies use chatbots to handle generic customer service requests, which require them to be flexible in translating questions into answers. The given problem is to design a chatbot for a social cause. In view of the current pandemic situation, a chatbot for Covid-19 patients and also people who are worried about getting infected should be created.

The coronavirus pandemic has created chaos among people by affecting our lives. There is a need to educate people about the virus to protect themselves and their loved ones from catching the virus. Keeping the current pandemic situation in mind, we have created a Covid-19 chatbot. This chatbot focuses on providing reliable information regarding coronavirus to its users. Users of this chatbot can ask their queries in the form of input to the chatbot and get them answered. Covi-19 chatbot is based on Artificial Intelligence and Natural Language Processing. This chatbot answers the frequently asked questions regarding the novel coronavirus disease. The dataset used for the development of this project id obtained from reliable sources such as official websites of World Health Organization (WHO), Centers for Disease Control and Prevention (CDC) and Food and Drug Administration (FDA). The collected data is formatted and pre-processed and fed to the built deep learning model that will aid in predicting the response of the chatbot. The chatbot has also been equipped to collect feedback from its users which could be helpful in improving the performance of the chatbot. 

The Covid-19 chatbot can be further developed by supporting interactions in regional languages such as Kannada, Telugu, etc. which will be very helpful for people residing in remote areas to learn about covid-19. This bot can also be integrated with Covid-19 related websites and various messaging platforms for better access. The chatbot can be further developed by connecting users to healthcare professionals if a user’s health condition is analysed to be critical

### Built With
* Python
* Heroku
* GitHub
* Spyder Notebook

<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple steps.


### Prerequisites
#### Software Requirements
* Anaconda - [Download and install Anacondo](https://docs.anaconda.com/anaconda/install/windows/)
* Spyder IDE - [Download and install Sypder IDE](https://www.spyder-ide.org/)
* Heroku CLI - [Download and install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
* Python - [Download and install Python 3.6 or greater](https://www.python.org/downloads/)

#### Hardware Requirements
* Processors: Intel Core i3 processor or any processor greater or equal to it
* Operating systems: Windows 7 or later, macOS and Linux

### Installation
1. Clone the repo
```sh
   git clone https://github.com/Rahul-Raman-R/chatbot_covid_bot.git
   ```
2. Create a virtual environment on anaconda
```sh
  conda create -n yourenvname python=x.x anaconda
  source activate yourenvname
   ```
3. Installing necessary packages
cd to the directory where the cloned repository is located
```sh
  conda install --file requirements.txt
   ```
Or else you can manually install the packages in requirements.txt

4. Running the project on local server
* Open the sypder notebook
* Create a new project and add the cloned repository
* Open the app.py file and run it 
* Now the flask application will be available on the local server

<!-- USAGE EXAMPLES -->
## Usage
Here you can see some examples of the flask application usage.
![alt text](https://github.com/Rahul-Raman-R/chatbot_covid_bot/blob/main/static/img/ss1.png?raw=true)

![alt text](https://github.com/Rahul-Raman-R/chatbot_covid_bot/blob/main/static/img/ss2.png?raw=true)

## Deployment
1. Create Heroku account.
2. Create a new app on Heroku:
We have to name our app and now we can deploy the app through CLI or through the Heroku web site. Here we have used the website.
In deployment method we chose GitHub.
![alt text](https://github.com/Rahul-Raman-R/chatbot_covid_bot/blob/main/static/img/ss3.png?raw=true)
Then we deploy the main branch of the repository. Then Heroku starts with Procfile and then deploys the web application on an URL.
[https://covid-bot1.herokuapp.com/](https://covid-bot1.herokuapp.com/)
![alt text](https://github.com/Rahul-Raman-R/chatbot_covid_bot/blob/main/static/img/ss4.png?raw=true)
Now the web application can be accessed using this URL from anywhere.

<!-- CONTACT -->
## Contact
* Rahul Raman R - [Email](rahulr.is17@bmsce.ac.in)
* Sanjana V - [Email](sanjana.is17@bmsce.ac.in)
* Sushmitha J - [Email](sushmithaj.is17@bmsce.ac.in)


