from pelican import signals

cjk_range = [
    (u'\u3040', u'\u309F'),    # Japanese Hiragana
    (u'\u30A0', u'\u30FF'),    # Japanese Katakana
    (u'\u3400', u'\u4DB5'),    # CJK Unified Ideographs Extension A
    (u'\u4E00', u'\u9FEF'),    # CJK Unified Ideographs
    (u'\uF900', u'\uFAFF'),    # CJK Compatibility Ideographs
    (u'\U00020000', u'\U0002A6D6'),  # CJK Unified Ideographs Extension B
    (u'\U0002A700', u'\U0002B734'),  # CJK Unified Ideographs Extension C
    (u'\U0002b740', u'\U0002B81D'),  # CJK Unified Ideographs Extension D
    (u'\U0002B820', u'\U0002CEA1'),  # CJK Unified Ideographs Extension E
    (u'\U0002ceb0', u'\U0002EBE0'),  # CJK Unified Ideographs Extension F
    (u'\U0002F800', u'\U0002FA1F'),  # CJK Compatibility Ideographs Supplement
]

punc_range = [
    (u'\u0000', u'\u0020'),  # space
    (u'\u003c', u'\u003c'),  # less-than sign
    (u'\u003e', u'\u003e'),  # grater-than sign
    (u'\u3000', u'\u303f'),  # CJK Symbols and Punctuation
    (u'\uff00', u'\uffef'),  # Halfwidth and Fullwidth Forms
    (u'\u200D', u'\u200D'),           # ZERO WIDTH JOINER
    (u'\uFE0E', u'\uFE0F'),           # VARIATION SELECTOR-15/16
]

def _chinese_auto_spacing(text):

    def _with_range(char, check_range):
        # XXX: actually this kind of searching will see a improvment from O(n)
        # to O(1) when using patricia instead of list. but for a blog plugin
        # processing offline, I think it doesn't matter too much. for those who
        # writes a lot, this improvements may be expected.
        for start, end in check_range:
            if char >= start and char <= end:
                return True
        return False

    def is_cjk(char):
        return _with_range(char, cjk_range)

    def is_punc(char):
        return _with_range(char, punc_range)

    ret = u''
    prev = None

    for char in text:
        sp = u''
        curr_is_cjk = is_cjk(char)
        curr_is_punc = is_punc(char)

        if prev:
            prev_is_cjk, prev_is_punc = prev

            if curr_is_punc or prev_is_punc:
                # do not add space around punctuation
                sp = u''

            elif prev_is_cjk != curr_is_cjk:
                sp = u' '

        ret = ret + sp + char
        prev = (curr_is_cjk, curr_is_punc)

    return ret


def process_content(content):
    if content._content is None:
        return

    content._content = _chinese_auto_spacing(content._content)


def process_title(generator, metadata):
    if ('CJK_AUTO_SPACING_TITLE' not in generator.settings
            or not generator.settings['CJK_AUTO_SPACING_TITLE']):
        return

    if u'title' in metadata:
        metadata[u'title'] = _chinese_auto_spacing(metadata[u'title'])


def register():
    signals.content_object_init.connect(process_content)
    signals.article_generator_context.connect(process_title)
