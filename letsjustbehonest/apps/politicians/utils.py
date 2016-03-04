import datetime
import requests

from .models import Politician, Role, Statement
from .politifact_data import SPEAKER_LIST

# too large a query for the API > 200 > majority of speaker statement totals
STATEMENTS_LIMIT = 200


def backload_statements_by_speaker():
    base_url = 'http://www.politifact.com/'
    api_path = 'api/v/2/statement/?speaker__name_slug={0}&format=json&limit={1}'

    def store_statements_from_api(next_url=None):
        url = base_url + api_path.format(politician.slug, STATEMENTS_LIMIT) \
            if not next_url else base_url + next_url

        resp = requests.get(url)
        data = resp.json()
        for obj in data.objects:
            statement_date = convert_datestring_to_date(obj.statement_date)
            ruling_date = convert_datestring_to_date(obj.ruling.ruling_date)
            Statement.objects.create(
                speaker=politician,
                ruling=obj.ruling.ruling,
                ruling_headline=obj.ruling.ruling_headline,
                quote=obj.statement,
                context=obj.statement_context,
                url=obj.canonical_url,
                statement_date=statement_date,
                ruling_date=ruling_date
            )
        if data.meta and data.meta.next:
            store_statements_from_api(data.meta.next)

    def convert_datestring_to_date(date_string):
        year, month, day = date_string.split('-')
        date_object = datetime.date(year=year, month=month, day=day[:2])
        return date_object

    for speaker in SPEAKER_LIST:
        try:
            politician = Politician.objects.get(slug=speaker.slug)
        except Politician.DoesNotExist:
            politician = Politician.objects.create(
                slug=speaker.slug, first_name=speaker.first,
                last_name=speaker.last, party=speaker.party
            )
            for r in speaker.roles:
                role = Role.objects.get_or_create(label=r)
                politician.roles.add(role)
        store_statements_from_api(politician)
