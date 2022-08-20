# O que eu fiz para rodar esse role no docker

Antes de mais nada, é necessário [instalar o Docker](https://docs.docker.com/get-docker/) na sua máquina.

Basicamente, escrevi o arquivinho *test.py* que imprime em tela umas informações da máquina que está executando o script. Ele identifica caso esteja rodando em Mac ou outro OS.

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
    print("Não to mais executando no Mac.")
    
print("\n")
```

Então, escrevi o *Dockerfile* (que não tem nenhuma extensão do arquivo mesmo):

```Dockerfile
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /my-tests
COPY . .
CMD ["python3", "test.py"]
```

Descrevendo esse arquivo linha por linha:
1. Configuro a syntax de escrita do arquivo;
2. Escolho a imagem que irá executar o código, que aqui é uma imagem padrão de python 3.8;
3. Defino a pasta de execução na imagem;
4. Copio os arquivos da minha máquina para a imagem;
5. Executo o código.

Até aí beleza. Agora eu preciso fazer o build do dockerfile em uma imagem, e em seguida executar a imagem (run) em um container.

Para fazer isso, eu tive certeza que meu terminal estava no diretório raiz do projeto (/my-test) e executei o comando com a flag de tag para nomear a imagem:

```shell
% docker build --tag my-test .
```

Esse comando cria uma imagem nomeada **my-test** com as configurações necessárias para a execução do meu código. No fim, o que essa imagem vai fazer é executar os comandos que eu escrevi no Dockerfile.

Para executar o código dentro de um container, eu executei no terminal:

```shell
% docker run my-test
```

E foi isso. Tive o seguinte output:

```
% docker run my-test

Qual o sistema operacional??

O nome do OS é posix...
e a plataforma é Linux
sendo que a release é 5.10.104-linuxkit

Logo...

Não estou mais executando no Mac.
```

É isso! Para mais infos, [link para o tutorial](https://docs.docker.com/language/python/build-images/)


Mas e agora? Será que o container ainda tá executando mesmo depois de finalizar a execução o meu código python? Podemos ver todos os containers com:

```shell
% docker ps -a
```

Uma vez que está com o STATUS "Exited", o container não está mais executando.

Agora fica o questionamento, o que qcontece se eu atualizar meu código python e só der `docker run my-test`? Para testar isso, troquei a linha 17 do meu código por:

```python
print("Será que ele roda com o arquivo mais novo?")
```

Vou rodar `docker run my-test`:

```
% docker run my-test


Qual o sistema operacional??

O nome do OS é posix...
e a plataforma é Linux
sendo que a release é 5.10.104-linuxkit

Logo...

Não estou mais executando no Mac.
```

Não atualizou. Nesse caso, somente dá certo quando eu dei build e run novamente:

```shell
% docker build --tag my-test .
% docker run my-test
```

Et voilà! Tudo atualizado.