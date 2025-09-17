import story
from text import TextStyler

#def start():
#    styler = TextStyler(default_color="bright_yellow", default_style="blink")
#
#    print(f"{story.STARTING}\n\n")
#    for level in range(1, len(story.levels)):
#        level = str(level)
#        styler.slow_print(styler.style_text(story.levels[level])
#        story.level_story[level]
#        user = styler.slow_print(user_choice_level(story.choices[level]),erase=True)
#
#start()



def start1():
    styler = TextStyler()
    styler.slow_print("nope",erase=True)
    for level in range(1,len(story.levels)):
        level=str(level)
        styler.title(story.levels[level])
        user= styler.user_choice_level(story.choices[level])
start1()