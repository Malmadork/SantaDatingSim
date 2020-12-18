# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define santa = Character(_("Santa"), color="#20943A")
define claus = Character(_("Claus"), color="#20943A")
define krampus = Character(_("Krampus"), color="#9E2F4F")
define jack = Character(_("Jack"), color="#27BDC9")
define clarice = Character(_("Clarice"), color="#7ECFD6")
define bernard = Character(_("Bernard"), color="#39AA45")
define me = Character("Me", color="#eff")
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

        renpy.image("day_count_0", Image("images/day_count_0.png", xalign=0.01, yalign=0.01))
        renpy.image("day_count_1", Image("images/day_count_1.png", xalign=0.01, yalign=0.01))
        renpy.image("day_count_2", Image("images/day_count_2.png", xalign=0.01, yalign=0.01))

        renpy.image("dec19th_img", Image("images/dec19th_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec20th_img", Image("images/dec20th_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec21st_img", Image("images/dec21st_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec22nd_img", Image("images/dec22nd_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec23rd_img", Image("images/dec23rd_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec24th_img", Image("images/dec24th_img.png", xalign=0.01, yalign=0.16))
        renpy.image("dec25th_img", Image("images/dec25th_img.png", xalign=0.01, yalign=0.16))

        renpy.image("dream_background", Image("images/dream_background.png"))

        renpy.image("Bernard Rough", Image("images/Bernard Rough.png"))
        renpy.image("Claus Rough", Image("images/Claus Rough.png"))
        renpy.image("Jack Rough", Image("images/Jack Rough.png"))
        renpy.image("Krampus Rough", Image("images/Krampus Rough.png"))

        christmas_spirit = 0
        claus_aff = 0
        krampus_aff = 0
        jack_aff = 0
        clarice_aff = 0
        bernard_aff = 0

        max_aff = "None"
        max_aff_desc = "None"

        def sort_aff(arr):
            return arr[1]

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
                    mf = "{u}, a red cap with a white fluffy microphone. You pick up the scent of chocolate and peppermint.{/u}"
                elif(arr[0][0] == "bernard"):
                    mf = "{u}a pocket watch ticking in the distance. You pick up the scent of sawdust, and hear a train whistle.{/u}"
                elif(arr[0][0] == "krampus"):
                    mf = "{u}a pair of curling horns. You pick up the scent of gingerbread and sugar.{/u}"
                elif(arr[0][0] == "jack"):
                    mf = "{u}a smile that sparkles as bright as the moon. You pick up on the scent of pine needles and brisk morning air.{/u}"
                else:
                    mf = "{u}a hairy six pack. You pick up the scent of freshly piled hay.{/u}"

            return mf

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


        settings = ['Courtyard', 'Toy Shop', 'Santa\'s Office', 'Kitchen', 'Frozen Lake', 'Stables']

        day = 1
        interaction = 0
        max_interactions = 3

        current_location = 'None'
        areas_visited = []

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    show day_count_0:
        xalign 0.01
        yalign 0.01

    show dec21st_img:
        xalign 0.01
        yalign 0.16


    # jump test_menu


    "You finally made it to the North Pole and today is your first day working at Santa’s Workshop. You feel nervous. Taking a moment to calm yourself, you release long puffs of air into the freezing atmosphere creating small clouds with each breath."

    label init_choice_a:
        menu:
            "I'm ready.":
                jump init_ready
            "I can't do this":
                jump init_close_game

    label init_ready:
        "You go inside Santa’s Workshop, enter into Toy Shop."

    label toy_shop_a:
        "Entering the Toy Shop, you immediately feel the energy of the Christmas season. All around you, tiny hammers are clacking, elves are bustling about, and toys are being charted off in every direction."
        "As you stand there in wonder of the workshop your eyes land on an angry elf quickly heading towards you with a pocket watch in hand."

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
                "Bernard looks at you and takes a deep breath in."
                bernard "Oooo you're a jokester huh?"
                bernard "I will not tolerate rudeness in my employees."

                $ bernard_aff -= 1
            "Yes Sir.":
                "You nod and listen to what Bernard has to say."

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

    label santa_office_day_1_interaction:

        ### todo: Insert an image for location!!!

        "{color=#39AA45}Bernard{/color} leads you to a room with a sign above the door that reads {i}A Life Full of Wonder is a Life Full of Joy.{/i}"
        "As {color=#39AA45}Bernard{/color} opens the door, you’re greeted by an overwhelming scent of hot chocolate, peppermint and cinnamon. Red walls with gold trims dazzle the room as magical toys float through the air. Pacing around a desk in the center of the room is a large man dressed all in red."
        "He seems to be talking into the end of his hat as his beard flutters in the wind."
        "The man stops pacing as {color=#39AA45}Bernard{/color} approaches. He quickly tells the man something then leaves the room. The man turns to greet you as the door shuts behind you."

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

        "You find the Kitchen off the Toy Shop like {color=#20943A}Claus{/color} said. The Kitchen was massive in comparison to the elves who were snacking on milk and cookies."
        "Despite all the traffic, everything was quite clean. The black marble countertops glistened while the hanging pots reflected the bright hats of the elves."
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

        pause 1.0
        #call add_interaction

        jump game_map

    label courtyard_init:

        $ current_location = "Courtyard"

        if current_location in areas_visited:
            if day == 2:
                "You wander around the fully decorated tree, and decide to try to visit another area."

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

                jump game_map
            elif day == 3:
                "You walk into the courtyard in front of Santa's Workshop and see two people arguing"

                show Claus Rough at left
                show Bernard Rough at right

                # could do an small image left of dialogue to show who is talking

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

                        claus "It’s a shame to hear that. I was hoping you would be a bit more compassionate to the employees here."
                        "Claus leaves with a sad look on his face back to his Office."

                        $ bernard_aff += 1
                        $ claus_aff -= 1


                jump game_map

    label toy_shop_init:

        $ current_location = "Toy Shop"

        if current_location in areas_visited:
            if day == 2:
                "You walk back into the Toy Shop. Everyone seems busy with their work, and Bernard is inspecting the finished toys. You decide to head out and help somewhere else."

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
                                call add_interaction
                                $ areas_visited.append("Toy Shop")
                                jump game_map

                        "You finish making toys for the day and decide to head out. You say goodbye to Bernard as you leave and he thanks you for the hard work."
                        hide Bernard Rough with dissolve
                        call add_interaction
                        $ areas_visited.append("Toy Shop")

                    "(Come back later, he seems stressed.)":
                        hide Bernard Rough with dissolve
                        "You decide to leave, and try to find another area to manage."

                jump game_map

    label santa_office_init:

        $ current_location = "Santa Office"

        if current_location in areas_visited:
            if day == 2:
                "You peer through the glass of the office you visited earlier. You decide not to bother Claus as he looks busy reading through some letters and check out another area."

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
                                call add_interaction
                                jump game_map

                            "(You think better of it, and decide not to say anything.)":
                                "You go through all the letters and decide to leave. He thanks you on your way out."
                                hide Claus Rough with dissolve
                                $ areas_visited.append("Santa Office")
                                call add_interaction
                                jump game_map



                    "Just checking in. I actually have something else to do.":
                        claus "Okay. Come back anytime."
                        jump game_map

                # $ areas_visited.append("Santa Office")
                #
                # jump game_map

    label kitchen_init:

        $ current_location = "Kitchen"

        if current_location in areas_visited:
            if day == 2:
                "You wander past the kitchen. Krampus looks focused on making some more dough. You decide it's best to leave him be at the moment and go somewhere else."

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
                                                call add_interaction
                                                jump game_map

                                            "I always assumed that you were like Jimmy Brando from the Scarygodmother Wiki":
                                                "Krampus looks appalled."
                                                krampus "I'm not some imp with animation issues or a Victorian woman who whips children. All I did was give children a simple slap on the wrist when they misbehaved. It's rude to just assume people are monsters when you don’t even know them. I'll take care of the rest. You can go."
                                                "You walk out the kitchen and feel bad about having judged him."

                                                hide Krampus Rough with dissolve
                                                $ krampus_aff -= 1
                                                $ areas_visited.append("Kitchen")
                                                call add_interaction
                                                jump game_map


                                    "(You realize that it would be silly to ask, and decide not to)":
                                        "You make a large amount of cookies until it is time for you to go. Krampus thanks you for the help and advises you wash up after you leave."
                                        hide Krampus Rough with dissolve
                                        $ areas_visited.append("Kitchen")
                                        call add_interaction
                                        jump game_map

                    "(Go somewhere else)":
                        "You decide to visit another area."
                        jump game_map


                # $ areas_visited.append("Kitchen")

                jump game_map

    # stables day 2 may need image fixing
    label stables_init:

        $ current_location = "Stables"

        if current_location in areas_visited:
            if day == 2:
                "You peer inside the stables, and Clarice seems to be enjoying himself while brushing a reindeer. You decide it best to leave him be at the moment."

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
                                                call add_interaction
                                                jump game_map
                                            "No, I think it suits you. You and the reindeer seem happy here.":
                                                clarice "Why thank ye! This job keeps me and my muscles busy, but I do try my best to keep 'em all cozy and full."
                                                clarice "It's nice talking with others who can speak back ya know? Anyway, I'm glad ya came here to help me and the rest of the workshop. Please stop by anytime and I can show you how wonderful these 'ere reindeer are."

                                                "Once all the reindeer have a nice pile of hay, you tell Clarice goodbye and head out into the cold with a smile on your face."

                                                $ clarice_aff -= 1
                                                $ areas_visited.append("Stables")
                                                hide Clarice Rough with dissolve
                                                call add_interaction
                                                jump game_map

                                    "(You decide it might be rude to ask)":
                                        "He thanks you for your help and tells you to come again. You head out exhausted from the hard work."
                                        $ areas_visited.append("Stables")
                                        hide Clarice Rough with dissolve
                                        call add_interaction
                                        jump game_map

                            "(Pet the closest reindeer and leave)":
                                "You find some enjoyment from petting the reindeer, and decide to go somewhere else."

                                jump game_map

                $ areas_visited.append("Courtyard")

                jump game_map

    label frozen_lake_init:

        $ current_location = "Frozen Lake"

        if current_location in areas_visited:
            if day == 2:
                "You stroll around the frozen lake. You spot Jack making snow angels. You glance away and decide to head somewhere else."

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
                                                call add_interaction
                                                jump game_map

                                            "Well, life can't be all play you know.":
                                                jack "Geez, here I thought you were more of a free spirit. Guess you’re just another cog in the machine who does nothing but grind away all day. I’ll let you get back to your job then. Wouldn’t be good if Bernard caught you out here. See you, then."
                                                "You walk away from Jack as he puts the last bit of decorations on the snowmen. Your mouth forms a frown as you leave."

                                                $ jack_aff -= 1

                                                $ areas_visited.append("Frozen Lake")
                                                hide Jack Rough with dissolve
                                                call add_interaction
                                                jump game_map

                                    "(You decide to just enjoy making snowmen with Jack)":
                                        "Jack tells you he had fun and you thank him for letting you join. You walk away feeling a little more relaxed."

                                        $ areas_visited.append("Frozen Lake")
                                        call add_interaction
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

            if(day > 1):

                python:
                    max_aff_desc = get_dream_desc()

                show dream_background with dissolve
                "You notice the sun go down after a long day. You decide to get some rest."
                "As you head to bed for the night, you think about all the awesome things you did today. You can’t wait to go back to work tomorrow and see what’s waiting in store for you to do."
                "As you drift to sleep once again, you see another blurry image appear before you but this time you can make out one particular feature, [max_aff_desc]"

                hide dream_background with dissolve

            python:

                day += 1
                interaction = 0
                areas_visited.clear()

        python:
            if(renpy.showing("day_count_0")):
                renpy.hide("day_count_0")
                renpy.show("day_count_1")
            elif(renpy.showing("day_count_1")):
                renpy.hide("day_count_1")
                renpy.show("day_count_2")
            elif(renpy.showing("day_count_2")):
                renpy.hide("day_count_2")
                renpy.show("day_count_0")
            # elif(renpy.showing("int_counter_3")):
            #     renpy.hide("int_counter_3")
            #     renpy.show("int_counter_0")

            if(day == 2):
                renpy.hide("dec21st_img")
                renpy.show("dec22nd_img")
            elif(day == 3):
                renpy.hide("dec22nd_img")
                renpy.show("dec23rd_img")

                renpy.say("", "You awake to another day at the North Pole and ready to get back to work. Along the way to Santa’s Workshop, you start wondering where you would like to go first.")

            elif(day == 4):
                renpy.hide("dec23rd_img")
                renpy.show("dec24th_img")
            elif(day == 5):
                renpy.hide("dec24th_img")
                renpy.show("dec25th_img")

                #renpy.show("day_counter_0", at=[Transform(pos=(0.005, 0.005))])


        # jump test_menu
        return

    label game_map:

        $ renpy.call_screen("game_map", _layer="screens")

        #jump test_menu


    #image daybox = "day_box.png"

    label close_game:

    # This ends the game.

    return
