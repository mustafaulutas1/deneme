def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    
    # İlk adımı print etme
    print("Parça 1:", left)
    print("Parça 2:", right)
    print()
    
    # Parçaları sırala ve birleştir
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Birleştirme işlemini print etme
    print("Birleştirme:", merged + left[i:] + right[j:])
    print()
    
    return merged + left[i:] + right[j:]

# Rastgele unique elemanlardan oluşan 18 elemanlı bir liste oluşturalım
import random
data = random.sample(range(1, 101), 18)

print("Başlangıç veri kümesi:", data)
print()

sorted_data = merge_sort(data)

print("Sıralanmış veri kümesi:", sorted_data)
