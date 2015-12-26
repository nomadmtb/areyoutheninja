from imgur import ImgurAPI

api = ImgurAPI()
link = api.get_random_image('https://api.imgur.com/3/gallery/r/lolcats')
print(link)
