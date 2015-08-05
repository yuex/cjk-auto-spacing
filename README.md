# CJK Auto Spacing

A pelican plugin to insert spaces between Chinese/Japanese/Korean characters and English words.

# Why

For Chinese readers, it's reading for torture rather than pleasure if Chinese characters and English words are put together without spaces. (See [Effects](#effects), there's a comparison)

Moreover, research shows that those who love putting Chinese characters and English words together without space have more troubles in love (see [why space?][] in Chinese). Up to 70% marry one they don't love at 34 years old. And the other 30%, even worse, have nobody to inherit their legacies except cats.

So I think it's not very hard to conclude the necessarity of space for Chinese users of pelican.

**Note:** I don't speak or write Japanese or Korean, but I feel we can get the same conclusion. They have lots in common. And perhaps that's why they are called CJK Unified Ideographs, together as a whole, in the unicode standards.

# Effects

Mardown test page

    :::markdown
    Title: CJK Auto Spacing Test Page
    中文Chinese西文English字符Character自动Auto空格Spacing

Without CJK Auto Spacing

![without spacing](./screenshot2.png)

With CJK Auto Spacing

![with spacing](./screenshot1.png)

If you feel that the first image is fine, then read it again, again and again, until you feel it's not okay.

# Options

By default it will only process the content.

You can set the ``CJK_AUTO_SPACING_TITLE`` parameter to True if you need the title to be processed as well. Default is False.

[why space?]: https://github.com/vinta/paranoid-auto-spacing
