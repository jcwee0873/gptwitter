from gpt_witter.agent.trait import Job, Gender, Wealth, MBTI


INTRODUCE_TEMPLATE = """

"""


class WitterUser:
    def __init__(
        self,
        **kargs
    ) -> None:
        """
        AI GPT-WITTER User initialization.
        
        User has traits such as job, gender, wealth, mbti, etc.

        Parameters
        ----------
        job: str
            gpt_witter.agent.trait.Job / default: random
        gender: str 
            gpt_witter.agent.trait.Gender / default: random
        mbti: str
            gpt_witter.agent.trait.MBTI / default: random
        wealth: float
            Top income bracket / range: 0.00 ~ 100.00 / default: random

        Returns
        -------
        None
        """
        self.name = kargs.get('name')
        self.job = kargs.get('job', Job.random())
        self.gender = kargs.get('gender', Gender.random())

        self.wealth = kargs.get('wealth', Wealth.random())
        if not (0.00 <= self.wealth <= 100.00):
            raise ValueError("Parameter wealth must be between 0.00 and 100.00")

        self.mbti = kargs.get('mbti', MBTI.random())


    def to_dict(self):
        return {
            "job": self.job.value,
            "gender": self.gender.value,
            "wealth": self.wealth,
            "mbti": self.mbti.value
        }


    def introduce(self):
        return INTRODUCE_TEMPLATE.format(**self.to_dict)
    
