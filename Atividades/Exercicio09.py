"""9) Um sistema financeiro automatizado aprova um empréstimo
(emprestimo_aprovado) se todas as exigências abaixo forem atendidas:
1. Renda mensal (renda) de pelo menos R$ 5.000,00 OU Score de crédito (score)
maior ou igual a 700.
2. Idade do solicitante (idade) entre 21 e 65 anos (inclusive).
3. O valor da prestação mensal (calculado por valor_emprestimo / parcelas) não pode
exceder 30% da renda mensal do solicitante.
Crie o script em Python que declare as entradas e monte a variável booleana final."""

renda = float(input("Digite sua renda atual: "))
score = float(input("Digite seu score: "))
idade = int(input("Digie sua idade"))
valor_do_emprestimo = float(input("valor que voce necessita : "))
parcelas = int(input("Digite o valor das parcelas : "))

porcentagem_da_renda = valor_do_emprestimo (30 / 100)
calculo = (( renda => 5000 ) and ( score => 700 )) and  ( idade > 21 and idade < 65 ) and 