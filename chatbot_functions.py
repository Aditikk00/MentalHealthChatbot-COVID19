""" functions for COVID-19 mental health chatbot"""

import random
import string
import pandas as pd
import nltk

nltk.download('punkt')

# pandas dataframe
col_names = ['First Name', 'Last Name', 'Grade/Year', 'Location', 'Nervous', 'Hopeless', 'Restless',
            'Depressed','Effort','Worthless','K6_Score', 'Pre-COVID',
            'Unable to work', 'Half capacity', 'Reason for visit']
# dataframe of single row created each time function run
psych_df = pd.DataFrame(columns = col_names)

# final dataframe withh all rows stored
full_psych_df = pd.read_csv('Cogs18_dataframe.csv')

# end chat taken from A3 Chatbots
def end_chat(input_list):
    """
    Function to end chatbot when user types 'quit'
    
    Parameters
    ----------
    input_list: list
        user input string converted to list.
    Returns
    -------
    output: Boolean
        if user enters 'quit', output = True and chatbot will end
    """
    if 'quit' in input_list:
        output = True
        
    else:
        output = False
        
    return output

# function taken from A3 Chatbots
def remove_punctuation(input_string):
    """
    removes punctuation from input string
    
    Parameters
    ----------
    input_string: string
        user input message
    
    Returns
    -------
    out_string: string
        output string with no punctuation
    """
    out_string = ''
    
    for char in input_string:
        
        # checks if character is not a punctuation and adds it to out_string
        if char not in string.punctuation:
            out_string += char
            
    return out_string

def string_to_list(input_string):
    """
    converts input string to a list of lower case words with no punctuation
    
    Parameters
    ----------
    input_string: string
        user input message
    
    Returns
    -------
    output_list: list
        input string broken into list of lower case words with no punctuation
    """
    
    input_string = remove_punctuation(input_string)
    
    # makes string all lower case
    input_string = input_string.lower()
    
    # splits words in a sentence into separate items in a list
    output_list = nltk.word_tokenize(input_string)
    
    return output_list

# Function to turn output list back to string
def list_to_string(input_list, seperator = ' '):
    """
    Converts input list of string objects to a string joined by separator
    
    Parameters
    ----------
    input_list: list
            the output message in the form of a list of string objects
    separator: string, default = ' '
            the string that will be used to separate the objects in input list
            
    Returns
    -------
    output: string
        output message in the form of a string
    """
    # modified from A3 which used for loop to concatenate
    output = seperator.join(input_list)
    
    return output

def to_dataframe(column, input_val):
    """
    Adds user input to specified column in DataFrame
    
    Parameters
    ----------
    column: string
        Name of column in DataFrame to add user input to
    input_val: list
        input message from user 
            
    Returns
    -------
    psych_df: DataFrame
        The dataframe that collects new data from chatbot function
    """
    
    user_input=[]
    
    # converts list of words input to string
    input_val = list_to_string(input_val)
    
    user_input.append(input_val)
    
    # adds user input to specified column
    psych_df[column] = user_input
    
    return psych_df

INTRO_MSG = 'Welcome to the COVID-19 Psychological Services chatbot. \n' +\
'The COVID-19 pandemic has brought a number of challenges to both our physical ' +\
'and mental health.\n'+\
'We understand that as students, this can be an even more stressful time. \n'+\
'Thank you for visiting us. Please have a chat with our chatbot \n' +\
'in order for us to collect the required information before ' +\
'your meeting with our psychologist \n' +\
'\n' +\
"Type 'quit' if you would like to exit at any time"

def intro(input_msg):
    """
    Intro greeting to get user name
    
    Parameters
    ----------
    input_msg: list
            user input full name in the form of list of words
    Returns
    -------
    output_msg: string
            Greeting message including user's name gained from input_msg
    """
    # gets first name and capitalizes
    f_name = input_msg[0].capitalize()

    output_msg = 'Hi ' + f_name + '! How are you feeling today?'
    
    return output_msg

greet_good_in = ['good', 'great', 'happy', 'ok', 'better']
greet_good_out = ['Awesome!', "That's great!", 'Happy to hear that!']
greet_bad_in = ['bad', 'sad', 'depressed','stressed','lonely','bored','tired']
greet_bad_out = ["It's good to hear from you", 'I hope we can help']

# selector function from A3 modified to suit 3 different lists
def greeting(input_list):
    
    """
    Check user input to 'how are you feeling' and select appropriate response
    
    Parameters
    ----------
    input_list: list
            user input response to 'how are you feeling'
    Returns
    -------
    output_msg: string
            random choice of string response from appropriate greetings list

    """
    
    output_msg = None 
    
    for item in input_list:
        
        # if user input is good or some synonym, corresponding output
        if item in greet_good_in:
            output_msg = random.choice(greet_good_out)
            break
            
        # if user input is bad or some synonym, corresponding output    
        elif item in greet_bad_in:
            output_msg = random.choice(greet_bad_out)
            break
            
        # if neither of the options above, generic response below  
        else:
            output_msg = "I'm looking forward to learning more about you"
            
    return output_msg

def location(input_list):
    
    """
    Gets location of user and generates corresponding output
    
    Parameters
    ----------
    input_list: list
            list of words from user input
    
    Returns
    -------
    output_msg: string
            corresponding output message depending on location
    """
    
    for item in input_list:
        
        # checks if student location in san diego or la jolla
        if item in ['diego', 'jolla']:
            output_msg = "Good to have you here. Please type 'Yes' to continue"
            # counter to keep track of question number in main chatbot function
            counter = 5
            break
            
        # if user not in SD or La Jolla   
        else:
            output_msg = "Hi from San Diego!. Please type 'Yes' to continue"
            
    return output_msg

# chatbot K6 segment 
def kesseler():
    
    """
    Chatbot segment for Kesseler Psychological Distress scale. 
    Gets user answer to K6 questions and calculates K6 score.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None 
    
    Note: run dataframe psych_df to see result of function
    """
    # Introduction message with info about Kesseler Psychological Distress scale
    print('We will now be using the Kesseler Psychological Distress scale (K6) to ask a few questions\n' +
         'For more information, visit: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3370145/')
    print('')
    print('0 = None of the time \n'+
         '1 = A little of the time \n' + 
         '2 = Some of the time\n' +
         '3 = Most of the time\n' + 
         '4 = All of the time')
    print('')
    
    # Attributes tested in K6 to ask in each question. 
    attributes = ['nervous?', 'hopeless?','restless or fidgety?',
                 'so depressed that nothing could cheer you up?',
                 'that everything was an effort?',
                 'worthless?']
    
    # Initializing score variable which will add total K6 score after each question
    score = 0
    
    for item in attributes:
        
        while True:
            
            try:
                # Question asked which attributes varied each time, collects user input
                print('During the past 30 days, how often did you feel ' + item)
                input_msg = input('Type Here: ')
                
                # Column names in Dataframe to add user input to
                k6_col_name = ['Nervous', 'Hopeless', 'Restless', 'Depressed','Effort','Worthless']
                
                # Iterates through attributes and column names together
                for single_attribute, col in zip(attributes, k6_col_name): 
                   
                    if 'quit' in input_msg:
                        break
                    
                    # Raise Value error if user input not 0-4
                    elif int(input_msg) not in range(0,5):
                        raise ValueError
                    
                    # Checks which attribute being asked in question and
                    #adds user input to corresponding
                    # column in DataFrame
                    elif item == single_attribute:
                        to_dataframe(col, str(input_msg))
                        
                        # calculates score after each iteration
                        score = score + int(input_msg)
                        
            # If user input not in 0-4, repeats same question again and prompts re-entry         
            except ValueError:
                
                print('Enter a number from 0 to 4. Try again')
                continue
                
            break
            
    # adds total score to score column in DataFrame
    to_dataframe('K6_Score', str(score))
    
def comparison_q(input_list):
    
    """
    Question to compare K6 results to pre-covid
    
    Parameters
    ----------
    input_list: list
            list of words from user input
    
    Returns
    -------
    output_msg: string
        corresponding string based on user input
    
    """
    for item in input_list:
        
        # if user responds more/less often, corresponding output
        if item in ['more', 'less']:
            output_msg = "COVID has been a major change for all of us. It's normal to feel this way"
            break
            
        # if user responds same, corresponding output
        else:
            output_msg = 'We hope this session helps you'
            
    return output_msg

def append_df(row_df):
    """
    Appends row dataframe created when chatbot run to main dataframe
    
    Parameters
    ----------
    row_df: DataFrame
        In this case will be psych_df which is created each time chatbot 
        run and contains one row only
    
    Returns
    -------
    full_psych_df: DataFrame
                Main dataframe with all data
    """
    # allowing full_psych_df to be used inside function
    global full_psych_df
    
    # appending row dataframe to main dataframe
    full_psych_df = full_psych_df.append(row_df)
    
    return full_psych_df

def question_1(user_inp):
    """
    Function to run first question and collect user data
    
    Parameters
    ----------
    user_inp: list
        Full name that the user will enter
    
    Returns
    -------
    output_msg: string
            same as output of intro() function. Greeting with user's name
    """
    # output is same as output of intro function
    output_msg = intro(user_inp)
    
    # stores user full name to DataFrame
    to_dataframe('First Name', user_inp[0])
    to_dataframe('Last Name', user_inp[-1])
    
    return output_msg

def question_2(user_inp):
    """
    Function to run second question and prompt next question
    
    Parameters
    ----------
    user_inp: list
            User response to 'How are you feeling today'
    
    Returns
    -------
    next_q: string
        Question 3 output
    """
    # output_msg same as output for greeting function
    output_msg = greeting(user_inp)
    print(output_msg)
    
    # Next question to ask
    next_q = 'What year are you at UCSD?'
    
    return next_q

def question_3(user_inp):
    """
    Function to collect user input from 3rd question and add to DataFrame
    
    Parameters
    ----------
    user_inp: list
            User response to 'What year are you at UCSD'
    Returns
    -------
    next_q: string
        prompts question 4 to be asked
    """
    # assigns first word entered to year
    year = user_inp[0]
    
    # output phrase using first word entered 
    output_msg = year + ' year is my favorite!'
    
    # saves year to DataFrame
    to_dataframe('Grade/Year', year)
    
    print(output_msg)
    
    # Question 4 prompted
    next_q = 'Please enter the city and country you are in currently'
    
    return next_q

def question_4(user_inp):
    """
    Function to collect user input from 4th question and add to DataFrame
    
    Parameters
    ----------
    user_inp: list
            User response with city and country name
    Returns
    -------
    output_msg: string
            same output as location function
    """
    # call location function
    output_msg = location(user_inp)
    
    # save data to DataFrame
    to_dataframe('Location', user_inp)
    
    return output_msg

def question_5():
    """
    Function to run kessler() and prompt next question
    
    Parameters
    ----------
    None
    
    Returns
    -------
    next_q: string
        prompts next question to ask
    """
    # asks series of questions from kesseler function
    kesseler()
    
    next_q = "Did the feelings mentioned above occur 'More Often', 'About the same', or " +\
                 "'Less often' during COVID-19"
    return next_q

def question_7():
    """
    Function to ask question 7
    
    Parameters
    ----------
    None
    
    Returns
    -------
    next_q: string
        next question to ask
    
    """
    
    next_q = 'During the past 30 days, how many days out of 30 were you totally ' +\
    'unable to work or carry out your normal activities because of these feelings?'
    
    return next_q

def question_8(user_inp):
    """
    Function to collect user response to question 8
    
    Parameters
    ----------
    user_inp: list
        user input to question
    Returns
    -------
    output_msg: string
        fixed text specified in function
    """
    
    output_msg = "Not counting the days you reported in response previously, " +\
    "how many days in the past 30 were you able to do only half or " +\
    "less of what you would normally have been able to do, because of these feelings?"
    
    to_dataframe('Unable to work', user_inp)
    
    return output_msg

def question_9(user_inp):
    """
    Adds user input to DataFrame and asks next question
    
    Parameters
    ---------
    user_inp: list
            user input as list of words
    Returns
    -------
    next_q: string
        Next question to be asked
    """
    to_dataframe('Half capacity', user_inp)
    
    next_q = 'What is the reason for your visit today?'
    
    return next_q

def question_10(user_inp):
    """
    Collect user input and final output message
    
    Parameters
    ---------
    user_inp: list
        User input for 'Reason for visit'
    Returns
    -------
    output_msg: string
        final output message
    
    """
    
    to_dataframe('Reason for visit', user_inp)
    
    output_msg = 'Thank you for your time. A representative will be in contact soon'
    
    return output_msg

def lets_talk():
    """
    Main chatbot function. Partially based on A3
    
    """
    # Introduction message + question asking full name
    print(INTRO_MSG)
    print('')
    print('\nPlease enter your first and last name')
    
    # counter to iterate through questions one by one
    counter = 1
    
    chatbot = True
    while chatbot:
        
        input_msg = input('Type Here: ')
        output_msg = None 
        
        # convert user input string to a list
        input_msg = string_to_list(input_msg)
        
        # end chat if user types in 'quit'
        if end_chat(input_msg):
            chatbot = False
        
        # counter counts through iteration of question, calls corresponding question function
        elif counter == 1:
            print(question_1(input_msg))
            counter += 1
            
        elif counter == 2:
            print(question_2(input_msg))
            counter += 1
            
        elif counter == 3:
            print(question_3(input_msg))
            counter += 1
            
        elif counter == 4:
            print(question_4(input_msg))
            counter += 1
            
        elif counter == 5:
            print(question_5())
            counter += 1
            
        # special case of iteration to calculate k6 score  
        elif counter == 6:
            # collects user input and adds to DataFramce
            output_msg = comparison_q(input_msg)
            to_dataframe('Pre-COVID',input_msg)
            
            # if user answered 0 for all K6 questions ('None of the time'), then survey ends here
            if '0' in psych_df.K6_Score.values:
                # Adds 'None' to columns of questions beyond 'Pre-COVID' question
                psych_df[['Unable to work', 'Half capacity', 'Reason for visit']] = 'None'
                print('Thank you for your time. A representative will be in contant soon')
                chatbot = False
            
            # else, further questions continued
            else:    
                print(output_msg)
                print("Type 'Yes' to move on")
                counter += 1

        elif counter == 7:
            print(question_7())
            counter += 1
            
        elif counter == 8:
            print(question_8(input_msg))
            counter += 1
        
        elif counter == 9:
            print(question_9(input_msg))
            counter += 1
            
        # Last question, chatbot ends
        elif counter == 10:
            print(question_10(input_msg))
            chatbot = False 
            
    # appends row dataframe created when running this function to main DataFrame
    append_df(psych_df)
    
    # DataFrame output to csv file
    full_psych_df.to_csv('Cogs18_dataframe.csv', index = False)