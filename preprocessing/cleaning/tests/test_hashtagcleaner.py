from usure.preprocessing.cleaning.hashtagcleaner import HashtagClener

def can_remove_all_hashtags_test():
    cleaner = HashtagClener()
    text = "#Hola #test_sd amigos esto es un prueba #test #prueba #aqui_probando"
    cleaned_text = " amigos esto es un prueba"
    procesed_text = cleaner.clean(text)
    assert procesed_text == cleaned_text