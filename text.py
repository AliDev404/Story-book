import sys
import time

class TextStyler:
    def __init__(self, default_color=None, default_bg=None, default_style=None, default_delay=1):
        self.default_color = default_color
        self.default_bg = default_bg
        self.default_style = default_style
        self.default_delay = default_delay

        self.COLORS = {
            "black": 30, "red": 31, "green": 32, "yellow": 33,
            "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
            "bright_black": 90, "bright_red": 91, "bright_green": 92,
            "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
            "bright_cyan": 96, "bright_white": 97
        }

        self.BACKGROUNDS = {name: code + 10 for name, code in self.COLORS.items()}

        self.STYLES = {
            "bold": 1, "dim": 2, "italic": 3, "underline": 4,
            "blink": 5, "inverse": 7, "hidden": 8, "strike": 9
        }

    def style_text(self, text, color=None, bgcolor=None, style=None):
        color = color or self.default_color
        bgcolor = bgcolor or self.default_bg
        style = style or self.default_style

        codes = []
        if color in self.COLORS:
            codes.append(self.COLORS[color])
        if bgcolor in self.BACKGROUNDS:
            codes.append(self.BACKGROUNDS[bgcolor])
        if style in self.STYLES:
            codes.append(self.STYLES[style])

        code_str = ";".join(map(str, codes))
        return f"\033[{code_str}m{text}\033[0m" if codes else text

    def slow_print(self, text, delay=1, erase=False):
        delay = delay if delay is not None else self.default_delay

        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        if erase:
            time.sleep(1)
            sys.stdout.write('\r' + ' ' * len(text) + '\r')
            sys.stdout.flush()

    def user_choice_level(self, text):
        if text:
            while True:
                userInput = input(f"{self.style_text(text, 'bright_cyan')} : ")
                if userInput in ("1", "2"):
                    break
                else:
                    print("\a!!Invalid Input!!")
            return userInput

    def h_fonts(self):
        pass
