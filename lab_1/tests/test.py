import numpy as np

def read_matrix_from_txt(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Считываем размеры матрицы
    rows, cols = map(int, lines[0].split())
    
    # Читаем данные и создаем массив numpy
    data = [list(map(float, line.split())) for line in lines[1:]]
    matrix = np.array(data)
    
    return matrix

if __name__ == "__main__":
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for size in sizes:
        a = f"C:/Users/Darowiin/Desktop/labs/ParallelProgramming/lab_1/tests/results/a{size}.txt"
        b = f"C:/Users/Darowiin/Desktop/labs/ParallelProgramming/lab_1/tests/results/b{size}.txt"
        result = f"C:/Users/Darowiin/Desktop/labs/ParallelProgramming/lab_1/tests/results/result{size}.txt"
        
        a_matrix = read_matrix_from_txt(a)
        b_matrix = read_matrix_from_txt(b)
        result_matrix = read_matrix_from_txt(result)
        
        y = np.dot(a_matrix, b_matrix)
        if np.allclose(y, result_matrix, atol=1e-9):
            print(f"Verification passed for size {size} ✅")
        else:
            print(f"Verification failed for size {size} ❌")
