<p align="center">
<img src="img/liber.png"/>
</p>

<h2 align="center">pre-commit-hooks</h2> 

Bibliotecas de hooks para a validação e padronização dos projetos.
São bibliotecas personalisadas que são usados em conjuto com [pre-commit](https://pre-commit.com/)


### Dependências:

 - Python 3 
 - PIP

### Buiild

O projeto contem um MakeFile que pode ser usado para configurar o projeto.
usando o comando:
```
make build 
 ```
Será criado um virtualenv na pasta chamada  **_venv_** e instalado todas as dependências contidas em
[requirements.txt](requirements.txt)


### Hooks
#### prepare-commit-msg
Esse hook será executando no git stage [pre_merge_commit](https://git-scm.com/docs/githooks#_pre_merge_commit) e fará
a validação das mensagens quando trigado pelo comando **_git commit_**.

Para instalar  é preciso adicionar o comando _**-t prepare-commit-msg**_ ao executar o comando **_pre-commit install_**

**Padrão de mensagem**
 
    <code-type>(<jira-code>): Mensage do commit
 

|code     |                                                                                                               |
|---------|---------------------------------------------------------------------------------------------------------------|
| **feat**    | Cria um novo recurso no código.                                                                               |
| **fix**     | Corrige um bug no código.                                                                                     |
| **refactor** | Uma alteração que não corrige um bug, nem adiciona um novo recurso.                                           |
| **perf**    | Mudança de Código que melhora performance.                                                                    |
| **test**    | Adicionando testes ausentes ou corrigindo testes existentes.                                                  |
| **chore**   | Outras alterações que não modificam os arquivos src ou de teste                                               |
| **docs**    | Apenas a documentação.                                                                                        |
| **style**   | Mudanças que não afetam o significado do código (espaço em branco, formatação falta de ponto-e-vírgula, etc). |
| **build**   | Alterações que afetam o sistema de compilação ou dependências externas (npm, gulp, broccoli).                 |
| **ci**      | Alterações em nossos arquivos e scripts de configuração de CI (Travis, Circle, github actions).               |


#### prepare-commit-msg
Esse hook será executando no git stage [pre_push](https://git-scm.com/docs/githooks#_pre_push) e fará
a validação da branch ao executar o comando **_git push_**.


Para instalar  é preciso adicionar o comando _**-t pre-push**_ ao executar o comando **_pre-commit install_**


Branch naming:

**Release:**

    release/(versão)
    release/v1.0.1


**Feature**: _É para adicionar, refatorar ou remover um recurso._


    feature/(jira)-titulo
    feature/RSS-13-novo-campo

**Task**: _É para resolver questões que não é ligado a um recurso ou um bug_

    task/(jira)-titulo
    task/RSS-16-add-lib

**Hotfix**: _É para corrigir o código com uma solução sem seguir o processo normal_   
  
    hotfix/(jira)-titulo
    hotfix/RSS-13-corrigir-campo

**BugFix**: _É para corrigir um bug_

    bugfix/(jira)-titulo
    bugfix/RSS-13-corrigir-campo

**Test**: _É para experimentar algo fora de uma issue/ticket._

    test/nome-do-teste
