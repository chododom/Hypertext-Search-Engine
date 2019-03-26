class Page:
    id = -1
    page_url = ''
    text_content = ''
    page_rank = 0
    inlinks = set()
    outlinks = set()

    def __init__(self, id, page_url, text_content, outlinks):
        self.id = id
        self.page_url = page_url
        self.text_content = text_content
        self.outlinks = outlinks

