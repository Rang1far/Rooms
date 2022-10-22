import winsound

def start_quest_sound():
    winsound.PlaySound("main_quest.wav", winsound.SND_ASYNC)


def true_end_sound():
    winsound.PlaySound("true_end.wav", winsound.SND_ASYNC)


def inf_door_end_sound():
    winsound.PlaySound("inf_door_end.wav", winsound.SND_ASYNC)

def bad_end_sound():
    winsound.PlaySound("Bad_end.wav", winsound.SND_ASYNC)
