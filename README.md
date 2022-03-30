# Foodie Restaurant Chatbot

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities.

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience.

Zomato apis are used for searching the restaurants https://developers.zomato.com/documentation#/


### Prerequisites

1. Python (requires Python 3.6 or 3.7)
2. Visual studio or Pycharm for python development
3. Create and activate a virtual environment
4. MacOS environment
5. Create a virtual environment : `python3 -m venv --system-site-packages ./venv`
6. Activate the virtual Environment: `source ./venv/bin/activate`

### Installation:
Install Rasa NLU (version 1.10.7) and Spacy (version 2.3.1) using the following code:

cd path <path to project>

`$pip install rasa`
`$pip install spacy`
`$python -m spacy download en_core_web_md`
`$python -m spacy link en_core_web_md en`

###### How to find rasa and spacy version

```
$python -c "import rasa; print(rasa.__version__)"
1.10.7
$python -c "import spacy; print(spacy.__version__)"
2.3.1
```

### Project Structure

cd path <path to project>

Project includes the following files:
1. __init__.py: an empty file that helps python find actions
2. actions.py: code for custom actions
3. config.yml: configuration of NLU and Core models
4. credentials.yml: details for connecting to other services
5. data/nlu.md: NLU training data
6. data/stories.md: traininig stories
7. domain.yml: chatbot assistant’s domain
8. endpoints.yml: details for connecting to channels like messenger etc.
9. models/<timestamp>.tar.gz: initial model


### Train the nlu data & core conversational flow
Whenever new NLU or Core data is added, or updates to domain or configuration, we need to re-train a neural network on the example stories and NLU data. To do this, run the command below which calls the Rasa Core and NLU train functions and store the trained model into the models/ directory.

`$rasa train && rasa run actions`

### Talk to your assistant
Once the core model training is completed, the next step is to try it out. Start talking to your assistant by running:

`$rasa shell`

### Train dialogue flow online and add stories
Generated stories can be exported and added to stories.md. Retrain the model and check dialogue flow.

`$rasa interactive`

### Example in a rasa shell
Some sample conversations are as follows:
```
User: Hi
Bot: Hey, How is it going. How May I help you Today.
User: Can you suggest some good restaurants in bangalore
Bot: What kind of cuisine would you like?
   1: Chinese
   2: Mexican
   3: Italian
   4: American
   5: South Indian
 » 6: North Indian
User: North Indian
Bot: What budget are you looking at?
   1: Lesser than Rs. 300
 » 2: Rs. 300 to 700
   3: More than 700
User: 300 to 700
Bot: Here are our top recommendations:
---------------
1. Royal Andhra Spice in OSR Hotels, 60 Feet Road, Near BEML Bus Depot, Rajarajeshwari Nagar, Bangalore has been rated 4.5
2. Manjit Da Dhaba in 107, 1st Floor, Wheeler Road, Near Railway Cross, Cox Town, Frazer Town, Bangalore has been rated 4.4
3. Mumbai Tiffin in 2345, 17th Cross, Opposite Water Tank, Sector 1, HSR, Bangalore has been rated 4.3
4. Grill Biryanis in 9, Jalahalli Cross Circle, Jalahalli, Bangalore has been rated 4.1
5. Hyderabadi Spice in 70/1, Opposite Wipro Technologies Gate 12, Electronic City, Bangalore has been rated 4.1
---------------
Bot: Do you want a list of restaurants in your email?
 » 1: Yes
   2: No
User: Yes
Bot: Please, enter your email id.
User: example@gmail.com
Bot: **** Email sent. Happy dining. ****
```
