# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define santa = Character(_("Santa"), color="#20943A")
define claus = Character(_("Claus"), color="#20943A")
define krampus = Character(_("Krampus"), color="#D3B1B1")
define jack = Character(_("Jack"), color="#27BDC9")
define clarice = Character(_("Clarice"), color="#7ECFD6")
define bernard = Character(_("Bernard"), color="#39AA45")
define me = Character("Me", color="#eff")
define unknown = Character(_("???"), color="#eee")


# The game starts here.

label start:

    # python blocks can be used inside the script file.
    # init python always runs when the game starts, good for loading images and
    # initializing variables. (Python does not need to have a variable type in front of variables).
    #
    # you can just use "python:" for anything after the start, or
    # $ for single line code

    init python:
        # This makes the player unable to skip choice menus and dialogue.
        config.allow_skipping = False

        # This is how I loaded some of the images in. There are several ways you can load images in,
        # but this is how I chose to do it as it gave me flexibility with positioning.
        #
        # The syntax for adding an image this way is:
        # renpy.image( KEYWORD , Image( FILEPATH , ARGS )) # where ARGS is optional
        # The "int_counter_#" images were for the 4 interactions per day, but now I use "day_count_#"
        renpy.image("int_counter_0", Image("images/int_counter_0.png", xalign=0.01, yalign=0.01))
        renpy.image("int_counter_1", Image("images/int_counter_1.png", xalign=0.01, yalign=0.01))
        renpy.image("int_counter_2", Image("images/int_counter_2.png", xalign=0.01, yalign=0.01))
        renpy.image("int_counter_3", Image("images/int_counter_3.png", xalign=0.01, yalign=0.01))

        # These are the current interaction counter images
        renpy.image("day_count_0", Image("images/day_count_0.png", xalign=0.01, yalign=0.01))
        renpy.image("day_count_1", Image("images/day_count_1.png", xalign=0.01, yalign=0.01))
        renpy.image("day_count_2", Image("images/day_count_2.png", xalign=0.01, yalign=0.01))

        # These are the images for all of the days. Some are not used atm.
        renpy.image("dec19th_img", Image("images/dec19th_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec20th_img", Image("images/dec20th_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec21st_img", Image("images/dec21st_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec22nd_img", Image("images/dec22nd_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec23rd_img", Image("images/dec23rd_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec24th_img", Image("images/dec24th_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec25th_img", Image("images/dec25th_img.png", xalign=0.01, yalign=0.16))

        # A background for when the player goes to sleep
        renpy.image("dream_background", Image("images/dream_background.png"))

        # Images for the characters
        renpy.image("Bernard Rough", Image("images/Bernard Rough.png"))
        renpy.image("Claus Rough", Image("images/Claus Rough.png"))
        renpy.image("Jack Rough", Image("images/Jack Rough.png"))
        renpy.image("Krampus Rough", Image("images/Krampus Rough.png"))
        renpy.image("Clarice Rough", Image("images/Clarice Rough.png"))

        # Images for head shots in dual interactions
        renpy.image("Head Bernard", Image("images/Head Bernard.png"))
        renpy.image("Head Claus", Image("images/Head Claus.png"))
        renpy.image("Head Jack", Image("images/Head Jack.png"))
        renpy.image("Head Krampus", Image("images/Head Krampus.png"))

        # Images for backgrounds
        renpy.image("courtyard", Image("images/courtyard.jpeg"))
        renpy.image("toy shop", Image("images/toy_shop.jpeg"))
        renpy.image("frozen lake", Image("images/frozen_lake.jpeg"))
        renpy.image("stables", Image("images/stables.jpeg"))
        renpy.image("santa office", Image("images/santa_office.jpeg"))
        renpy.image("kitchen", Image("images/kitchen_bg.jpeg"))
        renpy.image("map_image", Image("images/map_image.png"))

        # affection counters
        claus_aff = 0
        krampus_aff = 0
        jack_aff = 0
        clarice_aff = 0
        bernard_aff = 0

        # used for dream description of the character you have most affection for
        max_aff_desc = "None"

        max_aff = "none"

        # used for sorting the arrays for getting highest affection
        def sort_aff(arr):
            return arr[1]

        # sorting arrays alphabetically
        def sort_alph(arr):
            return arr[0]

        # gets the dream description of the character you have most affection for
        def get_dream_desc():

            arr = []
            claus_a = ["claus", claus_aff]
            bernard_a = ["bernard", bernard_aff]
            krampus_a = ["krampus", krampus_aff]
            jack_a = ["jack", jack_aff]
            clarice_a = ["clarice", clarice_aff]

            arr.append(claus_a)
            arr.append(bernard_a)
            arr.append(krampus_a)
            arr.append(jack_a)
            arr.append(clarice_a)

            arr.sort(key=sort_aff, reverse=True)

            mf = "{u}a red cap with a white fluffy microphone. You smell the scent of chocolate and peppermint.{/u}"

            if(arr[0][1] == arr[1][1]):
                mf = "{u}but it quickly dissipates into nothing. You can faintly pick up some scents in the air, but they are muddled together.{/u}"
            else:
                if(arr[0][0] == "claus"):
                    mf = "{u}a red cap with a white fluffy microphone. You pick up the scent of chocolate and peppermint.{/u}"
                elif(arr[0][0] == "bernard"):
                    mf = "{u}a pocket watch ticking in the distance. You pick up the scent of sawdust, and hear a train whistle.{/u}"
                elif(arr[0][0] == "krampus"):
                    mf = "{u}a pair of curling horns. You pick up the scent of gingerbread and sugar.{/u}"
                elif(arr[0][0] == "jack"):
                    mf = "{u}a smile that sparkles as bright as the moon. You pick up on the scent of pine needles and brisk morning air.{/u}"
                else:
                    mf = "{u}a hairy six pack. You pick up the scent of freshly piled hay.{/u}"

            return mf

        # gets the 2 highest characters for dual interactions
        def get_highest_dual():
            arr = []
            claus_a = ["claus", claus_aff]
            bernard_a = ["bernard", bernard_aff]
            krampus_a = ["krampus", krampus_aff]
            jack_a = ["jack", jack_aff]
            clarice_a = ["clarice", clarice_aff]

            arr.append(claus_a)
            arr.append(bernard_a)
            arr.append(krampus_a)
            arr.append(jack_a)
            arr.append(clarice_a)

            arr.sort(key=sort_aff, reverse=True)

            return [arr[0], arr[1]]

        def get_highest_aff():
            arr = []
            claus_a = ["claus", claus_aff]
            bernard_a = ["bernard", bernard_aff]
            krampus_a = ["krampus", krampus_aff]
            jack_a = ["jack", jack_aff]
            clarice_a = ["clarice", clarice_aff]

            arr.append(claus_a)
            arr.append(bernard_a)
            arr.append(krampus_a)
            arr.append(jack_a)
            arr.append(clarice_a)

            arr.sort(key=sort_aff, reverse=True)
            if(arr[0][1] == arr[1][1]):
                return "none"
            else:
                return arr[0][0]


        high_dual = []

        # Used for counting the days and interactions
        day = 1
        interaction = 0
        max_interactions = 3

        # used for checking if you have already visited an area on day 2 especially
        current_location = 'None'
        areas_visited = []


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene dream_background

    # Shows the first interaction counter. It should already be aligned, but added alignment to be safe
    show day_count_0 onlayer screens:
        xalign 0.01
        yalign 0.01


    # Shows the first day counter. It should already be aligned, but added alignment to be safe
    show dec21st_img onlayer screens:
        xalign 0.01
        yalign 0.16

    # First day initial text
    "You finally made it to the North Pole and today is your first day working at Santa’s Workshop. You feel nervous. Taking a moment to calm yourself, you release long puffs of air into the freezing atmosphere creating small clouds with each breath."

    # The first choice the player makes.
    # Originally for day 1, I had it just jump to the correct label, but I soon realized that
    # doing things dynamically works better. I still have day 1 set up like this since
    # it works a bit different than day 2 in that there is not a limited interaction count.

    ### BEGIN DAY 1
    label init_choice_a:
        menu:
            "I'm ready.":
                jump init_ready
            "I can't do this":
                jump init_close_game

    label init_ready:

        scene toy shop
        "You go inside Santa’s Workshop."

    label toy_shop_a:
        "Entering into the Toy Shop, you immediately feel the energy of the Christmas season. All around you, tiny hammers are clacking, elves are bustling about, and toys are being charted off in every direction."
        "As you stand there in wonder of the workshop, your eyes land on an angry elf quickly heading towards you with a pocket watch in hand."

        show Bernard Rough with dissolve

        unknown "You must be the new elf. First day of work and you're already 3 minutes late."

        menu:
            "I'm very sorry. It won't happen again.":
                jump bernard_day_1_menu_1_1

            "Who are you?":
                jump bernard_day_1_menu_1_2

    label bernard_day_1_menu_1_1:

        unknown "I'll let it slide this time, but you better be on time from here on out."

        bernard "My name is Bernard. I am the Head Elf here at Santa's Workshop. You can call me Sir."

        $ bernard_aff += 1

        menu:
            "Can I call you 'Saint' Bernard?":
                "Bernard just stares at you for a moment. It seems he doesn't know how to respond."
                "Your small smile at the joke slowly fades. You cough and look to the side."
                bernard "Anyway..."
            "'Sir' seems a little excessive. Are you a knight?":
                "Bernard looks at you and takes in a deep breath."
                bernard "Ooooh you're a joker huh?"
                bernard "I will not tolerate rudeness in my employees."

                $ bernard_aff -= 1
            "Yes, Sir.":
                "You nod and listen to what Bernard has to say."

        jump bernard_day_1_final_interaction

    label bernard_day_1_menu_1_2:
        unknown "I am the Head Elf at Santa's Workshop, and you're unapologetically late. I will not tolerate rudeness in my employees."
        "He shakes his head."
        bernard "My name is Bernard. You may only address me as Sir."

        $ bernard_aff -= 1

        jump bernard_day_1_final_interaction

    label bernard_day_1_final_interaction:
        bernard "This here is the Toy Shop where all the toys are made. Your job will be to monitor all of the stations and make sure everything is ready for Christmas."
        bernard "Follow me to get your assignment."

    label santa_office_day_1_interaction:

        ### todo: Insert an image for location!!!
        scene santa office
        "{color=#39AA45}Bernard{/color} leads you to a room with a sign above the door that reads {i}A Life Full of Wonder is a Life Full of Joy.{/i}"
        "As {color=#39AA45}Bernard{/color} opens the door, you’re greeted by an overwhelming scent of hot chocolate, peppermint and cinnamon. Red walls with gold trim shine bright in the room as magical toys float through the air. Pacing around a desk in the center of the room is a large man dressed all in red."
        "He seems to be talking into the end of his hat as he strokes his white beard."
        "The man stops pacing as {color=#39AA45}Bernard{/color} approaches. Bernard quickly tells the man something then leaves the room. The man turns to greet you as the door shuts behind you."

        hide Bernard Rough with dissolve
        show Claus Rough with dissolve

        santa "You are here for the new position, right? {color=#39AA45}Bernard{/color} filled me in."
        santa "It's good to have the extra help at this time of year. Here is the list of tasks that need to be completed over the next week."

        "Santa hands you a piece of parchment paper. The assignments and locations written in a neat cursive. Turning the paper over reveals a map of the North Pole. You recognize a few of the areas."

        santa "You should take some time to familiarize yourself with the area. You can find the Kitchen next to the Toy Shop and the Stables are outback next to the Frozen Lake."


        menu:
            santa "Do you have any other questions?"

            "How would you like me to address you sir?":
                claus "Oh, I'm sorry, how rude of me. You can call me 'Claus', but I prefer it to Santa. I'm happy to have you on board here. It will be a real help."

                $ claus_aff += 1

                me "What about Mr. Claus?"

                claus "Ah... well, um..."
                "His energy suddenly shifts from the jolly tone he held a moment ago. It seems like he can't find the words to answer your questions."
                claus "Just... Claus is fine. No 'Mr.' needed."

                jump santa_interaction_day_1_1

            "Are you Tim Allen?":
                santa "Oh no, I'm a different Santa. And before you ask, I didn't kill anyone to get this position."
                claus "You can call me Claus."

                $ claus_aff -= 1

                jump santa_interaction_day_1_1

    label santa_interaction_day_1_1:
        claus "Now if you'll excuse me, I'm really busy with Christmas being right around the corner. If you need anything don't be afraid of asking Bernard. Oh! And feel free to help yourself to snacks from the Kitchen."
        claus "I'm glad to have your help."

        hide Claus Rough with dissolve

        #call add_interaction

        "You head back into the Toy Shop as {color=#20943A}Claus{/color} excuses you. All that hot chocolate and peppermint really made you hungry. Maybe you should go to the Kitchen next and get a bite to eat."

    label kitchen_interaction_day_1_1:

        scene kitchen

        "You find the Kitchen off the Toy Shop like {color=#20943A}Claus{/color} said. The Kitchen was massive in comparison to the elves who were snacking on milk and cookies."
        "Despite all the traffic, everything was quite clean. The marble countertops glistened while the hanging pots reflected the bright hats of the elves."
        "Following the scent of peppermint and gingerbread, you inquire about getting a bit to one of the elves. They point you to a man by one of the large ovens."

        "Removing a tray of cookies from the oven is a tall figure with horns and bull like legs. You notice he's only got on a pink apron with a gingerbread man on the front, but maybe if you're covered in black fur, you don't need clothes. He puts the tray down on the counter and looks up at you."

        show Krampus Rough with dissolve

        menu:
            unknown "Who are you and what are you doing in my kitchen?"

            "I'm the new hire. I was lured in by the amazing smell of your cookies. {color=#20943A}Claus{/color} suggested that I come here to get something to eat.":
                krampus "Ah, so you're the new manager they hired. I'm Krampus. This is my kitchen. Here, take some cookies while they're fresh."
                "You eat your fill of cookies and decide to investigate the rest of the workshop."

                $ krampus_aff += 1

            "I'm hungry.":
                krampus "What do you expect me to do about that? Just because I cook means I'm ombligated to feed you huh? I guess you're the new person they hired. I'm Krampus and I run this kitchen. Take these cookies and get out."

                $ krampus_aff -= 1

            "BEGONE HOT SATAN!":
                "A barrage of cookies rushes you and other elves out of the kitchen as pans clatter behind you."

                $ krampus_aff -= 5

        hide Krampus Rough with dissolve
        #call add_interaction
        jump stables_interaction_day_1_1

    label stables_interaction_day_1_1:

        scene stables

        "Munching on the freshly baked cookies, you see the stables and head over there because you want to see the famous reindeers. You walk in and see something like a well built rug as the scent of hay hits you."

        show Clarice Rough with dissolve

        menu:

            unknown "Ello, how can I help ya?"

            "Hello. I'm the new manager. I'm just looking around. It's nice to meet you.":
                clarice "So ye're the new boss. Welcome to the North Pole. Name's Clarice by the way and I'm the caretaker of these stables. Let me know if ya need anything."

                $ clarice_aff += 1

            "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa":
                clarice "Oh no, don't scream! Yer gonna upset the reindeer. I ain't gonna hurt ya. M' name's Clarice. I'm the caretaker of these stables."

                $ clarice_aff += 1

            "So you watch over the reindeer?":
                clarice "Yup! I feed 'em, brush 'em, train 'em. All day, Everyday so they're ready for Christmas. Oh! An' don't believe them fairy tales about reindeer and grandmas either. These guys won't run ov'r a fly. They're well trained."
                clarice "Name's Clarice. I have to prepare the reindeer's food so I must be goin', but feel free to come see the reindeer anytime ye want."

                $ clarice_aff += 0

        hide Clarice Rough with dissolve
        #call add_interaction
        "You head outside, realizing it just started to get dark."

        jump frozen_lake_interaction_day_1_1

    label frozen_lake_interaction_day_1_1:

        scene frozen lake

        "Outside, you follow the pasture fence until you come to a clearing. Surrounded by snow coated pine trees, you see a frozen lake reflecting the moonlight. You notice a figure gliding gracefully along its surface. As you walk to the lake's edge, the figure skates towards you."
        show Jack Rough with dissolve

        unknown "And who are you? I haven't seen your face before. Are you new around here?"
        me "I'm the new manager at the toy shop. And who are you?"

        jack "Name's Jack Frost. Everyone calls me Jack though. You showed up during the busiest time of year."

        menu:
            "Everyone certainly seems to be busy. Well, except you of course.":
                jack "Excuse you. Before you judge me, no, I'm not skipping work. I don't work at the workshop. I'm allowed to just come and go whenever I want to."

                $ jack_aff -= 1

            "I've got my work cut out for me. What are you doing out here? It's so peaceful.":
                jack "I'm having fun skating. It's great playing out here in the snow. You should join me sometime. The cold's always better with two."
                "He winks, and something sparkles in air."

                $ jack_aff += 1

        hide Jack Rough with dissolve
        "Jack skates away from you, and you decide to call it a day. You can't wait to start helping around the workshop tomorrow."
        show dream_background with dissolve
        "As you sleep, you start dreaming about a mysterious figure that keeps changing shape. What could it mean?"
        hide dream_background with dissolve

        pause .01
        $ day = 2
        hide dec21st_img
        show dec22nd_img onlayer screens:
            xalign 0.01
            yalign 0.16
        #call add_interaction

        jump game_map


    ### END DAY 1

    ### THESE ARE USED FOR ALL FUTURE DAYS
    label courtyard_init:

        scene courtyard

        $ current_location = "Courtyard"

        if current_location in areas_visited:
            if day == 2:
                "You wander around the fully decorated tree, and decide to try to visit another area."
            elif day == 3:
                "You wander around the fully decorated tree. You think a bit about what happened earlier, then you decide to try to visit another area."
            elif day == 4:
                "You wander around the tree. Some elves are gathered, waiting for Claus to leave. You decide to look at another area."
            jump game_map
        else:
            if day == 2:
                "Tying your snow boots and wrapping yourself in a scarf, you head out to the courtyard to decorate the central tree. The gigantic tree is at least 4 times your size. Tinsel in hand you stand there wondering how you, let alone the elves, are going to decorate this thing."
                "Holding a ball of lights, an elf wearing a mini jetpack zips around the tree stringing lights as he goes."
                "They whistle and another elf zips over. The elves move to either side of you and slowly lift you off the ground."
                "After suppressing a momentary feeling of panic, you smile and nod to the elves. They bring you towards the tree and circle you through the air around it. Soon the tree is completely decorated with ornaments, popcorn, and dazzling lights."
                "As you and the rest of the elves admire the tree, a younger elf tugs your shirt. Looking down, you notice they're holding a star out to you. With the help of the elves, you float to the top of the tree to add the final touch."
                "With the tree finished, you should go check the other areas."

                $ areas_visited.append("Courtyard")
                call add_interaction from _call_add_interaction
                jump game_map

            elif day == 3:

                python:
                    high_dual = get_highest_dual()
                    high_dual.sort(key=sort_alph)


                if(high_dual[0][0] == "bernard" and high_dual[1][0] == "claus"):
                    jump bernard_v_claus_day_3
                elif(high_dual[0][0] == "claus" and high_dual[1][0] == "krampus"):
                    jump claus_v_krampus_day_3
                elif(high_dual[0][0] == "claus" and high_dual[1][0] == "jack"):
                    jump claus_v_jack_day_3
                elif(high_dual[0][0] == "clarice" and high_dual[1][0] == "claus"):
                    jump clarice_v_claus_day_3
                elif(high_dual[0][0] == "bernard" and high_dual[1][0] == "krampus"):
                    jump bernard_v_krampus_day_3
                elif(high_dual[0][0] == "bernard" and high_dual[1][0] == "jack"):
                    jump bernard_v_jack_day_3
                elif(high_dual[0][0] == "bernard" and high_dual[1][0] == "clarice"):
                    jump bernard_v_clarice_day_3
                elif(high_dual[0][0] == "jack" and high_dual[1][0] == "krampus"):
                    jump jack_v_krampus_day_3
                elif(high_dual[0][0] == "clarice" and high_dual[1][0] == "krampus"):
                    jump clarice_v_krampus_day_3
                elif(high_dual[0][0] == "bernard" and high_dual[1][0] == "krampus"):
                    jump jack_v_clarice_day_3



                jump game_map

            elif day == 4:
                "You wander around the tree. Some elves are gathered, waiting for Claus to leave. You decide to look at another area."
                jump game_map

    label toy_shop_init:

        scene toy shop

        $ current_location = "Toy Shop"

        if current_location in areas_visited:
            if day == 2:
                "You walk back into the Toy Shop. Everyone seems busy with their work, and Bernard is inspecting the finished toys. You decide to head out and help somewhere else."
            elif day == 3:
                "You walk back into the Toy Shop. Everyone seems busy with their work, and Bernard is giving a final inspection on some of the consoles. You decide to head out and help somewhere else."
            elif day == 4:
                "You walk back into the Toy Shop. Bernard has a slight smile on his face as he prepares the last few toys. You decide to head out for now."
            jump game_map
        else:
            if day == 2:
                "You walk into the Toy Shop and see Bernard intensely inspecting some toys. He must have noticed a problem because he's pointing at the toy and audibly lecturing one of the elves. Turning around, he sees you and walks over."
                show Bernard Rough with dissolve
                bernard "You're late. I've got toy painting and assembly to do today. What do you want to do today?"

                menu:
                    "(Go help Bernard.)":
                        menu:
                            "I've come to help with the toy painting.":
                                bernard "Alright, follow me."
                                "He leads you over to a table with some wooden toy nutcrackers and paints of various hues. Both you and him sit at the table."
                                bernard "I'll show you how to paint them today since you don't have any experience yet. Watch carefully."
                                "He places a nutcracker in front of each of us and then hands you a brush before grabbing one for himself."
                                bernard "You'll paint the hat and shoes black, the chest red, and the pants blue."
                                "He proceeds to demonstrate how it's done, and puts it between us when finished to use as an example."
                                "After painting for a while, you consider asking him a question."
                                $ bernard_aff += 1

                            "I've come to help with toy assembly.":
                                bernard "Alright, follow me."
                                "He leads you over to a table with some wooden parts of various sizes and shapes. Both you and him sit at the table."
                                bernard "I'll show you how to assemble the toy planes, trains, and automobiles today since you don't have any experience yet."
                                "Bernard proceeds to build each of the different toys with components from each pile. Once completed, he puts the newly constructed toys in front of us to use as a reference."
                                "After amassing a good stock of toys, you consider asking him a question."
                                $ bernard_aff += 1

                        menu:
                            "What is it like being the Head Elf here?":
                                "Bernard sighs, clearly not interested in making small talk. At first you think he's just going to ignore you, but without looking up, he answers."
                                bernard "It's a demanding responsibility that requires you to be everywhere at once and know how to do everything. I, of course, am more than capable of fulfilling my role here. Hiccups only occur when other people don't do their jobs."

                                menu:
                                    "You sure sound full of yourself":
                                        bernard "I'm only stating the facts. As long as I'm in charge, nothing will disrupt Christmas from going off without a hitch. Enough talking. It'll distract from your work."
                                        $ bernard_aff -= 1

                                    "Seems like you do a good job from what I can tell.":
                                        bernard "I'm glad you can see that. Not everyone appreciates what I do around here. If that's all, lets focus on finishing this pile of toys."
                                        "You return to your duties. Taking another glance at Bernard, you notice that he looks sort of... relaxed."
                                        $ bernard_aff +=1

                            "(Don't ask anything)":

                                "You finish up with the toys for the day. Bernard thanks you for the hard work and you leave."
                                hide Bernard Rough with dissolve
                                call add_interaction from _call_add_interaction_1
                                $ areas_visited.append("Toy Shop")
                                jump game_map

                        "You finish making toys for the day and decide to head out. You say goodbye to Bernard as you leave and he thanks you for the hard work."
                        hide Bernard Rough with dissolve
                        call add_interaction from _call_add_interaction_2
                        $ areas_visited.append("Toy Shop")

                    "(Come back later, he seems stressed.)":
                        hide Bernard Rough with dissolve
                        "You decide to leave, and try to find another area to manage."

                jump game_map
            elif day == 3:
                "As you walk into the Toy Shop, Bernard is waiting for you to by the door."
                show Bernard Rough with dissolve

                bernard "Good.You’re here. I need you to come with me to the console section."

                menu:
                    "Alright, lead the way.":
                        "You follow Bernard over to a room at the back of the Toy Shop. Inside you see walls full of game consoles from every generation. Several elves are scrambling around the various tables and conveyors trying to assemble as many consoles as possible."
                        "You see a Soulja Boy console on one of the shelves and wonder why anyone would wish for that for Christmas when Bernard speaks up."
                        bernard "We are currently trying to meet the demand for PS5 and Xbox Series X consoles, but have run into an issue where a couple of the elves are sick. The two of us will have to cover the slack. We need to playtest the consoles and check for bugs."
                        "Bernard sighs and mutters as he heads off to some TVs..."
                        bernard "Of course, this just has to happen. Right when we’re so close to Christmas."

                        "You follow Bernard to a set of tvs each with a couple of consoles hooked up to them. He pops  ‘Bugsnax’ into my console and ‘Knack II’ in his. We sit down and start playing. Bernard tells me to note if I experience any issues with the system."
                        "After playing for a while, you glance over at Bernard who’s focused on the screen. He appears to be muttering to himself, almost like he’s talking to the game."

                        menu:
                            "So you do know how to have fun.":
                                bernard "This isn’t meant to be fun. It’s just another job. I wouldn’t even be doing this unless I had to."

                                menu:
                                    "Do you really only want to work all the time?":
                                        bernard "It doesn’t really matter what I want. I’m the Head Elf here. Without me things would be chaos. I have to make sure nothing goes wrong and I can’t do that if I’m ‘having fun’."
                                        "You can tell that Bernard means what he says, but there is something melancholy about his tone. You notice that his head is down and he’s staring at the controller. You realize there is one more thing you need to say."
                                        $ bernard_aff += 1

                                        menu:
                                            "What if you had someone to rely on?":
                                                "Bernard looks up at you then and meets your gaze. The slightest of smiles forms on his face and almost reaches his eyes."
                                                bernard "Maybe you're right."
                                                "Both of you go back to testing the consoles. For once, the silence felt quite peaceful and held a hint of something more."
                                                $ bernard_aff += 1
                                                hide Bernard Rough with dissolve
                                                call add_interaction from _call_add_interaction_3
                                                $ areas_visited.append("Toy Shop")
                                                jump game_map

                                            "That's rough buddy.":
                                                bernard "Ha, tell me about it. Nobody here understands what I go through everyday to make things perfect. Let’s hurry up and get this testing done. I’ve got other things that need to get done."
                                                "Both of you go back to testing the consoles. The silence is slightly uncomfortable until you’re finally allowed to leave."

                                                $ bernard_aff -= 1
                                                hide Bernard Rough with dissolve
                                                call add_interaction from _call_add_interaction_4
                                                $ areas_visited.append("Toy Shop")
                                                jump game_map

                                        #INSERT Here
                                    "You know you’re about as fun as Vanessa Hudgens in Christmas movies.":
                                        "Bernard pauses his game and blinks at you."
                                        bernard "First of all, I find that insulting. And secondly, why do I have to have fun?"
                                        bernard "I’m just supposed to make sure things run smoothly and everything’s ready to go for Claus on Christmas day. Playing will do nothing but waste time."
                                        "Bernard is clearly angry about what you just said. You realize you want to try and fix the current atmosphere."

                                        $ bernard_aff -= 1

                                        menu:
                                            "It's not bad to want to focus on work.":
                                                bernard "You say that, but everyone thinks I’m obsessed. What’s wrong with wanting everything to be perfect? You can’t do that by playing around."
                                                "Bernard sounds angry, but slightly hurt. You feel that he’s trying to justify something though it feels more like he’s trying to prove it to himself. There is something more to Bernard that you’re curious to find out."

                                                $ bernard_aff += 1
                                                hide Bernard Rough with dissolve
                                                call add_interaction from _call_add_interaction_5
                                                $ areas_visited.append("Toy Shop")
                                                jump game_map


                                            "It was just a joke.":
                                                bernard "You remind me of Jack and I don’t consider that a good thing. Jokes are for people with too much time on their hands."
                                                "It seems that Bernard is done talking. When you finish testing, Bernard walks away without saying anything else to you."

                                                $ bernard_aff -= 1
                                                hide Bernard Rough with dissolve
                                                call add_interaction from _call_add_interaction_6
                                                $ areas_visited.append("Toy Shop")
                                                jump game_map

                                        # INSERT HERE
                                    "Bugsnax is life BBYYY!":
                                        "He glares at you and tells you that this is work and not play time. You leave once you’re done with testing."
                                        $ bernard_aff -= 1
                                        hide Bernard Rough with dissolve
                                        call add_interaction from _call_add_interaction_7
                                        $ areas_visited.append("Toy Shop")
                                        jump game_map

                            "(He seems busy so I'll just focus on the game.)":
                                "The two of you finish up with testing. He thanks you for your help and you leave."
                                call add_interaction from _call_add_interaction_8
                                hide Bernard Rough with dissolve
                                $ areas_visited.append("Toy Shop")
                                jump game_map

                    "There is another matter I have to attend to.":
                        bernard "Fine. Hurry back."
                        hide Bernard Rough with dissolve
                        jump game_map
            elif day == 4:
                "As you walk up the path to the Toy Shop, you hear shouting. In a rush of panic, you open the door to see what is going on."
                "Near the center of the room, Bernard is screaming at a group of elves. This is the angriest you've ever seen him. You walk over to see what the problem is."

                show Bernard Rough with dissolve
                bernard "What do you mean that we're missing some presents?! It's Christmas Eve and Claus is to leave soon! We cannot afford a delay or even one hair out of place. Who was the one in charge of those packages anyway?"

                "One of the elves pipes up, \"You were, sir. A few consoles never made it to the packaging conveyor.\""

                "Bernard's face goes white as understanding hits him. You realize too that the consoles in question were the ones you had tested with Bernard. Bernard sees you, bringing him back to reality."

                menu:
                    bernard "We need to fix this."

                    "It's going to be okay Bernard. We'll find them.":
                        bernard "Okay? Okay?! What about this is okay? I've just ruined Christmas! How could I have made such a careless mistake? I'm supposed to be perfect."
                        "Bernard's anger was ebbing away into sobs as the weight of everything began to hit him. As his anxiety grows, you see that now is the time to get everything out in the open."
                        $ bernard_aff -= 1

                    "Let's get going. We don't have any time to lose.":
                        bernard "Right. If we hurry, we might be able to make it in time. I can't believe I let this happen. I don't make mistakes. I can't make mistakes."
                        "Bernard seems on the verge of panicking and his voice is almost coming out in sobs. You know that the two of you need to talk."

                me "Bernard. Everything will be alright. We'll get the presents in time. I know it's Christmas Eve, but you've been a second from breaking since I got here. There's no need to be like this."

                "Bernard nearly stops in his tracks but the need to get the consoles spurs him on."
                bernard "Easy for you to say. You've been perfect since you got here. It's taken me years to get where I am and now I've gone and blown it. All I wanted was Christmas to be perfect."
                "The concern on your face makes Bernard open up completely."
                bernard "All my life, Christmas has been the most important thing in my life. Stories of Santa flying through the night sky on a sled pulled by reindeer, of children all over the world waking up to find presents waiting for them."
                bernard"The idea that this Workshop brought such joy to those kids. I knew that I wanted to be a part of it."

                bernard "So, I joined as just another toy maker. Before I knew it, I was the head elf here. I kept telling myself that I was doing it for the children so I couldn't afford any mistakes."
                bernard "I always pushed myself and so I thought that I needed to do the same to everyone else. That way of thinking, it's made me a real asshole huh?"

                menu:
                    "(Nod)":
                        "We get the consoles and head back. Some elves take the consoles away to be packaged. Bernard apologizes to the elves. It may take some time, but you believe they’ll forgive him eventually."
                    "Definitely.":
                        "We get the consoles and head back. Some elves take the consoles away to be packaged. Bernard apologizes to the elves. It may take some time, but you believe they’ll forgive him eventually."
                "As the elves walk away, Bernard turns to you and with a smile on his face says, “I guess I’m perfect when I have you. Thank you, for everything.”"

                $ bernard_aff += 1

                hide Bernard Rough with dissolve
                $ areas_visited.append("Toy Shop")
                call add_interaction from _call_add_interaction_9
                call add_interaction from _call_add_interaction_10
                call add_interaction from _call_add_interaction_11
                jump game_map

    label santa_office_init:

        scene santa office

        $ current_location = "Santa Office"

        if current_location in areas_visited:
            if day == 2:
                "You peer through the glass of the office you visited earlier. You decide not to bother Claus as he looks busy reading through some letters and check out another area."
            elif day == 3:
                "You peer through the glass of the office you visited earlier. You decide not to bother Claus as he looks busy sorting out some presents and go to check out another area."
            elif day == 4:
                "You peer through the glass of the office you visited earlier. Claus' shoulders seem broader than usual and his eyes have a sparkle to them as he finishes some preparations."
            jump game_map
        else:
            if day == 2:
                "You decide to head to Santa's Office and see if you can help him with anything. Claus is behind his desk looking at a stack of papers. He notices you come in and gets up to greet you."
                show Claus Rough with dissolve
                claus "Ah, what brings you up here. Have you come to help me out today?"

                menu:
                    "I'm here to help.":
                        claus "I appreciate the help. Do you think you could go through my mail with me? The children's letters just keep coming and it seems to grow exponentially as Christmas gets closer."
                        "You walk over to his desk where he hands you a stack of letters, each a different color and size with various styles of handwriting in several different languages."
                        "Claus gestures to a wall with hundreds of openings and explains that they need to be sorted by country of origin."
                        claus "Just place the letter in the correct cubby based on the sender's address."
                        "You grab a stack of letters, then head over to the wall to begin orgainizing them. After a while, you glance over at Claus who's busy combing through some other documents. You consider asking a question."
                        $ claus_aff += 1

                        menu:
                            "What's it like being Santa Claus?":
                                "He looks up from his papers and takes off his glasses."
                                claus "It's a wondrous and rewarding job. A little repetitive though. Every year is the same: make a list, organize mail, oversee the workshop, deliver toys, and repeat."

                                menu:
                                    "Seems to be a lot of work.":
                                        claus "You are correct that there is a lot involved with this job, but it's so much more than that. The joy of these children is quite rewarding in its own way."
                                        "His eyes brush over the wall of letter slots with a sort of sparkle."
                                        claus "This job is my life and I do not know what else I would do. I appreciate all your help with the letters."
                                        "You finish sorting all the letters and decide to leave. You say goodbye, but Claus doesn't respond. He seems occupied with the documments on his desk. You think he looks quite tired as you head out the door."

                                        $ claus_aff += 1
                                    "Why bother doing all that?":
                                        "Claus frowns a bit."
                                        claus "If I do not, who will? I am Santa Claus; not some stranger at the mall. It is my responsibility to fufill the wonder of Christmas. I would think that would be obvious to everyone here."

                                        "Leaving you in silence, you finish up the letters and see yourself out. You feel guilty as you walk out the door."

                                        $ claus_aff -= 1

                                hide Claus Rough with dissolve
                                $ areas_visited.append("Santa Office")
                                call add_interaction from _call_add_interaction_12
                                jump game_map

                            "(You think better of it, and decide not to say anything.)":
                                "You go through all the letters and decide to leave. He thanks you on your way out."
                                hide Claus Rough with dissolve
                                $ areas_visited.append("Santa Office")
                                call add_interaction from _call_add_interaction_13
                                jump game_map



                    "Just checking in. I actually have something else to do.":
                        claus "Okay. Come back anytime."
                        jump game_map

                # $ areas_visited.append("Santa Office")
                #
                # jump game_map
            elif day == 3:
                "You walk into the Office, but Claus is nowhere to be seen. You walk over to his desk to see if he left a clue about where he went. Something catches your eye and you see that it’s a photo with a man in front of a sleigh."
                "It appears to be Claus, yet, while his features are still the same, he seems full energy and his smile lights up his whole face. It’s a Claus that truly embodies the wonder and joy of Christmas."
                "You start wondering what happened to that Claus when the door to the Office opens and in steps the current Claus."

                show Claus Rough with dissolve

                claus "Oh, did you have business with me today? Sorry, I had to check up on Donner. Apparently, he got hold of Krampus’ sweets again. Did you need anything?"

                menu:
                    "I was wondering if you need any help today.":
                        "I can always use the help. Work keeps piling up on me as the clock ticks down. How about you help me with ..."
                        "He trails off as he notices the picture in your hands. The way he gets quiet as he sees the image makes you worried."
                        $ claus_aff += 1

                        menu:
                            "Sorry for looking at this, but this is you right?":
                                claus "Yes, it’s me. It was taken in the early years after I took over Santa’s Workshop. Things were simpler back then and there was less to do."
                                claus "Now there’s more of … of everything, but I’ll deliver the presents to all the children like I do every year. I’m Santa after all, who else is gonna do it."
                                "Claus had a smile on his face as he started to reminisce, but it quickly faded as he came back to present day."

                                $ claus_aff += 1

                                menu:
                                    "I’m sure the children really appreciate everything you do.":
                                        claus "I know deep down that you're right, but it’s so much harder to connect with them nowadays. They just want more and I have to keep ramping up production and expanding to keep up with the demand. It’s just more to manage and more to do."
                                        "Claus seems dispirited after speaking and you try to cheer him up."

                                        $ claus_aff += 1

                                        menu:
                                            "I believe you can do it.":
                                                claus "Thank you. Hiring you is probably one of the best things I’ve done. I don’t know what I would do without your help."
                                                "Claus looks at you with a smile on his face. You decide to ask him what he wanted help with. After doing present inventory, you leave with the image of a joyful Claus stuck in your head."
                                                $ claus_aff += 1
                                                call add_interaction from _call_add_interaction_14
                                                hide Claus Rough with dissolve
                                                $ areas_visited.append("Santa Office")
                                                jump game_map

                                            "I'm sure it can't be that bad.":
                                                claus "You’ll understand how much worse it gets when you’ve been here for a few years. Now, I really need to get this present inventory completed."
                                                "You help Claus with the inventory. He thanks you and you leave. You wonder if there was more you could’ve done to make him feel better."

                                                $ claus_aff -= 1
                                                call add_interaction from _call_add_interaction_15
                                                hide Claus Rough with dissolve
                                                $ areas_visited.append("Santa Office")
                                                jump game_map

                                    "Everyone around the world relies on you.":
                                        claus "You don’t need to remind me about that. I’m well aware how much the children are depending on me. If I miss even one house, one child, or even one present, then I’ve ruined Christmas."
                                        "Claus' words were sharp and he seemed to be brooding afterwards. You try to calm him down."

                                        $ claus_aff -= 1

                                        menu:
                                            "I don't think anything can go wrong with you as Santa":
                                                claus "I appreciate the confidence, but that’s why I have to put so much effort in to ensure that all the children are happy. Things used to be so much easier."
                                                "Claus sighs..."
                                                claus "Anyway, can you help me finish the present inventory?"
                                                "The two of you finish the present inventory. Claus’s mood seems a little better but something is still bothering him as you leave."

                                                $ claus_aff += 1
                                                call add_interaction from _call_add_interaction_16
                                                hide Claus Rough with dissolve
                                                $ areas_visited.append("Santa Office")
                                                jump game_map

                                            "Christmas isn’t ruined if you make one mistake.":
                                                claus "How could it not be? Can you imagine how a child would feel if they woke up and they didn’t get a single present? It would devastate them."
                                                "Claus takes a deep breath as he controls the sorrow that washes over him."
                                                claus "Please help me with the present inventory so we ensure that doesn’t happen."
                                                "Once inventory is done, you head out of the Office. You leave Claus in a foul mood."

                                                $ claus_aff -= 1
                                                call add_interaction from _call_add_interaction_17
                                                hide Claus Rough with dissolve
                                                $ areas_visited.append("Santa Office")
                                                jump game_map

                            "Sorry for picking this up without permission.":
                                "You put the picture back and ask him what he needs help with. He accepts your apology and then he sets you to helping him with categorizing presents. After you’re done, Claus thanks you and you head out."

                                call add_interaction from _call_add_interaction_18
                                hide Claus Rough with dissolve
                                $ areas_visited.append("Santa Office")
                                jump game_map


                    "No, I'm good. See you later.":
                        "You head out of the office looking for somewhere else to go."
                        hide Claus Rough with dissolve
                        jump game_map
            elif day == 4:
                "You go to Claus’s Office and notice Claus is frantically talking on his earpiece. You go in to see what is wrong. Claus notices as you walk in."
                show Claus Rough with dissolve
                claus "Good. You’re here. If I have to listen to the elves about proper present presentation. Even Krampus was nagging me to eat every bloody cookie and drink all my milk. Krampus!"
                claus "He seriously has the nerve to tell me that I’m not acting like Santa. I’m delivering the presents aren’t I? What more can they expect from me? I don’t have time to treat every child like they’re some precious jewel!"
                "You could see the anger rising in Claus. He was no longer {i}Santa{/i}, just a man who had been pushed past the point of exhaustion. You want to say something to help him."

                menu:
                    "I’m here to help you. Remember?":
                        claus "Yes, I remember. I needed … no, I need help and there you were. It was like a Christmas miracle, but a miracle doesn’t deliver all these presents. I do. And I just can’t keep up."
                        "Claus slumps against his desk. A man defeated. You recall seeing something when at his office earlier and you go to retrieve it."
                        $ claus_aff += 1

                    "What do you want me to do?":
                        claus "You’ve done everything you can, but no matter how helpful you are, you can’t be {i}Santa{/i}. It’s a burden I have to carry alone. I chose this and there’s no backing out."
                        "Claus is firm in his resolve, but the magic that twinkled in his eyes is no longer there. You need to remind him why he’s Santa."
                        $ claus_aff -= 1
                "You go to the back of the office and retrieve an old and well worn letter. You stand directly in front of Claus and hold out your hand so that he’ll take the letter."

                menu:
                    claus "What's this?"

                    "Your purpose":
                        "Claus opens the letter and tears start to fall as he reads it. He makes sure that not a single drop hits the paper."
                    "Why you became {i}Santa{/i}":
                        "Claus opens the letter and tears start to fall as he reads it. He makes sure that not a single drop hits the paper."
                claus "This was the first letter I ever received as Santa. Little Sophie. She was just 5 years old and all she wanted was a little bell. Sophie kept that bell all her life and she would send a letter every year."
                claus "She even sent Thank You notes the day after Christmas. I remember the way her cookies tasted. They were the best I ever had."
                claus "When she got older she would knit sweaters and give them out to all the children as she went caroling. Each sweater unique. To this day, I miss her."
                "Claus’ eyes fill with tears and he chokes back a sob. He looks at you with such despair. "
                claus "\"What have I become?\" (He wails.) \"I became Santa because I loved the wonder of Christmas. Not to become some lifeless shipping company! Well that ends today.\""
                claus "From now on, I’m not leaving each house till every present is just right and no plate shall go untouched. Christmas is not about things, it’s about touching other’s hearts."
                claus"I do this for the children and the hopes that they’ll never lose that wonderful magic."
                "Claus springs to action. The sadness and exhaustion that had mired him was now gone. As he bounds out the door, he stops to look at you."
                pause .05
                claus "Thank you. For showing me how lost I had become. For a life full of wonder is a life full of joy."
                $ claus_aff += 1

                hide Claus Rough with dissolve
                $ areas_visited.append("Santa Office")
                call add_interaction from _call_add_interaction_19
                call add_interaction from _call_add_interaction_20
                call add_interaction from _call_add_interaction_21
                jump game_map


    label kitchen_init:

        scene kitchen

        $ current_location = "Kitchen"

        if current_location in areas_visited:
            if day == 2:
                "You wander past the kitchen. Krampus looks focused on making some more dough. You decide it's best to leave him be at the moment and go somewhere else."
            if day == 3:
                "You wander past the kitchen. Krampus looks focused on making some more decorations. You decide it's best to leave him be at the moment and go somewhere else."
            if day == 4:
                "You wander past the kitchen. Krampus looks focused on making a batch of cookies, and some elves are there watching. You decide it's best to leave him be at the moment and go somewhere else."
            jump game_map
        else:
            if day == 2:
                "You walk into the Kitchen and see it teeming with life as elves go to and fro between stations. The Christmas aroma washes over you as you see Krampus working at the island."
                menu:
                    "(Walk over to Krampus)":
                        show Krampus Rough with dissolve
                        krampus "You're back again are you? What do you want this time?"
                        menu:
                            "I would like to help out around here.":
                                krampus "Really now? I guess you can help me bake some cookies. The elves are voracious little things that only consume sugar. They need a lot of cookies to keep up their pace and get everything done by Christmas."
                                "He leads you over to a counter with jars and dishes of ingredients to make the cookies. Krampus quickly prepares a batch of cookie dough that he cuts into different shapes. Once the cookies are ready to go, he puts them in the oven."
                                "Together, you start working on making several more sheets of cookies. Standing next to him, you work up the courage to ask him something."
                                $ krampus_aff += 1

                                menu:
                                    "How come you're a baker?":
                                        krampus "Why not? I've always enjoyed baking and it's nice to be in charge of people. Why do you ask like it's weird for me to make sweets?"
                                        menu:
                                            "The stories always described you so differently, but I guess they're just stories after all.":
                                                krampus "Those old stories always did like to exaggerate. I was simply scolding naughty children and giving them coal as Claus made his rounds. I stopped going out a long time ago. People just assumed I was the bad guy because of the coal, and a monster because of how I looked."
                                                "Krampus seems to roll the cookies a bit faster as he reminisces."

                                                menu:
                                                    "(Reach out to touch his arm)":
                                                        "Krampus pauses as he glances towards your hand. He moves away to get the cookie cutters."
                                                        $ krampus_aff -= 1
                                                    "I'm sure they'd think differently if they tasted your cookies.":
                                                        "Krampus gives a chuckle and cracks a smile."
                                                        $ krampus_aff += 1

                                                krampus "I'm glad you are at least a little more open minded. You did a good job today. Why not take some cookies to go as a treat."
                                                "You head out of the kitchen covered in flour with delicious cookies stuffed in your mouth. You were glad to have talked to him."
                                                hide Krampus Rough with dissolve
                                                $ krampus_aff += 1
                                                $ areas_visited.append("Kitchen")
                                                call add_interaction from _call_add_interaction_22
                                                jump game_map

                                            "I always assumed that you were like Jimmy Brando from the Scarygodmother Wiki":
                                                "Krampus looks appalled."
                                                krampus "I'm not some imp with animation issues or a Victorian woman who whips children. All I did was give children a simple slap on the wrist when they misbehaved. It's rude to just assume people are monsters when you don’t even know them. I'll take care of the rest. You can go."
                                                "You walk out the kitchen and feel bad about having judged him."

                                                hide Krampus Rough with dissolve
                                                $ krampus_aff -= 1
                                                $ areas_visited.append("Kitchen")
                                                call add_interaction from _call_add_interaction_23
                                                jump game_map


                                    "(You realize that it would be silly to ask, and decide not to)":
                                        "You make a large amount of cookies until it is time for you to go. Krampus thanks you for the help and advises you wash up after you leave."
                                        hide Krampus Rough with dissolve
                                        $ areas_visited.append("Kitchen")
                                        call add_interaction from _call_add_interaction_24
                                        jump game_map

                    "(Go somewhere else)":
                        "You decide to visit another area."
                        jump game_map


                # $ areas_visited.append("Kitchen")

                jump game_map
            elif day == 3:
                "Walking into the Kitchen, you're greeted by several of the elves as you walk toward the back. Some of them offer you sweets and you happily take them."
                "Nibbling your treats, you come up to Krampus’ corner where he has bags of sugar, bowls of food coloring, various candies, and a dozen spools of string. He looks up from what he’s doing."

                show Krampus Rough with dissolve
                krampus "Bout time you showed up. I need help making ornaments and all the elves are busy making their own decorations."

                menu:
                    krampus "You in?"

                    "Of course, sounds fun.":
                        krampus "Good choice. These ornaments are gonna be the best in all of the North Pole. You can use whatever you want here on this table. Let me know if you need help."
                        "You cut a length of string and start grabbing random candies. Krampus is skillfully making little, delicate wreaths. You consider starting a conversation with him."

                        $ krampus_aff += 1

                        menu:
                            "Did you not want to work with the elves":
                                krampus "I feel that the elves and I have a mutual desire to stay away from each other. It’s easier this way because I can do what I want without having to worry about upsetting anyone."
                                "You stand there a minute putting popcorn on your string when what he says finally sinks in."

                                menu:
                                    "You’ve never upset me.":
                                        krampus "Come on, I know I have a temper and my words never quite come out how I mean them too. I must have said something mean to you at least once, you’re just too nice to admit or too stupid to care."
                                        "You suppress a small bit of laughter. Krampus was definitely abrasive but you could tell he never meant any harm with his words."

                                        $ krampus_aff += 1

                                        menu:
                                            "I think they wouldn’t mind if they got to know you.":
                                                krampus "I want to think that was true but it’s been this way for a long time. I don’t see that changing anytime soon. The thought alone does bring a smile to my lips."
                                                "Krampus did have a smile on his lips, but there was still sadness in his eyes. Once a significant pile of ornaments had been made, Krampus grabbed some up and left to start decorating. You watch him leave before doing the same."

                                                $ krampus_aff += 1
                                                hide Krampus Rough with dissolve
                                                call add_interaction from _call_add_interaction_25
                                                $ areas_visited.append("Kitchen")
                                                jump game_map

                                            "I just think it’s your pride getting in the way.":
                                                krampus "My pride is the only thing that keeps me here. I won't give up my own Kitchen just because some elves don’t like me. I’m not the one with the problem."
                                                "Krampus is clearly angry and doesn’t speak to for the rest of the time. When a large pile of decorations starts to form, Krampus grabs them up and leaves. You take that as a cue to do so as well."

                                                $ krampus_aff -= 1
                                                hide Krampus Rough with dissolve
                                                call add_interaction from _call_add_interaction_26
                                                $ areas_visited.append("Kitchen")
                                                jump game_map


                                    "You can be abrasive at times.":
                                        krampus "I am merely stating what I think. I can’t help it if others don’t like it or take it the wrong way."
                                        krampus "I’m sure even if I did happen to say something nicely, they would still think I was boarish. The best thing to do is just stay away."
                                        "Krampus is angry, but you could also tell that he hated the truth he felt in those words. You wondered if Krampus would ever get along with the elves."

                                        $ krampus_aff -= 1

                                        menu:
                                            "I think they could come around, eventually.":
                                                krampus "I try to not get my hopes up. Besides, I’ve got my baking and … I’ve got you right? There’s no point in asking for more."
                                                "Krampus’ words make your chest tighten. You’re happy he thinks highly of you but you don’t want him to give up on making friends with the elves either."
                                                "As your supplies dwindle, Krampus takes a pile of decorations and leaves the Kitchen. You decide that should too."
                                                $ krampus_aff += 1
                                                hide Krampus Rough with dissolve
                                                call add_interaction from _call_add_interaction_27
                                                $ areas_visited.append("Kitchen")
                                                jump game_map

                                            "Nothing will ever change with that attitude.":
                                                krampus "I’ve had this {i}attitude{/i} for years. It’s not like I plan on changing anytime soon. I’m fine like I am and I’m fine on my own."
                                                "He grabs up the decorations already made and storms out of Kitchen. As you leave, you wonder if Krampus will ever get along with the elves."

                                                $ krampus_aff -= 1
                                                hide Krampus Rough with dissolve
                                                call add_interaction from _call_add_interaction_28
                                                $ areas_visited.append("Kitchen")
                                                jump game_map

                            "(It's peaceful making decorations)":
                                "You both make dozens of decorations. It was obvious which ones were yours and which were his."
                                "Krampus says he is gonna go hang them around the Workshop. He gathers a pile in his arms then leaves the Kitchen. You exit the Kitchen as well."

                                hide Krampus Rough with dissolve
                                call add_interaction from _call_add_interaction_29
                                $ areas_visited.append("Kitchen")
                                jump game_map

                    "I need to do something else first.":
                        "You head out of the kitchen to finish something you needed to do."
                        hide Krampus Rough with dissolve
                        jump game_map
            elif day == 4:
                "You head toward the Kitchen and see a stream of elves going in and out the door. Krampus is at his usual corner standing over some sort of structure with an intense focus. You go over to see what he’s doing and he lifts his head up when you get close."
                show Krampus Rough with dissolve

                krampus "Can you lend me a hand with this? I need this gingerbread house ready for the Christmas celebration."
                "He indicates to the piece in front of him. You can see that the base is mostly done and, from the relative layout, you determine that the final product will be reminiscent of Santa’s Workshop. Knowing Krampus it will be exact, done to the most miniscule detail."

                menu:
                    "I can help, but why aren’t the elves?":
                        krampus "I don’t need the elves. You and I can do this without them. I don’t want them getting in the way and potentially messing it up. Now grab that bag of frosting and give me a hand."
                        "Krampus seems set to not include the elves and tries to hurry me along. It’s clear that he’s struggling to get this finished and you’re tired of his stubbornness."
                        $ krampus_aff += 1

                    "Have you asked the elves for help?":
                        krampus "Why would I? Do you think I’m imcompentent? I would do this all by myself if I wasn’t under a time crunch. Besides, I don’t need people who don’t even want to be around me. You’re the only one here who I want helping me."
                        "Krampus gives you a bag of frosting and starts indicating where to use it. You’re tired of his attitude and decide to put your foot down."
                        $ krampus_aff -= 1
                me "I’m not doing anything until you tell me your problem with the elves."
                "“Wha...What?” Krampus sputters, “I don’t know what you’re talking about.”"

                "The look you give him is hard and he quickly loses any will to fight back."
                krampus "My problem is that they don’t like me. It wasn’t just the humans that believed the stories. They all think that I’m the evil being the stories said I was. I tried to show them that I wasn’t by coming to work in the Kitchen."
                krampus "I made them cookies and any other sweets they could possibly desire, but nothing ever seems to work. Talking to them would just make them more afraid."
                krampus "I don’t intend to sound mean, but I’ve always had an abrasive personality. The more frustrated I got, the angrier I’d sound. I thought if I acted tough, it would hurt less when they avoided me. I see now I was just making my situation worse."
                krampus "You’re one of the few people who saw past my defenses and I’m grateful for that. Can you do me one more favor and help them see that I’m not a bad guy?"
                "Krampus’ eyes are pleading with you to help him. He didn’t look like some big, ole demon. Just a man who wants to be understood."

                menu:
                    "Of course.":
                        "You take Krampus’ hand and drag him over to some elves. The elves are scared at first but seeing you there he relaxes."
                    "Always":
                        "You take Krampus’ hand and drag him over to some elves. The elves are scared at first but seeing you there he relaxes."
                me "Will you help us make the gingerbread house?"

                "They seem like they’re about to refuse when you hear Krampus say, “Please.”"
                "Though they are startled and confused, they decide to help. You, Krampus, and the small group of elves finish the gingerbread workshop with plenty of time to spare. Other elves that had been watching the process come over when you are done to congratulate a job well done on such a magnificent work of art."
                "The elves that you worked with didn’t seem so afraid of Krampus now that they had spent some time with him. You knew it would take time, but you felt that everything would be alright for Krampus in the end."
                "As you leave Krampus to get to know his new friends, you see Krampus mouth ‘Thank You’."

                $ krampus_aff += 1
                $ areas_visited.append("Kitchen")
                call add_interaction from _call_add_interaction_30
                call add_interaction from _call_add_interaction_31
                call add_interaction from _call_add_interaction_32
                jump game_map


    # stables day 2 may need image fixing
    label stables_init:

        scene stables

        $ current_location = "Stables"

        if current_location in areas_visited:
            if day == 2:
                "You peer inside the stables, and Clarice seems to be enjoying himself while brushing a reindeer. You decide it best to leave him be at the moment."
            elif day == 3:
                "You peer inside the stables, and Clarice seems to be enjoying himself petting one of the reindeer. You decide it best to leave him be at the moment."
            elif day == 4:
                "You peer inside the stables, and Clarice seems to be really happy. He puts on the last few bells on the reindeer's harnesses. You decide it best to leave him be at the moment."
            jump game_map
        else:
            if day == 2:
                "You trudge through the snow to the stables. The thought of petting the reindeers puts a pep in your step."
                "You walk in and see the reindeers lined up in their stalls, each with their head out like they are expecting something. It surprises you that the space doesn’t actually smell like a barn. Clarice is at the far end by a big haystack."
                menu:
                    "(Walk over to Clarice)":
                        show Clarice Rough with dissolve
                        menu:
                            clarice "Oh, yer back. Glad to see ya returned. I knew ya could'nt resist these cuties. What can I do fer ye?"

                            "I want to help you take care of the reindeers.":
                                clarice "That so? Well, I'm glad to 'ave the help. Was just about to feed these guys if ya wouldn't mind lending a hand. I'll show ya what you gotta do."
                                "He goes over to the wall and grabs two pitchforks, one of which he hands to you. Clarice stabs the pitchfork into the pile of hay and pulls away a big clump. With a simple swing of his arms, the small stack lands in the corner of one of the reindeers' stall."
                                "\"Blitzen\", as the nameplate fixed to the door states, walks over to enjoy the fresh pile. Following Clarice's lead, you do the same thing for the other reindeers. The sounds of ruffling hay and chewing reindeers prompts you to ask a question."
                                $ clarice_aff += 1

                                menu:
                                    "Why are you a stablehand?":
                                        clarice "What else is there to do? Sit in a cave and make snow cones hoping somebody comes by? No way."
                                        clarice "I need some company and there ain't no better company than these reindeer right here. They listen to all my stories and I can put my muscles to good use. Should I be somptin else?"

                                        menu:
                                            "No, It makes sense that a big, furry beast would be around other animals.":
                                                clarice "Oh come now, I may be a yeti, but I ain't no beast. I have feelings too ya know just like these reindeers do. I thought you were more accepting than that. Guess I wasn't that good of a judge. Ya can go now. I can finish up the rest."
                                                "You leave Clarice to feed the rest of the reindeers. You regret what you said to him as you walk out into the cold."

                                                $ clarice_aff -= 1
                                                $ areas_visited.append("Stables")

                                                hide Clarice Rough with dissolve
                                                call add_interaction from _call_add_interaction_33
                                                jump game_map
                                            "No, I think it suits you. You and the reindeer seem happy here.":
                                                clarice "Why thank ye! This job keeps me and my muscles busy, but I do try my best to keep 'em all cozy and full."
                                                clarice "It's nice talking with others who can speak back ya know? Anyway, I'm glad ya came here to help me and the rest of the workshop. Please stop by anytime and I can show you how wonderful these 'ere reindeer are."

                                                "Once all the reindeer have a nice pile of hay, you tell Clarice goodbye and head out into the cold with a smile on your face."

                                                $ clarice_aff -= 1
                                                $ areas_visited.append("Stables")
                                                hide Clarice Rough with dissolve
                                                call add_interaction from _call_add_interaction_34
                                                jump game_map

                                    "(You decide it might be rude to ask)":
                                        "He thanks you for your help and tells you to come again. You head out exhausted from the hard work."
                                        $ areas_visited.append("Stables")
                                        hide Clarice Rough with dissolve
                                        call add_interaction from _call_add_interaction_35
                                        jump game_map

                            "(Pet the closest reindeer and leave)":
                                "You find some enjoyment from petting the reindeer, and decide to go somewhere else."

                                jump game_map

                $ areas_visited.append("Courtyard")

                jump game_map
            elif day == 3:
                "You head into the stables hopeful to play with the reindeers. As you look for Clarice, you hear him calling to you from inside one of the stalls with a brush in his hand."
                show Clarice Rough with dissolve
                clarice "I see yer back again for the reindeer. They’ve missed ya dearly since you’d last been back. I’m in the middle of grooming and inspecting ‘em for tomorrow’s flight."

                menu:
                    "I would love nothing more.":
                        clarice "See, I knew ya couldn’t resist ‘em. Come meet Vixen. She’s a sweetheart and her fur is so soft. I have extra brushes in here you can use. Watch out for her rack tho, she likes to shake her head when ya hit an itchy spot."
                        "Clarice hands you a brush as you walk into the stables and you begin to clean the dirt off her side. You wonder if you should make conversion during the process."

                        $ clarice_aff += 1

                        menu:
                            "What do you do when you aren’t working at the stable":
                                clarice "Well, I like to workout for one. Working ‘ere can only keep me so fit. I guess besides that I go on walks. Honestly, most of my time is spent ‘ere even when I don’t need to be."
                                clarice "The reindeer are my best friends after all. I guess, my only friends. But, hey, who could ask for better company. I know ya can’t."
                                "Clarice’s usually cheerful demeanor seems to diminish some and it feels as if he's forcing a smile. You wonder what you can say to him to put him at ease."

                                menu:
                                    "I think you’re pretty good company too.":
                                        clarice "Thank ya. I know that ya only say that because you’re nice, but I appreciate it nonetheless. I just ‘appen to come with the reindeer."
                                        "Clarice smiles but the melancholy doesn’t fully leave. Maybe if you said something else, he would believe you."

                                        $ clarice_aff += 1

                                        menu:
                                            "I think the reindeer are only fun because you’re here.":
                                                clarice "Ha Ha. I guess ya could say that. I do keep them in good and in a good mood. Though Krampus gets angry when I spoil them with some of his treats. I can take pride as the Workshop’s stablehand. I’m darn good at it."
                                                "That seemed to cheer him up, but you don’t think he truly grasped what you were trying to say. After Vixen was nice and clean, you decided it was time to head out."

                                                $ clarice_aff += 1
                                                call add_interaction from _call_add_interaction_36
                                                $ areas_visited.append("Stables")
                                                hide Clarice Rough with dissolve
                                                jump game_map

                                            "I didn’t think a yeti could be so friendly.":
                                                clarice "People don’t think yetis can be a lot of things. Well, I’m one ‘ell of a stablehand and no one else can take care of these reindeer like I can."
                                                clarice "We understand each other better than any person ever can. Also, nothing good comes of being mean."
                                                "You think you might have made him worse. You decide to head out after you’re done grooming Vixen."

                                                $ clarice_aff -= 1
                                                call add_interaction from _call_add_interaction_37
                                                $ areas_visited.append("Stables")
                                                hide Clarice Rough with dissolve
                                                jump game_map

                                    "How about hanging out with other people?":
                                        clarice "Can’t talk to people who won’t even go near ya. Only those assigned to check up on and retrieve the reindeer come here. They’re always gone in a flash tho. I know people never come for me."
                                        "Clarice seems heartbroken and you don’t know what to say. You decide not to make it worse and spend the rest of the time brushing Vixen in silence. Clarice is facing away from you as you leave."

                                        $ clarice_aff -= 1
                                        call add_interaction from _call_add_interaction_38
                                        $ areas_visited.append("Stables")
                                        hide Clarice Rough with dissolve
                                        jump game_map

                            "(I'll just focus on the reindeer)":
                                "You and Clarice finish brushing all of the reindeer. He thanks you for your help and you head out."

                                call add_interaction from _call_add_interaction_39
                                $ areas_visited.append("Stables")
                                hide Clarice Rough with dissolve
                                jump game_map

                    "I don't have time today.":
                        "You head somewhere else to do find something to work on."
                        hide Clarice Rough with dissolve
                        jump game_map
            elif day == 4:


                "You notice commotion going on in the Stables and head over to check it out. Some elves are here as well and just assume they have come to get the reindeer for Claus’ sleigh."
                "You head inside and see Clarice messing with Comet’s harness. You walk up to him and he smiles when he sees you."
                show Clarice Rough with dissolve
                clarice "I’m glad ya came today. Ya don’t wanna miss the reindeer getting all dressed up for their big night. Ya wanna give me a ‘and with them?"

                menu:
                    "I can’t pass up the chance to hang out with the reindeer.":
                        clarice "Nope, ‘specially when Christmas Eve comes once a year. They look so pretty decked out in their bells. It is a little sad though, once they’re gone I’ll be all alone tonight."
                        clarice "Y’ll probably go to the celebration once everything is done here. I guess I can play my bagpipes without worry of waking anyone up. Nobody wants a monster crashing their party anyway."

                        "Clarice seems really disheartened. What he says about being a monster rings in your ears. You know he’s not a monster and other people should know that too."

                        $ clarice_aff += 1

                    "I can’t resist helping you.":

                        clarice "Come now, ya don’t need to butter me up. I know yer here for the reindeer. Everyone is. I appreciate ya wanting to help me all the time, but I rather ya didn’t pretend to be interested in a monster like me."
                        "Clarice’s words sting your heart. How could he possibly consider himself a monster. He needs to know that he is so much more."

                        $ clarice_aff -= 1

                "You go over and grab one of the elves. You drag him over to stand next to Clarice. Both Clarice and the elf seem scared and don’t say anything. You give the elf a bridle and tell him to go get Prancer."
                "Clarice is about to object when you silence him with a look. The elf goes to Prancer’s stall and opens the door. Prancer rushes out and starts to charge the elf who’s frozen with fear."
                "Before the reindeer connects with the elf, Clarice has stepped in front. The reindeer crashes into Clarice, but he hardly moves. Quicker than the eye can see, Clarice puts the bridle over Prancer’s head."
                "Prancer is soothed by a few words and pats from Clarice. Clarice ties Prancer to his station and then helps the elf up. "
                "Elf" "Thank you for saving me. I’m sorry for always avoiding you. You’re not the monster everyone thinks you are, are you?"
                clarice "I try not to be. I’m glad you’re okay. You should probably go get checked up by one of the medics outside just in case."
                "The elf nods their head and goes outside."

                "Once all the reindeer are ready and taken outside, Clarice decides to call it a day. Just as you are about to stop him, the elf from before comes back and addresses Clarice."
                "Elf" "Do you wanna come with me and my friends to the celebration tonight? I’m sure it will be fun."
                clarice "Sure. Thank you."
                "Elf" "There’s nothing you need to thank me for. I’ll be back later to pick you up. See you then."
                "The elf leaves Clarice with a shocked expression on his face. “Did I just make a friend? With a person?”"

                menu:
                    "Hey. What about me?!":
                        "Clarice’s smile is from ear to ear as he wraps you in a big hug. You head out of the stables knowing that Clarice is gonna be much happier from now on."
                    "Two friends! (You smile)":
                        "Clarice’s smile is from ear to ear as he wraps you in a big hug. You head out of the stables knowing that Clarice is gonna be much happier from now on."
                hide Clarice Rough with dissolve
                $ clarice_aff += 1
                call add_interaction from _call_add_interaction_40
                call add_interaction from _call_add_interaction_41
                call add_interaction from _call_add_interaction_42
                $ areas_visited.append("Stables")
                jump game_map


    label frozen_lake_init:

        scene frozen lake

        $ current_location = "Frozen Lake"

        if current_location in areas_visited:
            if day == 2:
                "You stroll around the frozen lake. You spot Jack making snow angels. You glance away and decide to head somewhere else."
            elif day == 3:
                "You stroll around the frozen lake. You spot Jack putting away his skates. You glance away and decide to head somewhere else."
            jump game_map
        else:
            if day == 2:
                "You decide to make a stop at the Frozen Lake to see if Jack was around. You see him over by a pile of snow to the east of the lake."
                menu:
                    "What do you want to do?"

                    "(Go see what Jack is up to)":
                        show Jack Rough with dissolve
                        jack "Ooo look what the snowcat dragged out. I guess you do wanna have some fun after all. I was thinking of making some snowmen today. Wanna join?"

                        menu:
                            "Sure, sounds nice.":
                                jack "Okay then, let’s start rolling up some big balls of snow for the base. Then we can start on the other sections. I've got a bunch of stuff we can put on them over there."
                                "Jack points to a pile with sticks, various clothing, rocks, and an assortment of other trinkets. You help him start rolling up the different balls to form the snowmen bodies."
                                "Once you have a few made, you both go over to Jack’s stash and begin decorating them. As you dress up the snowmen, you begin to ponder Jack."

                                $ jack_aff += 1

                                menu:
                                    "Do you always come here to play?":
                                        jack "I guess I do. This is my favorite place in the North Pole and I like stealing the freshly baked treats that Krampus makes. Those things are amazing. He always gets so mad."
                                        jack "He tries to chase me out of there but I’m waaaaay too fast. I’m as fast as the North Wind! No one can catch me! Bernard likes complaining to Claus about me. Says I’m just a nuisance. Dude needs to lighten up. Christmas is all about having fun you know?"

                                        menu:
                                            jack "Do you think I’m a nuisance?"

                                            "Nah. I think taking time for yourself is important.":
                                                jack "Exactly, if Bernard took a step back every now and then, I bet he wouldn’t be so uptight. I don’t need to be told how important Christmas is. I’m literally Christmas Snow. Besides, who doesn’t like a snow day?"
                                                jack "Anyway, thanks for playing with me. Hope I see you again."
                                                "You leave Jack to admire both of your guys' handiwork. As you say goodbye, you’re glad that you decided to spend time with him."

                                                $ jack_aff += 1

                                                $ areas_visited.append("Frozen Lake")
                                                hide Jack Rough with dissolve
                                                call add_interaction from _call_add_interaction_43
                                                jump game_map

                                            "Well, life can't be all play you know.":
                                                jack "Geez, here I thought you were more of a free spirit. Guess you’re just another cog in the machine who does nothing but grind away all day. I’ll let you get back to your job then. Wouldn’t be good if Bernard caught you out here. See you, then."
                                                "You walk away from Jack as he puts the last bit of decorations on the snowmen. Your mouth forms a frown as you leave."

                                                $ jack_aff -= 1

                                                $ areas_visited.append("Frozen Lake")
                                                hide Jack Rough with dissolve
                                                call add_interaction from _call_add_interaction_44
                                                jump game_map

                                    "(You decide to just enjoy making snowmen with Jack)":
                                        "Jack tells you he had fun and you thank him for letting you join. You walk away feeling a little more relaxed."

                                        $ areas_visited.append("Frozen Lake")
                                        call add_interaction from _call_add_interaction_45
                                        hide Jack Rough with dissolve
                                        jump game_map

                            "Maybe some other time, it's a bit chilly.":
                                "You find the cold air to be a bit harsh, and decide to head somewhere else."

                                hide Jack Rough with dissolve
                                jump game_map

                    "(It's too cold out here)":
                        "You find the cold air to be less than refreshing, and decide to head somewhere else."

                        jump game_map



                jump game_map
            elif day == 3:
                "Outside you head to the Frozen Lake, curious about what mischief Jack could be getting up to."
                "You see him skating on the Lake like the first time you saw him. You shout to get his attention. Once, he notices you he races towards your direction and stops at the edge of the lake."
                show Jack Rough with dissolve

                jack "You’re back again! Do you wanna ice skate with me? The moon is really nice out and the sky is clear. It’ll be fun I promise!"

                menu:
                    "I’ve never ice skated before.":
                        jack "Really? Well, then I’ll need to fix that. I have some skates over there that should be your size."
                        "Jack points to an area not too far from where you're standing. As you begin putting the skates on you realize that Jack isn’t wearing any skates himself and that these are just your size. He brought them just for you."
                        "You look up at Jack and it sees he understands the look on your face because he blushes."
                        jack "I thought you might need some skates if you came by. I asked the shoemakers to make a pair for you. It’s nothing creepy, I swear!"

                        "You chuckle and put the skates on."
                        $ jack_aff += 1

                        menu:
                            "I’m a little scared. I’ve never been skating before.":
                                jack "Then you haven’t lived yet. Here, take my hand. I can show you how it’s don’t worry. I’m not gonna let you fall."
                                "Jack has a stupid grin on his face as you grab his hand."
                                jack "Just one step at a time. Slide one leg forward then another. There you’re doing it!"
                                "You slowly start skating forward and are able to maintain a steady pace without falling after a while. Now that you’re no longer terrified of falling, you decide to ask Jack a question."

                                $ jack_aff += 1

                                menu:
                                    "Do you treat everyone who comes out here this nicely?":
                                        jack "I think so, but no one ever comes out here. Not to play at least. It’s usually just me what with the elves being busy for Christmas."
                                        jack "You’re the first person to join me in a long time. I wish everyday was like this."
                                        "Jack’s demeanor fell for a moment before he shook it off with a half-hearted laugh. You could feel his grip on your hand tighten, but you chose not to say anything."
                                        "After a while, you get tired and call it a day. You have a newfound love of ice skating now."

                                        $ jack_aff -= 1
                                        hide Jack Rough with dissolve
                                        call add_interaction from _call_add_interaction_46
                                        $ areas_visited.append("Frozen Lake")
                                        jump game_map

                                    "You’re a natural teacher.":
                                        jack "I am an expert ice skater. I didn’t do much though, you just have natural talent."
                                        jack "If you come skating with me more often, then you’ll be a pro before you know it. It’s always more relaxing when you have someone else with you."
                                        "Jack seems to be in a good mood as you continue skating. You conclude that skating is now one of your favorite things to do. As you head out for the day, you realize that Jack’s hand never let go of yours the entire time."

                                        $ jack_aff += 1
                                        hide Jack Rough with dissolve
                                        call add_interaction from _call_add_interaction_47
                                        $ areas_visited.append("Frozen Lake")
                                        jump game_map

                            "What would you have done with these if I hadn’t come?":
                                jack "I guess keep them with me till you did. It would be rude to just give them back after begging the shoemakers to make the skates for me."
                                jack "I don’t know what I’d do if you didn’t come. Do you want me to show you how to ice skate?"
                                "You nod to Jack and take his outstretched hand. He leads you away from the edge and begins giving you some pointers. After a while, you’re steady enough on your feet to try conversing again."

                                $ jack_aff -= 1

                                menu:
                                    "I bet other people would love to come skating with you.":
                                        jack "Even if they did, they’re too busy. No one has time to come out here and play. I just wish people could see that Christmas is about having fun too. At least you’ll skate with me and that’s something."
                                        "Jack grows quiet, losing the usual happy demeanor he always carried. Nothing else meaningful is said while the two of you skate. Jack’s hand reluctantly lets go of yours as you leave."

                                        $ jack_aff -= 1
                                        hide Jack Rough with dissolve
                                        call add_interaction from _call_add_interaction_48
                                        $ areas_visited.append("Frozen Lake")
                                        jump game_map

                                    "I love ice skating!":
                                        jack "I knew you would love it. If only everyone else could see how much fun it is. I wish that people weren’t always so busy."
                                        jack "What’s the point of the Holidays if you’re always working. I hope you come back to skate some more."
                                        "You and Jack call it a day after ice skating for a while. As you leave, Jack’s hand tightens around yours briefly before finally letting go. You definitely want to go ice skating again."

                                        $ jack_aff += 1
                                        hide Jack Rough with dissolve
                                        call add_interaction from _call_add_interaction_49
                                        $ areas_visited.append("Frozen Lake")
                                        jump game_map



                    "I’ll have to pass today.":
                        "You head off to another area."
                        hide Jack Rough with dissolve
                        jump game_map
            elif day == 4:
                "Trudging through the fresh snow, you make your way towards the Frozen Lake. As you emerge from the frost coated pine trees, you find the lake is silent. No snowmen being built. No sounds of skates on ice. Nothing."
                "Looking around, you don’t see the cheery spirit who roams the snow as you normally do. A breeze suddenly picks up and you shiver as the cold nibs at your exposed nose. Huddling down into your scarf, you hear a branch crack above you."
                "Looking towards the sound you notice a figure sitting in the tree. As you get closer, you notice it’s Jack. He doesn’t appear to have noticed the crunching of your footsteps."
                "In fact it doesn’t look like he’s noticing anything. He’s staring silently off into the distance. The sparkles that normally float around him are gone. He seems… cold."
                me "Jack? What are you doing?"
                "Jack blinks at his name and looks down. He smiles when he sees you, but his eyes don’t seem any warmer."
                show Jack Rough with dissolve
                jack "Oh hey snowflake. Sorry, I didn’t see you there. I’m just enjoying the breeze. The lake’s peaceful at this time of year. The wind’s brisk this morning. Oh! Merry Christmas Eve by the way. Must be busy at the workshop."
                "As he speaks, the fake smile he’s placed on his face slowly gets colder and colder. You don’t think he’s really looking at you anymore."

                menu:
                    "Things are fine, but are you okay? You don’t seem like you.":
                        "Jack’s face twitches a bit. He forcibly widens his smile."
                        jack "What do you mean I don’t seem like me? I’m Jack. Jack Frost. Spirit of the North Wind. Creator of snow and ice. Bringer of Christmas Cheer! Lonesome soul on Christmas."
                        "Jack’s gaze has settled back on the frozen lake in front of him."
                        $ jack_aff += 1

                    "Yeah, it’s pretty busy. I thought it’d be nice to come out here for a break from the chaos.":
                        "Jack’s fake smile widens, but his eyes grow dimmer."
                        jack "It is a nice place to go. It’s quiet. No loud Bernard. No snowball fights with elves. No cookies, and no reindeer treats. Just me and a lake."
                        $ jack_aff -= 1

                me "You’ve got me don’t you?"
                "Jack looks like he’s trying to smile..."

                jack "That’s what everyone says. ‘Jack’s here to bring Christmas Cheer. Oh! Let’s go play with Jack. He always has the best games. Oh it’s cold out. Must be Jack Frost nipping at my nose!’"
                jack "But after all the fun, all the games, everyone goes home where they talk and laugh and remember how much fun it all was. Without remembering that Jack was there too."
                jack "For a long time, I thought nothing was better than watching people have fun with the snow I made. It didn’t matter that I couldn’t join them because I felt like I was a part of it in some way, that I was a friend they just couldn’t see."
                jack " Eventually, I realized I wanted to see what that was like, to hang out and share happy moments with others. So I came here. Everyone here could see me and for a while they would play with me."
                jack "When Christmas time came around though, everyone would always get busy and they would stop coming to see me. Once again, I felt like I was always looking in from the outside, wishing for something more."
                jack "I’m supposed to represent the Christmas Spirit and the joy of bringing people together, but honestly, I’ve never felt more alone than during Christmas time..."

                "From his perch in the tree, you see the joyful Jack you know break down into tears which freeze on his face. The wind around you begins to pick up while hail swipes at your frozen cheeks. Using a scarf as a protective layer, you look up the crying spirit."

                menu:
                    "You’re not alone Jack Not this Christmas.":
                        "Tightening your mittens, you grab the lower branches of the pine tree and begin your ascent. A barrage of snow and ice make repeated attempts to halt your journey, but you push forward determined to comfort Jack in his time of need."
                    "(Start Climbing the Tree)":
                        "Tightening your mittens, you grab the lower branches of the pine tree and begin your ascent. A barrage of snow and ice make repeated attempts to halt your journey, but you push forward determined to comfort Jack in his time of need."
                "As you reach the branch Jack’s sitting on, you see that ice has begun forming around him in a sort of cocoon. You slowly crawl across the branch, blinking snow flurries and ice crystals out of your eyes."
                "The closer you get to Jack, the more intense the winds get. Lost in his sorrow, he doesn’t appear to notice you’ve left the ground until your hand grasps onto his arm. With a gasp, Jack takes his face out of his hands and looks at you."

                jack "What…. What are you doing?"
                me "Warming up a frozen heart."
                "You give Jack a soft smile. He seems confused by the fact that you’re in the tree next to him, but slowly he returns the smile."

                me "You’re not alone Jack. Not this time."

                "As the winds begin to die down, you attempt to shift closer to Jack. As you move, you lose your grip on the branch due to the freshly formed ice. Your arms and legs slide out from underneath you and everything moves as if in slow motion."
                "Suddenly you’re moving further away from Jack and the tree, while his face eyes slowly widen in panic. Instinctively, you twist in the air and outstretch your hands to grab onto something."
                "Anything, but you’re too heavy from the thinner branches below and can only watch as the white ground gets closer and closer. You instinctively close your eyes and brace for impact."
                "After a moment you’re met with a force but it’s much softer than you anticipated. And… warm? Slowly you open your eyes and see not white, but blue in front of you. Blinking, you look up to see Jack holding you in his arms and looking down at you."

                jack "Are you okay?"

                me "“I… I’m fine, but what-” You look around to see yourself flying above the lake as Jack sits on his staff and holds you in bridal style."

                menu:
                    "I- I didn’t know you could fly.":
                        jack "Jack smiled endearly, “Well, I’ve got a lot of tricks up my sleeve.”"
                    "You- you saved me.":
                        jack "Jack laughs, “No. You saved {i}{b}me{/b}{/i}."

                "Jack sets your legs onto the flying branch and wraps you in a hug."
                jack "Thank you. Thank you for making Christmas feel magical again. I’d been alone for so long I’d forgotten what it felt like to let someone else in. You gave me a place to call home, that’s safe, warm, and full of laughter."
                jack "I will always cherish you no matter where the North Wind blows."

                "You both sit looking up at the moon, until you have to reluctantly leave. You know that Jack will always be in your heart."

                $ jack_aff += 1
                hide Jack Rough with dissolve
                call add_interaction from _call_add_interaction_50
                call add_interaction from _call_add_interaction_51
                call add_interaction from _call_add_interaction_52
                $ areas_visited.append("Frozen Lake")
                jump game_map



    # BEGIN DAY 3

    # Added
    label bernard_v_claus_day_3:
        "You walk into the courtyard in front of Santa's Workshop and see two people arguing"

        show Claus Rough at left with dissolve
        show Bernard Rough at right with dissolve

        # could do an small image left of dialogue to show who is talking

        # $ renpy.show("Head Claus", zorder=5000)

        claus "Come now Bernard, you can’t expect everything to go to plan. Everyone makes mistakes from time to time."
        claus "The elves are doing their best to get everything done in time for Christmas. Why don’t you let them off the hook for now? Besides, it will take more time to scold them than to just help them."

        bernard "Forgive my rudeness sir, but we can’t afford any major screw-ups. Every mistake is time wasted."
        bernard "And it’s exactly because Christmas is almost here that people should do everything correctly the first time around. The elves will only learn if I’m hard on them."

        me "What's going on?"
        "The two of them look to you as you approach."

        claus "Ah, hello there. We were just discussing how to handle when the elves make a mistake. Bernard seems to believe scolding is the answer-"

        bernard "So they’ll learn their lesson and not do it again. If you don’t reprimand them they’ll just do it again."

        menu:
            "{color=#20943A}Claus{/color} and {color=#39AA45}Bernard{/color}" "What do you think?"

            "I think learning to forgive and let go is what the Christmas spirit is all about.":
                bernard "I thought you were more sensible than this. Don’t come complaining to me when things go wrong."
                "Bernard makes a huffing sound at you and walks away toward the Toy Shop."

                hide Bernard Rough with dissolve

                claus "It seems I was right to hire you. Bernard may be strict but he does keep this place running for me. Thanks for keeping up employee morale in this stressful time."
                "He smiles at you and heads back to his Office."

                hide Claus Rough with dissolve

                $ bernard_aff -= 1
                $ claus_aff += 1

            "Mistakes can cause major setbacks.":
                bernard "Finally, someone who gets how important this matter is. With you here, I bet we can get these elves in top shape before Christmas."
                "With a triumphant look and smile in your direction Bernard heads back into the Toy Shop."

                hide Bernard Rough with dissolve

                claus "It’s a shame to hear that. I was hoping you would be a bit more compassionate to the employees here."
                "Claus leaves with a sad look on his face back to his Office."

                hide Claus Rough with dissolve

                $ bernard_aff += 1
                $ claus_aff -= 1


        "You broke up their argument, yet feel that one of them is dissapointed in you. You decide to wander somewhere else."

        $ areas_visited.append("Courtyard")
        call add_interaction from _call_add_interaction_53
        jump game_map

    label claus_v_krampus_day_3:

        "You wander around the fully decorated tree. A lot of time passes without you knowing."
        "After staring at the tree for some time, you get up to wander somewhere else"

        $ areas_visited.append("Courtyard")
        call add_interaction from _call_add_interaction_54
        jump game_map

    label claus_v_jack_day_3:

        "You wander around the fully decorated tree. A lot of time passes without you knowing."
        "After staring at the tree for some time, you get up to wander somewhere else"

        $ areas_visited.append("Courtyard")
        call add_interaction from _call_add_interaction_55
        jump game_map

    label clarice_v_claus_day_3:

        "You wander around the fully decorated tree. A lot of time passes without you knowing."
        "After staring at the tree for some time, you get up to wander somewhere else"

        $ areas_visited.append("Courtyard")
        call add_interaction from _call_add_interaction_56
        jump game_map

    # Added
    label bernard_v_krampus_day_3:

        "You walk into the courtyard in front of Santa's Workshop and see two people arguing"

        show Bernard Rough at left
        show Krampus Rough at right

        bernard "We need you and the elves to ramp up production in the Kitchen. I need my workers at their peak to get everything done in time for Christmas."
        bernard "It can’t be that hard to make a few dozen more cookies if you guys sped up the process. The cookies don’t have to be a work of art since they’re just gonna be eaten."

        krampus "I can't just speed up the process you know. I have a finite amount of resources, help, and oven space. Not to forget, each cookie needs to be cooked long enough to be edible."
        krampus "And don’t you dare treat baking as less important than toy making. What if I told you to cut corners in your Toy Shop? I take just as much pride in my creations as you do."

        me "What's going on?"
        "The two of them notice you."

        krampus "Hard-ass here is asking me to sacrifice my cookies for his precious toys which is frankly insulting."
        bernard "I really don’t see the issue here. While delicious, they’re just cookies. The toys are the most important thing here."

        menu:
            "What do you think?"

            "Toys do last a longer time than cookies, and we are delivering those instead of cookies.":
                bernard "See, the new manager agrees with me. Cookies are just fuel to complete the more important tasks. I expect a 25% higher yield rate by the end of the day Krampus."
                "Bernard nods at you then walks into the Toy Shop, leaving you with an angry Krampus."

                hide Bernard Rough with dissolve

                krampus "Both you and him know nothing about the art of baking. You two better not come crying to me when the elves complain about bad tasting cookies."
                "Krampus storms away back to his Kitchen."

                hide Krampus Rough with dissolve

                $ bernard_aff += 1
                $ krampus_aff -= 1

            "You can’t slack on cookie making Bernard. If they’re not good, the elves won’t want to eat them.":
                "Bernard huffs..."
                bernard "It’s all a waste of time. Fine, keep doing things your way Krampus, no matter how inefficient it is. If the toys aren’t done on time, I’m blaming you manager."
                "Bernard sneers at you then heads to the Toy Shop."

                hide Bernard Rough with dissolve

                krampus "From now on I’m putting salt in all his cookies. At least someone here has some sense. There are other things that are just as vital as toy making. Thanks."
                "Krampus leaves, glaring in the direction of the Toy Shop."

                hide Krampus Rough with dissolve

                $ bernard_aff -= 1
                $ krampus_aff += 1

        "You broke up their argument, yet feel that one of them is dissapointed in you. You decide to wander somewhere else."

        $ areas_visited.append("Courtyard")
        call add_interaction from _call_add_interaction_57
        jump game_map

    label bernard_v_jack_day_3:

        "You wander around the fully decorated tree. A lot of time passes without you knowing."
        "After staring at the tree for some time, you get up to wander somewhere else"

        $ areas_visited.append("Courtyard")
        call add_interaction from _call_add_interaction_58
        jump game_map

    label bernard_v_clarice_day_3:

        "You wander around the fully decorated tree. A lot of time passes without you knowing."
        "After staring at the tree for some time, you get up to wander somewhere else"

        $ areas_visited.append("Courtyard")
        call add_interaction from _call_add_interaction_59
        jump game_map

    label jack_v_krampus_day_3:

        "You wander around the fully decorated tree. A lot of time passes without you knowing."
        "After staring at the tree for some time, you get up to wander somewhere else"

        $ areas_visited.append("Courtyard")
        call add_interaction from _call_add_interaction_60
        jump game_map

    label clarice_v_krampus_day_3:

        "You wander around the fully decorated tree. A lot of time passes without you knowing."
        "After staring at the tree for some time, you get up to wander somewhere else"

        $ areas_visited.append("Courtyard")
        call add_interaction from _call_add_interaction_61
        jump game_map

    label jack_v_clarice_day_3:

        "You wander around the fully decorated tree. A lot of time passes without you knowing."
        "After staring at the tree for some time, you get up to wander somewhere else"

        $ areas_visited.append("Courtyard")
        call add_interaction from _call_add_interaction_62
        jump game_map


    label day_5:

        $ max_aff = get_highest_aff()

        if(max_aff == "bernard"):
            scene toy shop
            "You walk into the Toy Shop to see Bernard already waiting for you."
            show Bernard Rough with dissolve
            bernard "“You’re late.” Seeing the look on your face he puts up his hands and laughs."
            bernard "“I’m kidding. Here.” He hands you a sled."
            bernard "You said I should relax right? I thought it would be good for us to spend the day together. Besides, I need to thank you for everything. I couldn’t have done it without you. You made me come back to myself."
            "He smiles brightly at you as he grabs your hand to take you outside. Just as you exit the door he stops, “But first,” Bernard points up and you see a cluster of mistletoe hanging above the door frame."
            "He smiles endearingly at you as he holds you in his arms. Slowly, he leans forward and kisses you as he whispers, “Perfect.”"
            hide Bernard Rough with dissolve

            "-Fin-"
            pause 0.5
            "Art and Story by Meghan\nStory by Mikaela\nProgramming by Luke"
            jump close_game

        elif(max_aff == "claus"):
            scene santa office

            "Claus was expecting you, evident by the door to his office being open. He is standing by his desk and, when he sees you, he shifts something behind his back."
            show Claus Rough with dissolve
            claus "Ah, thanks for coming. I was looking forward to this the whole time I was delivering presents. Can you close your eyes for a second? I’ve got one more present to give."
            "You close your eyes and Claus places something heavy in your outstretched hands. “Open them.” You open your eyes and in your hand is a snowglobe with a model of the workshop inside."
            "“Shake it.” You do and Claus flies over the workshop in his sleigh. “Now, whenever you need me, just shake it and I’ll always be there.”"
            claus "You gave me the most important thing of all, the joy of Christmas back. I owe you a thousand presents, my Christmas miracle. Now how about we go on that sleigh ride I promised."
            "As the two of you head out of the door, Claus makes one final comment:"
            me "You know, I really need to go on a Christmas Vacation. Hopefully it's nothing like National Lampoon’s. I heard that didn’t go so well."
            "You both laugh and close the door behind you."
            hide Claus Rough with dissolve

            "-Fin-"
            pause 0.5
            "Art and Story by Meghan\nStory by Mikaela\nProgramming by Luke"
            jump close_game

        elif(max_aff == "krampus"):
            scene kitchen

            "Walking into the kitchen you smell the familiar smell of gingerbread and peppermint."
            "Instead of seeing Krampus by himself however, you see a few elves standing next to him on stools as Krampus is giving instructions. His voice is as stern as usual, but his eyes seem to hold a new light."
            show Krampus Rough with dissolve
            me "What are you doing?"
            "Krampus looks over at the sound of your voice."
            krampus "I’m showing the elves how to cut cookies. They’re not terrible. Just a little short. They did give me some new cookie ideas for Bernard though."
            "Krampus turns around and picks up a tray of strawberry shaped cookies."
            krampus "The elves say it’s from a game called ‘Bugsnax’. They say it’s Bernard’s favorite."
            me "You give a laugh. “I’m sure Bernard will love them. Anything I can help with today?”"
            krampus "Actually yes."
            "Krampus puts down the tray of cookies and takes off his apron. This is the first time you’ve seen him without his apron on. He really does wear nothing but black fur and a pink apron."
            krampus "The elves want me to join in their game and I was hoping you’d come with me. For support."
            "The large goat-man almost seems bashful as he asks, but you smile and take his hand."

            me "Sure. I’ll watch your back."

            "Krampus smiles and turns back to the elves, “Alright you little demons, uh- rascals. Lets go.”"
            "The elves cheer and race ahead of you and Krampus as you turn off the kitchen lights and make your way outside."

            hide Klaus Rough with dissolve
            "-Fin-"
            pause 0.5
            "Art and Story by Meghan\nStory by Mikaela\nProgramming by Luke"
            jump close_game

        elif(max_aff == "clarice"):
            scene stables

            "The next morning, you approach the stables as the light of dawn reflects off the new fallen snow. As you draw closer, you hear the sound off...bagpipes?"
            "Pushing open the large stable door, you one large, bagpipe playing yeti standing in the center of a circle of sleeping reindeer. Hearing the door open, he drifts cuts off his song and waves to you."

            "Tiptoeing around the snoozing creatures, Clarice greets you at the door."
            show Clarice Rough with dissolve

            clarice "Good mornin’! Did you sleep alright? That was one heck of a party last night. I ain’t been to something that rowdy since Dasher and Cupid’s thirteen! I always believed I was a monster, doomed to be alone with no one but the reindeer to talk to."
            clarice "I love ‘em, but it’s not the same as having another person who can talk back. Just when I had given up hope, ‘ere yer were and I will treasure that moment for the rest of my life."

            "Clarice takes your hands in his and you gaze into each other’s eyes."

            clarice "I always felt lost, like I was in a fog so thick I would never find my way home. But then ya shown a light on my life and I can finally see a future. One in which I’m not alone and you’re there by my side. Thank ya. Thank ya for being my Rudolph."

            "Clarice wraps you in a large bear hug nestling you in his fur. You hug him back, knowing there’s nowhere else you’d rather be than with a yeti and his reindeer."

            hide Clarice Rough with dissolve

            "-Fin-"
            pause 0.5
            "Art and Story by Meghan\nStory by Mikaela\nProgramming by Luke"
            jump close_game

        elif(max_aff == "jack"):
            scene frozen lake

            "Once again, when you get to the Frozen Lake, Jack is skating across the ice. When he sees you, he runs over and grabs your arm as he drags you toward a tent."
            show Jack Rough with dissolve
            "In front of the tent is a small fire surrounded by a couple of logs. Jack seems to be practically bouncing."

            jack "I thought we could do something warm for once. I may be Winter incarnate, but even I like to do something hot every once in a while. Come take a seat, I got hot cocoa and s’mores."
            "You both take a seat on one of the logs. He hands you a mug, which you wrap your hands around to absorb the heat."
            jack "I never thought I would get to spend Christmas with someone. And who was actually aware of me at that. I’ve made a thousand wishes and waited so many years, but it was worth it because I finally met you. For once, I feel like I’m on the inside, looking out."
            "You give him a funny look and he laughs."
            jack "I know I’m physically outside, but hey the metaphor still works. We can go inside the tent. That’ll count right?"
            "You laugh and his grin gets bigger. He reaches over and places a hand on your cheek. As you look each other in the eyes, you both lean over and kiss."
            "As you pull back you ask, “How cold do you think it is?”"
            jack "One, but I’ve never felt warmer."
            hide Jack Rough with dissolve

            "-Fin-"
            pause 0.5
            "Art and Story by Meghan\nStory by Mikaela\nProgramming by Luke"
            jump close_game

        else:
            "You decide to wander around the North Pole on Christmas Day. You don't really have anyone in particular to spend it with, but you think you made a few friends along the way."

            "-Fin-"
            pause 0.5
            "Art and Story by Meghan\nStory by Mikaela\nProgramming by Luke"
            jump close_game

        jump close_game

    ### END ALL DAYS 2 - 5

    # used to close the game
    label init_close_game:
        "You chickened out and were fired for not showing up to work."
        jump close_game

    # A menu to test adding interactions
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

    # Used to check what day it is
    label what_day:

        "Today is day [day]"

        jump test_menu

    # Used to check what interaction it is
    label what_interaction:

        "You have made [interaction] interactions today"

        jump test_menu

    # A "Function" still used to add interactions to the game.
    # This needs to be updated with text for when the player wakes up
    # as well as possibly when the player wins over a character
    # on the final day.
    label add_interaction:

        # Adds an interaction
        python:
            interaction += 1

        # If we exceed max interactions...
        if(interaction >= max_interactions):



            # And the day isnt the first day...
            if(day > 1):

                # Get the dream description for most affection
                python:
                    renpy.show("day_count_0", layer="screens")
                    max_aff_desc = get_dream_desc()

                # This is how an image is shown (with animation)
                show dream_background with dissolve

                # Dream text
                if(day == 2):
                    "You notice the sun go down after a long day. You decide to get some rest."
                    "As you head to bed for the night, you think about all the awesome things you did today. You can’t wait to go back to work tomorrow and see what’s waiting in store for you to do."
                    "As you drift to sleep once again, you see another blurry image appear before you but this time you can make out one particular feature, [max_aff_desc]"

                    hide day_count_2
                    show day_count_0 onlayer screens:
                        xalign 0.01
                        yalign 0.01

                elif(day == 3):
                    "You notice the sun go down after a long day. You decide to get some rest."
                    "You go to bed that night thinking about all the things you did. The words and actions of the other people at the shop swirl in your head until you drift off to sleep."
                    "Once again you begin to dream a blurry image appears before you but this time you can make out one particular feature, [max_aff_desc]"
                elif(day == 4):
                    "As you drift off to sleep, tired from all the Christmas Eve festivities, you are greeted by one more dream. You don’t smell or see anything but you can faintly hear the words, “Thank you.” As exhaustion finally overtakes you."

                # This is how an image is hidden (with animation)
                hide dream_background with dissolve

            # Always increase the day count, and reset the interaction count.
            # Also resets the areas the player visited during the day.
            python:

                day += 1
                interaction = 0
                areas_visited.clear()

        # Shows the interaction count the player now has
        if(day < 4):
            if(interaction == 1):
                hide day_count_0
                show day_count_1 onlayer screens:
                    xalign 0.01
                    yalign 0.01
            elif(interaction == 2):
                hide day_count_1
                show day_count_2 onlayer screens:
                    xalign 0.01
                    yalign 0.01
            elif(interaction == 0):
                hide day_count_2
                show day_count_0 onlayer screens:
                    xalign 0.01
                    yalign 0.01
        elif(day == 4 and interaction == 0):
            hide day_count_2
            show day_count_0 onlayer screens:
                xalign 0.01
                yalign 0.01
        elif(day == 5 and interaction == 0):
            hide day_count_2
            show day_count_0 onlayer screens:
                xalign 0.01
                yalign 0.01

        # python:
        #     if(renpy.showing("day_count_0")):
        #         renpy.hide("day_count_0")
        #         renpy.show("day_count_1", layer="screens")
        #     elif(renpy.showing("day_count_1")):
        #         renpy.hide("day_count_1")
        #         renpy.show("day_count_2", layer="screens")
        #     elif(renpy.showing("day_count_2")):
        #         renpy.hide("day_count_2")
        #         renpy.show("day_count_0", layer="screens")
            ### # Deprecate
            ### elif(renpy.showing("int_counter_3")):
            ###     renpy.hide("int_counter_3")
            ###     renpy.show("int_counter_0")

            # Shows the new day icon, as well as the wake-up text
        if(day == 2 and interaction == 0):
            hide dec21st_img
            show dec22nd_img onlayer screens:
                xalign 0.01
                yalign 0.16
            hide day_count_2
            show day_count_0 onlayer screens:
                xalign 0.01
                yalign 0.01

            scene courtyard

        elif(day == 3 and interaction == 0):
            hide dec22nd_img
            show dec23rd_img onlayer screens:
                xalign 0.01
                yalign 0.16
            hide day_count_2
            show day_count_0 onlayer screens:
                xalign 0.01
                yalign 0.01

            scene courtyard

            "You awake to another day at the North Pole and ready to get back to work. Along the way to Santa’s Workshop, you start wondering where you would like to go first."



        elif(day == 4 and interaction == 0):
            hide dec23rd_img
            show dec24th_img onlayer screens:
                xalign 0.01
                yalign 0.16
            hide day_count_2
            show day_count_0 onlayer screens:
                xalign 0.01
                yalign 0.01

            scene courtyard

            "You awake to another day at the North Pole and ready to get back to work. Along the way to Santa’s Workshop, you start wondering where you would like to go first."

        elif(day == 5 and interaction == 0):
            hide dec24th_img
            show dec25th_img onlayer screens:
                xalign 0.01
                yalign 0.16

            scene courtyard

            "You awake on Christmas Day. A magical essence fills the air, and you head outside."

            jump day_5



        return

    # Sends the player to the game map
    label game_map:

        scene map_image
        $ renpy.call_screen("game_map", _layer="screens")

    # Ends the game
    label close_game:

    return
