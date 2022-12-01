import Data.List
import Data.Hashable
import Data.List.Split
import Test.QuickCheck
import qualified Data.HashSet as HS
import Data.List (subsequences)

combs4 k = HS.toList . HS.fromList . filter (\x -> length x == k) . subsequences


subList [] _ = True
subList (a:as) b = a `elem` b && subList as (delete a b)

combs :: (Num a, Eq a, Hashable a, Ord a) => Int -> [a] -> [[a]]
combs n x = HS.toList (HS.fromList [sort y | y <- sequence (replicate n x), y `subList` x])

combs_old n x = nub [sort y | y <- sequence (replicate n x), y `subList` x]

combs2 k = filter (\x -> length x == k) . nub . subsequences

combs3 n x = nub (filter (\y -> length y == n) (subsequences x))

prop_combs n x = n > 0 ==> combs n x == combs3 n x



xmas _ [] = -1
xmas p@(a:as) (b:bs) | b `elem` (map sum (combs_old 2 p)) = xmas (as++[b]) bs
                     | otherwise = b

contiger w ns (b:bs)
 | length x /= 0 = head x
 | otherwise = contiger w ([b] : (map (\y -> b:y) ns)) bs
  where x = filter (\y -> sum y == w) ns


main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = splitAt 25 (map read (lines input))
 let p1 = xmas (fst x) (snd x) :: Int
 print p1
-- let p2 = contiger p1 [] (snd x) :: [Int]
-- print (minimum p2 + maximum p2)
 print "done."
