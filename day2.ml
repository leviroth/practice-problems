open Base

let add_lists l1 l2 =
  let rec aux l1 l2 carry acc =
    match l1, l2 with
    | [], [] ->
      List.rev (if carry = 0 then acc else carry :: acc)
    | hd1 :: tl1, other
    | other, hd1 :: tl1 ->
      let hd2, tl2 =
        match other with
        | hd :: tl -> hd, tl
        | [] -> 0, []
      in
      let n = hd1 + hd2 + carry in
      let carry = n / 10 in
      let digit = n % 10 in
      aux tl1 tl2 carry (digit :: acc)
  in
  aux l1 l2 0 []
