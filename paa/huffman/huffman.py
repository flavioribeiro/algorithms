from helpers import Node, symbols_counter, create_bits_reprs

def encode(phrase):
  symbols = symbols_counter(phrase)
  reprs = create_bits_reprs(symbols)

  encoded_phrase = phrase

  for symbol in phrase:
    if symbol in encoded_phrase:
      encoded_phrase = encoded_phrase.replace(symbol, reprs[symbol])

  return encoded_phrase, reprs

def decode(sequence, symbols):
  decoded_phrase = ""
  tmp_symbol = ""
  symbols = dict((v,k) for k, v in symbols.iteritems())

  for bit in sequence:
    tmp_symbol += str(bit)
    if tmp_symbol in symbols.keys():
      decoded_phrase += symbols[tmp_symbol]
      tmp_symbol = ""

  return decoded_phrase
