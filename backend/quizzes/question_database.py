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
