import random

# Substitution Cipher
# There are 26! Keys = 4.03x10^26

def sub_codec(message,seed,cipher):
    # for a seed: 20,000 input bytes max
    random.seed(seed)
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key_0 = list(LETTERS)
    key_1 = random.sample(key_0, 26)
    msg_ary = list(message)
    if cipher:
        return (''.join(key_1[key_0.index(alpha)] for alpha in msg_ary))
    else:
        return (''.join(key_0[key_1.index(alpha)] for alpha in msg_ary))

seed = 3500
message = 'HELLOWORLD'

ciphered_msg = sub_codec(message,seed,True)
print(ciphered_msg)
print(sub_codec(ciphered_msg,seed,False))