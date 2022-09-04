from enum import Enum, IntEnum

from typing_extensions import Type


class Sign(IntEnum):
    # It's important to start with 0 because we want indexes in the array to match the enum values
    FIRE = 0
    EARTH = 1
    METAL = 2
    WATER = 3
    WOOD = 4


class AlgorithmSubStep(IntEnum):
    pass


class Step1SubSteps(AlgorithmSubStep):
    STEP1_SUBSTEP_10 = 10
    STEP1_SUBSTEP_20 = 20
    STEP1_SUBSTEP_30 = 30
    STEP1_SUBSTEP_40 = 40
    STEP1_SUBSTEP_50_60 = 50
    STEP1_SUBSTEP_70_80 = 70
    STEP1_SUBSTEP_90_100 = 90


class Step2SubSteps(AlgorithmSubStep):
    STEP2_SUBSTEP_10_20 = 10


class Step3SubSteps(AlgorithmSubStep):
    STEP3_SUBSTEP_10_20 = 10
    STEP3_SUBSTEP_30_40 = 30
    STEP3_SUBSTEP_50_60 = 50
    STEP3_SUBSTEP_70_80 = 70
    STEP3_SUBSTEP_90_100 = 90
    STEP3_SUBSTEP_110_120_130 = 110


class Step4SubSteps(AlgorithmSubStep):
    STEP4_SUBSTEP_10_20 = 10
    STEP4_SUBSTEP_30_40 = 30
    STEP4_SUBSTEP_50_60 = 50
    STEP4_SUBSTEP_70_80 = 70


class Step5SubSteps(AlgorithmSubStep):
    STEP5_SUBSTEP_10_20_30 = 10
    STEP5_SUBSTEP_40_50_60 = 40
    STEP5_SUBSTEP_70_80 = 70
    STEP5_SUBSTEP_90_100 = 90


class Step6SubSteps(AlgorithmSubStep):
    STEP6_SUBSTEP_10_20_30 = 10


class AlgorithmStep(IntEnum):
    STEP_1 = 1
    STEP_2 = 2
    STEP_3 = 3
    STEP_4 = 4
    STEP_5 = 5
    STEP_6 = 6

    def get_substep_class(self) -> Type[AlgorithmSubStep]:
        if self == AlgorithmStep.STEP_1:
            return Step1SubSteps
        if self == AlgorithmStep.STEP_2:
            return Step2SubSteps
        if self == AlgorithmStep.STEP_3:
            return Step3SubSteps
        if self == AlgorithmStep.STEP_4:
            return Step4SubSteps
        if self == AlgorithmStep.STEP_5:
            return Step5SubSteps
        if self == AlgorithmStep.STEP_6:
            return Step6SubSteps
        else:
            raise ValueError(f"Unknown step: {self}")
