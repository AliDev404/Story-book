import story
import text

def start():
	print(f"{story.STARTING}\n\n")
	for level in range(1,len(story.levels)):
		level=str(level)
		print(f"{settings.style_text(story.levels[level],"bright_yellow",style="blink")}\n{story.level_story[level]}")
		user=settings.User_choice_level(story.choices[level])


start()

#work