# Rhyme-Scheme-Finder
This is a small proof of concept for the larger goal of creating an app that will analyze the rhyme scheme of song lyrics. 

I've been learning Python as I write this project, and still have quite a bit to learn. As of now, the app is designed to take information from an api, and create a large list of potential rhymes for any given word. A list of rhymes is created for the first word as well as the second, and those lists are compared. If there is any overlap in the list of rhymes, the pair are marked as a rhyme.

This process is iterated through the entire string, done in such a way to never compare the same two words. 

When a rhyme is found a dictionary list is created with the key being the first rhyme, and the rest of the words are appended to the value. As of right now, the code is set up so that instead of setting the values to the words themselves, the values are the location of the word in the string. This will enable me to find the words again in the future, and give visible feedback to the user.

There are quite a few inefficiencies, and this api method is by no means a perfect solution, but its been an interesting learning experience and gives me a few directions to move forward with the idea. 

# Screenshot
<img width="705" alt="rhyme-screenshot" src="https://user-images.githubusercontent.com/99859819/155607895-a6443cba-b1a6-40ae-8aea-a20f59ded965.PNG">
