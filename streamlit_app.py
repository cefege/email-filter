import pandas as pd
import streamlit as st


def process_emails(email_list):
    # Remove any elements that do not contain '@'
    email_list = [email for email in email_list.split("\n") if "@" in email]

    # convert all emails to lowercase
    email_list = [email.lower() for email in email_list]

    # remove any leading or trailing whitespace
    email_list = [email.strip() for email in email_list]

    # remove duplicates
    email_list = list(set(email_list))

    # Split the email list into a list of tuples containing the name and domain
    email_tuples = [(email.split("@")[0], email.split("@")[1]) for email in email_list]

    # Convert the list of tuples into a pandas dataframe
    df = pd.DataFrame(email_tuples, columns=["name", "domain"])

    # Sort the dataframe by the domain column and then by the name column
    df = df.sort_values(["domain", "name"])

    # Combine the name and domain columns with '@' separator
    df["email"] = df["name"] + "@" + df["domain"]

    # Select only the email column for output
    output_df = df[["email"]]

    # Return the output dataframe
    return output_df


def app():
    # Define a text input for the list of emails
    email_list = st.text_area(
        "Enter a list of emails (one email per line). All duplicates will be removed. The list will be sorted by email domain in alphabateical order and then by name."
    )
    #  (Optional) Add a "Submit" button to trigger the processing of the emails
    emails_to_remove = st.text_area(
        "(OPTIONAL) Enter a list of emails to remove from the original list (one email per line). "
    )

    # Add a "Submit" button to trigger the processing of the emails
    if st.button("Submit"):
        # Process the email list using the process_emails function
        output_df = process_emails(email_list)

        emails_to_remove = process_emails(emails_to_remove)

        # only keep emails that are in output_df and not in emails_to_remove
        output_df = output_df[~output_df["email"].isin(emails_to_remove["email"])]

        # convert column "email" to a string split by \n
        output_df = output_df["email"].str.cat(sep="\n")

        # Write the output dataframe to the Streamlit app
        st.code(output_df)


if __name__ == "__main__":
    app()
