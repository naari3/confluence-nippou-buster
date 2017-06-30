# -*- coding: utf-8 -*-

import sys
import argparse

import markdown_processor
import confluence_processor

parser = argparse.ArgumentParser(description='This script is busting nippou system')

parser.add_argument('title_format', \
        action='store', \
        nargs=None, \
        const=None, \
        default=None, \
        type=str, \
        choices=None, \
        help='strftime format of nippou title', \
        metavar=None)

parser.add_argument('space', \
        action='store', \
        nargs=None, \
        const=None, \
        default=None, \
        type=str, \
        choices=None, \
        help='space name', \
        metavar=None)

parser.add_argument('parent_page_name', \
        action='store', \
        nargs=None, \
        const=None, \
        default=None, \
        type=str, \
        choices=None, \
        help='parent page name', \
        metavar=None)

def receive_pipe():
    markdown = "".join(sys.stdin.readlines())
    return markdown

def main(title_format, space, parent_page_name):
    raw_markdown = receive_pipe()
    html_markdown = markdown_processor.process(raw_markdown)

    page = confluence_processor.process(html_markdown, title_format, space, parent_page_name)

    print(f"page's url: {page['url']}")

if __name__ == '__main__':
    args = parser.parse_args()
    title_format = args.title_format
    space = args.space
    parent_page_name = args.parent_page_name

    main(title_format, space, parent_page_name)
