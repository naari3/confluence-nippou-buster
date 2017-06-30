from confluence import Confluence
import datetime

def process(html, title_format, space, parent_page_name):
    client = Confluence(profile='confluence')
    title = datetime.datetime.now().strftime(title_format)
    print(f'title:       {title}')
    print(f'space:       {space}')
    print(f'parent_page: {parent_page_name}')
    page = client.storePageContent(page=title, space=space, content=html, convert_wiki=False, parent_page=parent_page_name)

    return page
