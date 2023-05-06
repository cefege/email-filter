import pandas as pd
import streamlit as st

def process_emails(email_list):

    # Remove any elements that do not contain '@'
    email_list = [email for email in email_list.split('\n') if '@' in email]

    # remove duplicates
    email_list = list(set(email_list))

    # Split the email list into a list of tuples containing the name and domain
    email_tuples = [(email.split('@')[0], email.split('@')[1]) for email in email_list]

    # Convert the list of tuples into a pandas dataframe
    df = pd.DataFrame(email_tuples, columns=['name', 'domain'])

    # Sort the dataframe by the domain column
    df = df.sort_values('domain')

    # Combine the name and domain columns with '@' separator
    df['email'] = df['name'] + '@' + df['domain']

    # Select only the email column for output
    output_df = df[['email']]

    # Return the output dataframe
    return output_df

def app():
    # Define a text input for the list of emails
    email_list = st.text_area('Enter a list of emails (one email per line)')

    # Add a "Submit" button to trigger the processing of the emails
    if st.button('Submit'):
        # Process the email list using the process_emails function
        output_df = process_emails(email_list)

        # convert column "email" to a string split by \n
        output_df = output_df['email'].str.cat(sep='\n')

        # Write the output dataframe to the Streamlit app
        st.code(output_df)

if __name__ == '__main__':
    app()
