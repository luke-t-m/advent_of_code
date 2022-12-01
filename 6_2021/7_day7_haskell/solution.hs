import Data.List.Split

moves x n = map (\y -> abs (n-y)) x

sumToN :: Int -> Int
sumToN n = round (m/2 * m+1) where m = fromIntegral n


main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = map read (splitOn "," input) :: [Int]
 let potMoves = [(moves x n) | n <- [(minimum x)..(maximum x)]]
 print (minimum (map sum potMoves))
 print (minimum (map (sum . map sumToN) potMoves))
 print "done."
