"""
SPOOKY SYNTAX SYSTEM

Author: Jimmy Song
Course: CSCI 3725
Assignment: M7 - Poetry Slam
Date: November 24, 2024

Generation and evaluation of horror-themed poem
"""

import random
import pyttsx3
import os
import glob
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initial word lists following a theme of horror
subjects = ["A dark shadow", "An old man", "A ghostly figure", "The corpse",
            "A banshee", "The demon", "The spirit", "The possessed child",
            "The mangle body", "The dismembered body", "The faceless thing",
            "The malformed figure"]
verbs = ["lurched", "whispered", "screamed", "crawled", "dripped", "watched",
         "clawed", "reached", "tiptoed", "floated", "murmured"]
objects = ["through the darkness", "in the basement", "from the well",
           "into the abyss", "over the bones", "from the darkness"]
adjectives = ["rotting", "bloody", "screaming", "fading", "cold", "decayed",
              "emaciated", "putrid", "foul", "molding"]
places = ["under the bed", "in the haunted house", "on the abandoned road",
          "in the forgotten graveyard", "by the full moon",
          "in the abandoned asylum", "infront of the bloody altar",
          "under the blackened sky", "by the silent tomb",
          "on the abandoned road"]

# Expandable theme elements for evolving horror
themes = {
    'decay': ["decaying", "rotting", "flesh", "bones", "blood", "pale",
              "twitching", "putrid", "foul", "molding"],
    'paranoia': ["it’s watching", "I can’t escape", "a whisper", "a scream",
                 "its gaze", "everywhere I go"],
    'darkness': ["shadow", "blackness", "the void", "the abyss", "cold night",
                 "nothingness"],
    'death': ["the grave", "the end", "death", "resting place", "buried",
              "ashes", "deceased"]
}

def generate_sentence(previous_lines):
    """
    Generate a horror-themed sentence based on previous lines.

    This function dynamically selects random words from predefined lists 
    and constructs a sentence. It also expands on themes based on the 
    context provided by the previous lines to create a sense of continuity.

    Parameters:
        previous_lines (list of str): A list of previously generated lines 
                                      to inform the theme expansion.

    Returns:
        str: The generated horror-themed sentence.
    """

    # Dynamically update word lists based on previous lines
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object = random.choice(objects)
    adjective = random.choice(adjectives)
    place = random.choice(places)
    
    # Depending on previous content, expand on themes (paranoia, decay, etc.)
    if previous_lines:
        last_line = previous_lines[-1]
        # Increase the sense of unease or shift to another theme
        if 'watching' in last_line or 'gaze' in last_line:
            object = random.choice(themes['paranoia'])
        elif 'decay' in last_line or 'rotting' in last_line:
            adjective = random.choice(themes['decay'])
        elif 'shadow' in last_line or 'darkness' in last_line:
            subject = random.choice(themes['darkness'])
        elif 'death' in last_line or 'grave' in last_line:
            verb = random.choice(themes['death'])

    # Generate a new sentence using spaCy dependency parsing
    sentence = f"{subject} {verb} {adjective} {object} {place}."
    
    # Store the sentence for future context-building
    return sentence

# Function to generate the horror poem in a self-generating loop, given number
# of stanzas wanted
def generate_horror_poem(num_stanzas):
    """
    Generate a horror-themed poem with a specified number of stanzas.

    This function constructs a horror poem by generating sentences in a loop 
    and expanding on previous lines to create a theme-based narrative.

    Parameters:
        num_stanzas (int): The number of stanzas to generate.

    Returns:
        str: A string containing the full poem, with each stanza on a new line.
    """
    poem = []
    previous_lines = []
    
    # Number of stanzas
    for _ in range(num_stanzas):
        line = generate_sentence(previous_lines)
        poem.append(line)
        # Add the line to the context for the next generation
        previous_lines.append(line)
    
    return "\n".join(poem)

def speak(poem):
    """
    Speak the given poem out loud using the pyttsx3 text-to-speech engine.

    Parameters:
        poem (str): The poem to be spoken aloud.
    """

    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties
    engine.setProperty('rate', 100)  # Speed of speech
    engine.setProperty('volume', 0.6)  # Volume level

    # Make the engine say the poem
    engine.say(poem)

    # Wait for the speech to finish before continuing
    engine.runAndWait()

def display_poem(poem):
    """
    Display the poem with spooky visual effects using Matplotlib.

    This function uses Matplotlib to render the poem on a dark-themed background 
    with random font colors, sizes, and positions to enhance the spooky effect.

    Parameters:
        poem (str): The poem to be displayed with spooky effects.
    """
    # Choose Trattatello font from my local system, can be changed
    chosen_font = "Trattatello"

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Set the background color to dark, according to theme
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    
    # Hide axis lines
    ax.axis('off')

    # Title in spooky style (red Trattatello font)
    ax.text(0.5, 0.95, 'Your Spooky Poem', fontsize=30, ha='center', va='top', 
            color='red', fontname=chosen_font, alpha=0.9)
    
    # Display the poem with random spooky effects of size, color, etc.
    y_pos = 0.85
    for line in poem.split('\n'):
        ax.text(0.5, y_pos, line, fontsize=random.randint(12, 20), ha='center',
                va='top', 
                color=random.choice(['white', 'grey', 'red']), 
                fontname=chosen_font, alpha=0.8)
        y_pos -= 0.1  # Move down the line a bit

    # Show the plot
    plt.show()

def evaluate_sentiment(poem):
    """
    Evaluate the sentiment of the poem using VADER sentiment analysis.

    The function returns a compound score indicating the overall sentiment of 
    the poem, with values closer to -1 being negative and values closer to 1 
    being positive.

    Parameters:
        poem (str): The poem whose sentiment is to be evaluated.

    Returns:
        float: The compound sentiment score of the poem.
    """
    # Initialize the VADER sentiment intensity analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Get sentiment scores
    sentiment_scores = analyzer.polarity_scores(poem)  

    # Compound score for overall poem score
    compound_score = sentiment_scores['compound']

    return compound_score


def main():
    """
    Main function to interact with the user, generate a horror poem, and
    evaluate its sentiment and creativity.

    The user is asked for the number of stanzas they want, and the program
    generates a poem, speaks it, displays it with spooky effects, and evaluates
    its sentiment and creativity based on user feedback.
    """
    # Takes in number of stanzas desired by user
    num_stanzas = int(input("How many stanzas would you like?: "))

    poem = generate_horror_poem(num_stanzas)

    speak(poem)
    display_poem(poem)

    sentiment = evaluate_sentiment(poem)
    
    # based on the sentiment score, determine if poem is positive or negative
    positivity = "Neutral"
    if sentiment < 0:
        if sentiment < -0.7:
            positivity = "Very Dark"
        else:
            positivity = "Negative"
    elif sentiment == 0:
        if sentiment > 0.7:
            positivity = "Very Happy"
        else:
            positivity = "Neutral"
    else: positivity = "Positive"

    # Gather user feedback on creativity and negativity
    user_sentiment = int(input(
        "On a scale from 1-10, how negative/dark was the poem?: "))
    user_creativity = int(input(
        "On a scale from 1-10, how original was the poem?: "))
    
    # Calculate overallscore (1-20, 20 being the best)
    joint_score = sentiment * -1 * user_sentiment + user_creativity
    
    # get path to current directory to ensure compatability with other machines
    curr_directory = os.path.dirname(os.path.realpath(__file__))

    next_poem_index = (
        len(glob.glob(f"{curr_directory}/output/*.txt")) + 1
    )
    
    # Display poem and evaluation as text file
    text = (
        f"Created Poem:\n"
        f"{poem}\n\n"
        f"Sentiment (<0 means negative, >0 means positive): {str(sentiment)}\n"
        f"--> Therefore the Poem Seems {positivity}\n"
        f"User Negativity Sentiment (1-10): {str(user_sentiment)}\n"
        f"User Creativity Score (1-10): {str(user_creativity)}\n"
        f"Overall Score (1-20): {str(joint_score)}"
    )
    # write the poem and evaluation to output for future reference
    with open(
        f"{curr_directory}/output/"
        f"Poem_{next_poem_index}.txt", "w"
    ) as output_file:
        output_file.write(text)


if __name__ == "__main__":
    main()