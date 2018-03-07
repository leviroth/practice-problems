open Core_kernel

let find_peak arr =
  let get_safe i =
    match arr.(i) with
    | n -> n
    | exception Invalid_argument _ -> Int.min_value
  in
  let rec loop lo hi =
    if lo >= hi then lo
    else let mid = (lo + hi) / 2 in
      if get_safe mid < get_safe (mid + 1) then loop (mid + 1) hi
      else if get_safe mid < get_safe (mid - 1) then loop lo (mid - 1)
      else mid
  in
  loop 0 (Array.length arr)
