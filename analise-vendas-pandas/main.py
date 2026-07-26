import os
import pandas as pd
import matplotlib.pyplot as plt

OUT = "outputs"
os.makedirs(OUT, exist_ok=True)

df = pd.read_csv("vendas.csv")
# Garantir tipos
df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0)

print("Dados:")
print(df)
print("\nResumo estatístico:")
print(df.describe(include="all"))

total_faturamento = (df["Quantidade"] * df["Valor"]).sum()
print(f"\nFaturamento total: R$ {total_faturamento:,.2f}")

# KPIs por produto
kpis = df.copy()
kpis["Total"] = kpis["Quantidade"] * kpis["Valor"]
kpis = kpis.sort_values("Total", ascending=False)
print("\nKPIs por produto:")
print(kpis[["Produto", "Quantidade", "Valor", "Total"]])

# Gráfico: faturamento por produto
plt.figure(figsize=(8,5))
plt.bar(kpis["Produto"], kpis["Total"], color="tab:blue")
plt.title("Faturamento por Produto")
plt.ylabel("R$")
plt.xlabel("Produto")
plt.tight_layout()
chart_path = os.path.join(OUT, "faturamento_por_produto.png")
plt.savefig(chart_path)
print(f"\nGráfico salvo em: {chart_path}")
# plt.show()  # opcional em ambiente local
