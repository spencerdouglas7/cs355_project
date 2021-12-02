with open('passwords', 'w') as f:
  num_chars = 1024 * 1024 * 1024 * 4
  f.write('0' * num_chars)
