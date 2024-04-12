import requests
import json



def get_word_num(word):
  data = '{"word":"' + word + '"}'
  data = data.encode()




  cookies = {
      '_ym_uid': '1671375352424982255',
      '_ym_d': '1671375352',
      '__gads': 'ID=0efe472c8e2fad8a-22f803abe3da00c7:T=1672506622:RT=1672506622:S=ALNI_Mbm7Xo7GoUCLv0uadMiHChFDioHEQ',
      '__gpi': 'UID=00000b9b27f85f36:T=1672506622:RT=1673190110:S=ALNI_MZEa_0iuSzJxtSn0h8opqA4He7ApA',
      'django_session_id': '278e9f21-2b4b-408e-9c67-e569fb197cb2',
      '_ym_isad': '2',
      '_ym_visorc': 'w',
  }

  headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'en-US,en;q=0.5',
      # 'Accept-Encoding': 'gzip, deflate, br',
      'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA0NzM2OTU2LCJqdGkiOiJlNDM4NDZjMWU3ZmQ0ZjNmYTAxYzg3MjQ0Mjc3YzNlNiIsInVzZXJfaWQiOjE4fQ.jR0pCrsGBip7JJlYoIrvKsSr-bgBrQB6Q8Wbrt2BEfs',
      'Content-Type': 'application/json',
      'Origin': 'https://dev.guess-word.com',
      'Connection': 'keep-alive',
      'Referer': 'https://dev.guess-word.com/',
      # 'Cookie': '_ym_uid=1671375352424982255; _ym_d=1671375352; __gads=ID=0efe472c8e2fad8a-22f803abe3da00c7:T=1672506622:RT=1672506622:S=ALNI_Mbm7Xo7GoUCLv0uadMiHChFDioHEQ; __gpi=UID=00000b9b27f85f36:T=1672506622:RT=1673190110:S=ALNI_MZEa_0iuSzJxtSn0h8opqA4He7ApA; django_session_id=278e9f21-2b4b-408e-9c67-e569fb197cb2; _ym_isad=2; _ym_visorc=w',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
  }

  json_data = {
      'word': word,
  }

  response = requests.post('https://dev.guess-word.com/api/rooms/main/guess/', cookies=cookies, headers=headers, json=json_data)



  ans = response.text
  ans = json.loads(ans)
  #if ('guess_history' not in ans):
  #  return 1000000
  #ans = ans['guess_history'][0]
  if ('order' not in ans):
    return 1000000
  return (ans['order'])




def russian_code(word):
  rus_str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
  decoded = '%D0%B0%D0%B1%D0%B2%D0%B3%D0%B4%D0%B5%D1%91%D0%B6%D0%B7%D0%B8%D0%B9%D0%BA%D0%BB%D0%BC%D0%BD%D0%BE%D0%BF%D1%80%D1%81%D1%82%D1%83%D1%84%D1%85%D1%86%D1%87%D1%88%D1%89%D1%8A%D1%8B%D1%8C%D1%8D%D1%8E%D1%8F'
  answer = ''
  for i in range(len(word)):
    for j in range(len(rus_str)):
      if (rus_str[j] == word[i]):
        for k in range(6):
          answer += decoded[6*j+k]
  return answer


def get_top_words(word):
  cookies = {
      '_ym_uid': '1671552341568374239',
      '_ym_d': '1671552341',
      '_ym_isad': '2',
      '__gads': 'ID=7e264559480ce960-22d0475f35db0071:T=1673197453:RT=1673197453:S=ALNI_MbBxkwGlBblU8_dZV-9HqUDT6QgNw',
      '__gpi': 'UID=00000b9fbd0cc3c0:T=1673197453:RT=1673197453:S=ALNI_MbnUG9--M6sX3pYlfbySwIjtDKxmQ',
  }

  headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
      # 'Accept-Encoding': 'gzip, deflate, br',
      'Connection': 'keep-alive',
      # 'Cookie': '_ym_uid=1671552341568374239; _ym_d=1671552341; _ym_isad=2; __gads=ID=7e264559480ce960-22d0475f35db0071:T=1673197453:RT=1673197453:S=ALNI_MbBxkwGlBblU8_dZV-9HqUDT6QgNw; __gpi=UID=00000b9fbd0cc3c0:T=1673197453:RT=1673197453:S=ALNI_MbnUG9--M6sX3pYlfbySwIjtDKxmQ',
      'Upgrade-Insecure-Requests': '1',
      'Sec-Fetch-Dest': 'document',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-Site': 'cross-site',
  }

  response = requests.get(
      'https://wordassociation.ru/' + russian_code(word),
      cookies=cookies,
      headers=headers,
  )



  q = response.text
  count = 0
  answer = ''
  ans_list = list()
  rus_str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
  for i in range(15, len(q)):
    # <li><span>хоботок</span></li>
    if q[i] in rus_str:
      answer+=q[i]
    else:
      if len(answer) > 0:
        ans_list.append(answer)
        answer=''
  return ans_list



'''
API
get_word_num('клоун')
get_top_words('слон')
'''


def execute():
  word_queue = list()
  word_queue.append('комната')
  ind = 0
  while (len(word_queue) < 10000):
    cur_word_list = get_top_words(word_queue[ind])
    for i in cur_word_list:
      u = get_word_num(i)
      if (u < 1000):
      	print(i + " : " + str(u))
      if i not in word_queue:
      	word_queue.append(i)
    print(len(word_queue))
    ind += 1

execute()
