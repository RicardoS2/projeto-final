# 🏗️ Projeto Final: Catálogo de Engenharia Civil

Este é um projeto de aplicação web em **Python** e **Flask** para gerenciar e
visualizar um catálogo de itens de engenharia civil. O sistema pode ser
executado tanto como uma **aplicação web** quanto como uma **aplicação desktop**
usando `pywebview`.

---

## 👩‍💻 Equipe de Desenvolvimento

- **Ricardo**: Desenvolvedor Principal 💻
- **Max e Davi**: Organizadores 📋
- **Meriely e Katherine**: Designers 🎨

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**: Base do projeto 🐍
- **Flask**: Framework web para o backend 🌐
- **Tailwind CSS**: Interface moderna e responsiva 🎨
- **pywebview**: Para a versão desktop 🖥️
- **Requests**: Para validações e comunicação 📡

---

## 📂 Estrutura do Projeto

```
projeto-final/
├─ services/              # Lógica de negócio e integrações
│  ├─ __init__.py
│  ├─ firebase.py
│  ├─ itens.py
│
├─ static/
│  ├─ uploads/
│  └─ css/
├─ templates/             # Arquivos HTML da interface
│  ├─ admin.html
│  ├─ index.html
│  └─ item.html
├─ utils/                 # Funções de utilidade
│  ├─ __pycache__/
│  ├─ __init__.py
│  └─ upload.py
├─ app.py                 # Ponto de entrada da aplicação
├─ run_desktop.py         # Para rodar como desktop app
├─ requirements.txt       # Dependências do projeto
└─ README.md              # Documentação
```

---

## 🚀 Como Executar

### **Pré-requisitos**

Certifique-se de ter **Python 3.13+** e **pip** instalados. Depois, instale as
dependências:

```bash
pip install -r requirements.txt
```

> **Nota:** `pywebview` é opcional. Se não estiver instalado, a aplicação abrirá
> no navegador.

### **Executando a Versão Web**

#### No Windows

1. Abra o **Prompt de Comando** ou **PowerShell** na pasta do projeto.
2. Execute:

```bash
python app.py
```

3. Abra seu navegador e acesse: [http://127.0.0.1:5050](http://127.0.0.1:5050)

#### No Linux / macOS

1. Abra o **Terminal** na pasta do projeto.
2. Execute:

```bash
python3 app.py
```

3. Abra seu navegador e acesse: [http://127.0.0.1:5050](http://127.0.0.1:5050)

### **Executando a Versão Desktop**

#### No Windows

1. Abra o **Prompt de Comando** ou **PowerShell** na pasta do projeto.
2. Execute:

```bash
python run_desktop.py
```

3. Uma janela nativa será aberta (se `pywebview` estiver instalado) ou a
   aplicação será iniciada no navegador.

#### No Linux / macOS

1. Abra o **Terminal** na pasta do projeto.
2. Execute:

```bash
python3 run_desktop.py
```

3. Uma janela nativa será aberta (se `pywebview` estiver instalado) ou a
   aplicação será iniciada no navegador.

---

## 💡 Observações Importantes

- A porta padrão para execução local é **5050**
- Para desenvolvimento, você pode habilitar o modo de depuração do Flask, mas
  evite fazer isso em produção

---

## 📬 Contato

Para mais informações, entre em contato com o desenvolvedor principal:

- **Ricardo**:
  [ricardo.menezes@itec.ufpa.br](mailto:ricardo.menezes@itec.ufpa.br)
