#!/bin/bash

# Diretório base do projeto
PROJECT_DIR="gmn"

# Criar microsserviços
mkdir -p "$PROJECT_DIR/core/app/{domain,infrastructure,resources,services}"
mkdir -p "$PROJECT_DIR/demandas/app/{domain,infrastructure,resources,services}"
mkdir -p "$PROJECT_DIR/agenda_estrategica/app/{domain,infrastructure,resources,services}"

# Criar subpastas dentro de cada microsserviço (mantém as existentes e adiciona 'tests')
for MICROSERVICE in core demandas agenda_estrategica; do
    mkdir -p "$PROJECT_DIR/$MICROSERVICE/app/domain/{schemas,models,repositories,use_cases,validations}"
    mkdir -p "$PROJECT_DIR/$MICROSERVICE/app/infrastructure/{adapters,drivers,constants,monitoring_layer,open_api,logs}"
    mkdir -p "$PROJECT_DIR/$MICROSERVICE/app/resources/routers"
    mkdir -p "$PROJECT_DIR/$MICROSERVICE/app/services"
    mkdir -p "$PROJECT_DIR/$MICROSERVICE/app/tests/{domain,infrastructure,resources}" # Adiciona pasta de testes
done

# Criar arquivos básicos em cada microsserviço (mantém os existentes)
for MICROSERVICE in core demandas agenda_estrategica; do
    touch "$PROJECT_DIR/$MICROSERVICE/app/main.py"
    touch "$PROJECT_DIR/$MICROSERVICE/app/config.py"
    touch "$PROJECT_DIR/$MICROSERVICE/app/domain/__init__.py"
    touch "$PROJECT_DIR/$MICROSERVICE/app/infrastructure/__init__.py"
    touch "$PROJECT_DIR/$MICROSERVICE/app/resources/__init__.py"
    touch "$PROJECT_DIR/$MICROSERVICE/app/services/__init__.py"
done

# Criar pasta para o frontend React (considerando o build multi-estágio)
mkdir -p "$PROJECT_DIR/frontend"

# Criar pasta para volumes (conforme docker-compose.yml)
mkdir -p "$PROJECT_DIR/volumes/{elasticsearch,rabbitmq,redis}"

echo "Estrutura do projeto criada com sucesso!"