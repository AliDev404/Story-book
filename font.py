
def style_text(text, color=None, bgcolor=None, style=None):
    COLORS = {
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
        "bright_black": 90, "bright_red": 91, "bright_green": 92,
        "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
        "bright_cyan": 96, "bright_white": 97
    }

    BACKGROUNDS = {name: code + 10 for name, code in COLORS.items()}

    STYLES = {
        "bold": 1, "dim": 2, "italic": 3, "underline": 4,
        "blink": 5, "inverse": 7, "hidden": 8, "strike": 9
    }

    codes = []
    if color in COLORS: codes.append(COLORS[color])
    if bgcolor in BACKGROUNDS: codes.append(BACKGROUNDS[bgcolor])
    if style in STYLES: codes.append(STYLES[style])

    code_str = ";".join(map(str, codes))
    return f"\033[{code_str}m{text}\033[0m" if codes else text

