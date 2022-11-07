### Desafio OOP - 01

Nesse desafio os testes já estão implementados para vocês.
O objetivo é treinar um pouco mais sobre Orientaçao a Objeto.

Para isso, siga os passos abaixo para clonar e executar o projeto em sua máquina.

---
#### Instalação:

Crie uma pasta para o projeto.

Após, em seu terminal preferido digite:

`git clone https://github.com/rafaeltedesco/Desafio-Python-OOP-01.git`

*Recomendado:* 
Crie um ambiente virtual utilizando o comando
`python -m venv .venv`

Para ativar o ambiente virtual digite:
`.venv\Scripts\Activate`

Após ter ativado o ambiente virtual, instale as dependências do pytest utilizando o comando
`python install -r requirements.txt`

Execute no terminal o comando do pytest para verificar se os testes rodam
`pytest`

#### Estamos prontos para começar!

---
### O Desafio

#### 1 - Crie uma classe chamada Student

#### 2 - A classe Student deve poder também criar objetos com nome. Possuindo uma propriedade ´name´

#### 3 - Deve ser possível adicionar notas ao Student, por meio de um método chamado ´add_grade´

#### 4 - Deve ser lançada uma `Exception` quando a `grade` for menor que 0 e maior que 10 ou se o valor for uma palavra ou letra.
Para o item 4, você deve implementar o método estático `is_valid_grade` na classe Grade. O método deve ser chamado em add_grade de Student e se não for válido deve lançar uma exceção.

#### 5 - Deve ser possível calcular a média de um Student.
Para esse item, você deve implementar o método `calculate_mean` na class Grade.
# Desafio-OOP-1-Student
