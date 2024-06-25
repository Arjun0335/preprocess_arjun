from preprocess_arjun import Utils

__version__ = '0.0.3'

def get_wordcounts(x):
	return Utils._get_wordcounts(x)

def get_charcounts(x):
	return Utils._get_charcounts(x)

def get_avg_wordlength(x):
	return Utils._get_avg_wordlength(x)

def get_stopwords_counts(x):
	return Utils._get_stopwords_counts(x)


def get_hashtag_counts(x):
	return Utils._get_hashtag_counts(x)

def get_mentions_counts(x):
	return Utils._get_mentions_counts(x)

def get_digit_counts(x):
	return Utils._get_digit_counts(x)

def get_uppercase_counts(x):
	return Utils._get_uppercase_counts(x)

def cont_exp(x):
	return Utils._cont_exp(x)

def get_emails(x):
	return Utils._get_emails(x)

def remove_emails(x):
	return Utils._remove_emails(x)

def get_urls():
	return Utils._get_urls(x)

def remove_urls(x):
	return Utils._remove_urls(x)

def remove_rt(x):
	return Utils._remove_rt(x)

def remove_special_chars(x):
	return Utils._remove_special_chars(x)

def remove_html_tags(x):
	return Utils._remove_html_tags(x)

def remove_accented_chars(x):
	return Utils._remove_accented_chars(x)


def remove_stopwords(x):
	return Utils.remove_stopwords(x)

def make_base(x):
	return Utils._make_base(x)

def get_value_counts(df, col):
	return Utils._get_value_counts(df, col)

def remove_common_words(x, freq, n=20):
	return Utils._remove_common_words(x, freq, n)

def remove_rarewords(x, freq, n=20):
	return Utils._remove_rarewords(x, freq, n)

def spelling_correction(x):
	return Utils._spelling_correction(x)

