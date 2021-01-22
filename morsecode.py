# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    result = False
    if user_input.lower() == "h" or user_input.lower() == "help":
        result = True  

    return result
    # ==================================


def is_validated_english_sentence(user_input):
    # isalnum 적용해보기
    result = True
    sign = '_@#$%^&*()-+=[]{\"}\';:\\|`~' # 코드에 작용하는 기호는 백스페이스 넣기
    sign2 = '.,!?'
    cleaned = ''
    if user_input.split() == []:
        return False
    for i in user_input:
        if i.isdigit() or (i in sign):
            return False
        elif i in sign2:
            continue
        else :
            cleaned += i
    if cleaned == '':
        result = False
    return result
    # ==================================


def is_validated_morse_code(user_input):
    result = True
    if user_input == '' or user_input.split() == []:
        return False
    user_input = user_input.split()
    morse_code = get_morse_code_dict()
    for i in user_input:
        if i not in morse_code.values():
            result = False
            return result
    return result
    # ==================================



def get_cleaned_english_sentence(raw_english_sentence):
    result = ''
    for i in raw_english_sentence:
        if i not in ['.',',','!','?']:
            result += i
    result = result.strip()
    return result
    # ==================================


def decoding_character(morse_character):
    result = ''
    morse_code_dict = get_morse_code_dict()
    for i in morse_code_dict.keys():
        if morse_code_dict[i] == morse_character:
            result = i
    return result
    # ==================================


def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    if english_character == ' ':
        return ' '
    result = morse_code_dict[english_character.upper()]
    return result
    # ==================================


def decoding_sentence(morse_sentence):
    result = ''
    morse_sentence_list = morse_sentence.split(' ')
    for i in morse_sentence_list:
        if i == '':
            result += ' '
        else :
            result += decoding_character(i)
    return result
    # ==================================


def encoding_sentence(english_sentence):
    result = ''
    cleaned_sentence = get_cleaned_english_sentence(english_sentence)
    cleaned_sentence = ' '.join(cleaned_sentence.split())
    for i in cleaned_sentence:
        if i == ' ':
            result += ' '
        else:
            result += encoding_character(i)
            result += ' '
    return result
    # ==================================


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    while True:
        choice = input("Input your message(H - Help, 0 - Exit):")
        if choice == '0':
            break
        elif is_help_command(choice):
            print(get_help_message())
        elif (is_validated_morse_code(choice) or is_validated_english_sentence(choice)):
            if is_validated_morse_code(choice):
                print(decoding_sentence(choice))
            else:
                english_sentence = get_cleaned_english_sentence(choice)
                print(encoding_sentence(english_sentence))
        else:
            print('Wrong Input')
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
