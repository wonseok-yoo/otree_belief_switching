from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency, currency_range, Page, WaitPage,
)

import random


author = 'Won Seok Yoo'

doc = """
This app is about the belief updating - Task 0, Pure Belief Elicitation
"""


class Constants(BaseConstants):
    name_in_url = 'Task_0'
    players_per_group = None
    num_rounds = 15
    red_balls_box1 = 3
    green_balls_box1 = 6
    red_balls_box2 = 6
    green_balls_box2 = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        treatment_groups = ['Low_Cost', 'High_Cost']
        num_players = len(self.get_players())

        # Assign players to treatment groups randomly
        assigned_groups = random.choices(treatment_groups, k=num_players)

        for i, p in enumerate(self.get_players()):
            p.treatment_group = assigned_groups[i]

        for p in self.get_players():
            p.box = random.choice(['Green Box', 'Red Box'])
            p.box_endowment = {'Green Box': [Constants.green_balls_box1, Constants.red_balls_box1], 'Red Box': [Constants.green_balls_box2, Constants.red_balls_box2]}[p.box]
            p.ball_colors = []
            p.beliefs = []
            p.belief_dummy_1 = []
            p.belief_dummy_2 = []
            p.participant.vars['total_payoff'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prob_box1 = models.FloatField()
    prob_box2 = models.FloatField()
    ecu = models.FloatField(label = 'Belief Updating Reward', initial = 0)
    def update_probabilities(self, round_number):
        if round_number <= 5:
            self.prob_box1 = 0.25
            self.prob_box2 = 0.75
        elif 5 < round_number <= 10:
            self.prob_box1 = 0.5
            self.prob_box2 = 0.5
        else:
            self.prob_box1 = 0.75
            self.prob_box2 = 0.25
    box_initial = models.StringField(label = "intial Box")
    box_final = models.StringField(label = 'final box')
    ball_color = models.LongStringField(label = 'Signal for each round', initial = 'Red')
    belief = models.FloatField()
    belief_in = models.FloatField()
    decision = models.LongStringField(label = 'Swap or Not')
    cost = models.FloatField()
    treatment_group = models.StringField(label = 'Low_Cost or High_Cost')

class Introduction(Page):
    def is_displayed(player):
        return player.round_number == 1
    
class Introduction_2(Page):
    def is_displayed(player):
        return player.round_number == 1
       

class Instructions_0(Page):
    def is_displayed(player):
        return player.round_number == 1

class Waitt(WaitPage):
    wait_for_all_groups = True
    def is_displayed(player):
        return player.round_number == 1
    
class Practice_0(Page):
    def is_displayed(player):
        return player.round_number == 1
    
    
class Practice(Page):
    form_model = 'player'
    form_fields = ['belief_in']
    def is_displayed(player):
        return player.round_number == 1


class Practice_2(Page):
    form_model = 'player'
    form_fields = ['belief']
    def is_displayed(player):
        return player.round_number == 1
    def vars_for_template(player):
        previous = player.belief_in
        return {'pre_belief': previous}

class Practice_3(Page):
    form_model = 'player'
    form_fields = ['belief_in']
    def is_displayed(player):
        return player.round_number == 1
    def vars_for_template(player):
        previous = player.belief
        return {'pre_belief': previous}
    
class Start(Page):
    def is_displayed(player):
        return player.round_number == 1
    
class Instructions(Page):
    def is_displayed(player):
        return player.round_number == 1
    def vars_for_template(player):
        player.update_probabilities(player.round_number)
        prob = player.prob_box1
        return {'prob': int(prob*100), 'prob_inverse': int((1-prob)*100)}

class BoxEndowment(Page):

    def before_next_page(player, timeout_happened):
        if player.round_number % 5 == 1:
            player.update_probabilities(player.round_number)
            player.box_initial = random.choices(['Green Box', 'Red Box'], weights=(player.prob_box1, player.prob_box2))[0]
    def vars_for_template(player):
        player.update_probabilities(player.round_number)
        prob = player.prob_box1
        X = int(prob*4)
        return {'prob': int(prob*100), 'X': X}

    def is_displayed(player):
        return player.round_number%5 == 1

class InitialReportingBeliefs(Page):
    form_model = 'player'
    form_fields = ['belief_in']

    def vars_for_template(player):
        round = player.round_number % 5
        prob = player.prob_box1
        return {'round': round, 'pre_belief': 50, 'prob': int(prob*100)}
    def is_displayed(player):
        return player.round_number%5 == 1

class BallDrawing(Page):
    def vars_for_template(player):
        box_initial = player.in_round(1).box_initial
        if box_initial == 'Green Box':
            player.ball_color = random.choices(['Green', 'Red'], weights=(6, 3))[0]
        else:
            player.ball_color = random.choices(['Green', 'Red'], weights=(3, 6))[0]
        round = player.round_number%5
        if round ==0 :
            round = 5
        color_image = str(player.ball_color)+"_ball.png"
        return {'ball_color': player.ball_color, 'round': round, 'image' : color_image}


class ReportingBeliefs(Page):
    form_model = 'player'
    form_fields = ['belief']

    def vars_for_template(player):
        round = player.round_number % 5
        if round == 0:
            round = 5
        return {'round': round, 'pre_belief': player.in_round(player.round_number - 1).belief if round > 1 else player.in_round(player.round_number).belief_in, 'ball_color': player.ball_color}
class NextTask(Page):
    def is_displayed(player):
        return player.round_number == 5 or player.round_number == 10

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision', 'belief']
    def vars_for_template(player):
        if player.in_round(1).treatment_group == 'High_Cost':
            cost = 0.4
        elif player.in_round(1).treatment_group == 'Low_Cost':
            cost = 0.2
        else:
            cost = 0
        guess = player.belief
        return {'cost': cost, 'guess': guess}

    def before_next_page(player, timeout_happened):
        if player.decision == 'swap':
            if player.in_round(1).box_initial == 'Green Box':
                player.box_final = 'Red Box'
            else:
                player.box_final = 'Green Box'
        if player.decision == 'keep':
            player.box_final = player.in_round(1).box_initial

    def is_displayed(player):
        return player.round_number%5 == 0

class Payoff(Page):
    form_model = 'player'
    def vars_for_template(player):
        r = random.randint(0,2)
        k = random.randint(1,6)
        Box = player.in_round(5*r+1).box_initial
        if k == 6:
            report = player.in_round(5*r+1).belief_in
        else:
            report = player.in_round(5*r+k).belief
        if Box == 'Green Box':
            prob = (1-((100-report)/100)**2)
        if Box == 'Red Box':
            prob = (1-(report/100)**2)
        score = random.choices([2,0], weights=(prob, 1-prob))[0]
        player.payoff = score

        return {'payoff': player.payoff}
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    def before_next_page(player, timeout_happened):
        player.participant.payoff = 0
        player.participant.payoff = player.payoff
class Wait(WaitPage):
    wait_for_all_groups = True
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

page_sequence = [
    Introduction_2,
    Introduction,
    Instructions_0,
    Instructions,
    Practice_0,
    Practice,
    Waitt,
    Waitt,
    Practice_2,
    Practice_3,
    Waitt,
    Start,
    BoxEndowment,
    InitialReportingBeliefs,
    BallDrawing,
    ReportingBeliefs,
    NextTask,
    Payoff,
    Wait,
]
