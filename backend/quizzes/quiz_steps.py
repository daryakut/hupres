from enum import Enum


class QuizSubStep(Enum):
    STEP1_SUBSTEP_10 = '1__10'
    STEP1_SUBSTEP_20 = '1__20'
    STEP1_SUBSTEP_30 = '1__30'
    STEP1_SUBSTEP_40 = '1__40'
    STEP1_SUBSTEP_50_60 = '1__50_60'
    STEP1_SUBSTEP_70_80 = '1__70_80'
    STEP1_SUBSTEP_90_100 = '1__90_100'

    STEP2_SUBSTEP_10_20 = '2__10_20'

    STEP3_SUBSTEP_10_20 = '3__10_20'
    STEP3_SUBSTEP_30_40 = '3__30_40'
    STEP3_SUBSTEP_50_60 = '3__50_60'
    STEP3_SUBSTEP_70_80 = '3__70_80'
    STEP3_SUBSTEP_90_100 = '3__90_100'
    STEP3_SUBSTEP_110_120_130 = '3__110_120_130'

    STEP4_SUBSTEP_10_20 = '4__10_20'
    STEP4_SUBSTEP_30_40 = '4__30_40'
    STEP4_SUBSTEP_50_60 = '4__50_60'
    STEP4_SUBSTEP_70_80 = '4__70_80'

    STEP5_SUBSTEP_10_20_30 = '5__10_20_30'
    STEP5_SUBSTEP_40_50_60 = '5__40_50_60'
    STEP5_SUBSTEP_70_80 = '5__70_80'
    STEP5_SUBSTEP_90_100 = '5__90_100'

    STEP6_SUBSTEP_10_20_30 = '6__10_20_30'


class QuizStep(Enum):
    STEP_1 = '1'
    STEP_2 = '2'
    STEP_3 = '3'
    STEP_4 = '4'
    STEP_5 = '5'
    STEP_6 = '6'


TABLET_SUB_STEPS = [
    QuizSubStep.STEP1_SUBSTEP_10,
    QuizSubStep.STEP1_SUBSTEP_20,
    QuizSubStep.STEP1_SUBSTEP_30,
    QuizSubStep.STEP1_SUBSTEP_40,
]
