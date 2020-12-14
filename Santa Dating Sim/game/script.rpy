# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define santa = Character(_("Santa"), color="#20943A")
define krampus = Character(_("Krampus"), color="#9E2F4F")
define jack = Character(_("Jack Frost"), color="#27BDC9")
define snowman = Character(_("Abonimable Snowman"), color="#7ECFD6")
define bernard = Character(_("Bernard"), color="#39AA45")




# The game starts here.

label start:

    $ christmas_spirit = 0
    $ santa_aff = 0
    $ krampus_aff = 0
    $ jack_aff = 0
    $ snowman_aff = 0
    $ bernard_aff = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    "(This is a sample game I made, writing could be improved + visuals are placeholders from the engine)"



    # These display lines of dialogue.

    "I've worked at the North Pole for quite some time as an elf. I help make toys and other things for Santa... but I'm sure you know the rest. "

    "I've gotten to know all sorts of people at the North Pole."

    "Oh here comes my boss, Santa Claus."


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    santa "Ho Ho Ho! How is your work going today?"

    menu:

        "Why are you so cheery today?":
            jump santa_interaction_1_cheery

        "I'm very busy at the moment.":
            jump santa_interaction_1_busy

    label santa_interaction_1_cheery:

        santa "It's almost Christmas! How could one not be jolly at this time of year!"

        "How could I have forgotten? I must have been busy with my work..."

        "Me" "Are your preparations going well?"

        santa "Things are going well! Always busy of course!"

        santa "Speaking of, I need to go check on how my sleigh and reindeer are doing."

        menu:

            "Would you like some help?":
                jump santa_interaction_2_help

            "I will see you later then.":
                jump santa_interaction_2_leave

    label santa_interaction_2_help:

        santa "I would love your help. Meet me the barn in about 15 minutes."
        santa "I'll be off, I forgot I also to also check up on other things."
        "Me" "I'll see you then!"
        "(You gained affection points for santa)"

        $ santa_aff += 1

        jump santa_interaction_2_end


    label santa_interaction_2_leave:

        santa "Alright. I will check back later to see how the toys are getting finished."

        $ santa_aff -= 1

        jump santa_interaction_2_end

    label santa_interaction_1_busy:

        santa "You should get in the Christmas spirit! It's almost time you know"

        jump santa_interaction_2_end

    label santa_interaction_2_end:

        jump end

        "I best finish working on some of my toys so I can meet Santa at the barn in time."
        "(This is a placeholder for the toy making minigame if we do one?)"

        "Time to go meet Santa at the barn"

        jump end

    label end:

        "Thanks for playing!"


    # This ends the game.

    return
