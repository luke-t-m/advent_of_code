import Data.Char
import Data.List
import Data.List.Split
import Numeric

binToDec x = binToDecW (reverse x) 1
binToDecW [] _ = 0
binToDecW (x:xs) n = n * read [x] + binToDecW xs 2*n

decToBin x = leadingZeroes (showIntAtBase 2 intToDigit x "")
 where leadingZeroes i | (length i) `mod` 8 == 0 = i
                       | otherwise = leadingZeroes ('0' : i)

hexToBin :: String -> String
hexToBin x = decToBin (fst (head (readHex x)))



chopLiteral i = concat (map tail (j ++ [(take 5 (drop (5*(length j)) i))]))
 where j = takeWhile (\t -> head t == '1') (chunksOf 5 i)

chopOp (t:i) | t == '1' = [(take 11 i)]
             | t == '0' = [(take 15 i), (decToBin bnum)] 
  where nu = fixtid (analyse (fst (splitAt (binToDec (take 15 i)) (drop 15 i))))
        bnum = head [num | num <- [0..(length nu)], length (taker num nu) == length nu]

analyse i@(a:b:c:d:e:f:xs) | (d:e:[f]) == "100" = lit : analyse (drop ((((length (chopLiteral xs)) `div` 4)*5)+6) i) 
                           | length xs /= 0 && (head xs) `elem` "10" = op : analyse (drop (length (head (chopOp xs)) + 7) i)
  where lit = (a:b:[c]) : (d:e:[f]) : [chopLiteral xs]
        op = (a:b:[c]) : (d:e:[f]) : (chopOp xs)
analyse _ = []

fixtid x = map (\t -> take 2 t ++ [last t]) x

taker _ [] = []
taker 0 _ = []
taker n i@(a@(bpv:btid:[bval]):r)
                          | tid == 4 = a : taker (n-1) r
                          | tid /= 4 = a : (taker val r) ++ (taker (n-1) (drop (length (taker val r)) r))
  where tid = binToDec btid
        val = binToDec bval


boolToInt True = 1
boolToInt False = 0

eval [] = []
eval x@((bpv:btid:[bval]):r) | tid == 0 = (sum (eval (taker val r))) : (eval (drop (length (taker val r)) r))
                             | tid == 1 = (product (eval (taker val r))) : (eval (drop (length (taker val r)) r))
                             | tid == 2 = (minimum (eval (taker val r))) : (eval (drop (length (taker val r)) r))
                             | tid == 3 = (maximum (eval (taker val r))) : (eval (drop (length (taker val r)) r))
                             | tid == 4 = val : eval r
                             | tid == 5 = (boolToInt (a>b)) : (eval (drop (length (taker val r)) r))                     
                             | tid == 6 = (boolToInt (a<b)) : (eval (drop (length (taker val r)) r))
                             | tid == 7 = (boolToInt (a==b)) : (eval (drop (length (taker val r)) r))
  where tid = binToDec btid
        val = binToDec bval
        (a:b:_) = (eval (taker 2 r))

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = analyse (hexToBin input)
 putStr "Part 1: "
 print (sum (map (\t -> binToDec (head t)) x))
 putStr "Part 2: "
 print (head (eval (fixtid x)))
 print "done."
