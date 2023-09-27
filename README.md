# Banco de Usuários

Este projeto é referente a disciplina **Teste Unitários** do curso de pós graduação **Testes Ágeis** do **Cesar School**.

### Escopo:

#### 1 - Desenvolver o método add_user
- Verificar se os parametros é Str e diferente de None;
- Verificar se o nome não existe para adicionar;
#### 2 - Desenvolver o metodo remove_user
-  Verificar se os parametros é Str e diferente de None;
-  Verificar se o nome já existe para remover;
#### 3 - Desenvolver o método update_user
- Verificar se os parametros é Str e diferente de None;
- Verificar se o nome já existe para atualizar;
#### 4 - Desenvolver o método get_user_by_name
- Verificar se os parametros é Str e diferente de None;
- Verificar se o nome já existe para recuperar;
####5 – Desenvolver testes unitarios


### Folder strtures:

    .
    │ 
    ├── src                     # It includes all source code related the project
    │   ├── controller          # It includes all classes responsible for handling the application control logic          
    │   └── models              # It includes all data representations and business logic related to application objects or entities
    │   └── service             # It includes all classes that encapsulate the application's business logic
    │ 
    └── tests                   # It includes all test-related source code for the project
    │   ├── controller          # Includes all tests for controller classes
    │   └── models              # Includes all tests for models classes
    │   └── service             # Includes all tests for service classes