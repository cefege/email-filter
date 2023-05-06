# Streamlit App for Sorting by Emails Domain alphabetically

This is a simple Streamlit app that takes a list of emails as input, processes them, and displays the output as a string split by '\n' using `st.code`.

## Installation

To run this app locally, you need to have Python 3.x installed. Clone this repository, and navigate to the project directory in your terminal. Then, run the following command to install the required dependencies:

```
pip install pandas streamlit
```

## Usage

To run the app, run the following command in your terminal:

```
streamlit run app.py
```

This will start the app on your local machine, and open it in a web browser. 

Once the app is running, you can copy and paste a list of emails into the text area, and then click the "Submit" button to process the emails. The app will remove any elements that do not contain '@', split the email list into a list of tuples containing the name and domain, sort the dataframe by the domain column, combine the name and domain columns with '@' separator, and display the resulting list of emails as a string split by '\n'.

## Code Structure

The app consists of two functions:

1. `process_emails`: This function takes a list of emails as input, processes them, and returns the resulting dataframe.
2. `app`: This function defines the Streamlit app, including the text area for inputting the email list, the "Submit" button for triggering the processing of the emails, and the output area for displaying the processed emails as a string split by '\n'.

The app uses the `pandas` library for data processing, and the `streamlit` library for building the web interface.