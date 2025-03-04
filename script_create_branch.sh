#!/bin/bash

for repo in \
    git@github.com:EdgarLira25/Introducao-a-Programacao.git \
    git@github.com:EdgarLira25/Sistemas-Operacionais.git \
    git@github.com:EdgarLira25/gRpc-cliente-servidor.git \
    git@github.com:EdgarLira25/java-rmi-cliente-servidor.git \
    git@github.com:EdgarLira25/DB-mysql-interface.git \
    git@github.com:EdgarLira25/COO-exercicios.git \
    git@github.com:EdgarLira25/Jogo-Pacman.git \
    git@github.com:EdgarLira25/mergeSort-Cormen.git \
    git@github.com:EdgarLira25/IA-Multilayer-Perceptron.git \
    git@github.com:EdgarLira25/IA-convolutional-neural-network.git \
    git@github.com:EdgarLira25/IA-and-or-xor.git \
    git@github.com:EdgarLira25/EstruturaDeDados.git \
    git@github.com:EdgarLira25/criptografias-classicas.git \
    git@github.com:EdgarLira25/EP-Seg-informacao.git \
    git@github.com:EdgarLira25/flask_api_template.git \
    git@github.com:EdgarLira25/react_sql_template.git \
    git@github.com:EdgarLira25/ARQ_MIPS.git 
do
    repo_name=$(basename -s .git $repo)  # Nome do repositório
    git remote add $repo_name $repo
    git fetch $repo_name

    # Criar um branch temporário para o repositório
    git checkout -b temp-$repo_name $repo_name/main

    # Criar pasta e mover o conteúdo sem perder o histórico
    mkdir -p $repo_name
    mv * $repo_name/ 2>/dev/null || true

    git add .
    git commit -m "Movendo arquivos de $repo_name para a pasta correspondente"
    git checkout main
done
