# Project job-insights

Modulo 4: ciencias da computação - seção 1 "Introdução a Python" - cruso desenvolvimento web fullstack, na Trybe.


## Para ver o projeto em ação

 1. **criar o ambiente virtual**

  ```
  $ python3 -m venv .venv
   ```

  2. **ativar o ambiente virtual**

  ```
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```
  $ python3 -m pip install -r dev-requirements.txt
  ```
  O arquivo dev-requirements.txt contém todas as dependências que serão utilizadas no projeto
 
 Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente. Quando precisar desativar o ambiente virtual, execute o comando `deactivate`.

  4. **execulte o comando `flask run`, e acesse o site gerado pelo Flask em `http://localhost:5000`**

## Objetivo deste projeto foi:

> **Em:** src/insights/jobs.py
  as funções `read`, `get_unique_job_types`, `filter_by_job_type`

> **Em:** src/insights/industries.py
  as funções `get_unique_industries`, `filter_by_industry`

> **Em:** src/insights/salaries.py
  as funções `get_max_salary`, `get_min_salary`, `filter_by_salary_range`, `matches_salary_range`

> **Em:** tests/counter/test_counter.py
  o test `count_ocurrences`

> **Em:** tests/brazilian/test_brazilian_jobs.py
  o test `read_brazilian_file`

> **Em:** tests/sorting/test_sorting.py
  o test `sort_by`

Essa lista de funções e tests acima, já estava criada no projeto só me fora pedido pra implementar a logica de cada nos requisitos

As funções `check_min_and_max_salay_in_job`, `check_salay_is_valid`, `catch`. Em src/insights/salaries.py, foram feitas por mim para ajudar a reduzir a complexidade da função de um requisito e reutilizar em outro requisito caso fosse nescessario ( mas não foi ), a função catch foi um experimento pra ver como criar um list comprehension com try except para a função "filter_by_salary_range"

> **Em:** src/flask_app/routes_and_views.py, a rota `/job/<index>` foi um requisito bônus que usei de exemplo a rotas anteriores para aprender como implementar ela a função que é utilizada nela get_job e render_template alem de toda o código jinja foi feita pela Trybe
