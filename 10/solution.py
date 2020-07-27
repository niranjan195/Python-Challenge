global_dict = {1 : '1', 2: '11', 3: '21'}

def say_helper(string):
  tmp_string = string[0]
  for i in range(1,len(string)):
    if string[i] != tmp_string[-1]:
      tmp_string += "-"
    tmp_string += string[i]
  string_split = tmp_string.split("-")
  res = ''
  # print (string_split)
  for i in range(len(string_split)):
    res = res + str(len(string_split[i])) + str(string_split[i][0])
  return res


def look_and_say(N):
  if N in global_dict:
    return global_dict[N]
  string = str(look_and_say(N-1))
  result_number = say_helper(string)
  global_dict[N] = result_number 
  return result_number


if __name__ == "__main__":
    N = 31
    solution = len(look_and_say(N))
    print (solution)
    