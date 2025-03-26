class Node
{
	int data;
	Node left, right;
	
	Node(int item)
	{
	    data = item;
	    left = right = null;
	}
}


class Res{
    Node pre = null;
    Node succ = null;
}


class Info{
    Node pre = null;
    Node post = null;
    Node targetNode = null;
}

// This function finds predecessor and successor of key in BST.
// It sets pre and suc as predecessor and successor respectively
class Solution
{
    public static void findPreSucUtil(Node root, Info i, int key){
        if(root == null)
            return;
        
        if(root.data == key){
            i.targetNode = root;
            return;
        }
        
        if(root.data < key){
            i.pre=root;
            findPreSucUtil(root.right, i, key);
        }
        else{
            i.post=root;
            findPreSucUtil(root.left, i, key);
        }
    }
    
    public static void findPreSuc(Node root, Res p, Res s, int key)
    {
        Info i = new Info();
        findPreSucUtil(root, i, key);
        
        if(i.targetNode != null){
            Node temp1 = i.targetNode.left;
            while(temp1 != null){
                i.pre = temp1;
                temp1 = temp1.right;
            }
            
            Node temp2 = i.targetNode.right;
            while(temp2 != null){
                i.post = temp2;
                temp2 = temp2.left;
            }
        }
        
        p.pre = i.pre;
        s.succ = i.post;
    }
}

public class PredecessorSuccessor{
    static Node insert(Node node, int key)
    {
        if (node == null)
            return new Node(key);
        if (key < node.data)
            node.left = insert(node.left, key);
        else
            node.right = insert(node.right, key);
            
        return node;
    }

    public static void main(String[] args){
        int key = 65;
        /*
        * Let us create following BST
        *          50
        *         /  \
        *        30   70
        *       /  \ /  \
        *      20 40 60  80
        */
    
        Node root = null;
        root = insert(root, 50);
        insert(root, 30);
        insert(root, 20);
        insert(root, 40);
        insert(root, 70);
        insert(root, 60);
        insert(root, 80);

        Solution sol = new Solution();
        Res p = new Res();
        Res s = new Res();
        sol.findPreSuc(root, p, s, key);

        if (p.pre != null)
            System.out.println("Predecessor is " + p.pre.data);
        else
            System.out.println("No Predecessor");
    
        if (s.succ != null)
            System.out.println("Successor is " + s.succ.data);
        else
            System.out.println("No Successor");
    }
}