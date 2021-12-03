import System.IO

mlc :: (Int -> Int -> Bool) -> [Char] -> Char
mlc f x | length (filter (=='1') x) `f` length (filter (=='0') x) = '1'
        | otherwise = '0'

cbs :: [[Char]] -> (Int -> Int -> Bool) -> [Char]
cbs x f | length (head x) == 0 = []
        | otherwise = mlc f (map head x) : cbs (map tail x) f

chemgr :: [[Char]] -> Int -> (Int -> Int -> Bool) -> [[Char]]
chemgr x n f | length x == 1 = x
             | otherwise = chemgr (filter (\y -> (y!!n)==((cbs x f)!!n)) x) (n+1) f

binToDec :: [Char] -> Int
binToDec x = binToDecW (reverse x) 1

binToDecW :: [Char] -> Int -> Int
binToDecW [] _ = 0
binToDecW (x:xs) n = n * read [x] + binToDecW xs 2*n

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = lines input
 print (binToDec (cbs x (>=) ) * binToDec (cbs x (<) )) -- part 1
 print (binToDec (head ((chemgr x 0 (>=) ))) * binToDec (head ((chemgr x 0 (<) )))) --part 2
