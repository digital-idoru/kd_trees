#This is my implementation of K-d Trees as described in the original paper by Bently
#Daniel S. Hono II - 2014/5/14 
#Univeristy at Albany, SUNY 

#A classwrapper for a kd-Tree. 
#Contains root object, an instance of the kdNode class.  
#Contains functions for inserting a node into the K-d tree 
class kdTree:
    def __init__(self, dim):
        self.root = None; #Start the tree empty 
        self.k = dim; #Set the dimension 

    #Create a new kdNode instances and return it. 
    def newNode(self, d, v):
        tmp = kdNode(None, None, d);
        tmp.kList = v;
        return tmp;

    #Insert a node in the tree using Bently's algorithm. 
    def kdInsert(self, node, point, i):
        if self.root is None: #Empty tree
            self.root = self.newNode(i, point);
            return;
        elif node is None:
            return self.newNode(i, point);
        else:       
            if node.getDiscrimKey() < point[i]:
                i = (i + 1) % self.k;
                node.HISON = self.kdInsert(node.HISON, point, i);
                return node;
            else:
                i = (i + 1) % self.k; 
                node.LOSON = self.kdInsert(node.LOSON, point, i);
                return node;

    #Function to perform an exact match query on the k-d tree. Bently does not reccomend using kd-trees if the only purpose is for exact match queries.
    #This function is thus included for the sake of completeness. 
    def exactMatch(self, node, key):
        if node.getDiscrimKey != key[node.DISCRIM]: 
            return 0;

#A class the represents a kd-tree node. 
#Each node contains a left and right child pointer,
#keys (tuple), and a discriminator
class kdNode:
    #On creation of new kd-node it must have a LO and HI pointer.
    #These pointers may be null. 
    def __init__(self, LOSON, HISON, DISC):
        self.LOSON = LOSON;
        self.HISON = HISON;
        self.DISCRIM = DISC; 
        self.kList = None;

    def getDiscrimKey(self):
        return self.kList[self.DISCRIM];

    def nextDisc(self, k):
        return (self.DISCRIM + 1) % k; 

            
def main():

    #Initialize a new kdTree instance and insert some test nodes. 
    T = kdTree(2);
    T.kdInsert(T.root, (5, 4), 0);
    T.kdInsert(T.root, (1, 4), 0);
    T.kdInsert(T.root, (6, 7), 0);
    T.kdInsert(T.root, (3, 6), 0);
    T.kdInsert(T.root, (4, 2), 0);

    #print tree structure 
    print T.root.kList;
    print T.root.HISON.kList;
    print T.root.LOSON.kList;
    print T.root.LOSON.HISON.kList;
    print T.root.LOSON.LOSON.kList;

if __name__ == 'main':
    main();
