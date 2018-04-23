# Orthogons

This project aims to come up with some useful grids for design that
are not boring (like the kinds you get out of the box with a Bootstrap
or a Foundation).

It is motivated by Jen Simmons’ excellent [Layout Land
video series][layout-land]. In a [particularly amazing
episode][fr-units-video], she points to the *[content-out
layout][content-out-layout]* philosophy (articulated Mark Boulton and
Nathon Ford, drawing from Linda van Deursen).

My simple summary of the idea is this:

- Don’t start with a uniform grid just because; that’s context-free to
  the point of being generic.
- Take a good look at the content you have, and define relationships
  and structure based on this.
- Use this structure to build out suitable grids, and further, use
  [special ratios of widths and heights][orthogons] when doing so to
  make your design feel really organic!

In this repository, you’re going to find some experiments with these
ideas as I attempt to arrive at a more human layout for [my personal
website][my-site].

## Experiments with non-uniform grids

### 1. A look at the 12 orthogons of Wersin

This is a really basic first step, where I simply visualise all these
[special ratios][orthogons] on a 4 column grid. The first column
starts one unit wide, and the rest subsequently grow in multiples of
the ratio.

![12 orthogons of Wersin][exp-1-screenshot]

[The code][exp-1-code] in the repository has generators (in Python) that can be
tweaked for more columns (and ratios).


### 2. A simple article template

TODO: With outsets, asides, different width images, etc.

## Discussions and contributing

If you’d like to talk about this stuff or contribute to it, I’d love
to hear from you:

- You can talk to me like a human [on twitter][my-twitter]
- You can introduce your idea or suggestion as a [GitHub
  issue][gh-issue]
- You can introduce your idea or suggestion with code as a [GitHub
  pull request][gh-pull-request]

Do not be intimidated if you are new or inexperienced at this
stuff. All ideas are welcome and this is a safe place to share them.

## Copyright and license

Copyright (c) 2018 [Harish Narayanan][my-site].

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

[orthogons]: https://en.wikipedia.org/wiki/Dynamic_rectangle
[layout-land]: https://www.youtube.com/channel/UC7TizprGknbDalbHplROtag
[fr-units-video]: https://www.youtube.com/watch?v=ZPtpzuRajzM
[content-out-layout]: https://alistapart.com/article/content-out-layout
[my-site]: https://harishnarayanan.org/
[my-twitter]: https://twitter.com/copingbear
[gh-issue]: https://github.com/hnarayanan/orthogons/issues
[gh-pull-request]: https://github.com/hnarayanan/orthogons/pulls
[exp-1-code]: https://github.com/hnarayanan/orthogons/tree/master/experiment-1
[exp-1-screenshot]: https://github.com/hnarayanan/orthogons/raw/master/experiment-1/screenshot.png
