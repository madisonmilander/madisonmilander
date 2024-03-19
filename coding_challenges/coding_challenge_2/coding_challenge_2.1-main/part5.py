# # ############
# Dictionary containing letter scores for Scrabble
# letter_scores = {
#     "aeioulnrst": 1,
#     "dg": 2,
#     "bcmp": 3,
#     "fhvwy": 4,
#     "k": 5,
#     "jx": 8,
#     "qz": 10
# }
# # calculate the scrabble score of a word
# def calculate_scrabble_score(word):
#     score = 0
#     for letter in word:
#         for key in letter_scores:
#             if letter in key:
#                 score += letter_scores[key]
#                 break
#     return score
# # Ask the user for a word
# word = input("Enter a word: ").lower()  # Convert the input word to lowercase for consistency
#
# # Calculate and print the Scrabble score of the word
# scrabble_score = calculate_scrabble_score(word)
# print("The Scrabble score of the word '{word}' is: {scrabble_score}")