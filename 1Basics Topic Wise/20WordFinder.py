# this is program to find the list of words and return True or False depending on their presence 
# create class world
# create list of words within the class world
# find the length of each word 
# search the word in the matrix m*m , should be able to search in 4 possible ways top, down, left and right sides in the matrix

#if the word is present then print true for that list[i] else print False

class WordList:
    def __init__(self, words):
        # Initialize a list of words as a class attribute
        self.words = words

    def find_word_length(self):
        # Method to find the length of each word in the list
        return [len(word) for word in self.words]

    def search_word_in_matrix(self, matrix):
        # Method to search for each word in the matrix in all four directions
        result = []

        def search_in_direction(word, row, col, direction):
            # Helper function to search for a word in a specific direction
            word_length = len(word)

            if direction == "top":
                end_row = row - word_length
                if end_row < 0:
                    return False
                for i in range(row, end_row, -1):
                    if matrix[i][col] != word[word_length - i + row - 1]:
                        return False

            elif direction == "down":
                end_row = row + word_length
                if end_row > len(matrix):
                    return False
                for i in range(row, end_row):
                    if matrix[i][col] != word[i - row]:
                        return False

            elif direction == "left":
                end_col = col - word_length
                if end_col < 0:
                    return False
                for j in range(col, end_col, -1):
                    if matrix[row][j] != word[word_length - j + col - 1]:
                        return False

            elif direction == "right":
                end_col = col + word_length
                if end_col > len(matrix[0]):
                    return False
                for j in range(col, end_col):
                    if matrix[row][j] != word[j - col]:
                        return False

            return True

        for word in self.words:
            found = any(
                search_in_direction(word, row, col, direction)
                for row in range(len(matrix))
                for col in range(len(matrix[0]))
                for direction in ["top", "down", "left", "right"]
            )
            result.append(found)

        return result

# Example usage:

# Creating an instance of WordList with a list of words
word_list_instance = WordList(["apple", "banan", "orange", "grape"])

# Finding the length of each word in the list
word_lengths = word_list_instance.find_word_length()
print("Word Lengths:", word_lengths)

# Example matrix
example_matrix = [
    ['a', 'b', 'p', 'l', 'e'],
    ['d', 'a', 'f', 'p', 'r'],
    ['g', 'n', 'a', 'r', 't'],
    ['g', 'a', 'a', 'r', 't'],
    ['g', 'n', 'a', 'r', 't']
]

# Searching for each word in the matrix in all four directions
result = word_list_instance.search_word_in_matrix(example_matrix)

# Displaying the result
for i, word in enumerate(word_list_instance.words):
    print(f"Word '{word}' found in matrix: {result[i]}")

