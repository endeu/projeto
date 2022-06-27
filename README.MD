# Avaliação substitutiva - desenvolvimento WEB III


Para a avaliação SUBda disciplina, desenvolva um projeto em Django. Este projeto deve consumir os dados dos feriados e apresentar na página index, se hoje é ou não feriado. Caso seja feriado, informar qual o feriado do dia.

- Página principal (index) ( até 2 pontos )
    - Via URL /
    - Caso não seja feriado, apresentar a mensagem “Não é feriado”
    - Caso a data do dia seja uma data de feriado, informar qual o feriado em comemoração.
    - A consulta será via banco de dados / componentes ORM
- Gravar os feriados via API no banco de dados ( até 2 pontos )
    - Via URL /cadastroAPI
    - Com uso do ORM do Django, gravar os dados oriundos via API em um banco de dados SQL.
    - A classe FeriadoAPI, será compartilhado para esta avaliação.
    - A view responsável por esta operação irá ser executada uma única vez.
- Adicionar os feriados municipais ( até 2 pontos )
    - Via URL /cadastro
    - Seu sistema WEB deve permitir incluir, adicionar novos feriados no banco de dados
    - Utilize Forms ou ModelForms, o que for mais conveniente.
    - Testes ( até 4 pontos )
    - Testes dos modelos ( classe herdam de Model )
    - Testes dos Forms / Modelforms 