# coding=utf-8
import jieba


def load_file(file_name, charset='utf-8'):
    """
    读取文件，按列返回列表
    :param file_name: 文件路径
    :param charset: 文本内容decode的编码，默认为utf-8
    :return: 文本内容列表
    """
    f1 = open(file_name)
    line = f1.readline().decode(charset).strip()
    line_list = []
    while line:
        line_list.append(line)
        line = f1.readline().decode(charset).strip()
    return line_list


def write_file(file_name, line_list, charset='utf-8', mode='w'):
    """
    新建文件将line_list中每个元素按行写入
    :param mode: 打开文件的规格， 'w' 表示新建， 'a' 表示添加， 'r' 表示只读
    :param file_name: 新建文件的文件名和路径
    :param line_list: 写入文件的列表
    :param charset: 写入文件是encode的编码， 默认为utf-8
    :return: void
    """
    f1 = open(file_name, mode=mode)
    for line in line_list:
        line.encode(charset)
        f1.write(line+'\n')
    f1.flush()
    f1.close()


def cut_sentence(sentence_list, stop_word_list):
    """
    对句子列表进行分词并除去停用词
    :param sentence_list: 待分词的句子列表
    :param stop_word_list: 停用词列表
    :return: 每个句子的分词结果的二维列表
    """
    sentence_word_list = []
    for sentence in sentence_list:
        word_list = []
        for word in jieba.cut(sentence):
            if word not in stop_word_list:
                word_list.append(word)
        sentence_word_list.append(word_list)
    return sentence_word_list


def create_vocab(sentence_word_list):
    """
    创建词库
    :param sentence_word_list: 已分词的句子列表
    :return: 词库
    """
    vocab_list = []
    for sentence in sentence_word_list:
        for word in sentence:
            if word not in vocab_list:
                vocab_list.append(word)
    return vocab_list


def create_vector(word_list, vocab_list):
    """
    创建一个句子的向量
    :param word_list: 一句已分词的列表
    :param vocab_list: 词库
    :return: 对应该词库的向量
    """
    vector = [0] * vocab_list.__len__()
    for w in word_list:
        if w in vocab_list:
            vector[vocab_list.index(w)] += 1
    return vector

if __name__ == '__main__':
    comment_list = load_file('dataSet/c1.txt')
    comment_list += load_file('dataSet/c2.txt')
    stopwords = load_file('dataSet/stopWord.txt')
    comment_words = cut_sentence(comment_list, stopwords)
    vocab = create_vocab(comment_words)
    print vocab.__len__()
    # print ' '.join(vocab)
    # print ' '.join(comment_words[5])
    print create_vector(comment_words[0], vocab_list=vocab)
