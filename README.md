# CJK Auto Spacing

A pelican plugin to insert space between Chinese/Japanese/Korean character
and English word.

# Why

For Chinese readers, it's reading for torture instead of pleasure if Chinese
characters and English words are mingled togther without spaces. (See
[Effects](#effects) for comparison)

Moreover, research shows that those who love putting Chinese characters and
English words together without space have more troubles in love ([why space?][]
in Chinese). Up to 70% marry one they don't love at 34 years old. And the other
30%, even worse, have nobody to inherit their legacies except cats.

So, to Chinese users, it is not hard to see the necessarity of using spaces.

**Note**: I know nothing about Japanese and Korean, but I feel confidently we
can get the same conclusion. They have lots in common. And perhaps that's why
they are called CJK Unified Ideographs together as a whole in the unicode
standards.

# Options

By default it will only process the content. To process title, add following
line to your `pelicanconf.py`

    CJK_AUTO_SPACING_TITLE = True

# Effects

Mardown test page

    :::markdown
    Title: CJK Auto Spacing Test Page
    中文Chinese西文English字符Character自动Auto空格Spacing

Without CJK Auto Spacing

![without spacing](./screenshot2.png)

With CJK Auto Spacing

![with spacing](./screenshot1.png)

If you find nothing wrong in the first picture, re-read it until you find it's
wrong.

[why space?]: https://github.com/vinta/paranoid-auto-spacing
