# Este código usa a biblioteca PyCUDA para demonstrar a computação paralela em uma GPU NVIDIA. 
# Ele realiza a soma de dois vetores, mostrando como é possível acelerar operações matemáticas 
# utilizando a GPU. Para executar este código, instale o PyCUDA com o comando: 
# pip install pycuda

import pycuda.autoinit
import pycuda.driver as drv
import numpy as np

# Tamanho dos vetores
N = 1000000

# Criando vetores de entrada
a = np.random.randn(N).astype(np.float32)
b = np.random.randn(N).astype(np.float32)
c = np.empty_like(a)

# Alocando memória na GPU
a_gpu = drv.mem_alloc(a.nbytes)
b_gpu = drv.mem_alloc(b.nbytes)
c_gpu = drv.mem_alloc(c.nbytes)

# Copiando dados para a GPU
drv.memcpy_htod(a_gpu, a)
drv.memcpy_htod(b_gpu, b)

# Kernel CUDA para somar os vetores
mod = drv.SourceModule("""
__global__ void sum_vectors(float *a, float *b, float *c, int N) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < N) c[idx] = a[idx] + b[idx];
}
""")

# Definindo o número de threads e blocos
block_size = 256
grid_size = (N + block_size - 1) // block_size

# Executando o kernel
func = mod.get_function("sum_vectors")
func(a_gpu, b_gpu, c_gpu, np.int32(N), block=(block_size, 1, 1), grid=(grid_size, 1))

# Copiando o resultado de volta para a CPU
drv.memcpy_dtoh(c, c_gpu)

# Imprimindo os resultados
print("Resultado da soma dos vetores (primeiros 10 elementos):")
print(c[:10])