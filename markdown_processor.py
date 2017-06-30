# -*- coding: utf-8 -*-

from markdown import markdown as md_process
import emoji

def process(markdown):
    markdown = emoji.emojize(markdown, use_aliases=True)
    markdown = md_process(markdown, extensions=['gfm'])

    return markdown
