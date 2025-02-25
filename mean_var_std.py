import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.reshape(np.array(list), (3,3))
    calculations = {
                    'mean': [matrix.mean(axis=0), matrix.mean(axis=1), matrix.flatten().mean()],
                    'variance': [matrix.var(axis=0), matrix.var(axis=1), matrix.flatten().var()],
                    'standard deviation': [matrix.std(axis=0), matrix.std(axis=1), matrix.flatten().std()],
                    'max': [matrix.max(axis=0), matrix.max(axis=1), matrix.flatten().max()],
                    'min': [matrix.min(axis=0), matrix.min(axis=1), matrix.flatten().min()],
                    'sum': [matrix.sum(axis=0), matrix.sum(axis=1), matrix.flatten().sum()]

                    }


    return calculations

### My code returns the correct values, however, the test module provided can't compare the values lists from both dictionaries

if __name__ == '__main__':
    list_1 = [2,6,2,8,4,0,1,5,7]
    dictionary_1 = calculate(list_1)
    for key, value in dictionary_1.items():
        print(f'{key}: {value}') 

    expected = {'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889], 
                'variance': [[9.555555555555557, 0.6666666666666666, 8.666666666666666], [3.555555555555556, 10.666666666666666, 6.222222222222221], 6.987654320987654], 
                'standard deviation': [[3.091206165165235, 0.816496580927726, 2.943920288775949], [1.8856180831641267, 3.265986323710904, 2.494438257849294], 2.6434171674156266], 
                'max': [[8, 6, 7], [6, 8, 7], 8], 'min': [[1, 4, 0], [2, 0, 1], 0], 'sum': [[11, 15, 9], [10, 12, 13], 35]}

    
    
    list_2 = [9,1,5,3,3,3,2,9,0]
    dictionary_2 = calculate(list_2)
    for key, value in dictionary_2.items():
        print(f'{key}: {value}')

    expected2 = {'mean': [[4.666666666666667, 4.333333333333333, 2.6666666666666665], [5.0, 3.0, 3.6666666666666665], 3.888888888888889], 
                'variance': [[9.555555555555555, 11.555555555555557, 4.222222222222222], [10.666666666666666, 0.0, 14.888888888888891], 9.209876543209875], 
                'standard deviation': [[3.0912061651652345, 3.39934634239519, 2.0548046676563256], [3.265986323710904, 0.0, 3.8586123009300755], 3.0347778408328137], 
                'max': [[9, 9, 5], [9, 3, 9], 9], 'min': [[2, 1, 0], [1, 3, 0], 0], 'sum': [[14, 13, 8], [15, 9, 11], 35]}

    
    list_3 = [2,6,2,8,4,0,1,]
    dictionary_3 = calculate(list_3)
