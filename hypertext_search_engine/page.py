class Page:
    id = -1
    text_content = ''
    page_rank = 0
    inlinks = set()
    outlinks = set()

    def __init__(self, id, text_content, outlinks):
        self.id = id
        self.text_content = text_content
        self.outlinks = outlinks

