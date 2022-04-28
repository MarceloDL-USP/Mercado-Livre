ordenacao_de_produtos
==============================

Ordenação de produtos

2. Com que rapidez você pode encomendar esses produtos?

Descrição

A seção de ofertas https://www.mercadolibre.com.ar/ofertas#nav-header é uma seção que agrupa as melhores ofertas MELI, e em linhas gerais é uma lista de produtos em oferta ordenados por uma pontuação de ML e diferentes regras de negócios.

Anexo ao desafio, há um arquivo "ordenamiento.csv" que contém uma lista de produtos, com sua pontuação e categorias para este desafio.
Uma amostra deste csv se parece com isso:

A pontuação determina a qualidade de um item_id, sendo 1 o melhor valor possível.
Se não houver regras de negócio que imponham restrições à ordenação, a solução ideal seria ordenar nosso conjunto de dados do maior para o menor por pontuação, obtendo-se o seguinte resultado:

3 O problema é que esta ordenação deve refletir uma variedade de produtos e categorias, permitindo a descoberta de diferentes tipos de produtos, razão pela qual temos regras na produção como as seguintes:

1. O “domain_id” não pode ser repetido em 4 posições consecutivas.
2. O “vertical” não pode ser repetido em 1 posição consecutiva.
3. Se o id 641416750 existir na lista, ele deve estar na posição 3, sendo esta regra mais forte que as demais.
4. Se o id 22351223 existir na lista, deve estar na posição 6, sendo esta regra mais forte que as demais.
5. As posições 9,10,11 devem ter itens sim ou sim da categoria “HOME&DECO”, sendo esta regra mais forte que 1 e 2.
6. Cumprindo estas condições, a ordenação deve respeitar uma ordenação da pontuação mais alta para a mais baixa.

O desafio é projetar um algoritmo que, dado o conjunto de dados e essas restrições, retorne a lista final ordenada de itens. O algoritmo deve ser projetado para escalar de forma eficiente com o número de itens, e contemplar os casos em que as restrições não podem ser cumpridas. O tempo de execução é o fator chave!

Notebook entregável com o algoritmo para gerar a lista ordenada e seu tempo de execução.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
