open Core_kernel

type tree =
  | Leaf
  | Node of tree * int * tree

let rec ancestors cur target acc =
  match cur with
  | Leaf -> None
  | Node (left, v, right) ->
    let acc = v :: acc in
    if v = target then Some acc
    else Option.first_some (ancestors left target acc) (ancestors right target acc)

let last_match l1 l2 =
  let rec aux l1 l2 prev =
    match l1, l2 with
    | hd1 :: tl1, hd2 :: tl2 -> if hd1 = hd2 then aux tl1 tl2 hd1 else prev
    | _ -> prev
  in
  aux l1 l2 0

let get_ancestors tree v1 v2 =
  let a1, a2 =
    Option.value_exn (ancestors tree v1 []),
    Option.value_exn (ancestors tree v2 [])
  in
  last_match (List.rev a1) (List.rev a2)
