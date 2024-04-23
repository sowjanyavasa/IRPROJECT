# IR-PROJECT---CS-429
Abstract

    This project aims to build a scalable information retrieval system using a three-stage pipeline: web crawling, document indexing, and query processing. The development summary describes the integration of Scrapy for web crawling, Scikit-Learn for constructing a TF-IDF-based inverted index, and Flask for handling user queries with cosine similarity-based ranking.

    The objectives are to create a functional pipeline that can crawl web documents, index them for quick retrieval, and return relevant search results based on user queries. The system is designed to be modular, allowing for flexible updates and extensions.

    For the next steps, the project can expand the crawling scope, explore advanced indexing techniques, and improve query processing with features like spelling correction and semantic search. Further integration with third-party data sources could also be a future goal to increase the richness of the document corpus.

Overview
1. Solution Outline

    The system involves a Scrapy-based web crawler, a Scikit-Learn indexer, and a Flask query processor to create a text-based search solution. The crawler gathers web documents in HTML format, the indexer constructs an inverted index with TF-IDF, and the query processor uses cosine similarity to respond to user queries with top-ranked results.

2. Relevant Literature

    The system draws from established concepts in web crawling, TF-IDF scoring, and information retrieval. These concepts form the basis for document indexing and similarity measurement.

3. Proposed System

    The system's modular architecture allows for flexibility and scalability. It is designed for text-based search and can be used in applications like search engines, document clustering, and information retrieval. The integration of the three components ensures an efficient and cohesive workflow.

Design
1. System Capabilities

    The system can crawl web pages, build a TF-IDF-based index, and process user queries to find the most similar documents based on cosine similarity.

2. Interactions

    The crawler fetches web pages and stores them as html files.
    The indexer computes TF-IDF scores for the documents and creates an inverted index and displayed : TF-IDF score/weight representation, Cosine similarity.
    The processor validates and processes user queries, returning the top-K similar documents (eg- Top 5 Results).

3. Integration

    The system combines the crawler, indexer, and processor into a unified workflow, allowing for scalable crawling, efficient indexing, and responsive query handling.

Architecture

1. Software Components : The architecture includes a Scrapy-based crawler(wiki_spider.py), a Scikit-learn-based indexer(indexer.py), and a Flask-based processor(processor.py).

2. Interfaces: Components communicate through pickled data file(index.pickel), with the Flask processor(processor.py) offering an HTTP interface for query processing.

3. Implementation: Implemented in Python 3.11, using Scrapy 2.11 for crawling, Scikit-learn 1.2 for indexing, and Flask 2.2 for query handling.

Operation

1. Software Commands: Start the crawler with scrapy crawl wiki_spider. Build the index with the indexer's build_index method and Run the indexer with python3 indexer.py. Run the processor with python3 processor.py.

2. Inputs: web URLs for the crawler, html documents for the indexer, and pickel file for the processor.

3. Installation: Install Python 3.11, Scrapy, Scikit-learn, and Flask. Configure environment variables for the Flask application.

Conclusion

1. Success/Failure Results: The project successfully demonstrates web crawling, TF-IDF indexing, and query processing. Performance might vary with large data sets.

2. Outputs: JSON responses with top-5 similar documents for queries, pickled data for indices

3. Caveats/Cautions: Performance may be affected by network speed and data size. Crawling should respect website terms of use.

Data Sources

These are the List of Data source URLs to crawl for data, including Wikipedia. and Downloaded Pickled index files, crawled HTML documents.
        'https://en.wikipedia.org/wiki/Information_retrieval',
        'https://pypi.org/project/wikipedia/',
        'https://en.wikipedia.org/wiki/Scrapy',
        'https://en.wikipedia.org/wiki/Scikit-learn',
        'https://en.wikipedia.org/wiki/Flask',
        'https://en.wikipedia.org/wiki/Tf%E2%80%93idf',
        'https://en.wikipedia.org/wiki/Cosine_similarity',
        'https://en.wikipedia.org/wiki/Word2vec',
        'https://en.wikipedia.org/wiki/Natural_Language_Toolkit',
        'https://en.wikipedia.org/wiki/WordNet',
        'https://en.wikipedia.org/wiki/Inverted_index',
        'https://en.wikipedia.org/wiki/Web_crawler',
        'https://en.wikipedia.org/wiki/Search_engine',
        'https://en.wikipedia.org/wiki/Vector_space_model',
        'https://en.wikipedia.org/wiki/Boolean_model_of_information_retrieval',
        'https://en.wikipedia.org/wiki/Latent_semantic_analysis',
        'https://en.wikipedia.org/wiki/PageRank',
        'https://en.wikipedia.org/wiki/Information_extraction',
        'https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation',
        'https://en.wikipedia.org/wiki/Machine_learning'

Test Cases

    For crawler - Executed scrapy crawl wiki_spider. It generated html files.
    For Scikit-learn-based indexer - Executed python3 indexer.py. So it generated pickel file
    For Flask - Executed python3 processor.py. It returns URL - http://127.0.0.1:5000
    Sample curl commad used to test output - curl -X POST -H "Content-Type: application/json" -d '{"query": "WordNet"}' http://127.0.0.1:5000/query
    Example output - 
    {
  "Top 5 results": [
    {
      "Document Name": "WordNet - Wikipedia.html",
      "similarity": 0.2137278905421412
    },
    {
      "Document Name": "Natural Language Toolkit - Wikipedia.html",
      "similarity": 0.0042317291921854065
    },
    {
      "Document Name": "Vector space model - Wikipedia.html",
      "similarity": 0.0040142762659532705
    },
    {
      "Document Name": "Information extraction - Wikipedia.html",
      "similarity": 0.0034019932657762277
    },
    {
      "Document Name": "Cosine similarity - Wikipedia.html",
      "similarity": 0.002186599626423785
    }
  ]
    }

Source Code

    source code includes below modules
    For crawler - wiki_spider.py
    For Scikit-learn-based indexer - processor.py
    For Flask - indexer.py

Bibliography

https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089

https://www.machinelearningplus.com/nlp/cosine-similarity/

https://www.researchgate.net/publication/363808554_Top-k_Document_Ranking_and_Sentence_Similarity_Retrieval_System_for_Covid-19_Research_Papers