# O que eu fiz para rodar esse role no docker

```md
Antes de mais nada, é necessário [instalar o Docker](https://docs.docker.com/get-docker/) na sua máquina.
```

Basicamente, escrevi o arquivinho *test.py* que printa umas informações da máquina que está executando o script. Ele identifica caso esteja rodando em Mac ou outro OS.

```python
"""
Teste de execução do código dentro de um container docker.
"""

import os
import platform

print("\nQual o sistema operacional??\n")
print(f"O nome do OS é {os.name}...")
print(f"e a plataforma é {platform.system()}")
print(f"sendo que a release é {platform.release()}\n")
print("Logo...\n")


if platform.system() == 'Darwin':
    print("To rodando no Mac")
else:
    print("Não estou mais executando no Mac.")
    
print("\n")
```

Então, escrevi o *Dockerfile* (que não tem nenhuma extensão do arquivo msm):

```Dockerfile
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /my-tests
COPY . .
CMD ["python3", "test.py"]
```

Descrevendo esse arquivo linha por linha:
1. Seto a syntax de escrita do arquivo;
2. Escolho a imagem que irá executar o código, que aqui é uma imagem padrão de python 3.8 (não sei mais mts infos);
3. Defino a pasta de execução na imagem;
4. Copio os arquivos da minha máquina para a imagem;
5. Executo o código.

Até aí beleza. Agora eu preciso fazer o build do dockerfile em uma imagem, e em seguida executar a imagem (run) em um container.

Para fazer isso, eu tive certeza que estava no diretório raiz e executei o comando com a flag de tag para nomear a imagem:

```shell
docker build --tag my-test .
```

Esse comando cria uma imagem nomeada **my-test** com as configurações necessárias para a execução do meu código. No fim, o que essa imagem vai fazer é executar os comandos que eu escrevi no Dockerfile.

Para executar o código dentro de um container, eu executei no terminal:

```shell
docker run my-test
```

E fim. Tive o seguinte output:

```
rafaelapinter@Air-de-Rafaela my-test % docker run my-test

hmmmm, qual será o sistema operacional??

bom, o nome do os é posix...
e a plataforma é Linux
sendo que a release é 5.10.104-linuxkit

Não estou mais executando no Mac.
```

É isso! Para mais infos, [link para o tutorial](https://docs.docker.com/language/python/build-images/)


Tá, mas e agora? Será que o container ainda tá executando mesmo depois de acabar o meu código? Achei o seguinte código para rodar:

```shell
docker ps -a
```

Hmm, parece que não mais, uma vez que está com o STATUS "Exited".

Será que se eu atualizar meu código python e só der run? Troquei a última linha 17 do meu código por:

```python
print("será que ele roda com o arquivo mais novo?")
```

Vou rodar `docker run my-test`:

```
rafaelapinter@Air-de-Rafaela my-test % docker run my-test

hmmmm, qual será o sistema operacional??

bom, o nome do os é posix...
e a plataforma é Linux
sendo que a release é 5.10.104-linuxkit

to no mac não irmão
```

Ihh, não atualizou. Como fazer para atualizar minha imagem? Vou tentar dar build de novo e run. Aparentemente eu preciso remover o container antigo para poder criar um novo. Para isso, preciso rodar o `docker ps -a` e pegar ID do container. Com isso, dá para executar a sua remoção com:

`docker rm -f <container-id>`

Aparentemente, agora já daria para dar um `docker run my-test` de novo e teria o código novo... mas não deu.

Somente deu certo quando eu dei build e run novamente:

```shell
docker build --tag my-test .
docker run my-test
```

Et voilà! Tudo atualizado. 

Bom, acho que é isso para esse primeiro passo. Bons aprendizados hoje!