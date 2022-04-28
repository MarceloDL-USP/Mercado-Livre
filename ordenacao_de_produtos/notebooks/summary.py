import pandas as pd

def categorias_unicas(coluna_analisada):
    return len(coluna_analisada.unique())

def summary(df):
    metric_dict = {feature: ["max", "min", categorias_unicas] for feature in df.columns}
    return df.agg(metric_dict)

def print_type_info(df):
    dict_info = {}
    colunas = []
    Type = []
    unique_valor = []
    type_count = []
    nun_count = []
    none_count = []

    for i, column in enumerate(df.columns):
        colunas += [column]
        Type += [df[column].dtype]
        unique_valor += [df[column].unique()]
        type_count += [len(df[column].unique())]
        nun_count += [df[column].isna().sum()]
        none_count += [df[column][df[column] == "none"].count()
]

        # Quantidade de none
        
    dict_info.update({"Coluna": colunas, "Type": Type, "Type_Count": type_count, "Null_Count": nun_count, "None_Count": none_count, "Unique_Valor": unique_valor})
    df_info = pd.DataFrame(dict_info)

    pd.set_option('display.max_rows', None)     # Apresenta todas as linhas
    pd.set_option('display.max_columns', None)  # Apresenta todas as colunas
    pd.set_option('display.width', 100)        # Largura da tela em caracteres. Se definido como None o pandas detectará automaticamente a largura.
    pd.set_option('display.max_colwidth', 80)   # A largura máxima em caracteres de uma coluna na represntação de uma estrutura de dados pandas
    return df_info