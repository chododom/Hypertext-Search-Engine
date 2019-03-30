class Page:
    id = -1
    page_url = ''
    text_content = ''
    rank = 0
    # set of IDs of pages linking to self
    inlinks = set()
    # set of IDs of pages self links to
    outlinks = set()

    def __init__(self, id, page_url, text_content, outlinks):
        self.id = id
        self.page_url = page_url
        self.text_content = text_content
        self.outlinks = outlinks

