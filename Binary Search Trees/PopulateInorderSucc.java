class Node {
    int data;
    Node left, right,next;
    
    public Node(int data){
        this.data = data;
    }
}


class Solution{
    private static Node succ=null;

    public static void populateNextUtil(Node root){
        if(root != null){
            populateNextUtil(root.right);
            
            root.next = succ;
            succ = root;
            
            populateNextUtil(root.left);

        }
    }

    public void populateNext(Node root){
        succ = null;
        populateNextUtil(root);
    }
}


class PopulateInorderSucc{
    public static void main(String[] args){
        //     Input:
        //     10
        //    /  \
        //   8    12
        //  /
        // 3
    
        Node root = new Node(10);
        root.left = new Node(8);
        root.right = new Node(12);
        root.left.left = new Node(3);

        Solution sol = new Solution();
        sol.populateNext(root);
    }
}