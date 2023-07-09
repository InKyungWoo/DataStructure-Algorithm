# 허프만 - 최소 비용 계산

import heapq

class HuffmanNode:
	def __init__(self, freq, symbol):
		self.freq = freq
		self.symbol = symbol
		self.left = None
		self.right = None
	def __lt__(self, other):
		return self.freq < other.freq

def Huffman_code(frequencies):
	heap = []
	for i, freq in enumerate(frequencies):
		heapq.heappush(heap, HuffmanNode(freq, i))

	while len(heap) > 1:
		a = heapq.heappop(heap)
		b = heapq.heappop(heap)
		merged_freq = a.freq + b.freq
		merged_node = HuffmanNode(merged_freq, None)
		merged_node.left = a
		merged_node.right = b
		heapq.heappush(heap, merged_node)

	return heap[0]

def build_codes(node, code, codes):
	if node.symbol is not None:
		codes[node.symbol] = code
	else:
		build_codes(node.left, code + "0", codes)
		build_codes(node.right, code + "1", codes)

def calculate_min_cost(frequencies):
	root = Huffman_code(frequencies)
	codes = {}
	build_codes(root, "", codes)

	total_cost = 0
	for symbol, code in codes.items():
		freq = frequencies[symbol]
		code_length = len(code)
		cost = freq * code_length
		total_cost += cost

	return total_cost, codes

# n개의 자연수(빈도수)를 입력받아 리스트 f에 저장
f = [int(x) for x in input().split()]
min_cost, huffman_codes = calculate_min_cost(f)

#print("Huffman Codes:", huffman_codes)  # 코드 출력
print(min_cost)	# 최소 cost 출력
