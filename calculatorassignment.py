#Maria Clarin (2501990331)
#Nicholas Valerianus Budiman (2502055596)

# Defining tokens (as constants so its immutable) along with the lexeme
TOKEN_ASSIGN = 'assign'
TOKEN_PLUS = 'plus'
TOKEN_MINUS = 'minus'
TOKEN_TIMES = 'times'
TOKEN_DIV = 'div'
TOKEN_LPAREN = 'lparen'
TOKEN_RPAREN = 'rparen'
TOKEN_ID = 'id'
TOKEN_NUMBER = 'number'
TOKEN_COMMENT = 'comment'

#function to check if a char is a digit


def is_digit(char):
    return '0' <= char <= '9'

#function for tokenizing the input code, main lexical analysis portion


def lexer(input):
    tokens = []
    i = 0
    code_length = len(input)
    line = 1

    #while loop to traverse through the entirity of the code length
    while i < code_length:
        char = input[i]

        #Assign Tokenization
        if char == ':':
            if i + 1 < code_length and input[i + 1] == '=':
                tokens.append((TOKEN_ASSIGN, ':='))
                i += 2
            else:
                raise ValueError(f"Invalid token at position {i}: {char}")
        #Plus Tokenization
        elif char == '+':
            tokens.append((TOKEN_PLUS, char))
            i += 1
        #Minus Tokenization
        elif char == '-':
            tokens.append((TOKEN_MINUS, char))
            i += 1
        #Times (Multiplication) Tokenization
        elif char == '*':
            tokens.append((TOKEN_TIMES, char))
            i += 1
        #Division Tokenization
        elif char == '/':  
            #Single Line Comments
            if char == '/' and i + 1 < code_length and input[i + 1] == '/':
                i += 1
                comment = char
                while i < code_length and input[i] != '\n':
                    comment += input[i]
                    i += 1
                tokens.append((TOKEN_COMMENT, comment))
            #Multi Line Comments
            elif char == '/' and i + 1 < code_length and input[i + 1] == '*':
                comment = char
                i += 1
                while i + 1 < code_length and not (input[i] == '*' and input[i + 1] == '/'):
                    comment += input[i]
                    if input[i] == '\n':
                        line += 1
                    i += 1
                tokens.append((TOKEN_COMMENT, comment + "*/"))
                #Multiline comment error handling
                if i + 1 >= code_length:
                    print(f"Unterminated comment at line {line}, position {i - 1}")
                i += 2
            else:
                tokens.append((TOKEN_DIV, char))
                i += 1
        #Left Parentheses Tokenization
        elif char == '(':
            tokens.append((TOKEN_LPAREN, char))
            i += 1
        #Right Parentheses Tokenization
        elif char == ')':
            tokens.append((TOKEN_RPAREN, char))
            i += 1
        #Identifier (ID) Tokenization
        elif is_digit(char) or char.isalpha():
            try:
                j = 0
                #Number Tokenization
                if is_digit(char):
                    while i < code_length and is_digit(char) or char.isalpha():
                        while j < code_length and (input[i+j].isalpha() or input[i+j] == '_'):
                            print("Invalid identifier in line "+str(line) + ". Try again with a correct identifier format.")
                            exit()
                        number = char
                        i += 1
                        #Takes any digits/numeric values and '.'
                        while i < code_length and (is_digit(input[i]) or input[i] == '.'):
                            number += input[i]
                            i += 1
                        tokens.append((TOKEN_NUMBER, number))
                        char = input[i]
                #ID Tokenization
                elif input[i].isalpha():
                    #Takes any alphanumeric values and '_' as one instance
                    identifier = char
                    i += 1
                    while i < code_length and (input[i].isalnum() or input[i] == '_'):
                        identifier += input[i]
                        i += 1
                    tokens.append((TOKEN_ID, identifier))
            except IndexError:
                pass
        #Handling Whitespace (ignore)
        elif char == ' ' or char == '\t':
            i += 1
        #Handling Newlines 
        elif char == '\n':
            i += 1
            line += 1
        #Error handling for any other input values that are not declared
        else:
            raise ValueError(f"Invalid token at position {i}: {char}")

    return tokens

#function to prompt user input for the calculator lexical analysis


def user_input():
    print("Input your calculation (Add an empty line to enter): ")

    #it can take not only a single input line, so users can enter newlines and type their input,
    #but once it is just an empty line input, the lexer will prompt to start
    input_lines = []
    while True:
        line = input()
        if not line:
            break
        input_lines.append(line)
    return '\n'.join(input_lines)

#main function for the program to run, calling the necessary functions


def main():
    input = user_input()
    tokens = lexer(input)
    #printing each of the tokens and lexeme detected in the input
    for token_type, token_value in tokens:
        print(f"{TOKEN_ID if token_type == 'id' else token_type}: {token_value}")


main()
