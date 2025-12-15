#SCENE HELPER
def show_scene(engine, text, background, choices):
    engine.set_story(text)
    engine.set_background(background)
    engine.make_choice_buttons(choices)


#TITLE SCREEN
def title_screen(engine):
    engine.play_music("assets/music/bgm.mp3")

    show_scene(
        engine,
        text=(
            "BEASTBORN\n\n"
            "A post-apocalyptic survival tale\n\n"
            "Press Start to begin"
        ),
        background="assets/images/title.jpg",
        choices=[
            ("Start Game", lambda: start_game(engine))
        ],
    )



# START GAME
def start_game(engine):
    show_scene(
        engine,
        text=(
            "You awaken in a collapsed subway tunnel.\n"
            "Dust fills the air. You hear distant screeches.\n\n"
            "Where will you go?"
        ),
        background="assets/images/subway.webp",
        choices=[
            ("Climb the broken ladder to the streets", lambda: streets(engine), "assets/sfx/bus.mp3"),
            ("Crawl into the maintenance tunnel", lambda: maintenance(engine), "assets/sfx/ladder.mp3"),
            ("Break into the hospital sector", lambda: hospital(engine), "assets/sfx/hospital.mp3"),
        ],
    )



#SCENES
def streets(engine):
    show_scene(
        engine,
        text=(
            "The streets are burning.\n"
            "Creatures move between abandoned cars.\n\n"
            "What do you do?"
        ),
        background="assets/images/streets.jpg",
        choices=[
            ("Run to the police station", lambda: ending_survivor(engine),),
            ("Hide in a bus", lambda: ending_wanderer(engine),"assets/sfx/bus.mp3"),
            ("Follow a blood trail", lambda: ending_death(engine),"assets/sfx/death.mp3"),
        ],
    )


def maintenance(engine):
    show_scene(
        engine,
        text=(
            "You crawl into the maintenance tunnels.\n"
            "Something crawls in the dark.\n\n"
            "Your move?"
        ),
        background="assets/images/tunnel.webp",
        choices=[
            ("Sneak past quietly", lambda: ending_wanderer(engine)),
            ("Throw a rock", lambda: ending_death(engine)),
            ("Charge forward", lambda: ending_death(engine)),
        ],
    )


def hospital(engine):
    show_scene(
        engine,
        text=(
            "You break into the ruined hospital.\n"
            "A sealed sample glows bright green.\n\n"
            "What do you do?"
        ),
        background="assets/images/hospital.jpg",
        choices=[
            ("Search the labs", lambda: ending_failed_cure(engine)),
            ("Look for survivors", lambda: ending_survivor(engine)),
            ("Open the glowing sample...", lambda: ending_mutation(engine)),
        ],
    )


#ENDINGS
def ending_survivor(engine):
    engine.stop_sfx()
    show_scene(
        engine,
        text="ENDING: THE LAST FLIGHT\n\nYou escape the city alive.",
        background="assets/images/survivor.jpg",
        choices=[
            ("Try Again", lambda: title_screen(engine))
        ],
    )


def ending_wanderer(engine):
    engine.stop_sfx()
    show_scene(
        engine,
        text="ENDING: THE RUINS WANDERER\n\nYou wander the wasteland alone.",
        background="assets/images/wanderer.webp",
        choices=[
            ("Try Again", lambda: title_screen(engine))
        ],
    )


def ending_death(engine):
    engine.stop_sfx()
    show_scene(
        engine,
        text="ENDING: DEATH\n\nThe mutants overwhelm you.",
        background="assets/images/death.jpg",
        choices=[
            ("Try Again", lambda: title_screen(engine))
        ],
    )


def ending_failed_cure(engine):
    engine.stop_sfx()
    show_scene(
        engine,
        text="ENDING: FAILED CURE\n\nYou tried to help. Science failed you.",
        background="assets/images/lab.jpg",
        choices=[
            ("Try Again", lambda: title_screen(engine))
        ],
    )


def ending_mutation(engine):
    engine.stop_sfx()
    show_scene(
        engine,
        text=(
            "ENDING: BIRTH OF A BEAST\n\n"
            "Your skin burns. Your bones twist.\n"
            "You become one of them."
        ),
        background="assets/images/mutation.jpg",
        choices=[
            ("Try Again", lambda: title_screen(engine))
        ],
    )