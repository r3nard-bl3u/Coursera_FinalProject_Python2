projectTwitterData = open("project_twitter_data.csv", 'r')
resultingData = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

myfile = open('project_twitter_data.csv', 'r')
rows = myfile.readlines()[1:]
for line in rows:
    words = line.split()
    numbers = words[-1]
    twrt = numbers.split(',')
    print ('retweets: ', twrt[1], 'replies: ', twrt[2])
    pos_sco = 0
    neg_sco = 0
    for word in words:
        if word in positive_words:
            pos_sco = pos_sco + 1
        if word in negative_words:
            neg_sco = neg_sco + 1
    net_sco = pos_sco - neg_sco
    print ('positive words: ', pos_sco, 'negative words: ', neg_sco, 'Net score: ', net_sco )
    row_string = '{}, {}, {}, {}, {}'.format(twrt[1], twrt[2], pos_sco, neg_sco, net_sco)
    outfile.write(row_string)
    outfile.write('\n')
