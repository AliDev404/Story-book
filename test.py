import story
from text import TextStyler

def start():
    styler = TextStyler(default_color="bright_yellow", default_style="blink")

    print(f"{story.STARTING}\n\n")
    for level in range(1, len(story.levels)):
        level = str(level)
        print(f"{styler.slow_print(styler.style_text(story.levels[level]))}\n{story.level_story[level]}")
        user = styler.slow_print(user_choice_level(story.choices[level]),erase=True)

start()
