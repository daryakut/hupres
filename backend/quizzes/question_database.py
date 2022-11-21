from enum import Enum

from models.sign import Sign


class QuestionName(Enum):
    # First four tablet questions
    HEIGHT = 'Рост'
    BODY_SCHEME = 'Схема тела'
    EYE_COLOR = 'Цвет глаз'
    HAIR_COLOR = 'Цвет волос'

    # Rest of the questions
    STRUCTURE_OF_HAIR = 'Структура волос'
    FEATURES_OF_SKIN = 'Особенности кожи'
    BACK_OF_NOSE = 'Спинка носа'
    SIZE_OF_NOSE = 'Размер носа'
    FACE_SHAPE = 'Форма лица'
    NOSE_SHAPE = 'Форма носа'
    CONVEXITY_OF_NAILS = 'Выпуклость ногтей'
    SIZE_OF_PALMS = 'Размер ладони'
    BODY_FEATURES = 'Тело особенности'
    FINGER_SHAPE = 'Форма пальцев'
    NAIL_SHAPE = 'Ногти форма'
    WAIST = 'Талия'
    NOSE_TIP = 'Кончик носа'
    NOSTRILS = 'Ноздри'
    PALM_SHAPE = 'Форма ладони'
    WIDTH_OF_BACK_OF_NOSE = 'Ширина спинки носа'
    MUSCLE_VOLUME = 'Объем мышц'
    FAT_TISSUE = 'Жировая клетчатка'
    THICKNESS_OF_HAIR = 'Толщина волос'
    HAIR_DENSITY = 'Густота волос'
    FINGER_LENGTH = 'Длина пальцев'
    FEATURES_OF_BRUSHES = 'Особенности кистей'
    MUSCLE_DENSITY = 'Мышцы плотность'
    LENGTH_OF_NECK = 'Длина шеи'
    THICKNESS_OF_NECK = 'Толщина шеи'
    HAIR_FEATURES = 'Особенности волос'
    FEATURES_OF_FINGERS = 'Особенности пальцев'


class AnswerName(Enum):
    HARD_TO_SAY = 'Затрудняюсь ответить'

    # Height Descriptors
    HEIGHT_SHORT = 'Рост низкий'
    HEIGHT_AVERAGE = 'Рост средний'
    HEIGHT_TALL = 'Рост высокий'

    # Body Shape Descriptors
    SHAPE_SMALL_RECTANGLE = 'Малый прямоугольник'
    SHAPE_NARROW_RECTANGLE = 'Узкий прямоугольник'
    SHAPE_LARGE_WIDE_RECTANGLE = 'Больш шир прямоугольник'
    SHAPE_BROAD_SHOULDERS = 'Шире в плечах'
    SHAPE_BROAD_HIPS = 'Шире в бедрах'
    BODY_DRY = 'Тело сухое'
    BODY_VOLUMINOUS = 'Тело объемное'
    WAIST_DEFINED = 'Талия выражена'
    WAIST_SMOOTHED = 'Талия сглажена'

    # Fat Tissue Descriptors
    FAT_TISSUE_WEAK = 'Жир клетч слабая'
    FAT_TISSUE_STRONG = 'Жир клетч выражена'

    # Eye Color Descriptors
    EYES_BLUE = 'Голубые глаза'
    EYES_GRAY = 'Серые (стальные) глаза'
    EYES_GRAY_BLUE_DARK_SPECKS = 'Серо-голуб гл с темн вкрапл'
    EYES_GRAY_BLUE_YELLOW_GREEN_ZONES = 'Серо-голуб гл с жел-зел зонами'
    EYES_BLACK = 'Черные глаза'
    EYES_BROWN = 'Карие глаза'
    EYES_GREEN = 'Зеленые глаза'
    EYES_YELLOW_GREEN = 'Желто-зеленые глаза'
    EYES_HETEROCHROMATIC = 'Рябые глаза'

    # Hair Texture and Color Descriptors
    HAIR_THIN = 'Тонкие волосы'
    HAIR_MEDIUM_THICKNESS = 'Волосы средней толщины'
    HAIR_THICK = 'Толстые волосы'
    HAIR_SPARSE = 'Редкие волосы'
    HAIR_DENSE = 'Густые волосы'
    HAIR_STRAIGHT = 'Прямые волосы'
    HAIR_WAVY = 'Волнистые волосы'
    HAIR_CURLY = 'Кучерявые волосы'
    HAIR_RED = 'Рыжие волосы'
    HAIR_CHESTNUT = 'Каштановые волосы'
    HAIR_BLACK = 'Черные волосы'
    HAIR_DARK_BLONDE = 'Темно русые волосы'
    HAIR_BLONDE = 'Русые волосы'
    HAIR_LIGHT = 'Светлые волосы'
    HAIR_COARSE = 'Жесткие волосы'
    HAIR_EARLY_GRAYING = 'Ранняя седина'
    HAIR_EARLY_BALDING = 'Ранние залысины'

    # Facial Shape Descriptors
    FACE_ROUND = 'Круглое лицо'
    FACE_LONG_RECTANGLE = 'Вытянутый прямоугольник'
    FACE_LARGE_TRIANGLE = 'Большой треугольник'
    FACE_SMALL_TRIANGLE = 'Малый треугольник'
    FACE_BROAD_RECTANGLE_SQUARE = 'Широк прямоугольн "Квадрат"'

    # Nose Descriptors
    NOSE_SMALL = 'Малый нос'
    NOSE_LARGE = 'Крупный нос'
    NOSE_HUMP = 'Горбинка на носу'
    NOSE_HOOKED = 'Крючковидный нос'
    NOSE_STRAIGHT = 'Прямой нос'
    NOSTRILS_WIDE = 'Широкие ноздри'
    NOSTRILS_NARROW = 'Узкие ноздри'
    NOSE_SHARP_TIP = 'Острый кончик носа'
    NOSE_ROUND_TIP = 'Круглый кончик носа'
    NOSE_TURNED_UP_TIP = 'Курносый кончик носа'
    NOSE_DUCKLIKE = 'Нос "уточкой"'
    NOSE_LONG_BACK = 'Длинная спинка носа'
    NOSE_SHORT_BACK = 'Короткая спинка носа'
    NOSE_WIDE_BACK = 'Широкая спинка носа'
    NOSE_THIN_BACK = 'Тонкая спинка носа'

    # Neck Descriptors
    NECK_SHORT = 'Шея короткая'
    NECK_AVERAGE_LENGTH = 'Средняя длина шеи'
    NECK_LONG = 'Длинная шея'
    NECK_THICK = 'Толстая шея'
    NECK_AVERAGE_THICKNESS = 'Средняя толщина шеи'
    NECK_THIN = 'Тонкая шея'

    # Hand and Finger Descriptors
    HANDS_LARGE = 'Крупные ладони'
    HANDS_SMALL = 'Малые ладони'
    HAND_SHAPE_SQUARE = 'Квадрат'
    HAND_SHAPE_RECTANGLE = 'Прямоугольник'
    HAND_SHAPE_SMALL_RECTANGLE = 'Малый прямоугольник'
    HAND_SHAPE_NARROW_LONG_RECTANGLE = 'Узкий вытян прямоугольник'
    HAND_SHAPE_PADDLE = '"Весло"'
    HANDS_SOFT_LOOSE = 'Мягкие рыхлые ладони'
    HANDS_FULL_FIRM = 'Налитые плотные ладони'
    HANDS_DRY = '"Сухие" кисти'
    FINGERS_LONG = 'Длинные пальцы'
    FINGERS_AVERAGE_LENGTH = 'Средняя длина пальцев'
    FINGERS_SHORT = 'Короткие пальцы'
    FINGERS_STRAIGHT = 'Ровные пальцы'
    FINGERS_CONICAL = 'Конусообразные пальцы'
    FINGERS_CROOKED = 'Искривленные пальцы'
    FINGERS_KNOTTY = 'Узловатые пальцы'
    FINGERS_DRY = '"Сухие" пальцы'
    FINGERS_FLESHY = 'Мясистые пальцы'

    # Additional Descriptors
    SHAPE_LONG_RECTANGLE = 'Длинный прямоугольник'
    SHAPE_SHORT_TRAPEZOID = 'Трапеция короткая'
    SHAPE_LONG_TRAPEZOID = 'Трапеция длинная'
    NAILS_COIN_LIKE = 'Монетоподобные'
    NAILS_OVAL = 'Овальные'
    NAILS_CROSS_CURVED_CONVEX = 'Попер и прод выпукл (линза)'
    NAILS_CROSS_CURVED = 'Поперечно-выпуклые'
    NAILS_FLAT = 'Плоские'
    MUSCLES_THIN = 'Мышцы тонкие'
    MUSCLES_VOLUMINOUS = 'Мышцы объемные'
    MUSCLES_SOFT_LOOSE = 'Мягкие рыхлые мышцы'
    MUSCLES_FIRM_RUBBERY = 'Плотные "резиновые" мышцы'
    SKIN_LARGE_PORES = 'Крупные поры (лицо)'
    SKIN_EASILY_REDDENS = 'Кожа легко краснеет'
    SKIN_FRECKLES = 'Веснушки'


QUESTION_NAMES_FOR_SIGNS = {
    Sign.FIRE.value: [
        QuestionName.STRUCTURE_OF_HAIR,
        QuestionName.FEATURES_OF_SKIN,
        QuestionName.BACK_OF_NOSE,
        QuestionName.SIZE_OF_NOSE,
        QuestionName.FACE_SHAPE,
        QuestionName.NOSE_SHAPE,
        QuestionName.CONVEXITY_OF_NAILS,
        QuestionName.SIZE_OF_PALMS,
        QuestionName.BODY_FEATURES,
        QuestionName.FINGER_SHAPE,
        QuestionName.NAIL_SHAPE,
        QuestionName.WAIST,
        QuestionName.NOSE_TIP,
        QuestionName.NOSTRILS,
        QuestionName.PALM_SHAPE,
        QuestionName.WIDTH_OF_BACK_OF_NOSE,
        QuestionName.MUSCLE_VOLUME,
        QuestionName.FAT_TISSUE,

        # Rest of the questions just in case
        QuestionName.THICKNESS_OF_HAIR,
        QuestionName.HAIR_DENSITY,
        QuestionName.FINGER_LENGTH,
        QuestionName.FEATURES_OF_BRUSHES,
        QuestionName.MUSCLE_DENSITY,
        QuestionName.LENGTH_OF_NECK,
        QuestionName.THICKNESS_OF_NECK,
        QuestionName.HAIR_FEATURES,
        QuestionName.FEATURES_OF_FINGERS,
    ],
    Sign.EARTH.value: [
        QuestionName.BODY_FEATURES,
        QuestionName.THICKNESS_OF_HAIR,
        QuestionName.NOSTRILS,
        QuestionName.STRUCTURE_OF_HAIR,
        QuestionName.HAIR_DENSITY,
        QuestionName.FACE_SHAPE,
        QuestionName.NOSE_TIP,
        QuestionName.WIDTH_OF_BACK_OF_NOSE,
        QuestionName.FAT_TISSUE,
        QuestionName.FINGER_LENGTH,
        QuestionName.FEATURES_OF_SKIN,
        QuestionName.MUSCLE_DENSITY,
        QuestionName.FINGER_SHAPE,
        QuestionName.NAIL_SHAPE,
        QuestionName.PALM_SHAPE,
        QuestionName.MUSCLE_VOLUME,
        QuestionName.BACK_OF_NOSE,
        QuestionName.WAIST,
        QuestionName.FEATURES_OF_BRUSHES,
        QuestionName.FEATURES_OF_FINGERS,
        QuestionName.SIZE_OF_PALMS,

        # Rest of the questions just in case
        QuestionName.SIZE_OF_NOSE,
        QuestionName.NOSE_SHAPE,
        QuestionName.CONVEXITY_OF_NAILS,
        QuestionName.LENGTH_OF_NECK,
        QuestionName.THICKNESS_OF_NECK,
        QuestionName.HAIR_FEATURES,
    ],
    Sign.METAL.value: [
        QuestionName.BODY_FEATURES,
        QuestionName.BACK_OF_NOSE,
        QuestionName.NOSE_SHAPE,
        QuestionName.FACE_SHAPE,
        QuestionName.THICKNESS_OF_HAIR,
        QuestionName.HAIR_DENSITY,
        QuestionName.STRUCTURE_OF_HAIR,
        QuestionName.LENGTH_OF_NECK,
        QuestionName.WIDTH_OF_BACK_OF_NOSE,
        QuestionName.FINGER_LENGTH,
        QuestionName.FINGER_SHAPE,
        QuestionName.NAIL_SHAPE,
        QuestionName.PALM_SHAPE,
        QuestionName.FAT_TISSUE,
        QuestionName.NOSTRILS,
        QuestionName.PALM_SHAPE,
        QuestionName.FEATURES_OF_BRUSHES,
        QuestionName.SIZE_OF_PALMS,
        QuestionName.SIZE_OF_NOSE,
        QuestionName.THICKNESS_OF_NECK,
        QuestionName.FEATURES_OF_FINGERS,
        QuestionName.CONVEXITY_OF_NAILS,
        QuestionName.MUSCLE_VOLUME,

        # Rest of the questions just in case
        QuestionName.FEATURES_OF_SKIN,
        QuestionName.WAIST,
        QuestionName.NOSE_TIP,
        QuestionName.MUSCLE_DENSITY,
        QuestionName.HAIR_FEATURES,
    ],
    Sign.WATER.value: [
        QuestionName.BODY_FEATURES,
        QuestionName.THICKNESS_OF_HAIR,
        QuestionName.HAIR_DENSITY,
        QuestionName.NOSE_TIP,
        QuestionName.HAIR_FEATURES,
        QuestionName.NOSTRILS,
        QuestionName.WIDTH_OF_BACK_OF_NOSE,
        QuestionName.FACE_SHAPE,
        QuestionName.FAT_TISSUE,
        QuestionName.SIZE_OF_NOSE,
        QuestionName.MUSCLE_DENSITY,
        QuestionName.MUSCLE_VOLUME,
        QuestionName.SIZE_OF_PALMS,
        QuestionName.PALM_SHAPE,
        QuestionName.LENGTH_OF_NECK,
        QuestionName.THICKNESS_OF_NECK,
        QuestionName.FINGER_SHAPE,
        QuestionName.FINGER_LENGTH,
        QuestionName.WAIST,
        QuestionName.FEATURES_OF_BRUSHES,

        # Rest of the questions just in case
        QuestionName.STRUCTURE_OF_HAIR,
        QuestionName.FEATURES_OF_SKIN,
        QuestionName.BACK_OF_NOSE,
        QuestionName.NOSE_SHAPE,
        QuestionName.CONVEXITY_OF_NAILS,
        QuestionName.NAIL_SHAPE,
        QuestionName.FEATURES_OF_FINGERS,
    ],
    Sign.WOOD.value: [
        QuestionName.NOSE_SHAPE,
        QuestionName.STRUCTURE_OF_HAIR,
        QuestionName.BODY_FEATURES,
        QuestionName.FEATURES_OF_FINGERS,
        QuestionName.FINGER_SHAPE,
        QuestionName.NAIL_SHAPE,
        QuestionName.PALM_SHAPE,
        QuestionName.SIZE_OF_PALMS,
        QuestionName.HAIR_DENSITY,
        QuestionName.SIZE_OF_NOSE,
        QuestionName.FACE_SHAPE,
        QuestionName.MUSCLE_VOLUME,
        QuestionName.BACK_OF_NOSE,
        QuestionName.FINGER_LENGTH,
        QuestionName.MUSCLE_DENSITY,

        # Rest of the questions just in case
        QuestionName.FEATURES_OF_SKIN,
        QuestionName.CONVEXITY_OF_NAILS,
        QuestionName.WAIST,
        QuestionName.NOSE_TIP,
        QuestionName.NOSTRILS,
        QuestionName.FAT_TISSUE,
        QuestionName.THICKNESS_OF_HAIR,
        QuestionName.FEATURES_OF_BRUSHES,
        QuestionName.LENGTH_OF_NECK,
        QuestionName.THICKNESS_OF_NECK,
        QuestionName.HAIR_FEATURES,
    ],
}

ANSWER_SCORES = {
    QuestionName.HEIGHT: {
        AnswerName.HEIGHT_SHORT.value: [15, 6, -5, -3, -3],
        AnswerName.HEIGHT_AVERAGE.value: [0, 0, 0, 0, 0],
        AnswerName.HEIGHT_TALL.value: [-5, -3, 15, 8, 10],
    },
    QuestionName.BODY_SCHEME: {
        AnswerName.SHAPE_SMALL_RECTANGLE.value: [15, 0, 0, -5, -5],
        AnswerName.SHAPE_NARROW_RECTANGLE.value: [0, -7, 15, 3, 0],
        AnswerName.SHAPE_LARGE_WIDE_RECTANGLE.value: [-5, 0, 2, 15, 7],
        AnswerName.SHAPE_BROAD_SHOULDERS.value: [0, -3, 0, 7, 15],
        AnswerName.SHAPE_BROAD_HIPS.value: [0, 15, -7, 5, -5],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.BODY_FEATURES: {
        AnswerName.BODY_DRY.value: [5, -7, 15, -5, 7],
        AnswerName.BODY_VOLUMINOUS.value: [0, 15, -5, 10, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.WAIST: {
        AnswerName.WAIST_DEFINED.value: [5, 5, 3, -2, 3],
        AnswerName.WAIST_SMOOTHED.value: [0, 0, 0, 5, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.FAT_TISSUE: {
        AnswerName.FAT_TISSUE_WEAK.value: [3, -4, 7, 0, 3],
        AnswerName.FAT_TISSUE_STRONG.value: [-2, 7, -4, 7, -2],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.EYE_COLOR: {
        AnswerName.EYES_BLUE.value: [-5, 12, 5, -2, -5],
        AnswerName.EYES_GRAY.value: [-2, 7, 12, -5, -3],
        AnswerName.EYES_GRAY_BLUE_DARK_SPECKS.value: [2, 7, 7, 0, 3],
        AnswerName.EYES_GRAY_BLUE_YELLOW_GREEN_ZONES.value: [3, 5, 5, 5, -5],
        AnswerName.EYES_BLACK.value: [10, -7, -7, 0, 0],
        AnswerName.EYES_BROWN.value: [10, -7, -7, 0, 3],
        AnswerName.EYES_GREEN.value: [5, -3, 0, 15, 0],
        AnswerName.EYES_YELLOW_GREEN.value: [5, -3, 0, 15, 0],
        AnswerName.EYES_HETEROCHROMATIC.value: [0, -2, -3, 0, 10],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.THICKNESS_OF_HAIR: {
        AnswerName.HAIR_THIN.value: [3, 10, 10, 0, 0],
        AnswerName.HAIR_MEDIUM_THICKNESS.value: [0, 0, 0, 0, 0],
        AnswerName.HAIR_THICK.value: [0, -5, -5, 10, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.HAIR_DENSITY: {
        AnswerName.HAIR_SPARSE.value: [0, -3, 10, 0, 0],
        AnswerName.HAIR_DENSE.value: [0, 8, -5, 10, 7],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.STRUCTURE_OF_HAIR: {
        AnswerName.HAIR_STRAIGHT.value: [-5, 8, 8, 0, -3],
        AnswerName.HAIR_WAVY.value: [8, 0, 0, 0, 10],
        AnswerName.HAIR_CURLY.value: [10, -3, -5, 0, 5],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.HAIR_COLOR: {
        AnswerName.HAIR_RED.value: [15, 0, 0, 3, 0],
        AnswerName.HAIR_CHESTNUT.value: [8, 0, 0, 3, 5],
        AnswerName.HAIR_BLACK.value: [10, -5, -5, 0, 5],
        AnswerName.HAIR_DARK_BLONDE.value: [5, 0, -3, 5, 10],
        AnswerName.HAIR_BLONDE.value: [0, 0, 0, 10, 5],
        AnswerName.HAIR_LIGHT.value: [-5, 10, 10, -3, -5],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.HAIR_FEATURES: {
        AnswerName.HAIR_COARSE.value: [0, -3, -3, 5, 3],
        AnswerName.HAIR_EARLY_GRAYING.value: [0, 0, 0, 5, 0],
        AnswerName.HAIR_EARLY_BALDING.value: [0, 0, 3, 5, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.FACE_SHAPE: {
        AnswerName.FACE_ROUND.value: [0, 7, -2, 0, 0],
        AnswerName.FACE_LONG_RECTANGLE.value: [0, 0, 10, 0, 2],
        AnswerName.FACE_LARGE_TRIANGLE.value: [0, 0, 0, 0, 5],
        AnswerName.FACE_SMALL_TRIANGLE.value: [7, 0, -3, -3, 0],
        AnswerName.FACE_BROAD_RECTANGLE_SQUARE.value: [-2, 0, 0, 7, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.SIZE_OF_NOSE: {
        AnswerName.NOSE_SMALL.value: [8, 2, -2, -3, -3],
        AnswerName.NOSE_LARGE.value: [0, 5, 5, 7, 7],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.NOSE_SHAPE: {
        AnswerName.NOSE_HUMP.value: [0, 0, 0, 0, 7],
        AnswerName.NOSE_HOOKED.value: [0, 0, 0, 0, 10],
        AnswerName.NOSE_STRAIGHT.value: [7, 3, 10, 3, -5],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.NOSTRILS: {
        AnswerName.NOSTRILS_WIDE.value: [-5, 8, 0, 8, 0],
        AnswerName.NOSTRILS_NARROW.value: [5, -5, 7, -5, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.NOSE_TIP: {
        AnswerName.NOSE_SHARP_TIP.value: [5, -3, 3, -5, 0],
        AnswerName.NOSE_ROUND_TIP.value: [-3, 5, -3, 5, 0],
        AnswerName.NOSE_TURNED_UP_TIP.value: [0, 5, 0, 2, 0],
        AnswerName.NOSE_DUCKLIKE.value: [0, 0, 0, 10, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.BACK_OF_NOSE: {
        AnswerName.NOSE_LONG_BACK.value: [-5, -3, 15, 0, 5],
        AnswerName.NOSE_SHORT_BACK.value: [10, 5, -5, -2, -3],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.WIDTH_OF_BACK_OF_NOSE: {
        AnswerName.NOSE_WIDE_BACK.value: [-2, 7, -5, 7, 2],
        AnswerName.NOSE_THIN_BACK.value: [4, -2, 8, -3, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.LENGTH_OF_NECK: {
        AnswerName.NECK_SHORT.value: [0, 0, -5, 7, 0],
        AnswerName.NECK_AVERAGE_LENGTH.value: [0, 0, 0, 0, 0],
        AnswerName.NECK_LONG.value: [0, 0, 8, -2, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.THICKNESS_OF_NECK: {
        AnswerName.NECK_THICK.value: [0, 0, -3, 5, 0],
        AnswerName.NECK_AVERAGE_THICKNESS.value: [0, 0, 0, 0, 0],
        AnswerName.NECK_THIN.value: [0, 0, 5, -3, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.SIZE_OF_PALMS: {
        AnswerName.HANDS_LARGE.value: [-4, -3, 5, 7, 7],
        AnswerName.HANDS_SMALL.value: [7, 4, 0, -4, -3],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.PALM_SHAPE: {
        AnswerName.HAND_SHAPE_SQUARE.value: [0, 5, -2, 7, 0],
        AnswerName.HAND_SHAPE_RECTANGLE.value: [2, 0, 3, 2, 7],
        AnswerName.HAND_SHAPE_SMALL_RECTANGLE.value: [5, 0, 1, -3, 0],
        AnswerName.HAND_SHAPE_NARROW_LONG_RECTANGLE.value: [0, -4, 7, -4, 0],
        AnswerName.HAND_SHAPE_PADDLE.value: [-4, -3, 7, 0, 3],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.FEATURES_OF_BRUSHES: {
        AnswerName.HANDS_SOFT_LOOSE.value: [0, 5, -3, -2, -3],
        AnswerName.HANDS_FULL_FIRM.value: [0, -2, -3, 5, 0],
        AnswerName.HANDS_DRY.value: [2, -3, 7, -3, 3],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.FINGER_LENGTH: {
        AnswerName.FINGERS_LONG.value: [0, -3, 7, 0, 5],
        AnswerName.FINGERS_AVERAGE_LENGTH.value: [0, 0, 0, 0, 0],
        AnswerName.FINGERS_SHORT.value: [0, 7, 0, 5, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.FINGER_SHAPE: {
        AnswerName.FINGERS_STRAIGHT.value: [3, 5, 7, 5, -1],
        AnswerName.FINGERS_CONICAL.value: [5, 0, 0, 0, 0],
        AnswerName.FINGERS_CROOKED.value: [0, 0, 0, 0, 7],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.FEATURES_OF_FINGERS: {
        AnswerName.FINGERS_KNOTTY.value: [0, 0, 0, 0, 8],
        AnswerName.FINGERS_DRY.value: [2, -4, 5, -2, 2],
        AnswerName.FINGERS_FLESHY.value: [0, 5, -3, 2, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.NAIL_SHAPE: {
        AnswerName.SHAPE_LONG_RECTANGLE.value: [0, 0, 7, 0, 2],
        AnswerName.SHAPE_SHORT_TRAPEZOID.value: [0, 5, 0, 4, 0],
        AnswerName.SHAPE_LONG_TRAPEZOID.value: [0, 0, 2, 0, 5],
        AnswerName.NAILS_COIN_LIKE.value: [0, -2, -5, -2, 7],
        AnswerName.NAILS_OVAL.value: [5, 0, 0, 0, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.CONVEXITY_OF_NAILS: {
        AnswerName.NAILS_CROSS_CURVED_CONVEX.value: [7, 0, 0, 0, 3],
        AnswerName.NAILS_CROSS_CURVED.value: [2, 2, 5, 3, 1],
        AnswerName.NAILS_FLAT.value: [0, 3, 0, 1, 4],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.MUSCLE_VOLUME: {
        AnswerName.MUSCLES_THIN.value: [4, 0, 5, 0, 0],
        AnswerName.MUSCLES_VOLUMINOUS.value: [0, 5, -5, 7, 5],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.MUSCLE_DENSITY: {
        AnswerName.MUSCLES_SOFT_LOOSE.value: [0, 7, 0, -3, 0],
        AnswerName.MUSCLES_FIRM_RUBBERY.value: [0, -3, 0, 7, 4],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
    QuestionName.FEATURES_OF_SKIN: {
        AnswerName.SKIN_LARGE_PORES.value: [0, 5, -2, 3, 0],
        AnswerName.SKIN_EASILY_REDDENS.value: [2, 1, 1, 0, 0],
        AnswerName.SKIN_FRECKLES.value: [10, 0, 0, 0, 0],
        AnswerName.HARD_TO_SAY.value: [0, 0, 0, 0, 0],
    },
}

MULTIPLE_CHOICE_QUESTIONS = {
    QuestionName.FINGER_SHAPE,
    QuestionName.FEATURES_OF_FINGERS,
    QuestionName.NAIL_SHAPE,
    QuestionName.CONVEXITY_OF_NAILS,
    QuestionName.HAIR_FEATURES,
    QuestionName.FEATURES_OF_SKIN,
}

HEIGHT_EXPLANATION = "Ця ознака не вимагає спеціального вимірювання. Достатньо позначити як виглядає людина виглядає лише на погляд і у співставленні з іншими - високою чи низькою."

ANSWER_EXPLANATIONS = {
    QuestionName.HEIGHT: {
        AnswerName.HEIGHT_SHORT.value: HEIGHT_EXPLANATION,
        AnswerName.HEIGHT_AVERAGE.value: HEIGHT_EXPLANATION,
        AnswerName.HEIGHT_TALL.value: HEIGHT_EXPLANATION,
    },
    QuestionName.BODY_SCHEME: {
        AnswerName.SHAPE_SMALL_RECTANGLE.value: "Плечі та стегна рівні між собою та відносно вузькі при малому зрості.",
        AnswerName.SHAPE_NARROW_RECTANGLE.value: "Плечі та стегна вузькі та рівні між собою при високому зрості.",
        AnswerName.SHAPE_LARGE_WIDE_RECTANGLE.value: "І стегна, і плечі широкі. Зазвичай форма тіла наближається до квадрата або широкого прямокутника.",
        AnswerName.SHAPE_BROAD_SHOULDERS.value: "Плечі хоча б трохи ширше за стегна. Форма тіла виглядає атлетично, як перекинута трапеція.",
        AnswerName.SHAPE_BROAD_HIPS.value: "Стегна хоча б трохи ширше за плечі незалежно від зросту. Ширина стегон визначається на рівні кісточок стегнових кісток.",
    },
    QuestionName.BODY_FEATURES: {
        AnswerName.BODY_DRY.value: "Тіло виглядає сухим, схудлим, з невеликим об’ємом м’яких тканин. Особливо гарно це помітно на руках у вигляді міжкісткових проміжків та сухих пальців. Проглядаються сухожилля та інколи тонкі м’язи.",
        AnswerName.BODY_VOLUMINOUS.value: "Тіло із значною кількістю м’яких тканин – м’язів, жирової клітковини. Схильність до повноти. Кістки та суглоби майже не помітні.",
    },
    QuestionName.WAIST: {
        AnswerName.WAIST_DEFINED.value: "Чітко виражена талія, незалежно від кількості жирової клітковини.",
        AnswerName.WAIST_SMOOTHED.value: "Талія майже відсутня, незалежно від кількості жирової клітковини.",
    },
    QuestionName.FAT_TISSUE: {
        AnswerName.FAT_TISSUE_WEAK.value: None,
        AnswerName.FAT_TISSUE_STRONG.value: None,
    },
    QuestionName.EYE_COLOR: {
        AnswerName.EYES_BLUE.value: None,
        AnswerName.EYES_GRAY.value: None,
        AnswerName.EYES_GRAY_BLUE_DARK_SPECKS.value: None,
        AnswerName.EYES_GRAY_BLUE_YELLOW_GREEN_ZONES.value: None,
        AnswerName.EYES_BLACK.value: None,
        AnswerName.EYES_BROWN.value: None,
        AnswerName.EYES_GREEN.value: None,
        AnswerName.EYES_YELLOW_GREEN.value: None,
        AnswerName.EYES_HETEROCHROMATIC.value: None,
    },
    QuestionName.THICKNESS_OF_HAIR: {
        AnswerName.HAIR_THIN.value: "Таке волосся м’яке, легке, погано тримає зачіску. Густота не має значення.",
        AnswerName.HAIR_MEDIUM_THICKNESS.value: "Волосся не схоже ні на надто легке, ні на надто пружне.",
        AnswerName.HAIR_THICK.value: "Жорстке, пружне волосся.",
    },
    QuestionName.HAIR_DENSITY: {
        AnswerName.HAIR_SPARSE.value: None,
        AnswerName.HAIR_DENSE.value: None,
    },
    QuestionName.STRUCTURE_OF_HAIR: {
        AnswerName.HAIR_STRAIGHT.value: None,
        AnswerName.HAIR_WAVY.value: None,
        AnswerName.HAIR_CURLY.value: None,
    },
    QuestionName.HAIR_COLOR: {
        AnswerName.HAIR_RED.value: None,
        AnswerName.HAIR_CHESTNUT.value: None,
        AnswerName.HAIR_BLACK.value: None,
        AnswerName.HAIR_DARK_BLONDE.value: None,
        AnswerName.HAIR_BLONDE.value: None,
        AnswerName.HAIR_LIGHT.value: None,
    },
    QuestionName.HAIR_FEATURES: {
        AnswerName.HAIR_COARSE.value: None,
        AnswerName.HAIR_EARLY_GRAYING.value: None,
        AnswerName.HAIR_EARLY_BALDING.value: None,
    },
    QuestionName.FACE_SHAPE: {
        AnswerName.FACE_ROUND.value: "За рахунок значної кількості м’яких тканин обличчя виглядає майже круглим, з помітними пухкими щоками.",
        AnswerName.FACE_LONG_RECTANGLE.value: "При погляді анфас добре помітні широко розсунуті кути нижньої щелепи. Разом з верхніми вилицями вони створюють чіткі вершини витягнутого зверху донизу прямокутника.",
        AnswerName.FACE_LARGE_TRIANGLE.value: "Великий трикутник формується між вираженими верхніми вилицями та чітко видним міцним підборіддям, Підборіддя часто з ямочкою, але це не обов’язково. Обличчя досить велике. Дивитися треба прямо анфас.",
        AnswerName.FACE_SMALL_TRIANGLE.value: "Малий трикутник формується між добре помітними верхніми вилицями та вузьким підборіддям, як нижньою вершиною перевернутого трикутника. Дивитися треба прямо анфас.",
        AnswerName.FACE_BROAD_RECTANGLE_SQUARE.value: "При погляді анфас добре помітні широко розсунуті кути нижньої щелепи. Разом з верхніми вилицями вони створюють чіткі вершини широкого прямокутника, близького до квадрату.",
    },
    QuestionName.SIZE_OF_NOSE: {
        AnswerName.NOSE_SMALL.value: "Ніс виглядає малим (порівняно з іншими людьми або з розміром обличчя в цілому) незалежно від його форми та особливостей.",
        AnswerName.NOSE_LARGE.value: "Ніс виглядає великим (порівняно з іншими людьми або з розміром обличчя в цілому) незалежно від його форми та особливостей.",
    },
    QuestionName.NOSE_SHAPE: {
        AnswerName.NOSE_HUMP.value: "Ніс в цілому прямий, але в районі перенісся чітко помітна горбина. Якщо це можливо, уточніть, чи не є це наслідком травми носа в минулому.",
        AnswerName.NOSE_HOOKED.value: "Ніс має форму гачка з трохи нависаючим над верхньою губою кінчиком. Це добре помітно з боків.",
        AnswerName.NOSE_STRAIGHT.value: "Перенісся пряме і гладке.",
    },
    QuestionName.NOSTRILS: {
        AnswerName.NOSTRILS_WIDE.value: "Крила носа, утворюючі ніздрі, виглядають широкими та об’ємними.",
        AnswerName.NOSTRILS_NARROW.value: "Крила носа невеликі за розміром, тому ніздрі виглядають вузькими.",
    },
    QuestionName.NOSE_TIP: {
        AnswerName.NOSE_SHARP_TIP.value: "Самий кінчик носу виглядає загостреним, тонким.",
        AnswerName.NOSE_ROUND_TIP.value: "Кінчик носу виділяється над переніссям та крилами носу і має круглу об’ємну форму.",
        AnswerName.NOSE_TURNED_UP_TIP.value: "Кінчик носу наче задертий вгору. Помітно в анфас і в профіль.",
        AnswerName.NOSE_DUCKLIKE.value: "Кінчик носу наче приплесканий. Це добре видно з боків, а не анфас.",
    },
    QuestionName.BACK_OF_NOSE: {
        AnswerName.NOSE_LONG_BACK.value: "Спинка носу подовжена в порівнянні з невеликим кінчиком та крилами носа. В цілому ніс нагадує носи на стародавніх іконах.",
        AnswerName.NOSE_SHORT_BACK.value: "Спинка носу укорочена порівняно з кінчиком та крилами носа.",
    },
    QuestionName.WIDTH_OF_BACK_OF_NOSE: {
        AnswerName.NOSE_WIDE_BACK.value: "Перенісся має розлогу спинку по всій довжині носа.",
        AnswerName.NOSE_THIN_BACK.value: "Перенісся гостре, наче ніс корабля.",
    },
    QuestionName.LENGTH_OF_NECK: {
        AnswerName.NECK_LONG.value: "Шия витягнута і добре помітна. Часто тонка.",
        AnswerName.NECK_AVERAGE_LENGTH.value: "Шия не схожа ні на надто витягнуту, ні на надто коротку.",
        AnswerName.NECK_SHORT.value: "Шия коротка, наче голова лежить прямо на плечах.",
    },
    QuestionName.THICKNESS_OF_NECK: {
        AnswerName.NECK_THICK.value: "Шия широка, на рівні верхніх вилиць або, навіть, ширше. Не обов’язково коротка.",
        AnswerName.NECK_AVERAGE_THICKNESS.value: "Шия не схожа ні на надто широку, ні на надто тоншу.",
        AnswerName.NECK_THIN.value: "Шия помітно тонше верхніх вилиць, часто довга або такою виглядає.",
    },
    QuestionName.SIZE_OF_PALMS: {
        AnswerName.HANDS_LARGE.value: "Долоні виглядають великими в порівнянні з іншими людьми, або відносно своєї руки в цілому.",
        AnswerName.HANDS_SMALL.value: "Долоні відносно невеликого розміру в порівнянні з іншими людьми.",
    },
    QuestionName.PALM_SHAPE: {
        AnswerName.HAND_SHAPE_SQUARE.value: "Ширина та довжина долоні майже однакові. Розмір значення не має.",
        AnswerName.HAND_SHAPE_RECTANGLE.value: "Долоня має чітко прямокутну форму, а розмір середній або великий.",
        AnswerName.HAND_SHAPE_SMALL_RECTANGLE.value: "Долоня від зап’ястя до пальців довша за її ж ширину. Але долоня в цілому мала.",
        AnswerName.HAND_SHAPE_NARROW_LONG_RECTANGLE.value: "Довжина долоні (без пальців) суттєво більша за її ширину. Тому виглядає витягнутою вздовж руки.",
        AnswerName.HAND_SHAPE_PADDLE.value: "Долоня разом з пальцями виглядає непропорційно великою порівняно з тонкими кістками передпліччя та зап’ястя.",
    },
    QuestionName.FEATURES_OF_BRUSHES: {
        AnswerName.HANDS_SOFT_LOOSE.value: "Ця ознака пов’язана з об’ємними та м’якими м’язами. Найкраще виявляється на дотик. Але в деяких випадках це видно наочно.",
        AnswerName.HANDS_FULL_FIRM.value: "У людей з об’ємним тілом і пружними «гумовими» м’язами часто буває і ця ознака. Їх долоні також «налиті» і міцні, що добре відчувається на дотик.",
        AnswerName.HANDS_DRY.value: "Наочно видно сухість кисті у вигляді глибоких міжкісткових проміжків, тонких пальців. ",
    },
    QuestionName.FINGER_LENGTH: {
        AnswerName.FINGERS_LONG.value: "Пальці виглядають подовженими. Часто такі називають \"музичними пальцями\".",
        AnswerName.FINGERS_AVERAGE_LENGTH.value: "Пальці не схожі ні на надто подовжени, ні на надто короткі.",
        AnswerName.FINGERS_SHORT.value: "Пальці виглядають короткими у порівнянні з долонею та рукою в цілому.",
    },
    QuestionName.FINGER_SHAPE: {
        AnswerName.FINGERS_STRAIGHT.value: "Палець має майже однакову товщину по всій довжині і без будь-яких викривлень.",
        AnswerName.FINGERS_CONICAL.value: "Кінцеві фаланги пальців виглядають більш тонкими, ніж середні та перші. Палець наче виточується до кінчика.",
        AnswerName.FINGERS_CROOKED.value: "Деякі пальці мають викривлену форму. Частіше за все в сторону середнього пальця.",
    },
    QuestionName.FEATURES_OF_FINGERS: {
        AnswerName.FINGERS_KNOTTY.value: "За рахунок збільшених суглобів пальці виглядають наче бамбукова паличка. Якщо це можливо, уточніть, чи не є це наслідком артриту, який може давати набряки та викривлення суглобів. В такому разі ця ознака не достовірна.",
        AnswerName.FINGERS_DRY.value: "М’яких тканин на пальці мало. Тому він виглядає сухо, під шкірою гарно видно кістки та сухожилля.",
        AnswerName.FINGERS_FLESHY.value: "Пальці об’ємні за рахунок значної кількості м’яких тканин. В області суглобів в інколи можуть виникати невеличкі заглиблення.",
    },
    QuestionName.NAIL_SHAPE: {
        AnswerName.SHAPE_LONG_RECTANGLE.value: "Зверху виглядає витягнутим і прямокутним до самого кінчика пальця",
        AnswerName.SHAPE_SHORT_TRAPEZOID.value: "Ніготь розширюється в сторону кінчика пальця і має форму короткої трапеції, яка не доходить до кінчика пальця. Виглядає невеликим і коротким. Часто нігтьовий валик добре виражений і нависає над нігтем.",
        AnswerName.SHAPE_LONG_TRAPEZOID.value: "Ніготь розширюється в сторону кінчика пальця. Має форму довгої трапеції. Виглядає крупним.",
        AnswerName.NAILS_COIN_LIKE.value: "Ніготь має майже круглу форму, як монетка, і лежить зазвичай на самому кінчику пальця, прикриваючи його.",
        AnswerName.NAILS_OVAL.value: "Зверху ніготь має овальну форма, доходить майже до самого кінчика пальця.",
    },
    QuestionName.CONVEXITY_OF_NAILS: {
        AnswerName.NAILS_CROSS_CURVED_CONVEX.value: "Опуклість одночасно в двох напрямках: вздовж пальця від кореня до кінчика та впоперек пальця. Тому загальна форма нігтя нагадує шкарлупку мигдалю. Часто поєднується з овальною формою нігтя.",
        AnswerName.NAILS_CROSS_CURVED.value: "Ніготь вздовж пальця прямий і опуклий тільки впоперек пальця. Це найчастіший варіант. ",
        AnswerName.NAILS_FLAT.value: "Ніготь плоский, майже без опуклості. Часто поєднується з монетоподібною формою.",
    },
    QuestionName.MUSCLE_VOLUME: {
        AnswerName.MUSCLES_THIN.value: "М’язи за об’ємом невеликі навіть після довгих тренувань. На дотик міцні і перекочуються під пальцем.",
        AnswerName.MUSCLES_VOLUMINOUS.value: "М’язи відносно великі за об’ємом навіть без тренувань. Можуть бути і пружними, і м’якими на дотик.",
    },
    QuestionName.MUSCLE_DENSITY: {
        AnswerName.MUSCLES_SOFT_LOOSE.value: "М’язи пухкі на дотик, а також виглядають такими при рухах (наче холодець). Проте їх сила залежить тільки від тренованості.",
        AnswerName.MUSCLES_FIRM_RUBBERY.value: "М’язи дуже пружні, міцні на дотик, наче з литої гуми. Часто об’ємні, але вираженого рельєфу  не мають. Знаходяться в пружному стані навіть коли людина розслаблена.",
    },
    QuestionName.FEATURES_OF_SKIN: {
        AnswerName.SKIN_LARGE_PORES.value: "Пори на обличчі глибокі та широкі, краще помітні на носі та щоках довкола носа.",
        AnswerName.SKIN_EASILY_REDDENS.value: "Навіть при невеликому збудженні обличчя та зона декольте червоніє швидше та сильніше ніж у інших.",
        AnswerName.SKIN_FRECKLES.value: "Веснянки можуть бути сезонними, або постійними, або проходити з віком, на обличчі, або по тілу. Важливо позначити будь-який прояв веснянок.",
    },
}

BASE_IMAGE_URL = "https://hupres.com/stand/assets/pict/"


def _get_image(image_name: str) -> str:
    return BASE_IMAGE_URL + image_name + ".png"


ANSWER_IMAGE_LINKS = {
    QuestionName.HEIGHT: {
        AnswerName.HEIGHT_SHORT.value: None,
        AnswerName.HEIGHT_AVERAGE.value: None,
        AnswerName.HEIGHT_TALL.value: None,
    },
    QuestionName.BODY_SCHEME: {
        AnswerName.SHAPE_SMALL_RECTANGLE.value: _get_image("telo3"),
        AnswerName.SHAPE_NARROW_RECTANGLE.value: _get_image("telo2"),
        AnswerName.SHAPE_LARGE_WIDE_RECTANGLE.value: _get_image("telo1"),
        AnswerName.SHAPE_BROAD_SHOULDERS.value: _get_image("telo5"),
        AnswerName.SHAPE_BROAD_HIPS.value: _get_image("telo4"),
    },
    QuestionName.BODY_FEATURES: {
        AnswerName.BODY_DRY.value: _get_image("telo_f2"),
        AnswerName.BODY_VOLUMINOUS.value: _get_image("telo_f1"),
    },
    QuestionName.WAIST: {
        AnswerName.WAIST_DEFINED.value: _get_image("telo_fw1"),
        AnswerName.WAIST_SMOOTHED.value: _get_image("telo_fw2"),
    },
    QuestionName.FAT_TISSUE: {
        AnswerName.FAT_TISSUE_WEAK.value: None,
        AnswerName.FAT_TISSUE_STRONG.value: None,
    },
    QuestionName.EYE_COLOR: {
        AnswerName.EYES_BLUE.value: None,
        AnswerName.EYES_GRAY.value: None,
        AnswerName.EYES_GRAY_BLUE_DARK_SPECKS.value: None,
        AnswerName.EYES_GRAY_BLUE_YELLOW_GREEN_ZONES.value: None,
        AnswerName.EYES_BLACK.value: None,
        AnswerName.EYES_BROWN.value: None,
        AnswerName.EYES_GREEN.value: None,
        AnswerName.EYES_YELLOW_GREEN.value: None,
        AnswerName.EYES_HETEROCHROMATIC.value: None,
    },
    QuestionName.THICKNESS_OF_HAIR: {
        AnswerName.HAIR_THIN.value: None,
        AnswerName.HAIR_MEDIUM_THICKNESS.value: None,
        AnswerName.HAIR_THICK.value: None,
    },
    QuestionName.HAIR_DENSITY: {
        AnswerName.HAIR_SPARSE.value: None,
        AnswerName.HAIR_DENSE.value: None,
    },
    QuestionName.STRUCTURE_OF_HAIR: {
        AnswerName.HAIR_STRAIGHT.value: None,
        AnswerName.HAIR_WAVY.value: None,
        AnswerName.HAIR_CURLY.value: None,
    },
    QuestionName.HAIR_COLOR: {
        AnswerName.HAIR_RED.value: None,
        AnswerName.HAIR_CHESTNUT.value: None,
        AnswerName.HAIR_BLACK.value: None,
        AnswerName.HAIR_DARK_BLONDE.value: None,
        AnswerName.HAIR_BLONDE.value: None,
        AnswerName.HAIR_LIGHT.value: None,
    },
    QuestionName.HAIR_FEATURES: {
        AnswerName.HAIR_COARSE.value: None,
        AnswerName.HAIR_EARLY_GRAYING.value: None,
        AnswerName.HAIR_EARLY_BALDING.value: None,
    },
    QuestionName.FACE_SHAPE: {
        AnswerName.FACE_ROUND.value: _get_image("hair4"),
        AnswerName.FACE_LONG_RECTANGLE.value: _get_image("hair2"),
        AnswerName.FACE_LARGE_TRIANGLE.value: _get_image("hair1"),
        AnswerName.FACE_SMALL_TRIANGLE.value: _get_image("hair3"),
        AnswerName.FACE_BROAD_RECTANGLE_SQUARE.value: _get_image("hair5"),
    },
    QuestionName.SIZE_OF_NOSE: {
        AnswerName.NOSE_SMALL.value: None,
        AnswerName.NOSE_LARGE.value: None,
    },
    QuestionName.NOSE_SHAPE: {
        AnswerName.NOSE_HUMP.value: _get_image("nose5"),
        AnswerName.NOSE_HOOKED.value: _get_image("nose4"),
        AnswerName.NOSE_STRAIGHT.value: _get_image("nose3"),
    },
    QuestionName.NOSTRILS: {
        AnswerName.NOSTRILS_WIDE.value: _get_image("nose_f3"),
        AnswerName.NOSTRILS_NARROW.value: _get_image("nose_f2"),
    },
    QuestionName.NOSE_TIP: {
        AnswerName.NOSE_SHARP_TIP.value: _get_image("nose3"),
        AnswerName.NOSE_ROUND_TIP.value: _get_image("nose_f3"),
        AnswerName.NOSE_TURNED_UP_TIP.value: _get_image("nose2"),
        AnswerName.NOSE_DUCKLIKE.value: _get_image("nose1"),
    },
    QuestionName.BACK_OF_NOSE: {
        AnswerName.NOSE_LONG_BACK.value: _get_image("nose_f2"),
        AnswerName.NOSE_SHORT_BACK.value: _get_image("nose_f3"),
    },
    QuestionName.WIDTH_OF_BACK_OF_NOSE: {
        AnswerName.NOSE_WIDE_BACK.value: _get_image("nose_f1"),
        AnswerName.NOSE_THIN_BACK.value: _get_image("nose_f2"),
    },
    QuestionName.LENGTH_OF_NECK: {
        AnswerName.NECK_LONG.value: _get_image("neck1"),
        AnswerName.NECK_AVERAGE_LENGTH.value: None,
        AnswerName.NECK_SHORT.value: _get_image("neck2"),
    },
    QuestionName.THICKNESS_OF_NECK: {
        AnswerName.NECK_THICK.value: _get_image("neck4"),
        AnswerName.NECK_AVERAGE_THICKNESS.value: None,
        AnswerName.NECK_THIN.value: _get_image("neck1"),
    },
    QuestionName.SIZE_OF_PALMS: {
        AnswerName.HANDS_LARGE.value: None,
        AnswerName.HANDS_SMALL.value: None,
    },
    QuestionName.PALM_SHAPE: {
        AnswerName.HAND_SHAPE_SQUARE.value: _get_image("paml1"),
        AnswerName.HAND_SHAPE_RECTANGLE.value: _get_image("palm2"),
        AnswerName.HAND_SHAPE_SMALL_RECTANGLE.value: _get_image("palm3"),
        AnswerName.HAND_SHAPE_NARROW_LONG_RECTANGLE.value: _get_image("palm4"),
        AnswerName.HAND_SHAPE_PADDLE.value: _get_image("palm5"),
    },
    QuestionName.FEATURES_OF_BRUSHES: {
        AnswerName.HANDS_SOFT_LOOSE.value: None,
        AnswerName.HANDS_FULL_FIRM.value: None,
        AnswerName.HANDS_DRY.value: None,
    },
    QuestionName.FINGER_LENGTH: {
        AnswerName.FINGERS_LONG.value: None,
        AnswerName.FINGERS_AVERAGE_LENGTH.value: None,
        AnswerName.FINGERS_SHORT.value: None,
    },
    QuestionName.FINGER_SHAPE: {
        AnswerName.FINGERS_STRAIGHT.value: _get_image("finger1"),
        AnswerName.FINGERS_CONICAL.value: _get_image("finger2"),
        AnswerName.FINGERS_CROOKED.value: _get_image("finger4"),
    },
    QuestionName.FEATURES_OF_FINGERS: {
        AnswerName.FINGERS_KNOTTY.value: _get_image("finger3"),
        AnswerName.FINGERS_DRY.value: None,
        AnswerName.FINGERS_FLESHY.value: None,
    },
    QuestionName.NAIL_SHAPE: {
        AnswerName.SHAPE_LONG_RECTANGLE.value: _get_image("nail1"),
        AnswerName.SHAPE_SHORT_TRAPEZOID.value: _get_image("nail2"),
        AnswerName.SHAPE_LONG_TRAPEZOID.value: _get_image("nail3"),
        AnswerName.NAILS_COIN_LIKE.value: _get_image("nail4"),
        AnswerName.NAILS_OVAL.value: _get_image("nail5"),
    },
    QuestionName.CONVEXITY_OF_NAILS: {
        AnswerName.NAILS_CROSS_CURVED_CONVEX.value: _get_image("nail_f1"),
        AnswerName.NAILS_CROSS_CURVED.value: _get_image("nail_f2"),
        AnswerName.NAILS_FLAT.value: _get_image("nail_f3"),
    },
    QuestionName.MUSCLE_VOLUME: {
        AnswerName.MUSCLES_THIN.value: None,
        AnswerName.MUSCLES_VOLUMINOUS.value: None,
    },
    QuestionName.MUSCLE_DENSITY: {
        AnswerName.MUSCLES_SOFT_LOOSE.value: None,
        AnswerName.MUSCLES_FIRM_RUBBERY.value: None,
    },
    QuestionName.FEATURES_OF_SKIN: {
        AnswerName.SKIN_LARGE_PORES.value: None,
        AnswerName.SKIN_EASILY_REDDENS.value: None,
        AnswerName.SKIN_FRECKLES.value: None,
    },
}
