from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Page,
)

import random


class Constants(BaseConstants):
    name_in_url = 'mpl_experiment'
    players_per_group = None
    num_rounds = 1
    MPL = [
        (1,  "100% chance of 200 ECU", "0% of 400 ECU, and 100% chance of 0 ECU"),
        (2,  "100% chance of 200 ECU", "10% of 400 ECU, and 90% chance of 0 ECU"),
        (3,  "100% chance of 200 ECU", "20% of 400 ECU, and 80% chance of 0 ECU"),
        (4,  "100% chance of 200 ECU", "30% of 400 ECU, and 70% chance of 0 ECU"),
        (5,  "100% chance of 200 ECU", "40% of 400 ECU, and 60% chance of 0 ECU"),
        (6,  "100% chance of 200 ECU", "50% of 400 ECU, and 50% chance of 0 ECU"),
        (7,  "100% chance of 200 ECU", "60% of 400 ECU, and 40% chance of 0 ECU"),
        (8,  "100% chance of 200 ECU", "70% of 400 ECU, and 30% chance of 0 ECU"),
        (9,  "100% chance of 200 ECU", "80% of 400 ECU, and 20% chance of 0 ECU"),
        (10, "100% chance of 200 ECU", "90% of 400 ECU, and 10% chance of 0 ECU"),
        (11, "100% chance of 200 ECU", "100% of 400 ECU, and 0% chance of 0 ECU"),
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    choice_1 = models.StringField()
    choice_2 = models.StringField()
    choice_3 = models.StringField()
    choice_4 = models.StringField()
    choice_5 = models.StringField()
    choice_6 = models.StringField()
    choice_7 = models.StringField()
    choice_8 = models.StringField()
    choice_9 = models.StringField()
    choice_10 = models.StringField()
    choice_11 = models.StringField()


class Introduction(Page):
    pass

class MPLDecision(Page):
    form_model = 'player'
    form_fields = ['choice_1', 'choice_2','choice_3','choice_4','choice_5','choice_6','choice_7',
                   'choice_8','choice_9','choice_10','choice_11']
    def vars_for_template(player):
        return {'MPL': Constants.MPL}

class Result(Page):
    def vars_for_template(player):
        R = random.randint(1, 11)
        choice = getattr(player, f"choice_{R}")
        if choice == 'A':
            score = 2
        if choice == 'B':
            prob = (R+1)/10
            score = random.choices([4,0], weights=(prob, 1-prob))[0]
        player.payoff += score
        return {'payoff': player.payoff, 'choice':choice, 'R': R}


class Payoff(Page):
    def vars_for_template(player):
        payoff = player.participant.payoff_plus_participation_fee()
        return{'payoff': payoff}

page_sequence = [Introduction, MPLDecision, Result, Payoff]
