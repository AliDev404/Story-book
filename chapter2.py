


TITLE="The Sunken Temple"

STARTING="Armed with a rope, a rusty dagger, and a single torch, you stand before the entrance of the Sunken Temple. Locals whisper of ancient riches hidden inside, but also of the Guardian that devours intruders. The air is damp, and a faint chanting echoes from below."

levels ={
     "1" : "Temple Entrance",
     "2" : "Hall of Statues",
     "3" : "The Broken Bridge",
     "4" : "The Serpent Attack",
     "5" : "The Hidden Offering",
     "6" : "Chamber of Echoes",
     "7" : "The Inner Sanctum",
     "8" : "The Guardian’s Trial",
     "9" : "The Treasure or the Trap"
}

level_story={
     "1" : "The cracked stone doors creak open. Moss covers every surface, and water drips from the ceiling. Two paths stretch forward: one lined with silent statues, the other descending into darkness.",
     "2" : "You step into a hall filled with towering stone statues. Their eyes seem to follow you. One of them begins to crack… something stirs.",
     "3" : "A rushing underground river blocks your way. A broken stone bridge hangs over the water, just stable enough to try crossing.",
     "4" : "From the shadows, a giant serpent lunges! You raise your dagger as it coils around you.",
     "5" : "You discover an alcove with an ancient bowl. The carvings suggest that making an offering here could protect you.",
     "6" : "The chamber hums with strange echoes. Your torchlight flickers, and a hidden doorway opens to the inner sanctum.",
     "7" : "You find a vast chamber. At its center lies a golden pedestal, upon which rests a jeweled crown. Suddenly, the Guardian emerges—half man, half beast, wielding a blazing spear.",
     "8" : "The Guardian towers over you. It demands strength or sacrifice. You must decide how to face it.",
     "9" : "You reach the pedestal. The crown glitters with unearthly light. But is it treasure, or a trap?"
}

choices={
     "1" : ("Enter the Hall of Statues","Take the path to the Broken Bridge"),
     "2" : ("Fight the awakening statue","Search for a hidden passage"),
     "3" : ("Attempt to cross the bridge","Climb down and swim across"),
     "4" : ("Fight the serpent","Flee toward the alcove"),
     "5" : ("Offer a gold coin","Ignore the bowl and move on"),
     "6" : False,
     "7" : ("Challenge the Guardian in battle","Attempt to trick the Guardian"),
     "8" : ("Fight with all your strength","Offer the crown as tribute"),
     "9" : False
}

choice_outputs={
     "1" : (2,3), 
     "2" : (4,5), 
     "3" : (4,6), 
     "4" : (6,5),
     "5" : (6,6),
     "6" : (7),
     "7" : (8,9),
     "8" : (9,0),
     "9" : 0
}

ends={
     1:"You defeat the Guardian with valor. The crown is yours, shining with eternal glory. Victory!",
     2:"The Guardian accepts your tribute and vanishes. The temple crumbles, but you escape alive—without treasure. The End.",
     3:"The Guardian’s power overwhelms you. Darkness consumes the Sunken Temple. The End."
}
