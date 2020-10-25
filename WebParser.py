import sys
import os
import string
from debug1 import vr_debug



def index_text_file(txt_filename, idx_filename, 
    delimiter_chars=",.-#()&*%"):
    delim_chars="+!"
    try:
        txt_fil = open(txt_filename, "r")
        word_occurrences = {}
        line_num = 0
        str1=open('/Users/pavandoodi/Desktop/ProjectA/tomsawyer.txt','r').read()
        str2=str1.replace("\r\n","\n")
        pi=list(str2.split('\n\n'))

        for lin in txt_fil:
            line_num += 1
            vr_debug("line_num", line_num)
            # Split the line into words delimited by whitespace.
            words = lin.split()
            vr_debug("words", words)
            # Remove unwanted delimiter characters adjoining words.
            words2 = [ word.strip(delimiter_chars).lstrip('"').lstrip("',.!-_").rstrip("'").rstrip('",.!-_') for word in words ]
            vr_debug("words2", words2)
            
            # Find and save the occurrences of each word in the line.
            for word in words2:
                if word in word_occurrences:
                    word_occurrences[word].append(line_num)
                else:
                    word_occurrences[word] = [ line_num ]
            

        vr_debug("Processed {} lines".format(line_num))

        if line_num < 1:
            print("No lines found in text file, no index file created.")
            txt_fil.close()
            sys.exit(0)

        # Display results.
        word_keys = word_occurrences.keys()
        print("{} unique words found.".format(len(word_keys)))
        vr_debug("Word_occurrences", word_occurrences)
        word_keys = word_occurrences.keys()
        vr_debug("word_keys", word_keys)

        # Sort the words in the word_keys list.
        sorted(word_keys)
        vr_debug("after sort, word_keys", word_keys)

        # Create the index file.
        idx_fil = open(idx_filename, "w")

        for word in word_keys:
            line_nums = word_occurrences[word]
            idx_fil.write(word + " ")
            for line_num in line_nums:
                idx_fil.write(str(line_num) + " ")
            idx_fil.write("\n")
        #print(word_keys)
        s=raw_input("Enter the word:")
        liw=list(s.split())  #to capture the list of input
        op=[]  #intialze array to capture the operands
        p=list() #initialize list to capture the words
        for i in liw:
            if i in delim_chars:
                op.append(i)  #capture operands
            else:
                p.append(i)  #capture words
        for i1 in p:  #loop for entering into NOT case
            for i2 in i1:
                if i2 in delim_chars:
                    op.append(i2)
        for i in liw:
            for i3 in i:
                if i3 == '"':
                    if len(op) != 0:
                        op.pop()
                    op.append(i3)
        print(op)

        ln=list()  #initiliaze list to capture line number
        para=list() #nitialize list to capture paragraph
        paranum=list() #nitialize list to capture paragraph numbers
        #print(op)
        if len(op)==0:  #Space is given for OR operator
            for j in p:    #for j in list of input words captured
                if j in word_occurrences.keys():   #If the words in input preset in index dictionary
                    for t in word_occurrences.get(j):  #get the line numbers of the word from the dictinary values
                        if t in ln:  #if the line number already exists then pass else append it
                            pass
                        else:
                            ln.append(t)
                    for i in pi:    #pi is the list of paragraphs-- for each paragraph if input word is found capture them
                        if i.find(j) != -1:
                            if pi.index(i) in paranum:  # if paranum is already captured pass else append
                                pass
                            else:
                                paranum.append(pi.index(i))
                                para.append(i)
                        else:
                            pass
        elif op[0] == '"':
            for k in pi:
                m=k.replace('\n'," ")
                if m.find(s.strip('"')) != -1:
                    para=[word for line in para for word in line.split('\n')]
                    paranum.append(pi.index(k))
                    para.append(k)
                else:
                    pass
        
        elif op[0] == '+':   # for the AND operand     
                n1=list() #list to capture the Word without ! symbol
                n2=list()  #list to capture the Word without ! symbol
                for n in p:
                    if n.find('+') != -1:
                        n2.append(n.strip('+'))  # capturing the Word with ! symbol
                    else:
                       n1.append(n) # capturing the Word without ! symbol
                o1=set() #sets to capture paragraph numbers with 
                o2=set() 
                for o in pi:
                    g=0
                    h=0
                    for g in range(len(n1)):
                        if o.find(n1[g]) != -1:
                            o1.add(pi.index(o))
                            g +=1
                        else:
                            pass
                        
                    for h in range(len(n2)):    
                        if o.find(n2[h]) != -1:
                            o2.add(pi.index(o))
                            h +=1
                        else:
                            pass
                print(o1)
                print(o2)       
                f1=o1.intersection(o2)
                for s in f1:
                    paranum.append(s)
                    para.append(pi[s])


        elif op[0] == '!':
                print(p)
                n1=list() #list to capture the Word without ! symbol
                n2=list()  #list to capture the Word without ! symbol
                for n in p:
                    if n.find('!') != -1:
                        n2.append(n.strip('!'))  # capturing the Word with ! symbol
                    else:
                       n1.append(n) # capturing the Word without ! symbol
                o1=set() #sets to capture paragraph numbers with 
                o2=set() 
                for o in pi:
                    g=0
                    h=0
                    for g in range(len(n1)):
                        if o.find(n1[g]) != -1:
                            o1.add(pi.index(o))
                            g +=1
                        else:
                            pass
                        
                    for h in range(len(n2)):    
                        if o.find(n2[h]) != -1:
                            o2.add(pi.index(o))
                            h +=1
                        else:
                            pass
                        
                f1=o1.intersection(o2)
                f2=o1.difference(f1)
                for s in f2:
                    paranum.append(s)
                    para.append(pi[s])
        
         
        print("Paragraph Number and Paragraph text")
        print(paranum)

        print("Paragraph text")
        para=[word for line in para for word in line.split('\n')]
        print("\n".join(para))

        #print("Line number")
        #print(ln)
   
                         
        txt_fil.close()
        idx_fil.close()
       
    except IOError as ioe:
        sys.stderr.write("Caught IOError: " + repr(ioe) + "\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write("Caught Exception: " + repr(e) + "\n")
        sys.exit(1)


def usage(sys_argv):
    sys.stderr.write("Usage: {} text_file.txt index_file.txt\n".format(
        sys_argv[0]))


def main():
    if len(sys.argv) != 3:
        usage(sys.argv)
        sys.exit(1)
    index_text_file(sys.argv[1], sys.argv[2])
   
                



if __name__ == "__main__":
    main()

# EOF
