#!/usr/bin/env python
# coding: utf-8

# In[3]:


f = open("NM_207618.2.fasta", "r")
sequence = f.read()
sequence


# In[7]:


with open("NM_207618.2.fasta", "r") as inf:
    data = inf.read().splitlines(True)
print(data)


# In[15]:


with open("NM_207618.2.fasta", "r") as inf:
    data = inf.read().splitlines(True)
with open('dna1.txt', 'w') as outf:
    outf.writelines(data[1:])
f = open("dna1.txt", "r")
sequence = f.read()
sequence


# In[10]:


genetic_code = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}
genetic_code['ATA']


# In[18]:


def read_seq(inputfile):
    with open(inputfile, 'r') as f:
        sequence = f.read()
    sequence = sequence.replace(' ', '')
    sequence = sequence.replace('\n', '')
    sequence = sequence.replace('\r', '')
    return sequence
with open("NM_207618.2.fasta", "r") as inf:
    data = inf.read().splitlines(True)
with open('dna.txt', 'w') as outf:
    outf.writelines(data[1:])
dna = read_seq('dna.txt')
print(dna)


# In[21]:


def convert(seq):
    """DNA 시퀀스를 아미노산 시퀀스로 변환"""
    genetic_code = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):  # 데이터의 길이가 3의 배수이면 아래를 실행
            codon = seq[i:i+3]
            protein += genetic_code[codon]
    return protein
print(convert(dna[20:938]))


# In[22]:


print(convert(dna[20:935]))


# In[27]:


import numpy as np
x = np.array([1, 3, 5])
print(x.mean())  # 평균값
print(x.shape)   # 속성(3열,)


# In[31]:


import numpy as np # 나중에 다시 열면 오류 나니까 미리 써두기
x = np.array([1, 3, 5, 7, 9, 11]).reshape(3,2)
print(x)
print(x.shape)


# In[34]:


a = np.array([[1,2,3],[2,3,4]])
print(a.shape)


# In[35]:


y = np.ones([3,4])
print(y)


# In[36]:


x = np.array([[1,3,5], [2,4,6]])
print(x[1])  # [1]번째 원소 -> [2,4,6]
print(x[1].mean())  # [1]번째 원소의 평균값
print(x.mean())     # 전체 평균값
print(x.shape)      # 속성 (2행, 3열)


# In[38]:


list1 = [[1,11], [2,12], [3,13]]
print(list1[1][1])


# In[73]:


# 2열의 원소들 출력
list1 = [[1,11], [2,12], [3,13]]
print(list1[:][1])  # 원하는 결과가 아님
print(list1[:,1])   # 에러 발생


# In[39]:


import numpy as np
list1 = [[1,11], [2,12], [3,13]]
np_ary = np.array(list1)
print(np_ary[:,1])


# In[40]:


import numpy as np
list1 = [[1,11,111], [2,12,222], [3,13,333]]
np_ary = np.array(list1)
print(np_ary[:,2])


# In[74]:


import numpy as np
list1 = [[1,11], [2,12], [3,13]]
print(np.array(list1[0]))
print(np.array(list1[:][0]))  # [:] 없는것과 동일


# In[45]:


import math
math.sqrt(2)


# In[49]:


import numpy as np
np.sqrt([2,3,4])  # 넘파이로 각각의 루트 값 출력


# In[51]:


import numpy as np
a = np.arange(15)
print(a)


# In[52]:


import numpy as np
a = np.arange(15).reshape(3,5)
print(a)


# In[53]:


# quiz 9.4
import numpy as np
a = np.arange(15).reshape(3,5) 
print(a[1][1]) # 위에서 6만 추출


# In[56]:


import numpy as np
zero_vector = np.zeros(3) # 괄호 하나
print(zero_vector)


# In[58]:


zero_matrix = np.zeros((4,3)) # 괄호 두개
print(zero_matrix)


# In[62]:


zero_vector = np.zeros(5)
zero_vector # 자료 타입 리스트다! 알려줌


# In[63]:


zero_vector = np.zeros(5)
print(zero_vector)  # 프린트문 쓰면 자료형없이 값만 출력


# In[65]:


zero_matrix = np.zeros((5,3)) # 괄호 두개
zero_matrix


# In[67]:


import numpy as np
my_array = np.zeros(15).reshape(3,5)
my_array


# In[70]:


import numpy as np
my_array = np.zeros(15).reshape(3,5)
my_array += 4
my_array


# In[76]:


import numpy as np
ary = np.array([[1,2], [3,4]] )
print(ary.transpose())


# In[83]:


import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = x * y  # 사칙연산 디 가능함
print(z)


# In[85]:


import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = x + 1  # 사칙연산 디 가능함
w = y + 2
print(z, w)


# In[86]:


# 2개 numpy 배열 간의 계산
X = np.array([[1,2,3],[4,5,6],[7,8,9]])
Y = np.array([[2,3,4],[5,6,7],[8,9,10]])
print(X[:,1]+Y[:,1])


# In[99]:


# 리스트 인덱싱
a = np.array([10, 20, 30, 40, 50, 60, 70])
i = [1,3,5]
print(a[i])

