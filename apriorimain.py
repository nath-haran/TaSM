import csv
def apriori(dataset, min_support=0.5, verbose=False):
   
    C1 = create_candidates(dataset)
    D = map(set, dataset)
    F1, support_data = support_prune(D, C1, min_support, verbose=False) # prune candidate 1-itemsets
    F = [F1] # list of frequent itemsets; initialized to frequent 1-itemsets
    k = 2 # the itemset cardinality
    while (len(F[k - 2]) > 0):
        Ck = apriori_gen(F[k-2], k) # generate candidate itemsets
        Fk, supK = support_prune(D, Ck, min_support) # prune candidate itemsets
        support_data.update(supK) # update the support counts to reflect pruning
        F.append(Fk) # add the pruned candidate itemsets to the list of frequent itemsets
        k += 1

    return F, support_data

def create_candidates(dataset, verbose=False):
    
    c1 = [] # list of all items in the database of transactions
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()

    return map(frozenset, c1)

def support_prune(dataset, candidates, min_support, verbose=False):
    
    sscnt = {}
    for tid in dataset:
        for can in candidates:
            if can.issubset(tid):
                sscnt.setdefault(can, 0)
                sscnt[can] += 1

    num_items = float(len(dataset)) 
    retlist = [] 
    support_data = {} 
    for key in sscnt:
        support = sscnt[key] / num_items
        if support >= min_support:
            retlist.insert(0, key)
        support_data[key] = support

    
    return retlist, support_data

def apriori_gen(freq_sets, k):
    
    retList = [] 
    lenLk = len(freq_sets) 
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            a=list(freq_sets[i])
            b=list(freq_sets[j])
            a.sort()
            b.sort()
            F1 = a[:k-2] 
            F2 = b[:k-2] 

            if F1 == F2: 
                retList.append(freq_sets[i] | freq_sets[j])

    return retList

def rules_from_conseq(freq_set, H, support_data, rules, min_confidence=0.5, verbose=False):
    
    m = len(H[0])
    if m == 1:
        Hmp1 = calc_confidence(freq_set, H, support_data, rules, min_confidence, verbose)
    if (len(freq_set) > (m+1)):
        Hmp1 = apriori_gen(H, m+1) 
        Hmp1 = calc_confidence(freq_set, Hmp1, support_data, rules, min_confidence, verbose)
        if len(Hmp1) > 1:
            rules_from_conseq(freq_set, Hmp1, support_data, rules, min_confidence, verbose)

def calc_confidence(freq_set, H, support_data, rules, min_confidence=0.5, verbose=False):
    
    pruned_H = [] 
    for conseq in H: 
        conf = support_data[freq_set] / support_data[freq_set - conseq]
        if conf >= min_confidence:
            rules.append((freq_set - conseq, conseq, conf))
            pruned_H.append(conseq)

    return pruned_H

def generate_rules(F, support_data, min_confidence=0.5, verbose=True):
    
    rules = []
    for i in range(1, len(F)):
        for freq_set in F[i]:
            H1 = [frozenset([itemset]) for itemset in freq_set]
            if (i > 1):
                rules_from_conseq(freq_set, H1, support_data, rules, min_confidence, verbose)
            else:
                calc_confidence(freq_set, H1, support_data, rules, min_confidence, verbose)

    return rules

import csv
reader=csv.reader(open('trans4.csv','rb'))
clus=[]
k=0
for i in range(129):
    clus.append([])
for row in reader:
    for i in range(len(row)):
        if row[i]!='NULL':
            clus[k].append(row[i])
    k+=1
#print clus

import pprint
def load_dataset():
    return clus
dataset = load_dataset()
D = map(set, dataset)
#pprint.pprint(dataset)

C1 = create_candidates(dataset, verbose=True) 

F1, support_data = support_prune(D, C1, 0.05, verbose=True)

F, support_data = apriori(dataset, min_support=0.05, verbose=True)

H = generate_rules(F, support_data, min_confidence=0.5, verbose=True)
