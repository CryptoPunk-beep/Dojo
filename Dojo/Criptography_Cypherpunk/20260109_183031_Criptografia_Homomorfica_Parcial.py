# Este código demonstra a criptografia homomórfica parcial usando a biblioteca PySEAL. 
# A criptografia homomórfica permite realizar operações em dados criptografados sem a necessidade de descriptografá-los. 
# Para executar este código, instale a biblioteca com: pip install pyseal

from seal import *

def main():
    # Configuração do contexto de criptografia
    parms = EncryptionParameters(scheme_type.BFV)
    poly_modulus_degree = 4096
    parms.set_poly_modulus_degree(poly_modulus_degree)
    parms.set_coeff_modulus(CoeffModulus.BFVDefault(poly_modulus_degree))
    parms.set_plain_modulus(256)

    context = SEALContext.Create(parms)
    keygen = KeyGenerator(context)
    public_key = keygen.public_key()
    encryptor = Encryptor(context, public_key)
    decryptor = Decryptor(context, keygen.secret_key())
    evaluator = Evaluator(context)
    encoder = IntegerEncoder(context)

    # Codificando e criptografando dois números
    num1 = 5
    num2 = 10
    plain1 = encoder.encode(num1)
    plain2 = encoder.encode(num2)
    encrypted1 = encryptor.encrypt(plain1)
    encrypted2 = encryptor.encrypt(plain2)

    # Realizando a adição em dados criptografados
    encrypted_result = evaluator.add(encrypted1, encrypted2)

    # Descriptografando e decodificando o resultado
    plain_result = decryptor.decrypt(encrypted_result)
    result = encoder.decode(plain_result)

    print(f"O resultado da adição de {num1} e {num2} é: {result}")

if __name__ == "__main__":
    main()