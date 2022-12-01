import Data.List
import Data.List.Split


subList [] _ = True
subList (a:as) b = a `elem` b && subList as (delete a b)

combs n x = nub [sort y | y <- sequence (replicate n x), y `subList` x]


xmas _ [] = -1
xmas p@(a:as) (b:bs) | b `elem` (map sum (combs 2 p)) = xmas (as++[b]) bs
                     | otherwise = b

contiger w ns (b:bs)
 | length x /= 0 = head x
 | otherwise = contiger w ([b] : (map (\y -> b:y) ns)) bs
  where x = filter (\y -> sum y == w) ns


main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = splitAt 25 (map read (lines input))
 let p1 = xmas (fst x) (snd x)
 print p1
 let p2 = contiger p1 [] (snd x)
 print (minimum p2 + maximum p2)
 print "done."
