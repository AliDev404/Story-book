import story
from text import TextStyler



def start():
    styler = TextStyler()
    for level in range(1,len(story.levels)):
        level=str(level)
        styler.title(story.levels[level])
        styler.slow_print(story.level_story[level]+"\n")
        user= styler.user_choice_level(story.choices[level])
start() 