# IGTI - MBA em Engenharia de Dados
## Bootcamp - Engenheiro de dados Cloud
### Módulo 4 - DDE Desenho de arquiteturas de dados escaláveis

### Trabalho prático

| Arquivo | Descrição |
| - | - |
| carga-CadOp.ipynb | Jupyter Notebook utilizado para testes do código |
| carga-CadOp.py | aplicação de exemplo, em Python/pandas que efetua o download do cadastro de planos de saúde, filtra os registros do estado "PE" e lista na saúda padrão | 
| Dockerfile | Cria o container, efetuando a importação das libs Python (PIP) e copiando o arquivo do código executável |
| requirements.txt | arquivo contendo as libs python que serão importadas com o PIP no Dockerfile |
| .github/workflows/build.yml | configuração de workflow do github, para efetuar o build do dockerfile e enviar a imagem para o registry do GCP gcr.io/edc-bootcamp-325711/edc-m4-tp:latest |
| job.yml | yml para criacão de um JOB em kubernetes |


## Execução em Docker
```bash
docker run --rm gcr.io/edc-bootcamp-325711/edc-m4-tp:latest
```

## Execução em Kubernetes
```bash
kubectl apply -f job.yml
```

obter o nome do job com 
```bash
kubectl describe job carga-cadop
```

obter o log da execução
```bash
kubectl logs {nome do job obtido no passo anterior}
```

#### Referências
- Material de referência do bootcamp IGTI
- https://github.com/marketplace/actions/push-to-gcr-github-action
- https://pandas.pydata.org/docs/reference/index.html
