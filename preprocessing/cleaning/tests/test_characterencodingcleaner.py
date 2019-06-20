from usure.preprocessing.cleaning.characterencodingcleaner import CharacterEncodingCleaner


def can_encode_to_ascii_test():
    text = u'Šéf chomutovských komunistů dostal poštou bílý prášek, Qué oración más simpática! España Yigüirro'
    cleanedtext = 'dostal , !'
    cleaner = CharacterEncodingCleaner()
    result = cleaner.clean(text)
    assert result == cleanedtext