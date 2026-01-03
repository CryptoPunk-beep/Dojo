# Este código gera um Identificador Descentralizado (DID) e seu documento associado. 
# O DID é uma nova forma de identidade digital que permite que indivíduos e organizações 
# tenham controle sobre suas identidades sem depender de uma autoridade central. 
# Para rodar este código, instale a biblioteca `didkit` com o comando: 
# pip install didkit

import didkit

# Gerar um novo DID
did, key = didkit.key_create("Ed25519")

# Criar um documento DID
document = didkit.did_document_create(did, key)

# Imprimir o DID e seu documento
print("DID:", did)
print("Documento DID:", document)