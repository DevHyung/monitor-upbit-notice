import requests
from bs4 import BeautifulSoup
header = {
'Cookie':"__cfduid=d456afab2c873b2d2b9f78c96432e276c1524302950; newsession=hbpETLaqefXHsqse9AkIj%2FB7X%2B8b%2F57Pz1Q%2Ba%2FFA0JeuNnUr8M4KLg8ZgkWsTfa%2BKO3Y3xVxnewuJADr329d%2Bs8xXwJvLvrnAxqMkKxh68RnNegvQYI9kZm3xCTpZQn%2FiBh4tgXz%2FgzPxU%2FuxOnR3gThIdd%2FizXwgtZgjv86pCyleyd0VPdVQooMovIrfH8e5EzFy5qbkIQqlsiG3KYmcbl7mHP7AZH6Vk8OqQPF%2BxGnIUEMdvLP4JZapf2sJYasKOZPWdricLiJIG2Bi6jceukiDsnNTfRfly1HbQd8Q%2FXgh9%2FMtEbsg0ENnqGKdXfWnKRUn7ROu17xY298nEx0fytEFTJSrpwP4Xf8RiXcEpWZ%2Bl2zDz2dImb8l87myeRszvmCjDjmqORgxl8%2BFUacJKMjjq0eUV9rf%2FIQlJ4nLOo%3D13f59126ea37134432d15683fc5ebd9d59d18932"
}
if __name__=="__main__":
    html = requests.get('http://made-club.com/game/result?type=sport&page=240',headers=header)
    bs4 = BeautifulSoup(html.text,'lxml')
    print( bs4.prettify())