from hashlib import sha256
max_nonce = 1000000000000

def SHA256(text):
  return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
  prefix_str = '0'*prefix_zeros

  for nonce in range(max_nonce): 
    text = str(block_number) + transactions + previous_hash + str(nonce)
    new_hash = SHA256(text)
    if new_hash.startswith(prefix_str):
      print(f"Yay!!! mined bitcoin with nonce : {nonce}")
      return new_hash
  
  raise BaseException(f"Couldn't find correct hash after trying {max_nonce} times")


if __name__ == '__main__':
  transaction='''
  Dhaval->Krish->20,
  Mand0->Cara->100
  '''
  new_hash = mine(5, transaction, '0000000xa036944e295680cff17edbe038f81208fecf9a66be9a2b8321c6ec7', 4)
  print(new_hash)