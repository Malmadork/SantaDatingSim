# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define santa = Character(_("Santa"), color="#20943A")
define krampus = Character(_("Krampus"), color="#9E2F4F")
define jack = Character(_("Jack Frost"), color="#27BDC9")
define snowman = Character(_("Abonimable Snowman"), color="#7ECFD6")
define bernard = Character(_("Bernard"), color="#39AA45")
define me = Character("Me")
define unknown = Character(_("???"), color="#eee")


# The game starts here.

label start:

    # show screen baking_game(120)



    # show screen baking_game



    #pause 5.0

    init python:
        config.allow_skipping = False
        renpy.image("int_counter_0", Image("images/int_counter_0.png", xalign=0.01, yalign=0.01))
        renpy.image("int_counter_1", Image("images/int_counter_1.png", xalign=0.01, yalign=0.01))
        renpy.image("int_counter_2", Image("images/int_counter_2.png", xalign=0.01, yalign=0.01))
        renpy.image("int_counter_3", Image("images/int_counter_3.png", xalign=0.01, yalign=0.01))

        renpy.image("dec19th_img", Image("images/dec19th_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec20th_img", Image("images/dec20th_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec21st_img", Image("images/dec21st_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec22nd_img", Image("images/dec22nd_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec23rd_img", Image("images/dec23rd_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec24th_img", Image("images/dec24th_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec25th_img", Image("images/dec25th_img.png", xalign=0.01, yalign=0.16))

        christmas_spirit = 0
        santa_aff = 0
        krampus_aff = 0
        jack_aff = 0
        snowman_aff = 0
        bernard_aff = 0

        settings = ['Courtyard', 'Toy Shop', 'Santa\'s Office', 'Kitchen', 'Frozen Lake', 'Stables']

        day = 1
        interaction = 0
        max_interactions = 4

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    show int_counter_0:
        xalign 0.01
        yalign 0.01

    show dec19th_img:
        xalign 0.01
        yalign 0.16


    jump test_menu


    "You finally made it to the North Pole and today is your first day working at Santa’s Workshop. You feel nervous. Taking a moment to calm yourself, you release long puffs of air into the freezing atmosphere creating small clouds with each breath."

    label init_choice_a:
        menu:
            "I'm ready.":
                jump init_ready
            "I can't do this":
                jump init_close_game

    label init_ready:
        "You go inside Santa’s Workshop, enter into Toy Shop"

    label toy_shop_a:
        "Entering the Toy Shop, you immediately feel the energy of the Christmas season. All around you, tiny hammers are clacking, elves are bustling about, and toys are being charted off in every direction."
        "As you stand there in wonder of the workshop your eyes land on an angry elf quickly heading towards you with a pocket watch in hand."

        show eileen happy with dissolve

        unknown "You must be the new elf. First day of work and you're already 3 minutes late."

        menu:
            "I'm very sorry. It won't happen again":
                jump bernard_day_1_menu_1_1

            "Who are you?":
                jump bernard_day_1_menu_1_2

    label bernard_day_1_menu_1_1:

        unknown "I'll let it slide this time, but you better be on time from here on out"

        bernard "My name is Bernard. I am the Head Elf here at Santa's Workshop. You can call me Sir."

        $ bernard_aff += 1

        menu:
            "Can I call you 'Saint' Bernard?":
                "Bernard just stares at you for a moment. It seems he doesn't know how to respond."
                "Your small smile at the joke slowly fades. You cough and look to the side."
                bernard "Anyway"
            "'Sir' seems a little excessive. Are you a knight?":
                "Bernard looks at you and takes a deep breath in."
                bernard "Oooo you're a jokester huh?"
                bernard "I will not tolerate rudeness in my employees"

                $ bernard_aff -= 1
            "Yes Sir.":
                "You nod and listen to what Bernard has to say"

        jump bernard_day_1_final_interaction

    label bernard_day_1_menu_1_2:
        unknown "I am the Head Elf of Santa's Workshop, and you're unapologetically late. I will not tolerate rudeness in my employees."
        "He shakes his head."
        bernard "My name is Bernard. You may only address me as Sir."

        $ bernard_aff -= 1

        jump bernard_day_1_final_interaction

    label bernard_day_1_final_interaction:
        bernard "This here is the Toy Shop where all the toys are made. Your job will be to check all of the stations and make sure everything is ready for Christmas."
        bernard "Follow me to get your assignment."

    label init_close_game:
        "You chickened out and were fired for not showing up to work."
        jump close_game

    label test_menu:
        menu:
            "What Day is it?":
                jump what_day

            "What Interaction is it?":
                jump what_interaction

            "Add interaction":
                jump add_interaction

            "Go to map":
                jump game_map

    label what_day:

        "Today is day [day]"

        jump test_menu

    label what_interaction:

        "You have made [interaction] interactions today"

        jump test_menu

    label add_interaction:

        python:
            interaction += 1
            if(interaction >= max_interactions):
                day += 1
                interaction = 0

            if(renpy.showing("int_counter_0")):
                renpy.hide("int_counter_0")
                renpy.show("int_counter_1")
            elif(renpy.showing("int_counter_1")):
                renpy.hide("int_counter_1")
                renpy.show("int_counter_2")
            elif(renpy.showing("int_counter_2")):
                renpy.hide("int_counter_2")
                renpy.show("int_counter_3")
            elif(renpy.showing("int_counter_3")):
                renpy.hide("int_counter_3")
                renpy.show("int_counter_0")

            if(day == 2):
                renpy.hide("dec19th_img")
                renpy.show("dec20th_img")
            elif(day == 3):
                renpy.hide("dec20th_img")
                renpy.show("dec21st_img")
            elif(day == 4):
                renpy.hide("dec21st_img")
                renpy.show("dec22nd_img")
            elif(day == 5):
                renpy.hide("dec22nd_img")
                renpy.show("dec23rd_img")
            elif(day == 6):
                renpy.hide("dec23rd_img")
                renpy.show("dec24th_img")
            elif(day == 7):
                renpy.hide("dec24th_img")
                renpy.show("dec25th_img")

                #renpy.show("day_counter_0", at=[Transform(pos=(0.005, 0.005))])

        jump test_menu

    label game_map:

        $ renpy.call_screen("game_map", _layer="screens")

        #jump test_menu


    #image daybox = "day_box.png"
    # label intro:
    #
    #     "You finally made it to the North Pole and today is your first day working at Santa’s Workshop. You feel nervous and have to take a moment to calm yourself."
    #
    #     menu:
    #
    #         "I'm ready.":
    #             jump init_santa_workshop
    #
    #         "I can't do this.":
    #             jump init_end_game
    #
    # label init_santa_workshop:
    #
    #     show day_1_box:
    #         xalign -1.0
    #         linear 1.0 xalign 0.0
    #         pause 3.0
    #         linear 1.0 xalign -1.0
    #
    #     "You walk inside Santa's Workshop, and look around for the Toy Shop."
    #
    #     "You spot the Toy Shop, and notice someone angrily walking toward you."
    #
    #     show eileen happy
    #     with dissolve
    #
    #     unknown "You must be the new elf. First day of work, and you are already late."
    #
    #     menu:
    #
    #         "I'm very sorry.":
    #
    #             jump bernard_day1_menu_1_1
    #
    #         "Who are you?":
    #
    #             jump bernard_day1_menu_1_2
    #
    # label init_end_game:
    #
    #     "You chickened out and were fired for not showing up."
    #     "The End"
    #
    #     jump close_game
    #
    #
    # label bernard_day1_menu_1_1:
    #
    #     unknown "I’ll let it slide this time but you better be on time from here on out."
    #
    #     bernard "Anyway, I am the Head Elf. My name is Bernard, but you can call me Sir."
    #
    #     jump main_day_1_interaction_1
    #
    # label bernard_day1_menu_1_2:
    #
    #     unknown "I am the Head Elf of Santa’s Workshop and I will not tolerate rudeness in my employees."
    #
    #     bernard "My name is Bernard, but you may only address me as Bernard."
    #
    #     $ bernard_aff -= 1
    #
    #     jump main_day_1_interaction_1
    #
    # label main_day_1_interaction_1:
    #
    #     bernard "This here is the Toy Shop where all the toys are made. Your job will be to go to all the {color=#f00}stations{/color} in the workshop and make sure that everything is ready to go for Christmas."
    #     bernard "Follow me to get your assignment."
    #
    #     "Bernard leads you to a room with a sign above the door that reads {i}A Life Full of Wonder is a Life Full of Joy{/i}."
    #     "He opens it and a man with white hair, a beard, and dressed all in red is standing by a desk."
    #     "Bernard quickly tells him something then leaves the room. The man turns to greet you as the door shuts behind you."
    #
    #     jump close_game
    #
    # # These display lines of dialogue.
    #
    # # "I've worked at the North Pole for quite some time as an elf. I help make toys and other things for Santa... but I'm sure you know the rest. "
    # #
    # # "I've gotten to know all sorts of people at the North Pole."
    # #
    # # "Oh here comes my boss, Santa Claus."
    #
    #
    # # This shows a character sprite. A placeholder is used, but you can
    # # replace it by adding a file named "eileen happy.png" to the images
    # # directory.
    #
    # # show eileen happy
    # #
    # # santa "Ho Ho Ho! How is your work going today?"
    # #
    # # menu:
    # #
    # #     "Why are you so cheery today?":
    # #         jump santa_interaction_1_cheery
    # #
    # #     "I'm very busy at the moment.":
    # #         jump santa_interaction_1_busy
    #
    # label santa_interaction_1_cheery:
    #
    #     santa "It's almost Christmas! How could one not be jolly at this time of year!"
    #
    #     "How could I have forgotten? I must have been busy with my work..."
    #
    #     "Me" "Are your preparations going well?"
    #
    #     santa "Things are going well! Always busy of course!"
    #
    #     santa "Speaking of, I need to go check on how my sleigh and reindeer are doing."
    #
    #     menu:
    #
    #         "Would you like some help?":
    #             jump santa_interaction_2_help
    #
    #         "I will see you later then.":
    #             jump santa_interaction_2_leave
    #
    # label santa_interaction_2_help:
    #
    #     santa "I would love your help. Meet me the barn in about 15 minutes."
    #     santa "I'll be off, I forgot I also to also check up on other things."
    #     "Me" "I'll see you then!"
    #     "(You gained affection points for santa)"
    #
    #     $ santa_aff += 1
    #
    #     jump santa_interaction_2_end
    #
    #
    # label santa_interaction_2_leave:
    #
    #     santa "Alright. I will check back later to see how the toys are getting finished."
    #
    #     $ santa_aff -= 1
    #
    #     jump santa_interaction_2_end
    #
    # label santa_interaction_1_busy:
    #
    #     santa "You should get in the Christmas spirit! It's almost time you know"
    #
    #     jump santa_interaction_2_end
    #
    # label santa_interaction_2_end:
    #
    #     jump end
    #
    #     "I best finish working on some of my toys so I can meet Santa at the barn in time."
    #     "(This is a placeholder for the toy making minigame if we do one?)"
    #
    #     "Time to go meet Santa at the barn"
    #
    #     jump end
    #
    # label end:
    #
    #     "Thanks for playing!"
    #
    label close_game:

    # This ends the game.

    return
