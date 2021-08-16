# django-rest-api
Django Rest Framework
Roteiro de Teste – Desenvolvedor Backend
- Banco de Dados: Postgresql
- Linguagem de programação: Python 3.x, Django 3.0, Django Rest Framework 3.11
Observação: Leia todos os scripts / passos desse documento antes de iniciar. 

Observações: Considerar o campo ID da tabela Person como Inteiro Longo, se necessário
corrigir na estrutura exibida acima.

1. Definição dos Modelos

2. Criação de EndPoint para cada tabela no padrão REST FULL.
a. Necessário validação do campo CPF (se é um CPF válido)

3. Para execução do cadastro de foto da pessoa “Person_media”, carregar um arquivo .jpg
que pode estar em qualquer diretório do se computador, o arquivo deve ter até 256kb
de tamanho.
a. O campo “object_media” deve ser populado com conversão do arquivo.jpg para
base64.

4. A alimentação da tabela person_audit será realizada trigger no banco de dados com as
seguintes regras de execução:
a. Ao adicionar um cadastro de pessoa, inserir os dados menos o campo cpf_old
b. Ao editar o cadastro, monitorar se teve alteração de valor no campo CPF, se tiver
alteração incluir na tabela o valor novo e antigo do CPF. 
