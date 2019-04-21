import os
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID


def createSearchableData(root):
    schema = Schema(title=TEXT(stored=True), id=ID(stored=True), textcontent=TEXT(stored=True))
    if not os.path.exists("../indexdir"):
        os.mkdir("../indexdir")

    # Creating an index writer to add document as per schema
    ix = create_in("../indexdir", schema)
    writer = ix.writer()

    filepaths = [os.path.join(root, i) for i in os.listdir(root)]
    for path in filepaths:
        try:
            fp = open(path, 'r', encoding="utf-8")
            text = fp.read()
            writer.add_document(title=path.split("\\")[1], id=path, textcontent=text)
            fp.close()
        except:
            print("Error: " + path)
    writer.commit()


def search(query_str, topN):
    ix = open_dir("../indexdir")
    with ix.searcher(weighting=scoring.Frequency) as searcher:
        query = QueryParser("textcontent", ix.schema).parse(query_str)
        results = searcher.search(query, limit=None)
        for i in range(topN):
            print(results[i]['title'], str(results[i].score), results[i]['id'])