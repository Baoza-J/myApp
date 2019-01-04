import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

word_list = []
with open('报菜名.txt') as f:
    words = f.read()
words = " ".join(jieba.cut(words))
for word in words.split():
    word = re.sub(r'[A-Za-z0-9\；\，\“\”\？\！]', '',word)
    word_list.append(word)
words = ' '.join(word_list)

backgroud_image = plt.imread('shengdanshu.jpg')
wc = WordCloud(font_path='simkai.ttf', mask=backgroud_image,background_color="white", max_words=1000)
my_wc = wc.generate_from_text(words)
image_colors = ImageColorGenerator(backgroud_image)
plt.imshow(my_wc.recolor(color_func=image_colors),)
plt.axis('off')
my_wc.to_file('happy.png')
