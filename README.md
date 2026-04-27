# Google Cloud Tech Conference 2026

Este é um site informativo para uma conferência técnica de um dia sobre o Google Cloud. O projeto exibe a programação do evento (8 palestras e 1 almoço), detalhes de cada palestra (título, descrição, horário, categoria e palestrantes) e possibilita a busca em tempo real.

O projeto utiliza **Flask** (Python) no backend para fornecer os dados das palestras e renderizar o template principal, e **HTML, CSS e JS puros** no frontend para construir a interface.

## Estrutura do Projeto

- `app.py`: O servidor Flask e os dados fictícios da programação.
- `requirements.txt`: Dependências do Python.
- `templates/index.html`: A marcação e o layout da página principal.
- `static/style.css`: Estilização moderna e avançada com design "Glassmorphism".
- `static/main.js`: Lógica do relógio em tempo real e de busca por categoria, palestrante e título.

## Configuração e Execução

### Pré-requisitos
- Python 3.8+ instalado.

### Passos
1. **Clone o repositório** (ou acesse a pasta raiz do projeto).
2. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```
3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Execute o servidor Flask**:
   ```bash
   python app.py
   # ou
   flask run
   ```
5. **Acesse o site** no seu navegador em: `http://127.0.0.1:5000`

## Funcionalidades e Modificações Adicionais

- **Adicionar/Editar Palestras**: Abra `app.py` e edite a lista `schedule`. Cada item no dicionário representa uma palestra. Certifique-se de vincular um palestrante da lista `speakers`.
- **Modificar Design**: O estilo visual está todo definido no arquivo `static/style.css`. As variáveis principais de cor estão declaradas em `:root`. Para alterar a cor principal, mude o valor de `--primary-color`.
- **Filtros Personalizados**: Se quiser adicionar um novo filtro (por exemplo, duração), adicione um novo campo no `index.html` e integre a lógica na função `filterSchedule()` dentro de `static/main.js`.