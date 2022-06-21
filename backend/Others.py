def get_info_other(ending):
    if ending in negative:
        return "терс маани мүчө"
    elif ending in question:
        return "суроолуу мүчө"
    elif ending in plural:
        return "көптүк сан"
    else:
        return 'none'
def get_info_plural_for_num(ending):
    if ending in plural:
        return "затташып кеткен мучө"
    else:
        return 'none'

question = {
    'би', 'бы', 'бу', 'бү',
    'пи', 'пы', 'пу', 'пү',
}
negative = {
    'ба', 'бе', 'бө', 'бо',
    'па', 'пе', 'пө', 'по',
    'сыз', 'сиз', 'сүз', 'суз',
}
plural ={
    'дар', 'дер', 'дор', 'дөр',
    'тар', 'тер', 'тор', 'төр',
    'лар', 'лер', 'лор', 'лөр',
}