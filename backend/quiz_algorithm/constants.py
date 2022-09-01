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
    STEP1_SUBSTEP_50 = 50
    STEP1_SUBSTEP_60 = 60
    STEP1_SUBSTEP_70 = 70
    STEP1_SUBSTEP_80 = 80
    STEP1_SUBSTEP_90 = 90
    STEP1_SUBSTEP_100 = 100
    STEP1_SUBSTEP_110 = 110
    STEP1_SUBSTEP_120 = 120
    STEP1_SUBSTEP_130 = 130
    STEP1_SUBSTEP_140 = 140
    STEP1_SUBSTEP_150 = 150
    STEP1_SUBSTEP_160 = 160
    STEP1_SUBSTEP_170 = 170
    STEP1_SUBSTEP_180 = 180
    STEP1_SUBSTEP_190 = 190
    STEP1_SUBSTEP_200 = 200


class Step2SubSteps(AlgorithmSubStep):
    STEP2_SUBSTEP_10 = 10
    STEP2_SUBSTEP_20 = 20
    STEP2_SUBSTEP_30 = 30
    STEP2_SUBSTEP_40 = 40
    STEP2_SUBSTEP_50 = 50
    STEP2_SUBSTEP_60 = 60
    STEP2_SUBSTEP_70 = 70
    STEP2_SUBSTEP_80 = 80
    STEP2_SUBSTEP_90 = 90
    STEP2_SUBSTEP_100 = 100
    STEP2_SUBSTEP_110 = 110
    STEP2_SUBSTEP_120 = 120
    STEP2_SUBSTEP_130 = 130
    STEP2_SUBSTEP_140 = 140
    STEP2_SUBSTEP_150 = 150
    STEP2_SUBSTEP_160 = 160
    STEP2_SUBSTEP_170 = 170
    STEP2_SUBSTEP_180 = 180
    STEP2_SUBSTEP_190 = 190
    STEP2_SUBSTEP_200 = 200


class Step3SubSteps(AlgorithmSubStep):
    STEP3_STEP_10 = 10
    STEP3_STEP_20 = 20
    STEP3_STEP_30 = 30
    STEP3_STEP_40 = 40
    STEP3_STEP_50 = 50
    STEP3_STEP_60 = 60
    STEP3_STEP_70 = 70
    STEP3_STEP_80 = 80
    STEP3_STEP_90 = 90
    STEP3_STEP_100 = 100
    STEP3_STEP_110 = 110
    STEP3_STEP_120 = 120
    STEP3_STEP_130 = 130
    STEP3_STEP_140 = 140
    STEP3_STEP_150 = 150
    STEP3_STEP_160 = 160
    STEP3_STEP_170 = 170
    STEP3_STEP_180 = 180
    STEP3_STEP_190 = 190
    STEP3_STEP_200 = 200


class Step4SubSteps(AlgorithmSubStep):
    STEP4_SUBSTEP_10 = 10
    STEP4_SUBSTEP_20 = 20
    STEP4_SUBSTEP_30 = 30
    STEP4_SUBSTEP_40 = 40
    STEP4_SUBSTEP_50 = 50
    STEP4_SUBSTEP_60 = 60
    STEP4_SUBSTEP_70 = 70
    STEP4_SUBSTEP_80 = 80
    STEP4_SUBSTEP_90 = 90
    STEP4_SUBSTEP_100 = 100
    STEP4_SUBSTEP_110 = 110
    STEP4_SUBSTEP_120 = 120
    STEP4_SUBSTEP_130 = 130
    STEP4_SUBSTEP_140 = 140
    STEP4_SUBSTEP_150 = 150
    STEP4_SUBSTEP_160 = 160
    STEP4_SUBSTEP_170 = 170
    STEP4_SUBSTEP_180 = 180
    STEP4_SUBSTEP_190 = 190
    STEP4_SUBSTEP_200 = 200


class Step5SubSteps(AlgorithmSubStep):
    STEP5_SUBSTEP_10 = 10
    STEP5_SUBSTEP_20 = 20
    STEP5_SUBSTEP_30 = 30
    STEP5_SUBSTEP_40 = 40
    STEP5_SUBSTEP_50 = 50
    STEP5_SUBSTEP_60 = 60
    STEP5_SUBSTEP_70 = 70
    STEP5_SUBSTEP_80 = 80
    STEP5_SUBSTEP_90 = 90
    STEP5_SUBSTEP_100 = 100
    STEP5_SUBSTEP_110 = 110
    STEP5_SUBSTEP_120 = 120
    STEP5_SUBSTEP_130 = 130
    STEP5_SUBSTEP_140 = 140
    STEP5_SUBSTEP_150 = 150
    STEP5_SUBSTEP_160 = 160
    STEP5_SUBSTEP_170 = 170
    STEP5_SUBSTEP_180 = 180
    STEP5_SUBSTEP_190 = 190
    STEP5_SUBSTEP_200 = 200


class Step6SubSteps(AlgorithmSubStep):
    STEP6_SUBSTEP_10 = 10
    STEP6_SUBSTEP_20 = 20
    STEP6_SUBSTEP_30 = 30
    STEP6_SUBSTEP_40 = 40
    STEP6_SUBSTEP_50 = 50
    STEP6_SUBSTEP_60 = 60
    STEP6_SUBSTEP_70 = 70
    STEP6_SUBSTEP_80 = 80
    STEP6_SUBSTEP_90 = 90
    STEP6_SUBSTEP_100 = 100
    STEP6_SUBSTEP_110 = 110
    STEP6_SUBSTEP_120 = 120
    STEP6_SUBSTEP_130 = 130
    STEP6_SUBSTEP_140 = 140
    STEP6_SUBSTEP_150 = 150
    STEP6_SUBSTEP_160 = 160
    STEP6_SUBSTEP_170 = 170
    STEP6_SUBSTEP_180 = 180
    STEP6_SUBSTEP_190 = 190
    STEP6_SUBSTEP_200 = 200


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
