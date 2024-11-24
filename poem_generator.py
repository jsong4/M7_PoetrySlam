import spacy
import random

# import spaCy's language model to be used for dependency parsing
nlp = spacy.load("en_core_web_sm")

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

# Generate a horror-themed sentence using dependency structures
def generate_sentence(previous_lines):
    # Dynamically update word lists based on previous lines
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object_ = random.choice(objects)
    adjective = random.choice(adjectives)
    place = random.choice(places)
    
    # Depending on previous content, expand on themes (paranoia, decay, etc.)
    if previous_lines:
        last_line = previous_lines[-1]
        # Increase the sense of unease or shift to another theme
        if 'watching' in last_line or 'gaze' in last_line:
            object_ = random.choice(themes['paranoia'])
        elif 'decay' in last_line or 'rotting' in last_line:
            adjective = random.choice(themes['decay'])
        elif 'shadow' in last_line or 'darkness' in last_line:
            subject = random.choice(themes['darkness'])
        elif 'death' in last_line or 'grave' in last_line:
            verb = random.choice(themes['death'])

    # Generate a new sentence using spaCy dependency parsing
    sentence = f"{subject} {verb} {adjective} {object_} {place}."
    doc = nlp(sentence)
    
    # Store the sentence for future context-building
    return sentence, doc

# Function to generate the horror poem in a self-generating loop, given number
# of stanzas wanted
def generate_horror_poem(num_stanzas):
    poem = []
    previous_lines = []
    
    # Number of stanzas
    for _ in range(num_stanzas):
        line, doc = generate_sentence(previous_lines)
        poem.append(line)
        # Add the line to the context for the next generation
        previous_lines.append(line)
    
    return "\n".join(poem)

# Generate and print the self-generating horror poem
print(generate_horror_poem(4))