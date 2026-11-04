# 🤖 Python Web Automation & RPA: Product Registration Assistant

[PT] Robô de Automação de Processos (RPA) desenvolvido em Python para preenchimento e cadastro automatizado de listas de produtos em sistemas web a partir de uma base de dados estruturada.
[EN] Robotic Process Automation (RPA) bot built in Python to automatically fill out and register product lists on web systems from a structured database.

---

## 🇧🇷 Português

### 📌 Visão Geral do Projeto
Este projeto simula uma rotina corporativa real de cadastro em massa de mercadorias. A aplicação lê uma base de dados (`produtos.csv`) utilizando **Pandas**, mapeia as informações linha por linha e utiliza **PyAutoGUI** para controlar o navegador, realizar cliques, preencher formulários de forma automatizada e tratar exceções de campos opcionais.

### 🚀 Funcionalidades & Lógica de Automação
- **Mapeamento Lógico de Processos:** Organização sequencial das etapas manuais de navegação convertidas em código de automação.
- **Integração Dados + Interface (RPA):** Leitura dinâmica de arquivos CSV combinada com digitação simulada em tela.
- **Tratamento de Dados Vazios:** Validação condicional para verificar campos opcionais (`obs`) antes de efetuar o preenchimento.
- **Laço de Repetição Automatizado:** Varredura completa da tabela (`tabela.index`) para garantir o cadastro sequencial de todos os itens.

### 🛠️ Stack Tecnológica
- **Linguagem:** Python 3.10+
- **Manipulação de Dados:** `pandas`
- **Automação de Interface (RPA):** `pyautogui`
- **Controle de Tempo:** `time`

---

## 🇺🇸 English

### 📌 Project Overview
This project simulates a real-world enterprise routine for bulk product registration. The application reads a dataset (`produtos.csv`) using **Pandas**, maps the information row by row, and leverages **PyAutoGUI** to control the browser, click elements, fill out web forms automatically, and handle optional field conditions.

### 🚀 Features & Automation Logic
- **Process Logic Mapping:** Sequential breakdown of manual browser navigation steps converted into automation code.
- **Data + UI Integration (RPA):** Dynamic CSV data reading combined with simulated desktop keyboard and mouse inputs.
- **Missing Data Handling:** Conditional validation to check optional fields (`obs`) before data entry.
- **Automated Looping:** Full iteration over the dataset index (`tabela.index`) to ensure seamless sequential registration of all items.

### 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Data Manipulation:** `pandas`
- **GUI Automation (RPA):** `pyautogui`
- **Time Control:** `time`

---

## 📁 Como Executar / How to Run

1. **Clone o repositório / Clone the repo:**
   ```bash
   git clone [https://github.com/nwor1958/python-web-automation-rpa.git](https://github.com/nwor1958/python-web-automation-rpa.git)
   cd python-web-automation-rpa
