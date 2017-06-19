import re
def get_matching_words(regex):
    results = []
    words = [
        "baby",
        "baseball",
        "denver",
        "facetious",
        "issue",
        "mattress",
        "obsessive",
        "paranoia",
        "rabble",
        "union",
        "volleyball",
    ]
    for word in words:
        if re.search(regex, word):
            results.append(word)
    return results

# my_expression = r"ss"
# print get_matching_words(my_expression)

# my_expression = r"b\wb"
# print get_matching_words(my_expression)

# my_expression = r"b\w\w*b"
# print get_matching_words(my_expression)

# my_expression = r"a\w*e\w*i\w*o\w*u"
# print get_matching_words(my_expression)

# my_expression = r"[aeiou][aeiou]$"
# print get_matching_words(my_expression)

# my_expression = r"^[regularexpression]+$"
# print get_matching_words(my_expression)

# my_expression = r"^[^regex]+$"
# print get_matching_words(my_expression)

# my_expression = r"b\w*b"
# print get_matching_words(my_expression)

# my_expression = r"b\w?b"
# print get_matching_words(my_expression)

# my_expression = r"io"
# print get_matching_words(my_expression)

# my_expression = r"e$"
# print get_matching_words(my_expression)


my_expression = r"(.)\1\w*(.)\2"
print get_matching_words(my_expression)

