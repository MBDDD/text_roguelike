from subfunc import start

# Рогалик
# Техническое задание
# Написать простейший текстовый рогалик про путешествие по подземелью.
# Реализовать возможность автосохранения при каждом возвращении в город и загрузки герои из автосохранения.
# Например, играющему предлагается ввести имя для героя. После чего он отправляется в приключение.
# Пусть герой может встретить в каждой комнате подземелье одно или несколько событий:
# в комнате сокровище, гоблин, ловушка (пройти ловушку игрок может с некоторой вероятностью), пустая комната.
# В начале каждого похода у героя есть 3 единицы здоровья. При встрече с гоблином или при неудачном
# обезвреживании ловушки герой теряет одну жизнь. После открытия очередной комнаты и расчете событий в ней герою
# предлагается выбор — пойти в следующую комнату или вернуться в город. В городе герой может продать сокровища
# по фиксированной цене (5 золотых за шт.) и восполнить очки здоровья (бесплатно). Новый поход в подземелье
# стоит герою 10 золота. Записывать количество золота героя и количество походов из которых он успешно вернулся.
# В случае если у героя кончаются очки здоровья или не хватает золота на новый поход — игра заканчивается и выдается статистика.

start()