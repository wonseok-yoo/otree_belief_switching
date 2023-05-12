from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    participate = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Have you participated in a similar economic experiment?',
        widget=widgets.RadioSelect,
    )
    
    gender = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Was the instruction clear?',
        widget=widgets.RadioSelect,
    )
    
    crt_bat = models.LongStringField(
        label='''
        In scenario 0, you did not have any box. In scenario 3, you had the box, but could not make any decision to swap or to keep. Do you think there is any difference between the two? If so, what did you think it was?'''
    )
    crt_widget = models.LongStringField(
        label='''
        Did the fact that you have to pay costs to swap the box in scenario 2 affect your guess? If so, how? 
        '''
    )
    crt_c = models.LongStringField(
        label='''
            Did you report your best guess? Or, did you misreport your guess intentionally? If so, why? '''
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender','participate']


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_c']


page_sequence = [Demographics, CognitiveReflectionTest]
