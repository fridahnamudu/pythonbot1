import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "I don't love, i don't have feelings, but i wish  i had, just focus on yourself, life is too short for crazy love!"
def unknown():
    response = ['Could you re-phrase that?',
                "...",
                "Sounds about right",
                "Get out of here!"
                "What does that mean?"][random.randrange(4)]
    return response