title: Preview large text files online
num: 1
slug: preview-overview
date: 2021-04-07 20:00
category: Preview
lang: en
summary: Files often grow in size without limits. Especially logs and datasets. Opening such files can be a big problem for most text editors. Luckily it's possible to preview large text-based files sequentially, loading them piece by piece without "eating" all machine's memory. Your computer will thank you!

<div class="yt">
<iframe width="560" height="315" src="https://www.youtube.com/embed/wrk2ULCD-So" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## The main problem with large files

For most text processors opening files means loading them into memory. This approach makes it easier to process files, format them, search for something. The main problem is sometimes files are just too large to be loaded into RAM. The program becomes unresponsive and usually crashes.

## Loading a file sequentially, piece by piece

![Preview large files sequentially]({filename}/images/preview-large-files-sequentially.png)

A possible solution to this problem is loading files piece by piece. That makes it possible to preview only some part of a file. And in most cases, that's enough to understand what's inside the file. Linux users have built-in tools for this. Commands such as `less`, `head`, and `tail` load only small portions of text files. With *StatSim.Preview* it's now possible to preview large files in the browser. New text blocks are loaded dynamically, just when they are needed.

## Preview files in StatSim.Preview

*StatSim.Preview* is a simple web application. Just open a text-based file clicking the `Browse` button, or drag-and-drop it from a local folder. That will load only a small piece of the selected file and display its content in the main window. Scroll a page to load more text blocks or click the `Load all` button to load the complete file into memory.
