""" Python Object Trie Implementation """

class Trie(object):
  """ Trie class """

  def __init__(self):
    self.root_node = {}

  def check_present_and_add(self, word):
    """ Return False if word already in trie, otherwise return True and add """

    current_node = self.root_node
    is_new_word = False

    # iterate through trie adding missing notes
    for char in word:
      if char not in current_node:
        is_new_word = True
        current_node[char] = {}
      current_node = current_node[char]
    
    # mark end of word so that words that are prefixes of present words are not
    # returned - i.e. each word must have an explicit "End of Word" marker
    if "End of Word" not in current_node:
      is_new_word = True
      current_node["End on Word"] = {}

    return is_new_word
