""" Test functions for COVID-19 Mental health chatbot"""
from chatbot_functions import *

def test_end_chat():
    """ tests the `end_chat` function """
    # tests if multiple words in input
    assert end_chat(['i','quit']) == True
    
    # tests type of output
    assert isinstance(end_chat('input'), bool)
    
    assert callable(end_chat)
    
def test_remove_punctuation():
    """ tests remove_punctuation function"""
    # checks that no punctuation in output
    assert string.punctuation not in remove_punctuation('!!HI, how@$# are you.')
    
    # tests empty string input
    assert remove_punctuation('') == ''
    
    # tests input with no punctuation to remove
    assert remove_punctuation('no punc') == 'no punc'
    
def test_string_to_list():
    """ tests string_to_list function"""
    # checks if output lower case only
    assert string_to_list('Hi there')==['hi','there']
    
    # checks that punctuation is not included in list
    assert len(string_to_list('two sentences. In one')) == 4
    
    # tests type of output
    assert isinstance(string_to_list('hi'),list)
    
def test_list_to_string():
    """ tests list_to_string function""" 
    # tests empty list
    assert list_to_string([]) == ''
    
    assert list_to_string(['1','hi']) == '1 hi'
    
    # tests type of output
    assert isinstance(list_to_string(['welcome','hi']),str)
    
def test_to_dataframe():
    """ tests to_dataframe function"""
    
    # checks DataFrame exists
    assert isinstance(to_dataframe('First Name', ['hi']),pd.core.frame.DataFrame)
    
    assert callable(to_dataframe)
    
def test_intro():
    """ tests intro function"""
    
    # tests if function capitalizes first name and if output selects first element in list
    assert intro(['first','last']) == 'Hi First! How are you feeling today?'
    
def test_greeting():
    """ tests greeting function"""
    
    # tests if output in correct corresponding list. Tests multiple elements in input_list
    assert greeting(['I','am','good']) in greet_good_out
    
    # tests type of output
    assert isinstance(greeting(['bad']),str)
    
def test_location():
    """ tests location function"""
    
    # tests first if statement
    assert location(['san','diego']) == "Good to have you here. Please type 'Yes' to continue"
    
    # tests if location not San Diego or La jolla
    assert location(['New', 'York']) == "Hi from San Diego!. Please type 'Yes' to continue"
    
def test_kesseler():
    """ tests kesseler() function"""
    
    assert callable(kesseler)
    
def test_comparison_q():
    """ tests comparison_q function"""
    test1 = "COVID has been a major change for all of us. It's normal to feel this way"
    
    # tests if input is 'same' 
    assert comparison_q(['same']) == 'We hope this session helps you'
    
    # tests if more than one element in input list
    assert comparison_q(['more', 'often']) == test1
    
def test_append_df():
    """ tests append_df function"""
    # tests if function callable
    assert callable(append_df)
    
    # tests type of output DataFrame
    assert isinstance(full_psych_df, pd.core.frame.DataFrame)
    
def test_question_1():
    """ tests question1 function"""
    
    # check if output same as intro function output
    assert question_1(['Sally','Wilson']) == intro(['Sally','Wilson'])
    assert callable(question_1)
    
def test_question_2():
    """ tests question2 function"""
    
    assert question_2(['good']) == 'What year are you at UCSD?'
    
def test_question_3():
    """ tests question3 function"""
    
    assert isinstance(question_3(['hi']),str)
    
def test_question_4():
    """ tests question4 function"""
    
    # check if output same as location function output
    assert question_4(['test']) == location(['test'])
    
def test_question_7():
    """ tests question7 function"""
    assert isinstance(question_7(),str)
    
def test_question_8():
    """ tests question 8 function"""
    assert isinstance(question_8(['test']),str)
    
def test_question_9():
    """ tests question 9 function"""
    assert isinstance(question_9(['test']),str)
    
def test_question_10():
    """ tests question 10 function"""
    test10 = 'Thank you for your time. A representative will be in contact soon'
    assert question_10('n/a') == test10

def test_lets_talk():
    """ tests lets_talk function"""
    assert callable(lets_talk)


    
 
    