
def main():
  try:
    with open("books/frankenstein.txt") as f:
      file_contents = f.read()
  except:
    print("Please double check your file contents or path")
  else: 
    word_count = count_words(file_contents)
    print(word_count)
    word_dict = count_letters(file_contents)
    word_list = dict_to_list(word_dict)
    sorted_word_list = sort_list(word_list)
    make_report(sorted_word_list)

def count_words(book: str) -> int:
  words = book.split()
  return len(words)

def count_letters(book: str) -> dict:
  letter_count_dict = {}
  words = book.lower().split()
  for word in words:
    for letter in word:
      if letter in letter_count_dict:
        letter_count_dict[letter]+=1
      else:
        letter_count_dict[letter]=1
  return letter_count_dict

def dict_to_list(letter_count: dict):
  letter_list = []
  for key in letter_count:
    if(key.isalpha()):
      letter_list.append({"letter":key, "count":letter_count[key]})
  return letter_list


def sort_list(letter_list: list):
  letter_list.sort(key=lambda x: x['count'],reverse=True)
  return letter_list

def make_report(sorted_letter_list: list):
  for item in sorted_letter_list:
    print(f"The {item["letter"]} character was found {item["count"]} times")

main()