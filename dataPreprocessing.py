listOfPromoters = open("Am_EPDnew_001_amel5.bed", 'r')
promoters = [line.split()[3] for line in listOfPromoters]
promoterSequence = open("promoter_sequence.txt", 'r')
for row in promoterSequence:
    row = row.split()
    print(row[1])
sequence = [line.split()[1] for line in promoterSequence]
sequence = list(filter(lambda a: a != "None",sequence))