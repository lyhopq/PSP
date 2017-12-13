from PIL import Image
import argparse
import csv
import jieba.analyse
from scipy.misc import imread
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def cleanring(string):
    pass

def fetch_text(file):
    with open(file, 'r') as f:
        for line in f:
            # line = cleanring(line).strip()
            yield line

def word_segment(texts):
    jieba.analyse.set_stop_words('stopwords.txt')
    for text in texts:
        tags = jieba.analyse.extract_tags(text, topK=40)
        yield ' '.join(tags)

def generate_img(texts, mask, output):
    data = ' '.join(text for text in texts)
    mask_img = imread(mask, flatten=True)
    wc = WordCloud(
        font_path='msyh.ttc',
        background_color='white',
        mask=mask_img
    ).generate(data)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig(output, dpi=600)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-o', '--output', default='output.jpg')
    parser.add_argument('-m', '--mask', default='heart.jpg')

    args = parser.parse_args()
    generate_img(word_segment(fetch_text(args.file)), args.mask, args.output)