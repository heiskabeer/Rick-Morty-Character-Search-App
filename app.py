import streamlit as st
import pandas as pd
import base64

# Define the function that creates the Streamlit app
def app():
    # Load the data from a CSV file into a pandas data frame
    data = pd.read_csv('cleaned_rick_morty.csv')

    # Define the user interface using Streamlit components
    st.title('Rick and Morty Character Search')

    search_query = st.text_input('Enter a character name:')
    search_button = st.button('Search')


    # Define the logic for the search feature

    if search_button or search_query:
    # Filter the data frame based on the search query
        results = data[data['Name'].str.contains(search_query, case=False) | 
                    data['Status'].str.contains(search_query, case=False) | 
                    data['Gender'].str.contains(search_query, case=False) | 
                    data['Species'].str.contains(search_query, case=False)]
                    # data['Location'].str.contains(search_query, case=False) |
                    # data['nEpisode_Appeared'].astype(str).str.contains(search_query, case=False)]

        if results.empty:
            st.subheader("Record Not Found, Enter a Valid Character Name")
        else:
            results = results.reset_index(drop=True)

       
        # st.table(results)  # Display the search results in a Streamlit table

            for index, row in results.iterrows(): #Iterate and store data into a card container
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.image(row['Image'], width=115)
                with col2:
                    st.subheader(row['Name'])
                    st.write(f"**Status:** {row['Status']}")
                    st.write(f"**Gender:** {row['Gender']}")
                    st.write(f"**Species:** {row['Species']}")
                    st.write(f"**Location:** {row['Location']}")
                    st.write(f"**Number of Episodes Appeared:** {row['nEpisode_Appeared']}")
                    

            
            csv = results.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="search_results.csv">Download CSV</a>'
            st.markdown(href, unsafe_allow_html=True)

    footer = st.container()
    footer.write('<div style="position: fixed; bottom: 0; text-align: center; width: 100%;">Made with ❤️ by Kabeer</div>', unsafe_allow_html=True)


if __name__ == '__main__':
    app()

