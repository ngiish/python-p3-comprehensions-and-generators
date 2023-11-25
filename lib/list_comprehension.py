#!/usr/bin/env python3

def return_evens(num_list):
    even_numubers_list = [n for n in num_list if (n % 2 == 0)]
    return even_numubers_list


def make_exclamation(sentence_list):
    new_sentence = [sentence + "!" for sentence in sentence_list]
    return new_sentence
    