import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')
    #le o arquivo

    race_count = df['race'].value_counts()
    #conta o numero de ocorrecnias de cada raça

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    #filtra os homens e calcula a média de idade, arredondando para 1 casa decimal

    total_people = len(df)
    #numero de colunas
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    #quantas pessoas possuem o grau de escolaridade Bachelors
    percentage_bachelors = round((bachelors_count / total_people * 100), 1)
    #calcula porcentagem de pessoas com Bachelors, arredondando para 1 casa decimal


    higher_education_list = ['Bachelors', 'Masters', 'Doctorate']
    #cria lista com os graus de escolaridade maiores
    higher_education = df[df['education'].isin(higher_education_list)]
    #cria um dataframe filtrando as pessoas com grau de escolaridade maior
    lower_education = df[~df['education'].isin(higher_education_list)]
    #cria um dataframe filtrando as pessoas com grau de escolaridade menor

    higher_education_rich = round((len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100), 1)
    #calcula porcentagem de pessoas com escolaridade maior que ganham mais de 50K, arredondando para 1 casa decimal
    lower_education_rich = round((len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100), 1)
    #calcula porcentagem de pessoas com escolaridade menor que ganham mais de 50K, arredondando para 1 casa decimal

    min_work_hours = df['hours-per-week'].min()
    #encontra o menor valor de horas trabalhadas por semana

    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    #conta quantas pessoas trabalham com o menor numero de horas por semana
    rich_min_workers_count = len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])
    #conta quantas pessoas trabalham com o menor numero de horas por semana e ganham mais de 50K
    rich_percentage = round((rich_min_workers_count / num_min_workers * 100), 1)
    #calcula a porcentagem de pessoas que trabalham com o menor numero de horas por semana e ganham mais de 50K, arredondando para 1 casa decimal

    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    #conta quantas pessoas ganham mais de 50K por país
    total_by_country = df['native-country'].value_counts()
    #conta o total de pessoa por pais
    percentage_by_country = (rich_by_country / total_by_country * 100).sort_values(ascending=False)
    #calcula a porcentagem de pessoas que ganham mais de 50K por país e ordena em ordem decrescente
    
    highest_earning_country = percentage_by_country.index[0]
    #pega o primeiro país da lista ordenada
    highest_earning_country_percentage = round(percentage_by_country.iloc[0], 1)
    #pega a porcentagem do primeiro país da lista ordenada, arredondando para 1 casa decimal

    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    #filtra o dataframe para pessoas da India que ganham mais de 50K
    top_IN_occupation = india_rich['occupation'].mode()[0]
    #encontra a ocupação mais comum entre as pessoas da India que ganham mais de 50K

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
