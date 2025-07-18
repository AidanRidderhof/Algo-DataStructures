class Node {
    constructor(value) {
      this.left = null;
      this.right = null;
      this.value = value;
    }
  }

class BinarySearchTree {
    constructor(){
        this.root = null
    }
    insert(value){
      const newNode = new Node(value);

      if (this.root == null) {
        this.root = newNode
      }
      else {
        let currNode = this.root;
        while(true) {
          if (value < currNode.value) {
            if (!currNode.left) {
              currNode.left = newNode;
              return this
            }
            currNode = currNode.left;
          }
          else {
            if (!currNode.right) {
              currNode.right = newNode;
              return this
            }
            currNode = currNode.right;
          }
        }
      }
    }


    lookup(value){
        let currNode = this.root;
        while (currNode) {
          if (value == currNode.value) {
            return true;
          }
          else if (value<currNode.value) {
            currNode = currNode.left;
          }
          else {
            currNode = currNode.right;
          }
        }
        return false;
    }
}

let myTree = new BinarySearchTree();
myTree.insert(10);
myTree.insert(5);
myTree.insert(15);
myTree.insert(8);
console.log(myTree.lookup(8));
console.log(myTree);



