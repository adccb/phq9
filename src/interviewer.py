import colorama

colorama.init()

class Interviewer():
    def __init__(self, survey):
        self.survey = survey
        self.question = 0

        print(
            colorama.Fore.GREEN + 
            'over a period of the past two weeks, how often have you been bothered by each of the following problems?\n' +
            colorama.Style.RESET_ALL
        )

        for idx, choice in enumerate(self.survey.choices):
            print(f'  {idx} — {choice}')
        print()

    def ask_next_question(self):
        print(
            colorama.Fore.BLUE +
            self.survey[self.question] +
            colorama.Style.RESET_ALL
        )
        answer = int(input())
        self.survey[self.question] = answer
        self.question += 1
