#导入词云的包
from wordcloud import WordCloud, ImageColorGenerator
#导入matplotlib作图的包
import matplotlib.pyplot as plt

import imageio


class Gen_Word_Cloud(object):
	src_name = 'sources/'
	dst_name = ''

	def __init__(self, src_name):
		self.src_name += src_name
		self.dst_name = src_name


	def gen_pic(self):
		with open(self.src_name, 'r', encoding = 'utf-8') as f:
			text = f.read()

			back_coloring = imageio.imread('sources/pig_cartoon.jpg')
			# back_coloring = imageio.imread('sources/test.jpeg')

			#生成一个词云对象
			wordcloud = WordCloud(
			        background_color="black", #设置背景为白色，默认为黑色
			        # width=1500,              #设置图片的宽度
			        # height=960,              #设置图片的高度
			        margin=10,               #设置图片的边缘

			        # max_words=2000, # 词云显示的最大词数
			        max_font_size=80, # 字体最大值
			        random_state=42, # 随机产生的颜色种类数
			        mask = back_coloring, #设置背景图片
			        ).generate(text)

			image_colors = ImageColorGenerator(back_coloring) # 从背景图片生成颜色值
			# 绘制图片
			# plt.imshow(wordcloud)
			# 消除坐标轴
			plt.axis("off")
			# 按照背景图片 重新着色
			plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
			# 随机生成颜色
			# plt.imshow(wordcloud)
			# 展示图片
			plt.show()
			# 保存图片
			wordcloud.to_file( 'output/' + self.dst_name + '.png')


if __name__ == '__main__':
	gen_word_cloud = Gen_Word_Cloud('animal_farm.txt')
	gen_word_cloud.gen_pic()

