import re

with open('packet.txt', 'r') as f:
    packet = f.read()

    for i in range(len(packet)):
        is_duplicate = True
        snippet = packet[i:i+4]
        occurrences = []

        for j in range(len(snippet)):
            num_of_occur = snippet.count(snippet[j])
            occurrences.append(num_of_occur)
        
        all_unique = [i for i in occurrences if i == 1]
        if len(all_unique) == 4:
            print(snippet)
            print(i+4)
            break
