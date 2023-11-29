from suffix_array import skew
from bwt import make_bwt
from wavelet_tree.WaveletTree import WaveletTree

def main():
    text = 'the monkey eats a lot of bananas'

    # tokens = text.split()
    # print(tokens)
    # sa_list = [skew(token) for token in tokens]
    # transforms = [make_bwt(token, sa=sa) for token, sa in zip(tokens, sa_list)]
    # print(sa_list, transforms)
    # tree = WaveletTree(transforms[-1])
    # print(tree.rank_query('a', 7))

    text = 'banana'
    sa = skew(text)
    bwt = make_bwt(text, sa)
    tree = WaveletTree(bwt)
    print(sa)
    print(bwt)
    print(tree)
    print(tree.rank_query('a', 2))


if __name__ == '__main__':
    main()
