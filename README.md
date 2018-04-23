# Orthogons

This project is a simple experiment with using [some special
ratios][orthogons] to make non-uniform grids to guide
composition. That's a mouthful, but all we're trying to do is to come
up with some useful grids for design that are not boring (like the
kinds you get out of the box with a Bootstrap or a Foundation).

It is motivated by Jen Simmons' excellent [Layout Land
video series][layout-land]. In a [particularly amazing
episode][fr-units-video], she points to the *[content-out
layout][content-out-layout]* philosophy (articulated Mark Boulton and
Nathon Ford, drawing from Linda van Deursen). My simple summary of the
idea is this:

- Don't start with a uniform grid just because; that's context-free to
  the point of being generic
- Take a good look at the content you have, and define relationships
  and structure based on this
- Use this structure to build out suitable grids, and further, use
  [special ratios of widths and heights][orthogons] when doing so to
  really make your design feel organic!

In this repository, you're going to find some experiments with this as
I work out a new layout for [my personal website][my-site].

## Experiments

### 1. A look at the 12 orthogons of Wersin

This is a really basic first step, where I simply visualise all these
special ratios on a 4 column grid. The code in the repository has
generators (in Python) that can be tweaked for more columns (and ratios).


### 2. A simple article template

TODO: With outsets, asides, different width images, etc.


[orthogons]: https://en.wikipedia.org/wiki/Dynamic_rectangle
[layout-land]: https://www.youtube.com/channel/UC7TizprGknbDalbHplROtag
[fr-units-video]: https://www.youtube.com/watch?v=ZPtpzuRajzM
[content-out-layout]: https://alistapart.com/article/content-out-layout
[my-site]: https://harishnarayanan.org/
