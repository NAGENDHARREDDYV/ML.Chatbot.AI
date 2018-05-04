# ML.Chatbot.AI
[Nagendhar Reddy Vuppunuthula] reddy.vuppunuthula@gmail.com 
Copyrights. Open Source contribution

Chat bot for Buying a phone and Selecting a restro in one part of city

The bot can perform the below two skills:
• Buying a mobile phone. The user should be asked questions about Brand, Size, Accessories and other parameters.
Action: The bot should give a final selection
• Restaurants booking : Book a restaurant based on cuisine , cost type (cheap, medium, expensive), location ( east, west, north, south).
Action: Final action booking

Reference Chatbot Architecture: Refer to "Chatbot Architecture.pdf"

Components of a Chatbot Framework
•Dialog Manager
•Managing dialog state
•Natural Language Understanding
•Intent states
•Understanding the intent of a users input
•Conversation FSA (usually a tree)


Skills

•A skill is the ability to gather information required to perform a task
and to actually perform that task
•“With a custom Alexa Skill, you control the requests made by the user, as well
as the words they use to trigger the Skill.” –Amazon
•Each of the tasks provided are a skill
•A simple yet complete task 

Requirements
• Some parameters are required for a chatbot skill for a particular task
• What are the “attributes”
• What are the variables required to perform the task? (Source, Destination, time etc…)
• What are the entities?
• City names, store names, book names etc.
• What are the Responses?
• What should the bot say?
• If destination is not set : “Where do you want to go?”
• Possible user inputs
• Bot cannot understand text: We need to prime it for understanding.
• Dialog state
• Some of the above would be dependent on where you are in the conversation



Intent Classification

Intent: get_shows


What is playing in Lincoln Center
What movies are showing at Angelica Film center tonight
List movies at Film Forum after 7pm tomorrow


Intent: get_restaurants
Find inexpensive restaurants in Chelsea
Sushi restaurants in the Village
Brunch in Brooklyn Heights

Approach: supervised classification (SVM, CRF, Decision Tree, etc.)


Concept Labels

Intent: get_shows
What is playing in Lincoln Center/VENUE
What movies are showing at Angelica Film Center/VENUE tonight/TIME
List movies at Film Forum/VENUE after 7pm tomorrow/TIME

Intent: get_restaurants
Find inexpensive/PRICERANGE restaurants in Chelsea/NEIGHBORHOOD
Sushi/CUSINE restaurants in the Village/NEIGHBORHOOD
Brunch/CUSINE in Brooklyn Heights/NEIGHBORHOOD



