# Rick & Morty Character's Profile APP

This web app provides users with a searchable database of detailed character profiles from the animated series, Rick and Morty. 

It includes information such as **The characters Image, Name, Status, Gender, Species, Location, and the number of episodes the character appeared in**. 

This resource is designed to be user-friendly and easily accessible for anyone interested in learning more about the show's characters.

> Here is working live demo of the project: https://rickmorty.streamlit.app/

## How does the App Work?
The app works by allowing users to input a search query based on a character's name, gender, status, or species. The app then performs a **fuzzy search** on the database and returns a list of character profiles that match the search criteria, including information such as name, status, gender, species, location, and the number of episodes a character has appeared in.

```fuzzy search means that the web app is able to identify and return character profiles that partially match the user's search query, allowing for variations in spelling or minor differences in the search criteria. ```

The app also have a feature to allow users download the search result has a CSV file. 

## Sample Demo
![](https://github.com/heiskabeer/Rick-Morty-Character-Search-App/blob/main/sample%20demo.gif)


## Technologies Used
- `Requests:` Python libary used to communicate with web servers and API
- `Pandas:` Python library used for data manipulation and analysis
- `Streamlit:` Python libary used to build and share data apps

> You can do a simple `pip install <libary>` to install this libaries to your env

## Workflow
The project is broken down into 3 programs:
1. `scrape.ipynb:` which holds the code to connect to the source API and extract data. 
2. `cleaning.ipynb:` which holds the code to clean/manipulate the data.
3. `app.py:` which holds the code to build the data app.

## Blockage
I had no blockage scraping the data from the source API - it was authentication free and the request limit is quite fair.

The API Documentation was well structured, richly fed with clean Data - No typo errors of any kind. 

**However**, there was a **problem** with the **names** as there were instances where **different characters have the same name** - one example, we have three different characters named STEVE

This isn't much of a problem since each characters can be distinguished by pictures. but, i couldn't bring myself to over look it.

To fix this, i thought of a way to distinguish each character by adding roman numerals to their name. 

I spent a significant amount of time pondering on the logic to fix this problem. After extensive googling, ChatGPT prompting, and pondering, i was able to fix it. 

To think this problem was only fixed by a line of code still surprises me. You can find the solution in the `cleaning.ipynb` file.

**Another Blockage** i experienced was working with Streamlit libary as it was my first time picking up the stack. It was a fun ride thou. 

![](https://github.com/heiskabeer/Rick-Morty-Character-Search-App/blob/main/rick.gif)

---- 

MIT © [Kabeer](https://github.com/heiskabeer)
