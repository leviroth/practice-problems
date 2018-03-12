open Core_kernel

type tree =
  | Leaf
  | Node of tree * int * tree

let solve tree =
  let update_prefix prefix n = n + 10 * prefix in
  let rec solve tree acc prefix =
    match tree with
    | Leaf -> acc
    | Node (Leaf, d, Leaf) ->
      (update_prefix prefix d) + acc
    | Node (left, d, right) ->
      let prefix = update_prefix prefix d in
      solve left acc prefix + solve right acc prefix
  in
  solve tree 0 0

let tree = Node(Node(Leaf, 2, Leaf), 1, Node(Leaf, 3, Leaf))
let tree2 = Node(Leaf, 1, Node(Leaf, 3, Leaf))

let () =
  assert(solve tree = 25);
  assert(solve tree2 = 13)
