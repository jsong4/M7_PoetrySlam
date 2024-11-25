# M7_PoetrySlam

SPOOKY SYNTAX SYSTEM

Author: Jimmy Song\
Course: CSCI 3725\
Assignment: M7 - Poetry Slam\
Date: November 24, 2024

**HOW TO RUN:**

1) Make the following downloads in terminal:
        Download pyttsx3: "pip install pyttsx3"\
        Download matplotlib: "pip install matplotlib"\
        Download vaderSentiment: "pip install vaderSentiment"

        Note: Ensure that you have the "Trattatello" font in your computer
        (This is a standard font that should come with any macOS system).
        Otherwise, edit the "chosen_font" variable in the display_poem()
        function to one that is in your local device.
2) Run the poem_generator Python file
3) Input the desired number of lines/stanzas in the Terminal
4) After listening and seeing the outputted poem, close out of the Matplotlib
    pop-up window
5) Input the user review questions in the terminal
6) View Poem and Evaluation in the new text file added to 'output'

**DESCRIPTION:**

**Generation:**

The Spooky Syntax System creates a visually descriptive poem following the 
theme of horror and darkness. Taking from a pool of subjects, verbs, objects, 
adjectives, and places, the system randomly selects from each category 
and combines them into a scary line. Then, based on the number of lines 
desired by the user, the system will output more lines that will follow the 
previous theme. To create more continuity, it will expand upon themes 
of darkness, paranoia, decay, or death based on key words from the prior 
line.

To add to the theme of spookiness, the system uses a slowed and relatively 
quiet voice to read out the lines. It then uses matplotlib to display 
the poem, using a strange font and randomized sizes and colors to enhance 
this uneasy sensation.

**Creativity Evaluation Metrics:**

To evaluate the creativity of the outputted poem, the system strongly values 
user feedback, while also incorporating objective analysis. It asks the user 
how negative/dark the poem felt, as well as how original/novel the poem 
was to them. In addition, it uses vaderSentiment to give a compound score 
from -1 to 1 indicating how negative the text is, based on the words chosen.  
Since we want the poem to be as negative as possible, we ideally want the 
poem's score to be closer to -1.

Combining all these values of originality and value, we calculate a combined 
score between 1-20 for the performance of the generator. This number is 
derived from the negative of the vaderSentiment (because we want it to be 
negative) multiplied by the user sentiment, plus the user originality rating. 

**HOW WORKING ON THIS SYSTEM CHALLENGED ME AS A COMPUTER SCIENTIST:**

Creating this system challenged me as a computer scientist by making me 
use functionalities that I have never heard of before. For instance, I 
had to do research on how to make my system read my poem aloud. Another 
example would be the use of vaderSentiment -- I wanted to think of a 
non-user-based way to see how dark my poem really is, for instance by 
keeping track of the descrptive word choice, so I researched an came 
across vaderSentiment and learned how to incorporate it into my code 
and overall evaluation of my poems.

In a broader sense, working on this system was particularly challenging 
for me due to my other personal commitments resulting in a very limited 
amount of time available for this code. Having to balance the peak of 
my job application and interview process as a senior in college 
applying for full-time positions and other responsibilities as a leader 
in numerous on-campus teams and organizations made me ensure that my 
time spent on this system was optimal and efficiently used. I learned 
to error check, research new strategies, and evaluate my current work 
at much faster rates than before, which I believe made me a much 
stronger computer scientist all around.

**SCHOLARLY PAPERS THAT INSPIRED MY APPROACH:**

1) "[Evaluating Creativity in Computational Co-Creative Systems](https://arxiv.org/abs/1807.09886)"
   by Karimi, Grace, Maher, Davis

This paper discusses how computer programs that collaborate with 
human users should have their creativity be based on autonomous 
creative systems, not just user experience. This influenced me 
to incorporate an objective sentiment measurement with vader, not 
just listening to user feedback.

2) "[The Evaluation of Creative Systems](https://link.springer.com/chapter/10.1007/978-3-319-43610-4_8)"
   by Ritchie

This paper delves into how a lot of creative systems can only 
be evaluated subjectively and depend largely on the unique 
characteristics of each system. To calculate a more subjective 
POV on my system's output, I ask for users to provide their 
own feedback on how original and dark the created poem is.

3) 
