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
    ],
}


ANSWER_SCORES = {
    QuestionName.HEIGHT: {
        'Рост низкий': [15, 6, -5, -3, -3],
        'Рост средний': [0, 0, 0, 0, 0],
        'Рост высокий': [-5, -3, 15, 8, 10],
    },
    QuestionName.BODY_SCHEME: {
        'Малый прямоугольник': [15, 0, 0, -5, -5],
        'Узкий прямоугольник': [0, -7, 15, 3, 0],
        'Больш шир прямоугольник': [-5, 0, 2, 15, 7],
        'Шире в плечах': [0, -3, 0, 7, 15],
        'Шире в бедрах': [0, 15, -7, 5, -5],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.BODY_FEATURES: {
        'Тело сухое': [5, -7, 15, -5, 7],
        'Тело объемное': [0, 15, -5, 10, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.WAIST: {
        'Талия выражена': [5, 5, 3, -2, 3],
        'Талия сглажена': [0, 0, 0, 5, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.FAT_TISSUE: {
        'Жир клетч слабая': [3, -4, 7, 0, 3],
        'Жир клетч выражена': [-2, 7, -4, 7, -2],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.EYE_COLOR: {
        'Голубые глаза': [-5, 12, 5, -2, -5],
        'Серые (стальные) глаза': [-2, 7, 12, -5, -3],
        'Серо-голуб гл с темн вкрапл': [2, 7, 7, 0, 3],
        'Серо-голуб гл с жел-зел зонами': [3, 5, 5, 5, -5],
        'Черные глаза': [10, -7, -7, 0, 0],
        'Карие глаза': [10, -7, -7, 0, 3],
        'Зеленые глаза': [5, -3, 0, 15, 0],
        'Желто-зеленые глаза': [5, -3, 0, 15, 0],
        'Рябые глаза': [0, -2, -3, 0, 10],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.THICKNESS_OF_HAIR: {
        'Тонкие волосы': [3, 10, 10, 0, 0],
        'Волосы средней толщины': [0, 0, 0, 0, 0],
        'Толстые волосы': [0, -5, -5, 10, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.HAIR_DENSITY: {
        'Редкие волосы': [0, -3, 10, 0, 0],
        'Густые волосы': [0, 8, -5, 10, 7],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.STRUCTURE_OF_HAIR: {
        'Прямые волосы': [-5, 8, 8, 0, -3],
        'Волнистые волосы': [8, 0, 0, 0, 10],
        'Кучерявые волосы': [10, -3, -5, 0, 5],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.HAIR_COLOR: {
        'Рыжие волосы': [15, 0, 0, 3, 0],
        'Каштановые волосы': [8, 0, 0, 3, 5],
        'Черные волосы': [10, -5, -5, 0, 5],
        'Темно русые волосы': [5, 0, -3, 5, 10],
        'Русые волосы': [0, 0, 0, 10, 5],
        'Светлые волосы': [-5, 10, 10, -3, -5],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.HAIR_FEATURES: {
        'Жесткие волосы': [0, -3, -3, 5, 3],
        'Ранняя седина': [0, 0, 0, 5, 0],
        'Ранние залысины': [0, 0, 3, 5, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.FACE_SHAPE: {
        'Круглое лицо': [0, 7, -2, 0, 0],
        'Вытянутый прямоугольник': [0, 0, 10, 0, 2],
        'Большой треугольник': [0, 0, 0, 0, 5],
        'Малый треугольник': [7, 0, -3, -3, 0],
        'Широк прямоугольн "Квадрат"': [-2, 0, 0, 7, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.SIZE_OF_NOSE: {
        'Малый нос': [8, 2, -2, -3, -3],
        'Крупный нос': [0, 5, 5, 7, 7],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.NOSE_SHAPE: {
        'Горбинка на носу': [0, 0, 0, 0, 7],
        'Крючковидный нос': [0, 0, 0, 0, 10],
        'Прямой нос': [7, 3, 10, 3, -5],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.NOSTRILS: {
        'Широкие ноздри': [-5, 8, 0, 8, 0],
        'Узкие ноздри': [5, -5, 7, -5, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.NOSE_TIP: {
        'Острый кончик носа': [5, -3, 3, -5, 0],
        'Круглый кончик носа': [-3, 5, -3, 5, 0],
        'Курносый кончик носа': [0, 5, 0, 2, 0],
        'Нос "уточкой"': [0, 0, 0, 10, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.BACK_OF_NOSE: {
        'Длинная спинка носа': [-5, -3, 15, 0, 5],
        'Короткая спинка носа': [10, 5, -5, -2, -3],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.WIDTH_OF_BACK_OF_NOSE: {
        'Широкая спинка носа': [-2, 7, -5, 7, 2],
        'Тонкая спинка носа': [4, -2, 8, -3, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.LENGTH_OF_NECK: {
        'Шея короткая': [0, 0, -5, 7, 0],
        'Средняя длина шеи': [0, 0, 0, 0, 0],
        'Длинная шея': [0, 0, 8, -2, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.THICKNESS_OF_NECK: {
        'Толстая шея': [0, 0, -3, 5, 0],
        'Средняя толщина шеи': [0, 0, 0, 0, 0],
        'Тонкая шея': [0, 0, 5, -3, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.SIZE_OF_PALMS: {
        'Крупные ладони': [-4, -3, 5, 7, 7],
        'Малые ладони': [7, 4, 0, -4, -3],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.PALM_SHAPE: {
        'Квадрат': [0, 5, -2, 7, 0],
        'Прямоугольник': [2, 0, 3, 2, 7],
        'Малый прямоугольник': [5, 0, 1, -3, 0],
        'Узкий вытян прямоугольник': [0, -4, 7, -4, 0],
        '"Весло"': [-4, -3, 7, 0, 3],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.FEATURES_OF_BRUSHES: {
        'Мягкие рыхлые ладони': [0, 5, -3, -2, -3],
        'Налитые плотные ладони': [0, -2, -3, 5, 0],
        '"Сухие" кисти': [2, -3, 7, -3, 3],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.FINGER_LENGTH: {
        'Длинные пальцы': [0, -3, 7, 0, 5],
        'Средняя длина пальцев': [0, 0, 0, 0, 0],
        'Короткие пальцы': [0, 7, 0, 5, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.FINGER_SHAPE: {
        'Ровные пальцы': [3, 5, 7, 5, -1],
        'Конусообразные пальцы': [5, 0, 0, 0, 0],
        'Искривленные пальцы': [0, 0, 0, 0, 7],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.FEATURES_OF_FINGERS: {
        'Узловатые пальцы': [0, 0, 0, 0, 8],
        '"Сухие" пальцы': [2, -4, 5, -2, 2],
        'Мясистые пальцы': [0, 5, -3, 2, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.NAIL_SHAPE: {
        'Длинный прямоугольник': [0, 0, 7, 0, 2],
        'Трапеция короткая': [0, 5, 0, 4, 0],
        'Трапеция длинная': [0, 0, 2, 0, 5],
        'Монетоподобные': [0, -2, -5, -2, 7],
        'Овальные': [5, 0, 0, 0, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.CONVEXITY_OF_NAILS: {
        'Попер и прод выпукл (линза)': [7, 0, 0, 0, 3],
        'Поперечно-выпуклые': [2, 2, 5, 3, 1],
        'Плоские': [0, 3, 0, 1, 4],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.MUSCLE_VOLUME: {
        'Мышцы тонкие': [4, 0, 5, 0, 0],
        'Мышцы объемные': [0, 5, -5, 7, 5],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.MUSCLE_DENSITY: {
        'Мягкие рыхлые мышцы': [0, 7, 0, -3, 0],
        'Плотные "резиновые" мышцы': [0, -3, 0, 7, 4],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
    QuestionName.FEATURES_OF_SKIN: {
        'Крупные поры (лицо)': [0, 5, -2, 3, 0],
        'Кожа легко краснеет': [2, 1, 1, 0, 0],
        'Веснушки': [10, 0, 0, 0, 0],
        'Затрудняюсь ответить': [0, 0, 0, 0, 0],
    },
}
