# coding: utf-8
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter


def analyze(text):
    token_filters = [POSKeepFilter(['名詞'])]
    a = Analyzer(token_filters=token_filters)
    return a.analyze(text)


def find(toks, tok):
    for t in toks:
        if tok.reading[-1] == t.reading[0]:
            return t

    return None


def show(tok):
    if tok is None:
        print('見つかりませんでした。')
        return

    #print(tok.surface)
    return tok.surface


def update(pool, surface):
    """
    try:
        surface = input('in > ')
    except KeyboardInterrupt:
        return False
    if not len(surface):
        return True
    """

    toks = list(analyze(surface))
    if not len(toks):
        return True

    intok = toks[0]
    if intok.reading[-1] == 'ン':
        print('ざこ。')
        return True

    cputok = find(pool, intok)
    answer = show(cputok)

    return answer


def answer(surface):
    text = '''
    こたつの中でモゾモゾ動いている。何かがいるのか。そう思うと中から「ニャー」という鳴き声。ネコか。だが、今度は中から「クセがスゴい！」の声。ネコではなく千鳥・ノブなのか。大悟がどちらかを予想する中、こたつから出てきたのは「ニャー」とネコに扮したノブ。これは、『テレビ千鳥』（テレビ朝日）で2月に行われた「こたつから出とうないんじゃ!!」という企画内で自然発生的に生まれた、「ネコか？ノブか？ゲーム」だ。この番組の企画はいつもバカバカしくてシンプル。それを千鳥の2人や、彼らが信頼する少数の芸人たちでやることで爆発的な面白さを生み出している。中でも千鳥が絶大な信頼を寄せているのが麒麟・川島だ。どのようになるか「見えない」企画には必ずといっていいほどキャスティングされている。この日もそうだった。今回は「ネコか？ノブか？ゲーム」の「出張版」。何も知らない芸人のもとを訪れこのゲームをやってもらうのだ。その最初の“挑戦者”が川島だった。
    川島は困惑しつつも、こたつの中で「ニャー」と可愛く鳴いたかと思えば、「麒麟です」と低音ボイスをきかせる。大悟は「ネコ」で出てくると予想。実は番組冒頭で大悟は「ネコ以外で出てくるヤツ、おるんかな？」「ネコ以外で出る人はどんな人なのか？」と疑問を持ったことが企画の発端だと話していた。確かに「スベりたくない」という防衛本能が誰よりも敏感なのが芸人だ。待ち構えているときに登場するという状況はスベりやすい。自分のまま出てスベるより、「ネコ」というキャラを乗せた状態でスベるほうが逃げ場がある。だったら、自ずと「ネコ」で出ることを選ぶのは芸人の性だろう。果たして、川島が選んだのも「ネコ」。こたつの中にいるときは絶対に「麒麟です」で行こうと思ってた川島だが、こたつから顔を覗かせた瞬間、怖くなったのか、「ネコになっていた」と。2人目のブラックマヨネーズ・小杉も大悟の予想が的中し、やはり「ネコ」で出てくる。
    最後の挑戦者はワッキー。強力なギャグやキャラを持つワッキーがネコで出てくるなら、自分のままで出てくる芸人は誰もいないだろうと大悟は考え、初めて「ネコ」ではなく「ワッキー」と予想。そして出てきたのは真顔のワッキー。自分のまま、顔一本で勝負に出たのだ。ワッキーはその理由を、ネコで出たら「面白くないじゃん」と当たり前のように言い放つ。自分の“顔力”に絶対的な自信がないと言えないことだろう。スベる心配よりも、笑わせるという自信のほうが上回ったのだ。ゲーム自体はひたすらバカバカしい。けれど同時に芸人の生理をえぐり、その複雑な葛藤を垣間見ることができる奥深い企画だった。
    '''

    pool = list(analyze(text))
    word = update(pool, surface)
    
    """
    while update(pool):
        pass
    """

    return word


if __name__ == '__main__':
    answer("アリ")