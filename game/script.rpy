# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kai")

# The game starts here.

label start:

    "Kai wakes up early in the morning."

    jump island_1


label island_1:

    menu:
        "Kai doesn't know whether to stay inside or go out."

        "Stay inside":
            jump choice_1a
            
        "Go outside":
            jump choice_1b


label choice_1a:

    """
    Inside, Kai encounters his household dog Massie.
    
    Kai pets the dog.
    
    The dog reacts happily by licking his hand.
    """

    jump island_2


label choice_1b:

    "Kai goes outside the house."

    jump island_7


label island_2:

    menu:
        "The dog gets excited and starts becoming rougher. It grabs a toy and urges you to play."

        "Play with the dog":
            jump choice_2b
        
        "Stop and create distance":
            jump choice_2a


label choice_2a:

    """
    Kai stops playing and creates distance from the dog.
    
    He washes his hands and continues with his day.
    """

    jump island_2a


label choice_2b:

    """
    Kai continues playing with the dog.

    It accidentally scratches him.
    """

    jump island_2b


label choice_2bb:

    """
    Kai continues playing with the dog.
    
    Suddenly, it becomes too playful, licking him and the open wound from his fresh scratch.
    """

    jump island_3


label island_2a:

    """
    Kai comes back and feeds the dog.
    
    He takes the dog out. Kai notices stray dogs wandering around, so he avoids them and takes the dog back home.
    """

    jump ending_1


label island_2b:
    
    menu:
        "Kai inspects his wound.\n\nThere's no visible blood, only a red mark."

        "Clean the wound":
            jump choice_3a
        
        "Continue playing":
            jump choice_2bb


label choice_3a:

    """
    Kai cleans the wound with soap and running water for 5 to 15 minutes, applying  Betadine afterwards.
    """

    jump island_4


label choice_3b:

    """
    Kai doesn't think much of it, considering it a minor wound and does not wash the area. He ignores it.
    
    He recalls his friends' non-professional advise that since it was his household dog, his exposure doesn't need further medical attention.
    """

    jump choice_4b


label island_3:

    menu:
        "Kai inspects his wound.\n\nThere's no visible blood, only a red mark."

        "Clean the wound":
            jump choice_3a
        
        "Do nothing":
            jump choice_3b


label island_4:

    """
    Thinking deeply, Kai considers if the injury is serious or not as it was his own household dog.
    """

    jump choice_4a


label choice_4a:
    
    """
    After deciding, he goes visits the clinic in the same day and receives treatment:

        > Anti-tetanus shot
        > Anti-rabies vaccine (1st dose)
    
    The ABC personnel advises Kai that coming in within 24 hours after exposure was the right thing to do.
    """

    jump island_6


label choice_4b:

    """
    After 5 years, Kai starts shows symptoms of rabies.
        > Fever
        > Chills 
        > Muscle pain
        > Numbness
        > Headache 
        > Fear of water (hydrophobia) 
        > Fear or sensitivity to air/wind (aerophobia) 
        > Agitation or aggressive behavior

    Desperate, he searches online for remedies, which aren't formal sources of information.
    """

    jump island_5


label island_5:

    menu:
        "Kai decides whether to visit ABC or go directly to the hospital."
        
        "Go to an Animal Bite Center (ABC)":
            jump choice_5a
        
        "Go to the hospital":
            jump choice_5b
        

label choice_5a:

    """
    He goes to an ABC only to be advised to visit the hospital immediately as the anti-vaccine might no longer work because rabies symptoms are already present.
    """

    jump choice_5b


label choice_5b:

    """Kai is hospitalized."""

    jump ending_2


label island_6:

    menu:
        "The ABC Personnel advises Kai regarding the next follow-up doses:\n   > Anti-rabies vaccine (2nd & 3rd doses)"
        
        "Mark the date and come back as scheduled":
            jump choice_6a

        "Skip the scheduled doses":
            jump choice_6b


label choice_6a:

    """
    Kai completes the treatment successfully.
    """

    jump island_6bb


label choice_6b:

    """
    Kai skips the scheduled doses.

    His treatment is left incomplete. 
    """

    jump choice_4b


label island_6bb:

    menu:
        "Kai is anxious because he doesn't know if the dog has rabies or not.\n\nAfter being advised by the ABC, he has to decide whether or not to observe the dog for 14 days for rabies signs."

        "Ignore the dog":
            jump ending_3

        "Observe the dog for rabies":
            $ possibilities = ["possibility_a", "possibility_b"]
            $ possibility = renpy.random.choice(possibilities)
            $ renpy.jump(possibility)


label possibility_a:

    """
    Thankfully, his dog does NOT show signs of rabies.
    """

    jump ending_4


label possibility_b:

    """
    Kai's dog shows signs of rabies:
        > Changes in behavior  
        > Disoriented  
        > Aggression  
        > Hypersalivation  
        > Seizures  
        > Hypersensitivity to touch (hyperesthesia)  
        > Refusing to drink water 
        > Loss of appetite / refusing to eat
        > Death
    """

    jump island_8bb


label island_7:

    menu:
        "Kai sees his household dog in their family's front yard."

        "Ignore it and go outside":
            jump choice_7a

        "Interact with the dog":
            jump choice_7b


label choice_7a:

    """
    Kai goes outside and sees an aggressive dog roaming around the streets.
    """

    jump island_8


label choice_7b:

    """
    Kai opens the gate and feeds his dog.
    """

    jump island_9


label island_8:

    menu:
        "Suddenly, Kai sees the dog charging in his direction."

        "Kick the aggressive dog":
            jump choice_8a

        "Use an object (bag) to block the dog's attack":
            jump choice_8b


label choice_8a:

    """
    Kai quickly kicks the dog.
    
    After getting up, the dog charges and bites the his ankle.
    """

    jump island_8aa


label choice_8b:

    """
    Kai safely manages to block the dog, deterring it from attacking him again.

    He tries to avoid attracting its attention further.
    """

    jump island_6bb


label island_8aa:

    menu:
        "Kai inspects his wound and has to make a decision quickly."

        "Clean the wound":
            jump choice_3a

        "Do nothing":
            jump choice_8aaa


label island_8bb:

    menu:
        "Kai has to decide whether to contact the authorities or not."

        "Ignore the dog":
            jump ending_5

        "Report the dog to the authorities":
            jump ending_6


label choice_8aaa:

    """
    His wound gets infected and starts producing pus.
    """

    jump choice_4b


label island_9:

    menu:
        "Kai decides to return inside his house and opens the front door.\n\nAn outside dog sees their indoor dog, becoming aggressive and readying itself to attack."

        "Close the gate immediately":
            jump choice_9a

        "Block the gate using his feet":
            jump choice_9b


label choice_9a:

    """
    Kai closes the gate, preventing the dogs from attacking each other.
    """

    jump island_6bb


label choice_9b:

    """
    Kai blocks the aggressive dog using his foot.
    
    It lunges and bites his ankle.
    """

    jump island_10


label island_10:

    menu:
        "Kai carefully inspects his wound and decides whether to pay attention to his injury or not."

        "Do nothing":
            jump choice_8aaa
        
        "Clean the wound":
            jump choice_10a
    

label choice_10a:

    """
    Kai cleans the wound with soap and running water for 5 to 15 minutes, applying  Betadine afterwards.
    """

    jump island_12


label island_12:

    menu:
        "Kai decides whether to go to ABC immediately or not."

        "Dismiss the scratch":
            jump choice_4b

        "Go to an Animal Bite Center (ABC)":
            jump choice_4a


label ending_1:

    "ENDING 1\n\nKai is safe."
    return


label ending_2:

    "ENDING 2\n\nKai dies from rabies."
    return


label ending_3:

    "ENDING 3\n\nKai is safe. Whether the dog has rabies or not is unknown."
    return


label ending_4:

    "ENDING 4\n\nKai is safe and reassured. His dog remains healthy."
    return


label ending_5:

    "ENDING 5\n\nKai is safe but the dog can possibly transmit rabies to the nearby animals."
    return


label ending_6:

    "ENDING 6\n\nKai is safe while the authorities contain the dog to test for rabies, preventing further rabies transmision."
    return
