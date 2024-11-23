import pandas as pd

def calculate_demographic_data(print_data=True):
    df_dados = pd.read_csv('adult.data.csv', header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ])

    contagem_raca = df_dados["race"].value_counts()

    idade_media_homens = round(df_dados[df_dados["sex"] == "Male"]["age"].mean(), 1)

    porcentagem_bacharel = round(
        (df_dados["education"].value_counts().get("Bachelors", 0) / len(df_dados)) * 100, 1
    )

    educacao_superior = df_dados[df_dados["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    educacao_basica = df_dados[~df_dados["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    ricos_educacao_superior = round(
        (len(educacao_superior[educacao_superior["salary"] == ">50K"]) / len(educacao_superior)) * 100, 1
    )
    ricos_educacao_basica = round(
        (len(educacao_basica[educacao_basica["salary"] == ">50K"]) / len(educacao_basica)) * 100, 1
    )

    horas_minimas_trabalho = df_dados["hours-per-week"].min()

    trabalhadores_min_horas = df_dados[df_dados["hours-per-week"] == horas_minimas_trabalho]
    porcentagem_ricos_min_horas = round(
        (len(trabalhadores_min_horas[trabalhadores_min_horas["salary"] == ">50K"]) / len(trabalhadores_min_horas)) * 100, 1
    )

    paises_ricos = df_dados[df_dados["salary"] == ">50K"]["native-country"].value_counts()
    total_paises = df_dados["native-country"].value_counts()
    porcentagem_paises_ricos = (paises_ricos / total_paises * 100).dropna()
    pais_mais_ricos = porcentagem_paises_ricos.idxmax()
    porcentagem_mais_ricos = round(porcentagem_paises_ricos.max(), 1)

    profissao_top_india = df_dados[
        (df_dados["native-country"] == "India") & (df_dados["salary"] == ">50K")
    ]["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", contagem_raca)
        print("Average age of men:", idade_media_homens)
        print(f"Percentage with Bachelors degrees: {porcentagem_bacharel}%")
        print(f"Percentage with higher education that earn >50K: {ricos_educacao_superior}%")
        print(f"Percentage without higher education that earn >50K: {ricos_educacao_basica}%")
        print(f"Min work time: {horas_minimas_trabalho} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {porcentagem_ricos_min_horas}%")
        print("Country with highest percentage of rich:", pais_mais_ricos)
        print(f"Highest percentage of rich people in country: {porcentagem_mais_ricos}%")
        print("Top occupations in India:", profissao_top_india)

    return {
        'race_count': contagem_raca,
        'average_age_men': idade_media_homens,
        'percentage_bachelors': porcentagem_bacharel,
        'higher_education_rich': ricos_educacao_superior,
        'lower_education_rich': ricos_educacao_basica,
        'min_work_hours': horas_minimas_trabalho,
        'rich_percentage': porcentagem_ricos_min_horas,
        'highest_earning_country': pais_mais_ricos,
        'highest_earning_country_percentage': porcentagem_mais_ricos,
        'top_IN_occupation': profissao_top_india
    }
