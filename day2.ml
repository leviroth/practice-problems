open Base

let add_lists l1 l2 =
  let rec aux l1 l2 carry acc =
    match l1, l2 with
    | [], [] ->
      let acc = if carry = 0 then acc else carry :: acc in
      List.rev acc
    | hd :: tl, [] | [], hd :: tl ->
      let n = hd + carry in
      let carry = n / 10 in
      let digit = n % 10 in
      aux tl [] carry (digit :: acc)
    | hd1 :: tl1, hd2 :: tl2 ->
      let n = hd1 + hd2 + carry in
      let carry = n / 10 in
      let digit = n % 10 in
      aux tl1 tl2 carry (digit :: acc)
  in
  aux l1 l2 0 []
