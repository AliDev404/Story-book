import story
from text import TextStyler, user_choice_level

def start():
    styler = TextStyler(default_color="bright_yellow", default_style="blink")

    styler.slow_print(story.STARTING + "\n\n")  # starting message

    for level in range(1, len(story.levels)):
        level = str(level)

        # Print level title (styled + slow)
        styler.slow_print(styler.style_text(story.levels[level]))

        # Print story text (slow)
        styler.slow_print(story.level_story[level] + "\n")

        # Print choices + get user input (slow + erase previous line if wanted)
        choice_text = "\n".join(story.choices[level])
        styler.slow_print(choice_text, erase=False)

        user = user_choice_level(story.choices[level])
        styler.slow_print(f"You chose: {user}\n", erase=True)

start()
