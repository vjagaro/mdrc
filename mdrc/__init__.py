import re

__version__ = '0.1.0'


def convert(text):
    text = convert_reflinks_to_links(text)
    return convert_links_to_reflinks(text)


def convert_reflinks_to_links(text):
    refs = {}

    def replace_ref(m):
        i, url = m.groups()
        if i in refs:
            return f'[]: {url}'
        else:
            refs[i] = url
            return ''

    ref_matcher = re.compile(r' {0,3}\[(\d+)\]:\s*(.+)\s*\n?')
    text = ref_matcher.sub(replace_ref, text)

    def replace_reflink(m):
        inner, n = m.groups()
        url = refs.get(n, '')
        return f'[{inner}]({url})'

    reflink_matcher = re.compile(r'\[([^]]*)\]\[(\d+)\]', re.MULTILINE)
    text = reflink_matcher.sub(replace_reflink, text)

    return text


def convert_links_to_reflinks(text):
    link_matcher = re.compile(r'\[([^]]*)\]\(\s*([^)]+)\s*\)', re.MULTILINE)

    url_set = set()

    for m in link_matcher.finditer(text):
        inner, url = m.groups()
        url_set.add(url)

    urls = {}
    i = 1
    for url in sorted(url_set):
        urls[url] = i
        i += 1

    def replace_link(m):
        inner, url = m.groups()
        if url in urls:
            i = urls[url]
            return f'[{inner}][{urls[url]}]'
        else:
            # shouldn't be possible...
            return m.group(0)

    text = link_matcher.sub(replace_link, text)

    if len(urls) > 0:
        if len(text) >= 1 and text[-1] != '\n':
            text += '\n'
        if len(text) >= 2 and text[-2:] != '\n\n':
            text += '\n'
        for url, i in urls.items():
            text += f'[{i}]: {url}\n'

    return text
