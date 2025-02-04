# Declaração
nome_completo = "Weliton Silva"

nome_completo_aspas = """"Weliton
silva"""

nome_completo_quebras = "Weliton \
Silva"

nome = "Weliton"
sobrenome = "Silva"

# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Weliton" + "Silva")
print("Nome completo (4a forma):" + "Weliton", "Silva")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebras)
print("Nome completo (7a forma): %s " % nome_completo)
print("Nome completo (8a forma): %s %s " % (nome, sobrenome))
print(f"Nome completo (9a forma):{nome}. {sobrenome}")
print("Nome completo (10a forma): {}, {}".format(nome, sobrenome))