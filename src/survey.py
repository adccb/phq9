class Survey:
    choices = [ 'not at all', 'several days', 'more than half the days', 'nearly every day' ]
    questions = [ 'little interest or pleasure in doing things', 'feeling down, depressed, or hopeless', 'trouble falling or staying asleep, or sleeping too much', 'feeling tired or having little energy', 'poor appetite or overeating', 'feeling bad about yourself—or that you are a failure or have let yourself or your family down', 'trouble concentrating on things, such as reading the newspaper or watching television', 'moving or speaking so slowly that other people could have noticed. or the opposite—being so fidgety or restless that you have been moving around a lot more than usual', 'thoughts that you would be better off dead, or of hurting yourself']

    def __init__(self):
        self.answers = [ {'q': question, 'a': None} for question in self.questions ]

    def total(self):
        return sum([ x['a'] for x in self.answers ])

    def __getitem__(self, idx):
        if idx >= len(self.questions) or idx < 0:
            return False

        return self.questions[idx]

    def __setitem__(self, idx, ans):
        if idx >= len(self.questions):
            return False

        self.answers[idx]['a'] = ans

    def __len__(self):
        # len() should return only the number of unfinished answers
        return len([ x['a'] for x in self.answers if x['a'] is None ])

