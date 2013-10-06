from pelican import signals, contents

cjk_range = [
        (u'\u3400',u'\u4DB5'), #  CJK Unified Ideographs Extension A
        (u'\u4E00',u'\u9FA5'), #  CJK Unified Ideographs
        (u'\u9FA6',u'\u9FBB'), #  CJK Unified Ideographs
        (u'\uF900',u'\uFA2D'), #  CJK Compatibility Ideographs
        (u'\uFA30',u'\uFA6A'), #  CJK Compatibility Ideographs
        (u'\uFA70',u'\uFAD9'), #  CJK Compatibility Ideographs
        (u'\U00020000',u'\U0002A6D6'), # CJK Unified Ideographs Extension B
        (u'\U0002F800',u'\U0002FA1D'), # CJK Compatibility Supplement
        ]

punc_range = [
        (u'\u0000',u'\u0020'), # space
        (u'\u3000',u'\u303f'), #  CJK Symbols and Punctuation
        (u'\uff00',u'\uffef'), #  Halfwidth and Fullwidth Forms
        ]

def chinese_auto_spacing(content):
    if content._content == None:
        return

    def _with_range(char, check_range):
        for start,end in check_range:
            if char >= start and char <= end:
                return True
        return False

    def is_cjk(char):
        return _with_range(char, cjk_range)
    def is_punc(char):
        return _with_range(char, punc_range)

    ret = u''
    src = content._content
    prev = None
    for char in src:
        sp = u''
        curr_is_cjk = is_cjk(char)
        curr_is_punc = is_punc(char)

        if prev:
            prev_is_cjk, prev_is_punc = prev

            if curr_is_punc or prev_is_punc:
                # do not add space to punctuation
                sp = u''

            elif prev_is_cjk != curr_is_cjk:
                sp = u' '

        ret = ret + sp + char
        prev = (curr_is_cjk, curr_is_punc)

    if ret:
        content._content = ret

def register():
    signals.content_object_init.connect(chinese_auto_spacing)
