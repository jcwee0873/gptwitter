import random
from enum import Enum

import numpy as np 
from scipy.stats import lognorm


class Job(Enum):
    """
    """
    ACCOUNTANT = "ACCOUNTANT"
    ACTOR = "ACTOR"
    ARCHITECT = "ARCHITECT"
    ARTIST = "ARTIST"
    ATHLETE = "ATHLETE"
    CHEF = "CHEF"
    DENTIST = "DENTIST"
    DOCTOR = "DOCTOR"
    ENGINEER = "ENGINEER"
    FARMER = "FARMER"
    FIREFIGHTER = "FIREFIGHTER"
    JOURNALIST = "JOURNALIST"
    LAWYER = "LAWYER"
    MANAGER = "MANAGER"
    MUSICIAN = "MUSICIAN"
    NURSE = "NURSE"
    PHOTOGRAPHER = "PHOTOGRAPHER"
    PILOT = "PILOT"
    POLICE_OFFICER = "POLICE_OFFICER"
    SCIENTIST = "SCIENTIST"
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    WRITER = "WRITER"

    @classmethod
    def random(cls):
        return random.choice(list(cls))
    

class MBTI(Enum):
    """
    """
    ENFJ = "ENFJ"
    ENFP = "ENFP"
    ENTJ = "ENTJ"
    ENTP = "ENTP"
    ESFJ = "ESFJ"
    ESFP = "ESFP"
    ESTJ = "ESTJ"
    ESTP = "ESTP"
    INFJ = "INFJ"
    INFP = "INFP"
    INTJ = "INTJ"
    INTP = "INTP"
    ISFJ = "ISFJ"
    ISFP = "ISFP"
    ISTJ = "ISTJ"
    ISTP = "ISTP"

    @classmethod
    def random(cls):
        return random.choice(list(cls))
    

class Wealth:
    """
    """
    mean_log = np.log(54772)
    sigma_log = 0.7

    def random(self) -> tuple[float, float]:
        """
        """
        property_value = np.random.lognormal(self.mean_log, self.sigma_log)
        percentile = 100 - (lognorm.cdf(property_value, self.sigma_log, scale=np.exp(self.mean_log)) * 100)

        return round(percentile, 2)
    

class Gender(Enum):
    CISGENDER_MALE = "Cisgender Male"  # 생물학적 성별과 일치하는 남성
    CISGENDER_FEMALE = "Cisgender Female"  # 생물학적 성별과 일치하는 여성
    TRANSGENDER_MALE = "Transgender Male"  # 생물학적 성별과 일치하지 않는 남성
    TRANSGENDER_FEMALE = "Transgender Female"  # 생물학적 성별과 일치하지 않는 여성
    NON_BINARY = "Non-Binary"  # 이진적 성별 구분과 일치하지 않는 정체성
    GENDERQUEER = "Genderqueer"  # 전통적 성별 레이블과 일치하지 않는, 또는 그 사이의 정체성
    GENDERFLUID = "Genderfluid"  # 시간에 따라 성별 정체성이 변하는
    AGENDER = "Agender"  # 성별이 없는 또는 성별에 무관심한


    @classmethod
    def random(cls):
        return random.choice(list(cls))
    

class Education(Enum):
    NO_FORMAL_EDUCATION = "No Formal Education"
    ELEMENTARY = "Elementary School"
    MIDDLE_SCHOOL = "Middle School"
    HIGH_SCHOOL = "High School"
    ASSOCIATES_DEGREE = "Associates Degree"
    BACHELORS_DEGREE = "Bachelors Degree"
    MASTERS_DEGREE = "Masters Degree"
    DOCTORATE = "Doctorate"
    POST_DOCTORATE = "Post Doctorate"

    def random(cls):
        return random.choice(list(cls))