<div align="center">

<br/>

```


████████╗███████╗██╗  ██╗████████╗    ████████╗ ██████╗          ███████╗ ██████╗ ██╗     
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ╚══██╔══╝██╔═══██╗         ██╔════╝██╔═══██╗██║     
   ██║   █████╗   ╚███╔╝    ██║          ██║   ██║   ██║         ███████╗██║   ██║██║     
   ██║   ██╔══╝   ██╔██╗    ██║          ██║   ██║   ██║         ╚════██║██║▄▄ ██║██║     
   ██║   ███████╗██╔╝ ██╗   ██║          ██║   ╚██████╔╝         ███████║╚██████╔╝███████╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝          ╚══════╝ ╚══▀▀═╝ ╚══════╝
```

<h1>Text to SQL — AI-Powered Natural Language Query Engine</h1>

<p>
  <strong>Ask questions in plain English. Get SQL instantly.</strong><br/>
  No database expertise required. No syntax memorization. Just results.
</p>

<br/>

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://texttosql-q.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![AI Powered](https://img.shields.io/badge/AI%20Powered-LLM-412991?style=for-the-badge&logo=openai&logoColor=white)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live%20%26%20Active-00D4AA?style=for-the-badge)]()

<br/>

> **"What were our top 5 customers by revenue last quarter?"**
> → `SELECT customer_name, SUM(revenue) AS total_revenue FROM orders WHERE order_date >= DATE_TRUNC('quarter', CURRENT_DATE - INTERVAL '3 months') GROUP BY customer_name ORDER BY total_revenue DESC LIMIT 5;`

<br/>

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Usage Examples](#-usage-examples)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Author](#-author)

---

## 🧠 Overview

**Text to SQL** is an AI-powered web application that translates natural language questions into accurate, executable SQL queries. Built for analysts, developers, and business users who need database insights without writing SQL by hand.

The system understands schema context, handles complex multi-table joins, aggregations, filters, and ordering — all from a simple English prompt. Powered by a large language model and deployed on Streamlit Cloud for instant, zero-install access.

```
User Input (English)  →  LLM + Schema Context  →  SQL Query  →  Results
```

---

## 🚀 Live Demo

> **Try it now — no setup required:**

<div align="center">

### 👉 [texttosql-q.streamlit.app](https://texttosql-q.streamlit.app/)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🗣️ **Natural Language Input** | Type questions exactly as you'd ask a colleague |
| ⚡ **Instant SQL Generation** | LLM converts your question to accurate SQL in seconds |
| 🧩 **Schema-Aware** | Understands your table structure, columns, and relationships |
| 🔗 **Complex Query Support** | JOINs, GROUP BY, subqueries, window functions, and more |
| 📋 **Copy-Ready Output** | One-click SQL copy for use in any database tool |
| 🎨 **Syntax Highlighting** | Clean, readable SQL with color-coded formatting |
| 🔒 **Secure API Handling** | Environment-based key management — no credentials exposed |
| ☁️ **Zero Install** | Fully deployed on Streamlit Cloud — works in your browser |

---

## ⚙️ How It Works

```
┌─────────────────────────────────────────────────────────┐
│                     TEXT TO SQL PIPELINE                 │
│                                                         │
│  ┌──────────┐    ┌───────────────┐    ┌──────────────┐  │
│  │  User    │───▶│  Schema       │───▶│    LLM       │  │
│  │  Input   │    │  Context      │    │  (Prompt     │  │
│  │ (English)│    │  Injection    │    │   Engine)    │  │
│  └──────────┘    └───────────────┘    └──────┬───────┘  │
│                                              │           │
│  ┌──────────────────────────────────────────▼────────┐  │
│  │              Generated SQL Query                  │  │
│  │   SELECT, JOIN, GROUP BY, WHERE, ORDER BY ...     │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

**Step-by-step:**

1. **User enters** a plain English question about their data
2. **Schema context** (table names, columns, types) is injected into the prompt
3. **LLM processes** the combined input using carefully engineered prompts
4. **SQL is generated**, validated, and displayed with syntax highlighting
5. **User copies** the query and runs it in their database tool

---

## 🛠️ Tech Stack

```
┌─────────────────────────────────────┐
│           TECHNOLOGY STACK          │
├─────────────────┬───────────────────┤
│  Frontend       │  Streamlit        │
│  Language       │  Python 3.10+     │
│  AI Engine      │  LLM via API      │
│  Prompt Design  │  Custom Templates │
│  Deployment     │  Streamlit Cloud  │
│  Config         │  st.secrets / ENV │
└─────────────────┴───────────────────┘
```

| Layer | Technology |
|---|---|
| **UI Framework** | [Streamlit](https://streamlit.io) |
| **Language** | Python 3.10+ |
| **AI / LLM** | Large Language Model API |
| **Prompt Engineering** | Custom schema-aware templates |
| **Deployment** | Streamlit Cloud |
| **Security** | Environment-based API key management |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- An LLM API key (e.g., OpenAI, Gemini, or Anthropic)
- `pip` package manager

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/vicky-kumar-singh/text-to-sql.git
cd text-to-sql
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure your API key**

Create a `.streamlit/secrets.toml` file:
```toml
# .streamlit/secrets.toml
API_KEY = "your_api_key_here"
```

Or set as an environment variable:
```bash
export API_KEY="your_api_key_here"
```

**5. Run the application**
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 💡 Usage Examples

### Simple Query
```
Input:  "Show me all customers from Mumbai"

Output: SELECT * FROM customers
        WHERE city = 'Mumbai';
```

### Aggregation
```
Input:  "What is the total sales amount for each product category?"

Output: SELECT category, SUM(amount) AS total_sales
        FROM sales
        JOIN products ON sales.product_id = products.id
        GROUP BY category
        ORDER BY total_sales DESC;
```

### Date Filtering
```
Input:  "List all orders placed in the last 30 days with amount > 1000"

Output: SELECT order_id, customer_id, amount, order_date
        FROM orders
        WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
          AND amount > 1000
        ORDER BY order_date DESC;
```

### Multi-table JOIN
```
Input:  "Find the top 3 employees by total sales with their department names"

Output: SELECT e.name, d.department_name, SUM(s.amount) AS total_sales
        FROM employees e
        JOIN departments d ON e.dept_id = d.id
        JOIN sales s ON s.employee_id = e.id
        GROUP BY e.name, d.department_name
        ORDER BY total_sales DESC
        LIMIT 3;
```

---

## 📁 Project Structure

```
text-to-sql/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── .streamlit/
│   ├── config.toml         # Streamlit UI configuration
│   └── secrets.toml        # API keys (not committed to Git)
│
├── utils/
│   ├── prompt_builder.py   # Schema-aware prompt engineering
│   ├── llm_client.py       # LLM API integration & response handling
│   └── sql_formatter.py    # SQL output formatting & validation
│
└── assets/
    └── schema_examples/    # Sample database schemas for testing
```

---

## ⚙️ Configuration

| Variable | Description | Required |
|---|---|---|
| `API_KEY` | Your LLM provider API key | ✅ Yes |
| `MODEL_NAME` | LLM model to use (e.g., `gpt-4`) | Optional |
| `MAX_TOKENS` | Max tokens for response | Optional |
| `TEMPERATURE` | Response creativity (0–1) | Optional |

Configure via `.streamlit/secrets.toml` for local development, or through **Streamlit Cloud Secrets** for deployment.

---

## 📸 Screenshots

| Natural Language Input | Generated SQL Output |
|---|---|
| Type your question in plain English | Clean, syntax-highlighted SQL |

> **[Try the live demo](https://texttosql-q.streamlit.app/)** to see it in action!

---

## 🗺️ Roadmap

- [x] Natural language to SQL generation
- [x] Schema-aware prompt engineering
- [x] Streamlit Cloud deployment
- [x] Secure API key management
- [ ] Upload custom database schema (CSV / JSON)
- [ ] Multi-dialect support (MySQL, PostgreSQL, SQLite, BigQuery)
- [ ] Query explanation mode ("explain this SQL")
- [ ] Query history & session memory
- [ ] Direct database connection & live query execution
- [ ] Export results as CSV / Excel

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

**Vicky Kumar Singh**

*Full Stack Developer · M.Sc. Data Science · GITAM University, Hyderabad*

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vicky-kumar-singh)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/vicky-kumar-singh)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](https://your-portfolio.com)

<br/>

> *"The best interface is the one you already know how to use — your own words."*

</div>

---

<div align="center">

⭐ **If this project helped you, please give it a star!** ⭐

Made with ❤️ by Vicky Kumar Singh

</div>
