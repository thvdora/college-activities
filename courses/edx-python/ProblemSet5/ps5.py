import string

def load_words(file_name):

    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

def is_word(word_list, word):

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():

    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

###
def build_shift_dict(shift):
    dictionary = {}

    for letter in string.ascii_lowercase:
        index = string.ascii_lowercase.index(letter)
        index = (index + shift) % 26
        dictionary[letter] = string.ascii_lowercase[index]

    for letter in string.ascii_uppercase:
        index = string.ascii_uppercase.index(letter)
        index = (index + shift) % 26
        dictionary[letter] = string.ascii_uppercase[index]

    return dictionary


class Message(object):
    def __init__(self, text):

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]
        

    ### 1

    def apply_shift(self, shift):
        # cria o dicionário de shift
        shift_dict = build_shift_dict(shift)

        # cria uma str vazia para a mensagem cripto
        crypted_message = ''

        # percorre a mensagem original
        for char in self.message_text:
            # se o char for uma letra, substitui pela deslocada
            if char in shift_dict:
                crypted_message += shift_dict[char]
            # se não, mantém ele igual
            else:
                crypted_message += char

        return crypted_message

    ### 2

### Antes: Message → só texto e lista de palavras
### Agora: PlaintextMessage → texto + shift + dicionário de criptografia + mensagem cripto
class PlaintextMessage(Message):
    def __init__(self, text, shift):

        # super() chama a classe pai (message)
        super().__init__(text)

        # guarda o deslocamento na instância
        self.shift = shift
        # gera o dicionário das palavras deslocadas
        self.encrypting_dict = build_shift_dict(shift)
        # gera a mensagem cripto aplicando a função
        self.message_text_encrypted = self.apply_shift(self.shift)


    def get_shift(self):
        return self.shift

    def get_encrypting_dict(self):
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    # Se não atualizar os atributos que dependem do deslocamento,
    # todas as mensagens ficariam iguais, mas para isso, eu tenho que chamar ele:
    def change_shift(self, shift):

        self.shift = shift # atualiza o deslocamento
        # atribui novamente
        self.encrypting_dict = build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        super().__init__(text)

    def decrypt_message(self):
        best_shift = 0
        max_valid_words = 0
        best_message = ''
        for shift in range(26):
            # aplica o shift atual na mensagem
            decoded = self.apply_shift(shift)

            # divide a mensagem decodificada em palavras
            words = decoded.split(' ')

            # conta quantas palavras são válidas
            valid_count = 0
            for word in words:
                if is_word(self.valid_words, word):
                    valid_count += 1

            # se esse shift gerou mais palavras válidas que o melhor até agora
            if valid_count > max_valid_words:
                max_valid_words = valid_count
                best_shift = shift
                best_message = decoded
        return best_shift, best_message

def decrypt_story():
    encrypted_story = get_story_string()
    cipher = CiphertextMessage(encrypted_story)
    best_shift, decrypted_story = cipher.decrypt_message()
    return best_shift, decrypted_story

###

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())

#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
