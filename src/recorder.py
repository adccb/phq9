import json
import os
import datetime
from pathlib import Path

class Recorder():
    directory = f'{Path.home()}/.phq9'
    date = datetime.datetime.today().strftime('%Y-%m-%d')

    def __init__(self):
        self.filename = f'{self.directory}/history.json'
        self._make_storage_dir_if_not_exists()
        with open(self.filename, 'r') as file:
            self.answers = json.loads(file.read())

    def list_surveys(self):
        return { date: sum([ q['a'] for q in survey ]) for date, survey in self.answers.items() }

    def add_survey(self, survey):
        self.answers[self.date] = survey.answers
        with open(self.filename, 'w') as file:
            file.write(json.dumps(self.answers))

    def _make_storage_dir_if_not_exists(self):
        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                file.write('{}')
