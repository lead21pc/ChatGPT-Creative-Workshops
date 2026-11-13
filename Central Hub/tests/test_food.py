"""Static checks of the active Food wording against declared cases; no model execution."""
from test_hub_contracts import entry_path, package
import pytest


@pytest.fixture
def evidence_boundary():
    entry = entry_path(package('FOOD')).read_text(encoding='utf-8')
    return entry.split('## Evidence and purchase boundaries\n', 1)[1].split('\n## ', 1)[0]


@pytest.mark.parametrize(('case', 'required_rules'), [
    ('A closed branch', (
        'the specific branch',
        'Exclude options with a supported failure of a required condition',
        'Retain independently supported culinary findings.',
    )),
    ('B closed at the requested weekend time', (
        'requested time',
        'Exclude options with a supported failure of a required condition from the actionable set for that scope.',
    )),
    ('C listing present but ShopeeFood orders not accepted', (
        'dine-in or delivery channel',
        'it does not establish that the branch is open, accepts orders or offers the dish',
        'Exclude options with a supported failure of a required condition',
    )),
    ('D dessert-only partial menu', (
        'availability of the target dish through that channel',
        'A partial menu supports only what was observed; an omitted dish remains unverified from that menu.',
        'Send unresolved material conditions to Hub as scoped evidence questions.',
    )),
    ('E old mutton biryani menu', (
        'A past menu or review supports availability only within its evidenced scope and time.',
        'availability of the target dish through that channel',
        'Present unresolved options as conditional',
    )),
    ('F culinary style or region only', (
        'Apply operational checks only when they matter to the task',
        'style, regional and dish analysis alone do not require them.',
        'when an unresolved regional or other factual distinction materially affects the result',
    )),
    ('G supported and unresolved choices in one ranking', (
        'assess culinary fit and practical availability separately.',
        'Present unresolved options as conditional, distinct from options supported for the requested action.',
    )),
])
def test_restaurant_recommendation_contract(evidence_boundary, case, required_rules):
    for rule in required_rules:
        assert rule in evidence_boundary, case
