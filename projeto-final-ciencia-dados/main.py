import os
import pandas as pd
import matplotlib.pyplot as plt

OUT = "outputs"
os.makedirs(OUT, exist_ok=True)

# Leitura de CSV
csv_path = "vendas.csv"
df_csv = pd.read_csv(csv_path) if os.path.exists(csv_path) else pd.DataFrame()

# Leitura de Excel (opcional)
excel_path = "notas.xlsx"
df_xlsx = None
if os.path.exists(excel_path):
    df_xlsx = pd.read_excel(excel_path)

# Preparar e unir dados simples (exemplo)
if not df_csv.empty:
    df_csv["Quantidade"] = pd.to_numeric(df_csv["Quantidade"], errors="coerce").fillna(0).astype(int)
    df_csv["Valor"] = pd.to_numeric(df_csv["Valor"], errors="coerce").fillna(0.0)
    df_csv["Total"] = df_csv["Quantidade"] * df_csv["Valor"]

total = df_csv["Total"].sum() if not df_csv.empty else 0
top_produtos = df_csv.sort_values("Total", ascending=False).head(5) if not df_csv.empty else pd.DataFrame()

# Salvar gráfico
if not df_csv.empty:
    plt.figure(figsize=(8,4))
    plt.bar(top_produtos["Produto"], top_produtos["Total"], color="tab:green")
    plt.title("Top produtos por faturamento")
    plt.tight_layout()
    chart_path = os.path.join(OUT, "top_produtos.png")
    plt.savefig(chart_path)
else:
    chart_path = None

# Gerar relatório HTML simples
report_path = os.path.join(OUT, "relatorio.html")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("<html><head><meta charset='utf-8'><title>Relatório</title></head><body>")
    f.write("<h1>Relatório de Vendas</h1>")
    f.write(f"<p>Faturamento total: R$ {total:,.2f}</p>")
    if chart_path:
        f.write(f"<h2>Top produtos</h2><img src='{os.path.basename(chart_path)}' alt='Top produtos'/>")
    if df_xlsx is not None:
        f.write("<h2>Dados do Excel (notas)</h2>")
        f.write(df_xlsx.head().to_html(index=False))
    f.write("</body></html>")

print(f"Relatório gerado em: {report_path}")
if chart_path:
    print(f"Gráfico: {chart_path}")
