import System.IO


--shamelessly stolen from Philip Wadler's intro to FP slides on combinatorics
choose :: Int -> [a] -> [[a]]
choose 0 [] = [[]]
choose k (x:xs)
 | k == 0 = [[]]
 | k == n = [x:xs]
 | 0 < k && k < n = choose k xs ++
   map (x:) (choose (k-1) xs)
  where n = length (x:xs)

main :: IO ()
main = do
 inputs <- readFile "input.txt"
 let lS = lines inputs
     lI = map read lS
     poss = choose 3 lI  --swap to 2 to solve part 1 as well
     val = head (filter (\x -> sum x==2020) poss)
 print (product val)
