from os import environ

SESSION_CONFIGS = [
    dict(
        name='eliciting_beliefs',
        display_name="Belief Elicitation",
        num_demo_participants=5,
        app_sequence=['Task0', 'Task1', 'Task2', 'Task3', 'risk_elicit', 'survey','payment_info'],
    ),
]

INSTALLED_APPS = [
    # other apps
    'otree',
    'eliciting_beliefs',
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=10.00, doc=""
)

PARTICIPANT_FIELDS = ['total_payoff']
SESSION_FIELDS = []

LANGUAGE_CODE = 'en'

REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='Belief_Switching_Cost',
        display_name='Belief_Switching',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

SECRET_KEY = '6494541717266'
