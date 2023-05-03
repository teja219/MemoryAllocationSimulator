from collections import OrderedDict


def demote_superpage(superpage, tlb_mapping):
    # Get the starting and ending address of the superpage
    superpage_start = int(min(superpage))
    superpage_end = int(max(superpage))
    print("start,end :", superpage_start, superpage_end)
    # Remove the superpage from the TLB mapping
    superpage_pa = tlb_mapping[str(superpage_start)][0]
    tlb_mapping.pop(str(superpage_start))

    # Create new page entries for each smaller page in the superpage
    page_size = 4
    for i in range(superpage_start, superpage_end + 1, page_size):
        page_va = str(i)
        page_pa = superpage_pa + (i - superpage_start)
        tlb_mapping[page_va] = [page_pa]

    return tlb_mapping


tlb_mapping = OrderedDict(
    {'0': [0], '4': [4096], '8': [8192], '12': [12288], '16': [16384], '20': [20480], '24': [24576], '28': [28672],
     '32': [32768], '36': [36864], '40': [40960], '44': [45056], '48': [49152], '52': [53248], '56': [57344],
     '60': [61440]})

# Demote superpage [0, 15]
tlb_mapping = demote_superpage([str(i) for i in range(0, 32)], tlb_mapping)

print(tlb_mapping)
def promote(tlb_mapping):

    tlb_map_list = list(tlb_mapping.keys())
    print(tlb_map_list)
    i = 0
    prev = i
    while i < len(tlb_map_list):
        j = i+1
        while(j < len(tlb_map_list) and int(tlb_map_list[j])-int(tlb_map_list[prev]) == 1):
            current_va = str(tlb_map_list[j])
            current_pa = tlb_mapping[current_va]
            tlb_mapping.pop(current_va)
            # print("orig :",tlb_map_list[i])
            tlb_mapping[tlb_map_list[i]].append(current_pa)
            prev = j
            j = j+1
            # print("i,j :", i,j)
        i = j
    return tlb_mapping


tlb_mapping = OrderedDict()
tlb_mapping = {'1': [12], '2': [14], '3': [34], '4': [30], '5': [20], '8':[100], '10': [30]}

# print(promote(tlb_mapping))

import random
def main():
    processes = [1, 2, 3, 4, 5]
    virtual_address_size = 2 ** 10
    clock_cycles = 1000
    processId = random.choice(processes)
    for cycle in range(0,clock_cycles):

    # virtual_address_size = 2 ** 48
    # mmu = MMU()
    # previousProcessId = 0
    # for i in range(100):
    #     processId = random.choice(processes)
    #     virtual_address = random.randint(0, virtual_address_size - 1)
    #
    #     if previousProcessId is not processId:
    #         mmu.clear_TLB()
    #     physical_address = mmu.get_physical_address(virtual_address, processId)
    #     #         print(f"{processId},{virtual_address},{physical_address}")
    #     previousProcessId = processId
    # print("TLB_Misses", mmu.tlbMisses)

if __name__ == "__main__":
    main()
