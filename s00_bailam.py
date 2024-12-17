#region debai
"""
--- ma debai / id
greeting(hour_str)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday
   https://github.com/namgivu/toyagreetinghourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo trinhduyetweb de kiemtra tep s00_bailam.py, va lay diachi/url aka githubbailamurl

02b dán diachi githubbailamurl theo mẫu ở trang web duoiday
    https://forms.gle/oXmPGxt3NTorcGnN8

--- debai / problem
Viết hàm
  greeting(hour_str)
giúp chat bot in ra câu chào theo buổi sáng/chiều/tối trong ngày
00:00AM  - 11:59AM Good morning!
12:00PM  - 05:59PM Good afternoon!
06:00PM  - 11:59PM Good evening!

Khi chạy với đầuvào / input  | Kếtquả đẩura / output  | Thứtự mẫuthử
---------------------------- | ---------------------- | -----------
greeting(hour_str='6am')     | Good morning!          | 00

# AM / PM format
greeting('6am')              | Good morning!          | 01
greeting('6 am')             | Good morning!          | 02
greeting('6AM')              | Good morning!          | 03
greeting('6 AM')             | Good morning!          | 04

greeting('9pm')              | Good evening!          | 05
greeting('0900pm')           | Good evening!          | 06
greeting('09:00pm')          | Good evening!          | 07
greeting('09:00 pm')         | Good evening!          | 08
greeting('09:00 PM')         | Good evening!          | 09

greeting('1pm')              | Good afternoon!        | 10

# 24-hours format
greeting('06:00')            | Good morning!          | 11
greeting('0600')             | Good morning!          | 12
greeting('21:00')            | Good evening!          | 13
greeting('2100')             | Good evening!          | 14

"""
#endregion debai

#region bailam
def get_24hformat_hour(hour_str):
  if hour_str is None:
    return None

  hour_str = hour_str.strip().lower()

  is_pm = 'pm' in hour_str
  is_am = 'am' in hour_str

  hour_str = hour_str.replace('am', '').replace('pm', '').strip()

  try:
    if len(hour_str) > 2:
      hour_str = hour_str[:2]
    hour = int(hour_str)
  except ValueError:
    return None

  if is_pm and hour < 12:
    hour += 12
  elif is_am and hour == 12:
    hour = 0

  return int(hour)
def greeting(hour_str):
    hour = get_24hformat_hour(hour_str)

    if hour is None:
      return "Hi!"

    if 0 <= hour < 12:
      return "Good morning!"
    elif 12 <= hour < 18:
      return "Good afternoon!"
    elif 18 <= hour < 24:
      return "Good evening!"
    else:
      return "Hi!"

#endregion bailam
