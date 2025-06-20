
from django.shortcuts import render
from collections import defaultdict
from itertools import combinations

def index(request):
    return render(request, 'index.html')

def analisis(request):
    transactions = {
        1: {'Paracetamol', 'Amoxicillin'},
        2: {'Paracetamol', 'Antasida'},
        3: {'Paracetamol', 'Amoxicillin'},
        4: {'Amoxicillin', 'Antasida'}
    }
    min_support = 0.2
    itemsets = defaultdict(set)
    for tid, items in transactions.items():
        for item in items:
            itemsets[frozenset([item])].add(tid)

    frequent_itemsets = {}
    current_lset = itemsets
    k = 2
    while current_lset:
        for items, tids in current_lset.items():
            support = len(tids) / len(transactions)
            if support >= min_support:
                frequent_itemsets[items] = support

        next_lset = {}
        keys = list(current_lset.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                union = keys[i] | keys[j]
                if len(union) == k:
                    tids = current_lset[keys[i]] & current_lset[keys[j]]
                    if len(tids) / len(transactions) >= min_support:
                        next_lset[union] = tids
        current_lset = next_lset
        k += 1

    hasil = [{'kombinasi': ', '.join(k), 'support': round(v * 100, 2)} for k, v in frequent_itemsets.items()]
    return render(request, 'hasil_analisis.html', {'hasil': hasil})


