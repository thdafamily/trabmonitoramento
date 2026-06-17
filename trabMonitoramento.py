# ============================================================
#  SISTEMA DE MONITORAMENTO VIP - LPI
#  Disciplina: Laboratório de Programação I
#  Prof. Me. Renata Cristina Laranja Leite
#  Estruturas: 2 Vetores + 2 Matrizes (3x4)
# ============================================================

# ──────────────────────────────────────────────
#  VETOR 1 – Alunos (linhas da matriz)
# ──────────────────────────────────────────────
alunos = ['Thiago', 'Guilherme', 'Fábio']

# ──────────────────────────────────────────────
#  VETOR 2 – Meses (colunas da matriz)
# ──────────────────────────────────────────────
meses = ['Mês 1', 'Mês 2', 'Mês 3', 'Mês 4']

# ──────────────────────────────────────────────
#  MATRIZ 1 – Percentual de Gordura (3x4)
#  Inicializada com 0.0
# ──────────────────────────────────────────────
matriz_gordura = [
    [0.0, 0.0, 0.0, 0.0],   # linha 0 – Thiago
    [0.0, 0.0, 0.0, 0.0],   # linha 1 – Guilherme
    [0.0, 0.0, 0.0, 0.0],   # linha 2 – Fábio
]

# ──────────────────────────────────────────────
#  MATRIZ 2 – Frequência de Treinos (3x4)
#  Inicializada com 0
# ──────────────────────────────────────────────
matriz_treinos = [
    [0, 0, 0, 0],   # linha 0 – Thiago
    [0, 0, 0, 0],   # linha 1 – Guilherme
    [0, 0, 0, 0],   # linha 2 – Fábio
]

NUM_ALUNOS = len(alunos)   # 3
NUM_MESES  = len(meses)    # 4


# ══════════════════════════════════════════════
#  FUNÇÕES AUXILIARES
# ══════════════════════════════════════════════

def linha():
    print("-" * 56)

def ler_float(mensagem, minimo=0.0, maximo=None):
    """Lê um float validado dentro do intervalo [minimo, maximo]."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor < minimo:
                print(f"  ✗ Valor inválido! Deve ser >= {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ✗ Valor inválido! Deve ser <= {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ✗ Digite um número válido.")

def ler_inteiro(mensagem, minimo=0, maximo=None):
    """Lê um int validado dentro do intervalo [minimo, maximo]."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"  ✗ Valor inválido! Deve ser >= {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ✗ Valor inválido! Deve ser <= {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ✗ Digite um número inteiro válido.")


# ══════════════════════════════════════════════
#  OPÇÃO 1 – CADASTRAR AVALIAÇÕES E FREQUÊNCIA
# ══════════════════════════════════════════════

def cadastrar_avaliacoes():
    print("\n>> Opção 1: Módulo de Cadastro...")
    linha()

    # Percorre todos os alunos (linhas do Vetor 1)
    for i in range(NUM_ALUNOS):
        # Percorre todos os meses (colunas do Vetor 2)
        for j in range(NUM_MESES):
            print(f"\n  Aluno: {alunos[i]}  |  {meses[j]}")
            print(f"  (Matriz[{i}][{j}])")

            matriz_gordura[i][j] = ler_float(
                "  Percentual de gordura (0.0 a 100.0): ",
                minimo=0.0,
                maximo=100.0
            )

            matriz_treinos[i][j] = ler_inteiro(
                "  Quantidade de treinos  (0 a 31)    : ",
                minimo=0,
                maximo=31
            )

    print("\n  ✓ Todos os dados cadastrados com sucesso!")


# ══════════════════════════════════════════════
#  OPÇÃO 2 – LISTAR RELATÓRIO DE EVOLUÇÃO
# ══════════════════════════════════════════════

def listar_relatorio():
    print("\n>> Opção 2: Gerando Relatório...")
    linha()

    COL = 9   # largura de cada coluna de mês

    # Cabeçalho de colunas usando o Vetor 2 (meses)
    cabecalho_col = f"  {'Aluno':<12}" + "".join(f"{m:>{COL}}" for m in meses)

    # ── MATRIZ 1 — Percentual de Gordura ──
    print("\n  MATRIZ 1 — Percentual de Gordura Corporal (%)")
    print(cabecalho_col)
    linha()

    for i in range(NUM_ALUNOS):               # percorre linhas (alunos)
        linha_str = f"  {alunos[i]:<12}"      # nome via Vetor 1
        for j in range(NUM_MESES):            # percorre colunas (meses)
            valor = matriz_gordura[i][j]
            celula = f"{valor:.1f}%"
            linha_str += f"{celula:>{COL}}"
        print(linha_str)

    # ── MATRIZ 2 — Frequência de Treinos ──
    print("\n  MATRIZ 2 — Frequência de Treinos (sessões)")
    print(cabecalho_col)
    linha()

    for i in range(NUM_ALUNOS):               # percorre linhas (alunos)
        linha_str = f"  {alunos[i]:<12}"      # nome via Vetor 1
        for j in range(NUM_MESES):            # percorre colunas (meses)
            valor = matriz_treinos[i][j]
            linha_str += f"{str(valor):>{COL}}"
        print(linha_str)

    print()


# ══════════════════════════════════════════════
#  OPÇÃO 3 – ATUALIZAR DADOS (a implementar)
# ══════════════════════════════════════════════

def atualizar_dados():
    print("\n>> Opção 3: Atualização de Dados...")
    linha()
    pass


# ══════════════════════════════════════════════
#  OPÇÃO 4 – PESQUISA COM FILTRO (a implementar)
# ══════════════════════════════════════════════

def pesquisa_filtro():
    print("\n>> Opção 4: Pesquisa Gerencial...")
    linha()
    pass


# ══════════════════════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════════════════════

print("========================================")
print("  SISTEMA DE MONITORAMENTO VIP - LPI  ")
print("========================================")
print("Integrantes: Thiago, Guilherme, Fábio")
print("----------------------------------------\n")

while True:
    print("\n--- MENU DE OPÇÕES ---")
    print("1. Cadastrar Avaliações e Frequência")
    print("2. Listar Relatório de Evolução")
    print("3. Atualizar Dados de Monitoramento")
    print("4. Pesquisa com Filtro")
    print("5. Sair do Programa")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_avaliacoes()

    elif opcao == '2':
        listar_relatorio()

    elif opcao == '3':
        atualizar_dados()

    elif opcao == '4':
        pesquisa_filtro()

    elif opcao == '5':
        print("\nEncerrando o sistema...")
        break

    else:
        print("\n[ERRO] Opção inválida! Digite um número de 1 a 5.")
