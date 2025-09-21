import sys
import time
import os


class TextStyler:
    def __init__(self,  default_color=None, default_bg=None, default_style=None, default_delay=0):
        self.default_color = default_color
        self.default_bg = default_bg
        self.default_style = default_style
        self.default_delay = default_delay

        self.gothic_map = {
            "A": "𝕬", "B": "𝕭", "C": "𝕮", "D": "𝕯",
            "E": "𝕰", "F": "𝕱", "G": "𝕲", "H": "𝕳",
            "I": "𝕴", "J": "𝕵", "K": "𝕶", "L": "𝕷",
            "M": "𝕸", "N": "𝕹", "O": "𝕺", "P": "𝕻",
            "Q": "𝕼", "R": "𝕽", "S": "𝕾", "T": "𝕿",
            "U": "𝖀", "V": "𝖁", "W": "𝖂", "X": "𝖃",
            "Y": "𝖄", "Z": "𝖅",
        
            "a": "𝖆", "b": "𝖇", "c": "𝖈", "d": "𝖉",
            "e": "𝖊", "f": "𝖋", "g": "𝖌", "h": "𝖍",
            "i": "𝖎", "j": "𝖏", "k": "𝖐", "l": "𝖑",
            "m": "𝖒", "n": "𝖓", "o": "𝖔", "p": "𝖕",
            "q": "𝖖", "r": "𝖗", "s": "𝖘", "t": "𝖙",
            "u": "𝖚", "v": "𝖛", "w": "𝖜", "x": "𝖝",
            "y": "𝖞", "z": "𝖟"}


        self.script={
            "A": "𝓐", "B": "𝓑", "C": "𝓒", "D": "𝓓", "E": "𝓔", "F": "𝓕", "G": "𝓖", "H": "𝓗",
            "I": "𝓘", "J": "𝓙", "K": "𝓚", "L": "𝓛", "M": "𝓜", "N": "𝓝", "O": "𝓞", "P": "𝓟",
            "Q": "𝓠", "R": "𝓡", "S": "𝓢", "T": "𝓣", "U": "𝓤", "V": "𝓥", "W": "𝓦", "X": "𝓧",
            "Y": "𝓨", "Z": "𝓩",
        
            
            "a": "𝓪", "b": "𝓫", "c": "𝓬", "d": "𝓭", "e": "𝓮", "f": "𝓯", "g": "𝓰", "h": "𝓱",
            "i": "𝓲", "j": "𝓳", "k": "𝓴", "l": "𝓵", "m": "𝓶", "n": "𝓷", "o": "𝓸", "p": "𝓹",
            "q": "𝓺", "r": "𝓻", "s": "𝓼", "t": "𝓽", "u": "𝓾", "v": "𝓿", "w": "𝔀", "x": "𝔁",
            "y": "𝔂", "z": "𝔃",
        }       
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

    def slow_print(self, text, delay=0.05, clear_before=False):
        delay = delay if delay is not None else self.default_delay

        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        if clear_before:
            os.system('cls' if os.name == 'nt' else 'clear')

    def user_choice_level(self, text):
        if text:
            while True:
                print("Choose an option:")
                for i, opt in enumerate(text, start=1):
                    self.slow_print(f"{self.style_text(i, 'bright_cyan')}) {self.style_text(opt, 'bright_cyan')}\n", delay=None)
                userInput = input("")
                if userInput in ("1", "2"):
                    break
                else:
                    print("\a!!Invalid Input!!")
            self.slow_print("",clear_before=True)
            return userInput

    def font(self,text):
        fonted_text=""
        for i in text:
            if i in self.script:
                fonted_text=fonted_text+self.script[i]
            else:
                fonted_text=fonted_text+i
        return fonted_text


    def title(self,text):
        print(f"{self.style_text(self.font(text),"bright_yellow")}\n")

        
