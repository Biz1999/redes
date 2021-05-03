<img src="images/icon.png" align="right" width="100" height="150" />

# PROJETO 1 - SERVER EM PYTHON SEM BIBLIOTECAS

Projeto desenvolvido na matéria de Tópicos Avançados de Redes de Computadores com o intuito de implementar um servidor HTTP/1.1, capaz de interpretar alguns comandos ( GET, POST, PUT e DELETE).

### Integrantes

ISLAN SILVA FIGUEREDO       &emsp;&emsp;&emsp;&emsp;&emsp;                          RA: 22.119.027-5 <br />
LUCAS DA SILVA OLIVEIRA     &emsp;&emsp;&emsp;&emsp;&nbsp;                          RA: 22.119.031-7 <br />
ALESSANDRO BIZ              &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;        RA: 22.119.038-2 <br />
IVAN SANCHEZ TUZITA         &emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;        RA: 22.119.040-8 <br />

## Início
Primeira coisa ao baixar o arquivo é iniciar do diretório Projeto1 o arquivo <b>main.py</b>

```bash
python main.py
```


## GET

Todas as requisições de páginas e arquivos( css e json ) são realizadas no GET, então quando iniciado no navegador <b>'localhost:8081/'</b> no terminal é possível ver as solicitações:

<img src="images/GET.gif" height="400" />

## POST

Todas as requisições para criação dos recursos passam pelo POST, optamos por utilizar uri na imagem para não tratar a imagem no GET (Obs: ficar atento se a uri tem a extensão de imagem, pois sem ela o servidor não consegue exibir a mesma) <br />  
Ex: https://www.petlove.com.br/dicas/wp-content/uploads/2018/05/golden-idoso.jpg

Ao clicar em profile uma nova requisição GET é solicitada, será possível ver a página do usuário referente aquele nome

<img src="images/POST.GIF" height="400" />

## PUT

Todas as requisições para atualização do PUT, ao selecionar o ID o mesmo será atualizado (nome, sobrenome, img), ficar atento a imagem novamente

<img src="images/PUT.GIF" height="400" />

## DELETE

Todas as requisições para remover algum conteúdo passam ao DELETE, ao selecionar o ID o mesmo será deletado junto ao seu profile

<img src="images/DELETE.GIF" height="400" />

