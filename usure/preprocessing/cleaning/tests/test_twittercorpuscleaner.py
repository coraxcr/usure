from usure.preprocessing.cleaning.twittercorpuscleaner import TwitterCorpusCleaner


def can_remove_all_id_test():
    cleaner = TwitterCorpusCleaner()
    text = "\"406449856862232577\",\"\"Las despedidas no deberian existir\"\""
    cleaned_text = "\"\"Las despedidas no deberian existir\"\""
    procesed_text = cleaner.clean(text)
    assert procesed_text == cleaned_text
