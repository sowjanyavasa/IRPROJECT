import scrapy
import os

class WikiSpider(scrapy.Spider):
    name = "wiki_spider"

    start_urls = [
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
        'https://en.wikipedia.org/wiki/Machine_learning',
    ]

    def parse(self, response):
        title = response.xpath('//title/text()').get()
        content = response.css('div.mw-parser-output').extract_first()

        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        filename = f'{output_dir}/{title}.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.body.decode())

        self.logger.info(f'Saved file {filename}')

        yield {
            'title': title,
            'content': content
        }
