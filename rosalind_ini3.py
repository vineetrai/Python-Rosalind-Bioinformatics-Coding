def stringslice(text, a, b, c, d):
    return text[a:(b+1)] + " " + text[c:(d+1)]

sample = "ASpBYXaB4ccowuXPZwntIPrIY4uyfDBpeNsXm2k5XUsHCBShWkFiLxtBOtocoris7qpelagicustMYpxSwgEnrsx6kw0rjqVebuwz5nIflR1EHexpxQoEuv9uCHIXirZB2X1KDJwNhoucoMR5lsRrF1EIqP6FVt7t."
w = 56
x = 63
y = 66
z = 74

print(stringslice(sample, w, x, y, z))
